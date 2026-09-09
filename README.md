# SQL Doctor

Penganalisis basis data SQL bertenaga AI menggunakan RAG (Retrieval-Augmented Generation). Unggah file skema SQL Anda dan dapatkan penjelasan instan, query, serta wawasan tentang struktur basis data Anda.

## Fitur

- Menganalisis skema basis data SQL menggunakan bahasa alami
- Mendapatkan penjelasan detail tentang tabel, relasi, dan query
- Menghasilkan query SQL dari pertanyaan dalam bahasa Indonesia
- Mendukung beberapa file basis data
- Antarmuka CLI interaktif

## Prasyarat

- Python 3.8+
- API key MistralAI

## Instalasi

1. Clone repository:
```bash
git clone https://github.com/yourusername/sql-doctor.git
cd sql-doctor
```

2. Buat virtual environment:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. Instal dependensi:
```bash
pip install -r requirements.txt
```

4. Buat file `.env`:
```env
MISTRAL_API_KEY=your_api_key_here
BASE_URL=your_base_url_here
MISTRAL_MODEL=your_model_name_here
```

5. Tambahkan file SQL ke folder `db/`

## Penggunaan

1. Jalankan aplikasi:
```bash
python sql-doctor.py
```

2. Pilih file basis data dari daftar

3. Ajukan pertanyaan tentang basis data Anda:
```
Apa saja tabel yang ada di database ini?
Bagaimana cara membuat query untuk mengambil semua user?
Jelaskan hubungan antara tabel orders dan customers
```

4. Ketik `/q`, `/exit`, atau `/quit` untuk keluar

## Struktur Proyek

```
sql-doctor/
├── db/                 # File skema SQL
├── venv/               # Virtual environment
├── .env                # Variabel environment (tidak di-commit)
├── requirements.txt    # Dependensi Python
└── sql-doctor.py       # Aplikasi utama
```

## Cara Kerja

1. **Pemuatan Dokumen**: File SQL dimuat dan dibagi menjadi bagian-bagian kecil
2. **Embeddings**: Teks yang sudah dipecah dikonversi menjadi vektor embeddings menggunakan MistralAI
3. **Vektor Penyimpanan**: Embeddings disimpan di ChromaDB untuk pengambilan cepat
4. **Pipa RAG**: Pertanyaan pengguna mengambil konteks relevan dan menghasilkan respons

## Teknologi

- [LangChain](https://github.com/langchain-ai/langchain) - Framework LLM
- [ChromaDB](https://github.com/chroma-core/chroma) - Basis data vektor
- [MistralAI](https://mistral.ai/) - LLM dan embeddings

## Lisensi

MIT
"# SQL-Doctor" 
