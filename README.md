# Update: Dynamic TTS Output Length (v2025-07-22)

**How does the agent work?**
- On each call, the first AI voice response is limited to 200 characters for a concise intro.
- All following responses in the same call are limited to 100 characters each.
- This prevents long (1.5+ minute) TTS outputs and Twilio timeouts.
- You can easily change these limits in `app/main.py` (`max_tts_length`).

**Why?**
- Previously, long LLM outputs caused TTS to generate very long audio, leading to Twilio timeouts and failed calls.
- With this update, the system is robust, responsive, and Twilio-friendly by default.

---

# Türkiye'den Kullanıcılar için Hızlı Başlangıç Rehberi

Bu projeyi Türkiye'de kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyin:

1. **Python Kurulumu:**
   - Python 3.9 veya üzeri bir sürüm indirin ve kurun: https://www.python.org/downloads/
   - Kurulum sırasında "Add Python to PATH" seçeneğini işaretleyin.

2. **Projeyi İndirin:**
   - GitHub'dan projeyi indirin veya klonlayın:
     ```sh
     git clone https://github.com/PrinceNanChan/AI_Voice_Agent-Phi-2_Q4_K_M.git
     cd AI_Voice_Agent-Phi-2_Q4_K_M
     ```

3. **Sanal Ortam Oluşturun ve Aktif Edin:**
   - Windows:
     ```sh
     python -m venv .venv
     .venv\Scripts\activate
     ```
   - Linux/macOS:
     ```sh
     python3 -m venv .venv
     source .venv/bin/activate
     ```

4. **Gereken Paketleri Yükleyin:**
   ```sh
   pip install -r requirements.txt
   ```

5. **Model Dosyasını İndirin:**
   - `models/` klasörüne HuggingFace veya benzeri bir kaynaktan `phi-2.Q4_K_M.gguf` dosyasını indirin ve ekleyin.

6. **.env Dosyasını Oluşturun:**
   - Proje kök dizininde `.env.example` dosyasını kopyalayarak `.env` oluşturun ve kendi Twilio bilgilerinizi girin:
     ```sh
     copy .env.example .env  # Windows
     # veya
     cp .env.example .env    # Linux/macOS
     ```
   - `.env` dosyasını bir metin editörüyle açıp Twilio SID ve Auth Token'ınızı girin.

7. **Bilgi Tabanı Vektör İndeksini Oluşturun:**
   ```sh
   python -m app.vector_search
   ```

8. **Sunucuyu Başlatın:**
   ```sh
   uvicorn app.main:app --reload
   ```

9. **Ngrok ile Sunucunuzu Dışarıya Açın:**
   - Ngrok'u indirin ve çalıştırın:
     ```sh
     ngrok http 8000
     ```
   - Size verilen public URL'yi not alın (ör: `https://xxxxxx.ngrok-free.app`).

10. **Twilio Webhook Ayarlarını Yapın:**
    - Twilio hesabınızda, telefon numaranızın Voice webhook adresini şu şekilde ayarlayın:
      ```
      https://<ngrok-url>/twilio_voice
      ```
    - `<ngrok-url>` kısmını kendi ngrok adresinizle değiştirin.

11. **Test Edin:**
    - Kendi telefonunuzdan Twilio numaranızı arayarak sistemi test edebilirsiniz.

---
