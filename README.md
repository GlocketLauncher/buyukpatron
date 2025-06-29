# 🧠 Büyük Patron Discord Botu

Kariyer ve kişilik analizi yapan, eğlenceli GIF’lerle etkileşim kuran yapay zekâ destekli Discord botudur.

## 🚀 Özellikler

- 👤 `!analiz`: Kullanıcının sorulara verdiği cevaplara göre kişilik analizi yapar ve uygun meslek önerir.
- 💼 `!meslek <meslek_adı>`: Yazılan meslek hakkında GPT destekli detaylı bilgi verir.
- 🖼️ Otomatik GIF gönderimi:
  - "iş", "job", "snake", "invincible" gibi kelimeler geçtiğinde uygun görsel gönderir.
- 💾 SQLite veritabanına kişilik analizlerini kaydeder.
- 🤖 Yapay zekâ motoru olarak Groq AI (llama3) kullanır.

---

## 📦 Kurulum

1. Reponun bir kopyasını indir:
```bash
git clone https://github.com/GlocketLauncher/buyukpatron.git
cd buyukpatron



gerekli kütüphaneleri kur:
pip install -r requirements.txt



config_example.py dosyasını config.py olarak değiştir




📁 Dosya Yapısı



buyukpatron/
├── main.py              # Botun ana dosyası
├── ai.py                # Yapay zekâ yanıtları
├── data.py              # Veritabanı işlemleri (SQLite)
├── personality.py       # Sorular ve analiz algoritması
├── meme/                # İş kelimesi için gifler
├── invisible/           # Snake içerikleri
├── invincible/          # Sundowner içerikleri
├── config.py            # (GİZLİ) API anahtarları
└── README.md            # Bu dosya
