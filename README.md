# SIGMA — Sistem Informasi Government Monitoring & Assurance

Platform pemantauan keamanan dan operasional situs Organisasi Perangkat Daerah (OPD), dikembangkan sebagai project magang di Dinas Komunikasi, Informatika, Persandian dan Statistik (Diskominfosantik) Kabupaten Bekasi.

SIGMA berperan sebagai alat bantu tambahan yang terhubung dengan **BEKASIKAB-CSIRT** — bukan menggantikan, dan bukan entitas/tim baru.

**Status:** 🚧 Dalam pengembangan (project magang)

---

## Latar belakang

Ribuan situs pemerintah di Indonesia pernah disusupi konten judi online, dan gangguan layanan publik digital sering baru terdeteksi setelah ada laporan masyarakat, bukan lewat pemantauan internal yang proaktif. SIGMA dibangun untuk menutup celah itu dengan pemantauan otomatis dan berkala terhadap situs-situs OPD di lingkup Kabupaten Bekasi.

---

## Fitur utama

### Modul 1 — Cyber Threat & Reconnaissance
- Google dorking (via SerpAPI) untuk deteksi indikasi konten judi online (judol) pada sub-domain OPD, tanpa scraping langsung
- Port scanning dan vulnerability scanning
- Fingerprint CMS/plugin usang, pengecekan masa berlaku SSL
- Passive recon lewat Shodan API dan VirusTotal API

### Modul 2 — Operations & Risk Scoring
- Uptime dan latency monitoring real-time (HTTP health check paralel asinkron)
- Algoritma skor rapor keamanan A–E per OPD (gabungan temuan Modul 1 + metrik operasional)

### Modul 3 — AI Assistant & Alert
- RAG chatbot untuk SOP penanganan insiden dan regulasi e-Gov
- Notifikasi otomatis via Telegram bot

---

## Dashboard & akses
- Login dengan RBAC (Super Admin Diskominfo vs Staf OPD)
- Live regional status map, metric cards, threat/poisoning feed
- Portal publik (skor rapor dan status umum saja, tanpa detail teknis)

> ⚠️ Pemindaian aktif (port scan, vulnerability scan) terhadap domain OPD hanya dijalankan dengan izin tertulis dan ruang lingkup yang disetujui oleh Diskominfosantik Kabupaten Bekasi.

---

## Tech stack

| Layer | Teknologi |
|---|---|
| Backend | Python (FastAPI) |
| Frontend | React / Next.js, Tailwind CSS |
| Database | PostgreSQL + pgvector |
| Task queue | Celery + Redis |
| Real-time | WebSocket |
| AI / RAG | LangChain/LlamaIndex |
| Auth | JWT + Argon2 |
| Deployment | Docker Compose |

Detail lengkap tools per modul ada di [`JOBDESK.md`](./JOBDESK.md).

---

## Tim

| Nama | Peran |
|---|---|
| Fathir | Cyber Threat & Reconnaissance (Modul 1) |
| Filino (Ino) | Front-End — Dashboard & Portal Publik |
| Reyka | Back-End — Modul 2, Modul 3, Core Infrastructure |

Pembagian tugas lengkap dan final: lihat [`JOBDESK.md`](./JOBDESK.md).

---

## Disclaimer

Project ini dikembangkan untuk keperluan magang dan tugas akhir. Seluruh aktivitas pemindaian aktif terhadap sistem produksi dilakukan hanya dengan otorisasi tertulis dari Diskominfosantik Kabupaten Bekasi.

## Lisensi

(Belum ditentukan — sesuaikan dengan arahan pembimbing lapangan/instansi sebelum rilis publik.)
