![alt text](https://github.com/FelixHainslyMartin/Project-ASAS-Coding/blob/main/Image.png?raw=true)
---

## 📘 Bank Soal Matematika

Aplikasi web sederhana untuk mengelola soal-soal pelajaran Matematika berdasarkan tingkat kesulitan. Dibangun menggunakan **Flask**, **SQLite**, dan mengikuti pola **MVC (Model-View-Controller)**.

---

### 🔧 Fitur Utama

* Menambah soal matematika (pertanyaan + jawaban)
* Mengedit dan menghapus soal
* Filter soal berdasarkan tingkat kesulitan (Mudah, Sedang, Sulit)
* Tampilan modern dan responsif (mobile-friendly)
* Menggunakan database SQLite bawaan

---

### 📁 Struktur Proyek

```
bank_soal/
├── app.py              # Controller (routing dan logika utama)
├── models.py           # Model (ORM dengan SQLAlchemy)
├── soal.db             # Database SQLite
├── templates/          # View (HTML templates)
│   ├── base.html
│   ├── list_soal.html
│   └── form_soal.html
└── static/
    └── style.css       # Tampilan CSS modern
```

---

### ▶️ Cara Menjalankan

#### 1. 🔃 Clone atau unduh proyek ini

```bash
git clone https://github.com/FelixHainslyMartin/Project-ASAS-Coding
cd Project-ASAS-Coding
```

#### 2. 📦 Install dependensi

Pastikan kamu menggunakan **Python 3.7+** dan sudah mengaktifkan virtual environment:

```bash
pip install flask sqlalchemy
```

#### 3. 🚀 Jalankan server Flask

```bash
python app.py
```

Akses aplikasi melalui browser di:
👉 `http://127.0.0.1:5000`

---

### 💾 Database

Aplikasi ini menggunakan **SQLite** sebagai penyimpanan lokal. Tabel akan otomatis dibuat saat pertama kali dijalankan.

---

### 💡 Catatan Tambahan

* Untuk deploy ke server produksi, gunakan `gunicorn` atau `uwsgi`.
* Untuk versi dengan login admin, upload soal gambar, dan eksport PDF, bisa dikembangkan lebih lanjut.

---

### 🧑‍💻 Dibuat dengan Flask

Proyek ini cocok untuk:

* Tugas sekolah/kuliah berbasis web
* Contoh implementasi CRUD dengan Flask
* Latihan pengembangan aplikasi MVC dengan Python

---

-> Made by Felix Hainsly Martin XI IPA 1 <-