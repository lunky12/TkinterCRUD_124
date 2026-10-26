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

  # Logika Penentuan Prediksi Fakultas Berdasarkan Nilai Tertinggi
  if biologi > fisika and biologi > inggris:
    prediksi = "Kedokteran"
  elif fisika > biologi and fisika > inggris:
    prediksi = "Teknik"
  elif inggris > biologi and inggris > fisika:
    prediksi = "Bahasa"
  else:
    prediksi = "Umum / Nilai Bersaing Sama"

  # Menyimpan data ke database SQLite
  try:
    conn = sqlite3.connect("database_siswa.db")
    cursor = conn.cursor()
    cursor.execute(
        """
            INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, prediksi_fakultas)
            VALUES (?, ?, ?, ?, ?)
        """,
        (nama, biologi, fisika, inggris, prediksi),
    )
    conn.commit()
    conn.close()

    messagebox.showinfo(
        "Sukses",
        f"Data berhasil disimpan!\nPrediksi Fakultas: {prediksi}",
    )
    clear_entries()
  except Exception as e:
    messagebox.showerror("Error", f"Gagal menyimpan ke database: {e}")


def clear_entries():
  """Mengosongkan input field setelah submit"""
  entry_nama.delete(0, tk.END)
  entry_biologi.delete(0, tk.END)
  entry_fisika.delete(0, tk.END)
  entry_inggris.delete(0, tk.END)


