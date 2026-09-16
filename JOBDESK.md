# Job Desk — SIGMA (Sistem Informasi Government Monitoring & Assurance)

Project magang — Diskominfosantik Kabupaten Bekasi
Status: 🔒 **LOCKED — struktur final, tidak berubah sampai akhir project**

> Catatan: dokumen ini merupakan hasil penyusunan/finalisasi tim (dibantu AI untuk perapian format), bukan dokumen administratif resmi instansi. Pembagian tugas di bawah adalah acuan kerja internal kelompok.

---

## 1. Fathir — Modul 1: Cyber Threat & Reconnaissance

**Fokus:** Cyber threat detection dan passive reconnaissance.

**Tugas utama:**
- Membangun Google dorking crawler via **SerpAPI** untuk memindai indikasi kata kunci judi online pada sub-domain OPD, tanpa melakukan scraping langsung.
- Menjalankan port scanning dan vulnerability scanning berbasis template yang sudah ditentukan.
- Mendeteksi versi CMS/plugin yang usang (fingerprint), serta validasi dan pengecekan masa berlaku sertifikat SSL.
- Melakukan analisis eksposur data awal via **Shodan API** dan verifikasi reputasi domain via **VirusTotal API**.

**Tools:** Nmap (python-nmap), Nuclei, WhatWeb/Wappalyzer, Playwright (screenshot otomatis), sslyze/crt.sh, SerpAPI, Shodan API, VirusTotal API.

---

## 2. Filino (Ino) — Front-End: Dashboard & Portal Publik

**Fokus:** Antarmuka dashboard internal Diskominfo dan portal publik.

**Tugas utama:**
- Membangun sistem login dan hierarki tampilan dashboard dengan **RBAC** (Super Admin Diskominfo vs Staf OPD).
- Mengembangkan live regional status map, metric cards, dan feed ancaman/poisoning.
- Mengintegrasikan visualisasi grafik uptime & latency real-time.
- Menyiapkan portal publik dengan pembatasan informasi (hanya skor rapor & status umum, tanpa detail teknis).

**Tools:** React/Next.js, Tailwind CSS, Recharts/Chart.js, klien WebSocket.

---

## 3. Reyka — Back-End: Modul 2, Modul 3 & Core Infrastructure

**Fokus:** Ops & Risk Scoring (Modul 2), AI Assistant (Modul 3), infrastruktur inti.

**Tugas utama:**
- Membangun arsitektur API menyeluruh dengan **FastAPI**, autentikasi stateless berbasis JWT + Argon2.
- Mengelola database **PostgreSQL + pgvector** untuk data relasional dan vector embedding dokumen SOP.
- Mengonfigurasi task queue (Celery + Redis) untuk worker scanner asynchronous dengan interval rutin (mingguan / 6 jam / 1–5 menit).
- **Modul 2:** HTTP health check paralel asinkron + algoritma kalkulasi skor rapor (A–E).
- **Modul 3:** RAG chatbot berbasis dokumen regulasi e-Gov/SOP + integrasi bot notifikasi via Telegram.
- Menyusun deployment dengan Docker Compose.

**Tools:** Python (FastAPI), PostgreSQL + pgvector, Celery + Redis, httpx (async), LangChain/LlamaIndex, python-telegram-bot, JWT + Argon2, Docker Compose.

---

## Catatan penting kolaborasi

Algoritma skor rapor (A–E) adalah hasil penggabungan pembobotan temuan **Modul 1 (Fathir)** dan metrik **Modul 2 (Reyka)**. Fathir dan Reyka wajib koordinasi intensif untuk menentukan, menguji, dan menyesuaikan iterasi bobot algoritma berdasarkan hasil uji coba lapangan.

---

## Riwayat perubahan

| Tanggal | Perubahan | Oleh |
|---|---|---|
| — | Draf awal jobdesk disusun (referensi: dokumen DOC-CSIRT) | Tim |
| — | Finalisasi nama project → **SIGMA**, struktur di-lock | Tim |

> Jika ke depan *terpaksa* ada penyesuaian jobdesk, catat di tabel ini (tanggal, perubahan, alasan, siapa yang mengubah) — jangan diedit diam-diam.
