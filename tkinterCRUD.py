import sqlite3
from tkinter import messagebox
import tkinter as tk


def buat_tabel():
  """Membuat database dan tabel nilai_siswa jika belum ada"""
  conn = sqlite3.connect("database_siswa.db")
  cursor = conn.cursor()
  cursor.execute("""
        CREATE TABLE IF NOT EXISTS nilai_siswa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama_siswa TEXT,
            biologi INTEGER,
            fisika INTEGER,
            inggris INTEGER,
            prediksi_fakultas TEXT
        )
    """)
  conn.commit()
  conn.close()


def submit_data():
  """Fungsi untuk memproses nilai, memprediksi fakultas, dan menyimpan ke SQLite"""
  nama = entry_nama.get()

  # Validasi input kosong
  if not nama:
    messagebox.showwarning("Peringatan", "Nama siswa tidak boleh kosong!")
    return

  try:
    biologi = int(entry_biologi.get())
    fisika = int(entry_fisika.get())
    inggris = int(entry_inggris.get())
  except ValueError:
    messagebox.showerror(
        "Error", "Nilai Biologi, Fisika, dan Inggris harus berupa angka!"
    )
    return
