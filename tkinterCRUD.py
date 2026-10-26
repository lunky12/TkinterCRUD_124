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


