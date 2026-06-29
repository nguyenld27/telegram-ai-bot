# 🚀 DeepSeek API Setup & Pricing Guide

DeepSeek là LLM Trung Quốc mạnh mẽ, rẻ hơn Claude & OpenAI rất nhiều.

---

## 💳 Lấy API Key (2 phút)

### Bước 1: Tạo tài khoản DeepSeek
1. Vào https://platform.deepseek.com
2. Click **Sign Up** → Dùng Email / Google / GitHub
3. Xác thực email

### Bước 2: Tạo API Key
1. Dashboard → **API Keys**
2. Click **+ Create New API Key**
3. Copy key (dạng `sk-...`) → Lưu vào `.env`

### Bước 3: Add Credits
1. Vào **Billing** → **Recharge**
2. Nạp từ $5 trở lên (dùng card Visa/Mastercard)
3. Credits sẽ expire sau 1 năm nếu không dùng

---

## 💰 Pricing

### Chi phí API

| Model | Input (per 1M tokens) | Output (per 1M tokens) |
|-------|----------------------|------------------------|
| **deepseek-chat** | $0.14 | $0.28 |
| **deepseek-reasoner** | $0.55 | $2.19 |

**So sánh:**
- Claude 3.5 Sonnet: $3 input, $15 output
- GPT-4o: $5 input, $15 output
- **DeepSeek: $0.14 input, $0.28 output** ✨ (30x rẻ hơn!)

### Ước tính chi phí bot Telegram

**1 user chat 100 tin nhắn/ngày:**
- Mỗi tin: ~100 tokens input + 100 tokens output
- Chi phí/tin: $0.000042
- Chi phí/user/tháng: ~$0.13

**100 users → ~$13/tháng** (cực rẻ!)

---

## 🔧 Kiểm tra API hoạt động

```bash
# Test API call
curl -X POST https://api.deepseek.com/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "model": "deepseek-chat",
    "messages": [
      {"role": "user", "content": "Hello!"}
    ],
    "max_tokens": 100
  }'
```

Nếu response có `"content"` → API key đúng ✅

---

## ⚙️ Config bot để dùng DeepSeek

File `bot.py` đã sẵn config DeepSeek. Chi cần:

1. Lấy API Key từ https://platform.deepseek.com
2. Thêm vào `.env`:
```
DEEPSEEK_API_KEY=sk-xxx...
TELEGRAM_TOKEN=123...
```

3. Chạy bot:
```bash
python bot.py
```

---

## 🎯 Model nào dùng tốt nhất?

### **deepseek-chat** (Recommended)
- Nhanh, rẻ, tốt cho chat bình thường
- Đủ smart cho tóm tắt, viết content, QA
- Thích hợp sản xuất

### **deepseek-reasoner**
- Thông minh hơn (tương đương GPT-4)
- Chậm hơn (vì dùng reasoning)
- Giá gấp 10x
- Chỉ dùng cho bài toán phức tạp

**Bot này dùng `deepseek-chat` (đơn giản, nhanh, rẻ)**

---

## 🐛 Debug DeepSeek API

**Lỗi: "Unauthorized"**
- API key sai hoặc hết hạn
- Kiểm tra lại key tại https://platform.deepseek.com

**Lỗi: "Rate limit exceeded"**
- Gửi quá nhiều request
- DeepSeek sẽ rate limit nếu >60 requests/min
- Thêm delay giữa requests

**Lỗi: "Insufficient credits"**
- Hết balance
- Nạp thêm credits tại Billing

---

## 📊 So sánh LLM

| LLM | Input | Output | Speed | Tiếng Việt |
|-----|-------|--------|-------|-----------|
| **DeepSeek** | $0.14 | $0.28 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Claude 3.5 | $3 | $15 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| GPT-4o | $5 | $15 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| Llama 3.1 | Free (self-host) | Free (self-host) | ⭐⭐ | ⭐⭐ |

**DeepSeek thắng về:** Giá, tốc độ, tiếng Việt.

---

## 🎁 Free tier DeepSeek?

DeepSeek **không có free tier**, nhưng:
- $5 credits khi đăng ký (dùng test được 2-3 ngày)
- Rất rẻ → nạp $10 dùng hết 6-12 tháng

**Nên nạp:** $5-10 đầu tiên để test

---

## 🔐 Security

✅ API Key là secret — giữ kín trong `.env`
✅ Không commit `.env` lên GitHub (thêm vào `.gitignore`)
✅ DeepSeek không store chat history (lợi duyên bảo vệ)

---

*Chúc bạn dùng DeepSeek hiệu quả! 🚀*
