@echo off
REM Masuk ke direktori folder tempat file bat ini berada
cd /d %~dp0

REM Jalankan python dari dalam venv, lalu eksekusi file sql-doctor.py
venv\Scripts\python.exe sql-doctor.py

REM Menahan jendela Command Prompt agar tidak langsung tertutup setelah selesai
pause