# 🤖 AI Telegram Bot — Hướng dẫn đầy đủ (Powered by DeepSeek)

Bot Telegram tích hợp DeepSeek AI: chat thông minh, tóm tắt bài viết, viết content tự động.

---

## ⚡ Cài đặt (5 phút)

### 1. Clone & cài thư viện
```bash
git clone <repo-của-bạn>
cd telegram-ai-bot
pip install -r requirements.txt
```

### 2. Lấy Telegram Token
1. Mở Telegram, tìm **@BotFather**
2. Gõ `/newbot`
3. Đặt tên bot (VD: `MyShopAI`)
4. Copy token (dạng `123456789:ABC...`)

### 3. Lấy DeepSeek API Key
1. Vào https://platform.deepseek.com
2. Tạo tài khoản → API Keys → Create Key
3. Copy key (dạng `sk-...`)

### 4. Setup file .env
```bash
cp .env.example .env
# Mở .env và điền token + api key vào
```

### 5. Chạy bot
```bash
python bot.py
```

Bot chạy rồi! Mở Telegram tìm bot của bạn và gõ `/start`.

---

## 🚀 Deploy lên Render.com (100% FREE)

**Render cho phép chạy bot 24/7 hoàn toàn miễn phí, không sleep như Heroku cũ!**

📖 **Xem chi tiết:** Mở file `DEPLOY_FREE.md` để hướng dẫn đầy đủ.

### Quick Start:

1. Push code lên GitHub
```bash
git init
git add .
git commit -m "deploy telegram bot"
git remote add origin https://github.com/YOUR_USERNAME/telegram-ai-bot.git
git push -u origin main
```

2. Vào https://render.com → Sign up → New Web Service
3. Chọn GitHub repo
4. Config:
   - Build: `pip install -r requirements.txt`
   - Start: `python bot.py`
5. Add env vars: `TELEGRAM_TOKEN`, `DEEPSEEK_API_KEY`
6. Deploy → Done! ✅

**Để bot không bị pause:** Setup UptimeRobot (free) ping mỗi 10 phút.

---

### Các option deploy khác

- **Fly.io** - Chạy 24/7, free tier 3 instances
- **PythonAnywhere** - Python-specific, dễ setup
- **Replit** - Nhanh nhất, nhưng free chỉ 1h/ngày

Chi tiết xem `DEPLOY_FREE.md` 📄

## 📋 Tính năng của bot

| Lệnh | Chức năng |
|------|-----------|
| `/start` | Chào hỏi, hướng dẫn |
| `/help` | Danh sách lệnh |
| `/tom_tat [url]` | Tóm tắt bài viết từ link |
| `/viet [yêu cầu]` | Viết caption, email, post |
| `/clear` | Xóa lịch sử chat |
| Chat thường | Hỏi đáp AI có nhớ ngữ cảnh |

---

## 💰 Cách kiếm tiền với bot này

### Mô hình 1: Bán cho shop online ($200-500/bot)
**Pitch:**
> "Anh/chị có muốn bot Telegram tự động trả lời khách hàng 24/7,
> viết caption sản phẩm trong 5 giây, và tóm tắt phản hồi khách không?
> Tôi setup hết chỉ trong 1 ngày."

**Target khách hàng:**
- Shop bán hàng Facebook/Shopee có group Telegram
- Fanpage quần áo, mỹ phẩm, thực phẩm

---

### Mô hình 2: Subscription bot ($20-50/tháng/người)
**Pitch:**
> "Bot AI cá nhân của riêng bạn — tóm tắt tin tức, viết content,
> trả lời câu hỏi 24/7. Dùng thử miễn phí 7 ngày."

**Setup thêm:** Tích hợp payment (Stripe/VNPay), giới hạn usage theo gói.

---

### Mô hình 3: Freelance trên Upwork ($300-1500/project)
**Đăng gig:**
```
"I will build a custom AI Telegram bot with DeepSeek API
- Customer service automation
- Content generation
- URL summarization
- Multi-language support"
```

---

## 📈 Mở rộng tính năng (Để charge thêm tiền)

```python
# Thêm vào bot.py:

# 1. Tóm tắt YouTube (cần youtube-transcript-api)
# /youtube [link] → tóm tắt video

# 2. Phân tích ảnh sản phẩm (DeepSeek Vision)
# Gửi ảnh → AI mô tả + viết caption tự động

# 3. FAQ tự động (RAG)
# Upload file FAQ → bot trả lời theo nội dung của shop

# 4. Giới hạn usage (để làm subscription)
# Đếm số request/ngày per user_id
```

---

## 🐛 Debug thường gặp

**Bot không phản hồi:**
- Kiểm tra TELEGRAM_TOKEN trong .env
- Chạy lại `python bot.py`, xem log lỗi

**Lỗi DeepSeek API:**
- Kiểm tra DEEPSEEK_API_KEY
- Kiểm tra balance & rate limit tại https://platform.deepseek.com
- Đảm bảo API key có quyền access chat/completions

**Lỗi khi tóm tắt URL:**
- Một số site chặn scraping (Google, Facebook)
- Dùng URL báo chí, blog, tin tức thông thường

---

## 💡 Tech Stack

- **python-telegram-bot** — Telegram Bot API wrapper
- **deepseek-api** — DeepSeek AI API (via httpx)
- **httpx** — Async HTTP client (fetch webpage + API calls)
- **python-dotenv** — Load .env file
- **Render.com** — Deploy & hosting

---

*Chúc bạn kiếm được nhiều tiền với bot này! 🚀*
