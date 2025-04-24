# 🔔 Buzzer Game Web App

Aplikasi web buzzer interaktif untuk game show, kuis, atau perlombaan. Setiap pemain bisa menekan tombol buzzer di perangkat mereka masing-masing dan server akan mencatat urutan siapa yang pertama kali menekan.

---

## 🚀 Fitur
- Setiap pemain menekan tombol buzzer dan server langsung mencatat urutan buzzer.
- Hanya pemain yang pertama menekan tombol yang akan memutar suara khasnya.
- Panel admin (server) menampilkan urutan buzzer secara real-time.
- Game dapat di-reset kapan saja oleh admin.

---

## 📦 Struktur Proyek
```
├── app.py                  # Aplikasi Flask utama
├── requirements.txt        # Daftar dependency Python
├── Procfile                # Untuk deployment (Gunicorn, jika deploy di Railway)
├── static/
│   ├── style.css           # Styling untuk player
│   ├── server.css          # Styling untuk panel server
│   └── sounds/
│       ├── player1.mp3     # Suara pemain 1
│       ├── player2.mp3     # Suara pemain 2
│       └── ...             # Suara pemain lainnya
├── templates/
│   ├── player.html         # Halaman untuk setiap pemain
│   └── server.html         # Halaman panel server
```

---

## 💻 Menjalankan di Lokal dengan Ngrok

### 1. Clone repo dan masuk ke folder
```bash
git clone https://github.com/Kaguai10/bell_game.git
cd buzzer-app
```

### 2. Buat virtual environment dan aktifkan
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scriptsctivate     # Windows
```

### 3. Install dependensi
```bash
pip install -r requirements.txt
```

### 4. Jalankan aplikasi Flask
```bash
python app.py
```

Aplikasi akan berjalan di [http://localhost:5000](http://localhost:5000) di komputer kamu.

### 5. Jalankan Ngrok untuk membuat aplikasi publik
Download dan instal [ngrok](https://ngrok.com/), lalu jalankan perintah berikut di terminal:
```bash
ngrok http 5000
```

Ngrok akan memberikan URL publik yang mengarah ke server lokal kamu, misalnya:
```
Forwarding                    http://xyz123.ngrok.io -> http://localhost:5000
```

Kamu bisa membagikan URL yang diberikan oleh ngrok (misalnya `http://xyz123.ngrok.io`) ke pemain lain atau admin untuk bermain.

---

## ⚠ Catatan
- **ngrok** hanya akan aktif selama sesi berjalan. Jika kamu memulai ulang `ngrok` atau komputer, URL-nya akan berubah.
- Pastikan semua suara (misalnya `player1.mp3`, `player2.mp3`) ada di dalam folder `static/sounds/`.
- Jika kamu deploy di platform lain seperti Railway, pastikan **`Procfile`** berisi:
  ```
  web: gunicorn app:app
  ```
- Jika aplikasi perlu dijalankan dalam produksi (bukan development), gunakan **Gunicorn** untuk menjalankan Flask.

---

## 📫 Kontak
By: [@Kaguai](https://github.com/kaguai)
