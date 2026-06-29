"""
🤖 AI Telegram Bot - Powered by DeepSeek API
Tính năng:
  - /start: Chào hỏi + hướng dẫn
  - /help: Danh sách lệnh
  - /tom_tat [url]: Tóm tắt bài viết/webpage
  - /hoi: Hỏi đáp AI bất kỳ câu hỏi
  - /viet [yêu cầu]: Viết content (caption, email, post...)
  - /clear: Xóa lịch sử chat
"""

import os
import logging
import httpx
import json
from dotenv import load_dotenv
from telegram import Update, BotCommand
from telegram.ext import (
    Application, CommandHandler, MessageHandler,
    filters, ContextTypes
)

load_dotenv()

# ─── Config ─────────────────────────────────────────────────────────────────
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_API_URL = "https://api.deepseek.com/chat/completions"
MAX_HISTORY = 10  # Số lượt chat tối đa lưu trong bộ nhớ

# ─── Setup ──────────────────────────────────────────────────────────────────
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

async def post_init(app: Application) -> None:
    """Setup bot commands khi khởi động."""
    commands = [
        BotCommand("start", "Giới thiệu bot"),
        BotCommand("help", "Danh sách các lệnh"),
        BotCommand("tom_tat", "Tóm tắt bài viết từ URL"),
        BotCommand("viet", "Viết content (caption, email, post...)"),
        BotCommand("clear", "Xóa lịch sử hội thoại"),
    ]
    await app.bot.set_my_commands(commands)
    logger.info("✅ Bot commands setup xong")


# ─── Helper ─────────────────────────────────────────────────────────────────
def get_history(context: ContextTypes.DEFAULT_TYPE) -> list:
    if "history" not in context.user_data:
        context.user_data["history"] = []
    return context.user_data["history"]


def add_to_history(context, role: str, content: str):
    history = get_history(context)
    history.append({"role": role, "content": content})
    # Giữ tối đa MAX_HISTORY lượt
    if len(history) > MAX_HISTORY * 2:
        context.user_data["history"] = history[-(MAX_HISTORY * 2):]


async def ask_deepseek(messages: list, system: str = None) -> str:
    """Gọi DeepSeek API và trả về text response."""
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}"
    }
    
    payload = {
        "model": "deepseek-chat",
        "messages": messages,
        "max_tokens": 1024,
        "temperature": 0.7
    }
    
    if system:
        # Thêm system message vào đầu messages
        payload["messages"] = [{"role": "system", "content": system}] + messages

    async with httpx.AsyncClient(timeout=30) as client:
        try:
            response = await client.post(DEEPSEEK_API_URL, headers=headers, json=payload)
            response.raise_for_status()
            data = response.json()
            return data["choices"][0]["message"]["content"]
        except httpx.HTTPError as e:
            logger.error(f"❌ DeepSeek API error: {e}")
            raise Exception(f"API Error: {e}")


async def fetch_webpage_text(url: str) -> str:
    """Lấy nội dung text thô từ URL."""
    async with httpx.AsyncClient(timeout=15, follow_redirects=True) as http:
        r = await http.get(url, headers={"User-Agent": "Mozilla/5.0"})
        r.raise_for_status()
        text = r.text

    # Xóa HTML tags thô sơ
    import re
    text = re.sub(r"<style[^>]*>.*?</style>", " ", text, flags=re.DOTALL)
    text = re.sub(r"<script[^>]*>.*?</script>", " ", text, flags=re.DOTALL)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text[:8000]  # Giới hạn để không vượt token


# ─── Command Handlers ────────────────────────────────────────────────────────

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    name = update.effective_user.first_name or "bạn"
    await update.message.reply_text(
        f"👋 Xin chào <b>{name}</b>! Tôi là AI Assistant.\n\n"
        "📋 <b>Những gì tôi có thể làm:</b>\n"
        "• Chat bình thường — cứ nhắn tin tôi trả lời\n"
        "• <code>/tom_tat [url]</code> — tóm tắt bài viết\n"
        "• <code>/viet [yêu cầu]</code> — viết caption, email, bài đăng\n"
        "• <code>/clear</code> — xóa lịch sử để bắt đầu lại\n\n"
        "💡 Thử hỏi tôi bất cứ điều gì!",
        parse_mode="HTML",
    )


