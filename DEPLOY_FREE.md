# 🚀 Deploy Bot Telegram 100% FREE (2025)

Railway tính phí, nên dưới đây là các option **thực sự miễn phí**:

---

## Option 1: Render.com ⭐ (Recommended)

✅ **Free tier vĩnh viễn**  
✅ **Chạy 24/7 (không sleep như Heroku)**  
✅ **Dễ deploy nhất**

### Bước 1: Setup bot chạy dưới dạng service
Sửa `bot.py` thêm error handling:

```python
# Thêm ở dầu file
import time
import traceback

# Thêm vào hàm main() trước app.run_polling():
while True:
    try:
        logger.info("🤖 Bot đang chạy...")
        app.run_polling(allowed_updates=Update.ALL_TYPES)
    except Exception as e:
        logger.error(f"❌ Lỗi: {e}")
        traceback.print_exc()
        logger.info("⏳ Chờ 10 giây rồi restart...")
        time.sleep(10)
```

### Bước 2: Push code lên GitHub
```bash
git init
git add .
git commit -m "deploy telegram bot"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/telegram-ai-bot.git
git push -u origin main
```

### Bước 3: Deploy lên Render
1. Vào https://render.com → Sign up with GitHub
2. Click **New +** → **Web Service**
3. Chọn repo `telegram-ai-bot`
4. Config:
   - **Name:** telegram-ai-bot
   - **Runtime:** Python 3
   - **Build command:** `pip install -r requirements.txt`
   - **Start command:** `python bot.py`
5. Vào **Environment** → Add 2 biến:
   - `TELEGRAM_TOKEN` = token của bạn
   - `ANTHROPIC_API_KEY` = API key của bạn
6. Click **Deploy** → Xong!

Bot sẽ chạy 24/7 free, không bao giờ ngủ.

---

## Option 2: Fly.io 🎯

✅ **Free tier**: 3 shared VM instances  
✅ **Chạy 24/7**  
⚠️ **Hơi phức tạp hơn Render**

### Bước 1: Cài Flyctl CLI
```bash
# macOS
brew install flyctl

# Linux
curl -L https://fly.io/install.sh | sh

# Windows
choco install flyctl
```

### Bước 2: Deploy
```bash
flyctl auth login
flyctl launch  # Chọn Yes cho các prompts
flyctl deploy
```

### Bước 3: Set environment variables
```bash
flyctl secrets set TELEGRAM_TOKEN=your_token
flyctl secrets set ANTHROPIC_API_KEY=your_key
```

---

## Option 3: Replit (Nhanh nhất, nhưng có limit)

✅ **Không cần GitHub**  
✅ **Code online, run ngay**  
⚠️ **Free tier chỉ chạy 1 giờ/ngày** (cần subscription $7/tháng để 24/7)

### Bước 1: Upload code lên Replit
1. Vào https://replit.com → Create → Python
2. Upload files: `bot.py`, `requirements.txt`
3. Setup `.env` với token + API key

### Bước 2: Run
```bash
python bot.py
```

**Workaround để chạy 24/7 free:**  
Dùng **UptimeRobot** (free service):
1. Vào https://uptimerobot.com
2. Thêm Replit URL để "ping" mỗi 5 phút
3. Replit sẽ không tắt

---

## Option 4: PythonAnywhere 🐍

✅ **Python-specific, dễ setup**  
✅ **Free tier 24/7**  
⚠️ **Limited capabilities**

1. Vào https://pythonanywhere.com → Sign up
2. Upload files
3. Tạo Web App → Python + setup requirements
4. Run `python bot.py` trong console

---

## 💰 So sánh

| Platform | Giá | Uptime | Dễ |
|----------|-----|--------|-----|
| **Render** | FREE | 24/7 ✅ | ⭐⭐⭐⭐⭐ |
| **Fly.io** | FREE* | 24/7 ✅ | ⭐⭐⭐⭐ |
| **Replit** | FREE* | 1h/ngày | ⭐⭐⭐ |
| **PythonAnywhere** | FREE | 24/7 ✅ | ⭐⭐⭐⭐ |

*Fly.io & Replit có trả phí nếu dùng nhiều, nhưng free tier đủ cho bot nhỏ

---

## 🎯 Recommend: Render.com

**Tại sao?**
- 100% FREE, chạy 24/7, không sleep
- Deploy dễ nhất (chỉ cần push GitHub)
- Không cần setup CLI hoặc Docker
- Support tốt

**Chi phí thực tế:**
- $0/tháng (free tier unlimited)
- Nếu traffic cao thì pay-as-you-go, nhưng bot chat không bao giờ cao

---

## ⚠️ Cẩn thận

**Render sẽ pause service nếu:**
- Không có traffic 15 phút
- **Solution:** Dùng UptimeRobot để ping mỗi 10 phút (free)

**Setup UptimeRobot:**
1. Vào uptimerobot.com
2. Create monitor (HTTP) → điểm vào Render URL
3. Chọn interval 10 phút
4. Service sẽ luôn sống

---

## 🚀 Quick Start (Render)

```bash
# 1. Push lên GitHub
git push

# 2. Vào render.com
# Click New Web Service → Select GitHub repo
# Add env vars: TELEGRAM_TOKEN, ANTHROPIC_API_KEY
# Click Deploy

# 3. Setup UptimeRobot (ngăn Render pause)
# uptimerobot.com → Add HTTP monitor → interval 10 min

# 4. Done! Bot chạy 24/7 free
```

Sau khi deploy, hãy test bot trên Telegram — nó nên respond ngay!

---

*Chúc bạn kiếm tiền với bot free này! 💰*