async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📖 <b>Danh sách lệnh:</b>\n\n"
        "<code>/start</code> — Giới thiệu bot\n"
        "<code>/tom_tat [url]</code> — Tóm tắt webpage/bài viết\n"
        "<code>/viet [yêu cầu]</code> — Viết content theo yêu cầu\n"
        "<code>/clear</code> — Xóa lịch sử hội thoại\n\n"
        "Hoặc cứ nhắn tin bình thường để chat với AI!",
        parse_mode="HTML",
    )


async def clear(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["history"] = []
    await update.message.reply_text("🧹 Đã xóa lịch sử hội thoại!")


async def tom_tat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    if not args:
        await update.message.reply_text(
            "⚠️ Hãy cung cấp URL: <code>/tom_tat https://example.com</code>",
            parse_mode="HTML",
        )
        return

    url = args[0]
    msg = await update.message.reply_text("⏳ Đang đọc bài viết...")

    try:
        content = await fetch_webpage_text(url)
    except Exception as e:
        await msg.edit_text(f"❌ Không đọc được URL: {e}")
        return

    try:
        summary = await ask_deepseek(
            messages=[{"role": "user", "content": f"Tóm tắt bài viết này bằng tiếng Việt, ngắn gọn trong 5-7 câu:\n\n{content}"}],
            system="Bạn là trợ lý tóm tắt chuyên nghiệp. Hãy tóm tắt chính xác, rõ ràng, dễ hiểu.",
        )
        await msg.edit_text(f"📝 <b>Tóm tắt:</b>\n\n{summary}", parse_mode="HTML")
    except Exception as e:
        await msg.edit_text(f"❌ Lỗi AI: {e}")


async def viet(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text(
            "⚠️ Hãy nêu yêu cầu: <code>/viet caption cho ảnh mèo cute</code>",
            parse_mode="HTML",
        )
        return

    yeu_cau = " ".join(context.args)
    msg = await update.message.reply_text("✍️ Đang viết...")

    try:
        result = await ask_deepseek(
            messages=[{"role": "user", "content": yeu_cau}],
            system=(
                "Bạn là copywriter chuyên nghiệp người Việt. "
                "Viết nội dung hấp dẫn, đúng yêu cầu, phù hợp văn hóa Việt Nam. "
                "Không giải thích dài dòng, chỉ đưa ra nội dung cần viết."
            ),
        )
        await msg.edit_text(f"✅ <b>Kết quả:</b>\n\n{result}", parse_mode="HTML")
    except Exception as e:
        await msg.edit_text(f"❌ Lỗi: {e}")


async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Xử lý tin nhắn thông thường — chat có lịch sử."""
    user_msg = update.message.text
    add_to_history(context, "user", user_msg)

    msg = await update.message.reply_text("💭 Đang suy nghĩ...")

    try:
        reply = await ask_deepseek(
            messages=get_history(context),
            system=(
                "Bạn là trợ lý AI thông minh, thân thiện, trả lời bằng tiếng Việt. "
                "Câu trả lời ngắn gọn, rõ ràng và hữu ích."
            ),
        )
        add_to_history(context, "assistant", reply)
        await msg.edit_text(reply)
    except Exception as e:
        await msg.edit_text(f"❌ Lỗi: {e}")


# ─── Main ────────────────────────────────────────────────────────────────────

def main():
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    # Setup commands khi khởi động
    app.post_init = post_init

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("clear", clear))
    app.add_handler(CommandHandler("tom_tat", tom_tat))
    app.add_handler(CommandHandler("viet", viet))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

    logger.info("🤖 Bot đang chạy...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()