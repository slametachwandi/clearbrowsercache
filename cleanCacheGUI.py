import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import threading

# Daftar perintah erase dan RD satu per satu
commands = [
    'erase "%TEMP%\\*.*" /f /s /q',
    'for /D %%i in ("%TEMP%\\*") do RD /S /Q "%%i"',
    'erase "%TMP%\\*.*" /f /s /q',
    'for /D %%i in ("%TMP%\\*") do RD /S /Q "%%i"',
    'erase "%ALLUSERSPROFILE%\\TEMP\\*.*" /f /s /q',
    'for /D %%i in ("%ALLUSERSPROFILE%\\TEMP\\*") do RD /S /Q "%%i"',
    'erase "%SystemRoot%\\TEMP\\*.*" /f /s /q',
    'for /D %%i in ("%SystemRoot%\\TEMP\\*") do RD /S /Q "%%i"',
    'RunDll32.exe InetCpl.cpl,ClearMyTracksByProcess 8',
    'erase "%LOCALAPPDATA%\\Microsoft\\Windows\\Tempor~1\\*.*" /f /s /q',
    'for /D %%i in ("%LOCALAPPDATA%\\Microsoft\\Windows\\Tempor~1\\*") do RD /S /Q "%%i"',
    'erase "%LOCALAPPDATA%\\Google\\Chrome\\User Data\\*.*" /f /s /q',
    'for /D %%i in ("%LOCALAPPDATA%\\Google\\Chrome\\User Data\\*") do RD /S /Q "%%i"',
    'erase "%LOCALAPPDATA%\\Mozilla\\Firefox\\Profiles\\*.*" /f /s /q',
    'for /D %%i in ("%LOCALAPPDATA%\\Mozilla\\Firefox\\Profiles\\*") do RD /S /Q "%%i"'
]

# Fungsi untuk menjalankan pembersihan
def run_cleanup():
    progress["maximum"] = len(commands)
    for i, cmd in enumerate(commands, 1):
        status_var.set(f"Menjalankan: {cmd}")
        try:
            subprocess.run(cmd, shell=True, check=True)
        except subprocess.CalledProcessError:
            status_var.set(f"Gagal: {cmd}")
        progress["value"] = i
        root.update_idletasks()
    messagebox.showinfo("Selesai", "Pembersihan selesai.")
    status_var.set("Selesai.")

# Jalankan di thread agar GUI tidak freeze
def start_thread():
    t = threading.Thread(target=run_cleanup)
    t.start()

# GUI
root = tk.Tk()
root.title("Pembersih Sampah Windows")
root.geometry("500x200")
root.resizable(False, False)

frame = ttk.Frame(root, padding=20)
frame.pack(fill="both", expand=True)

ttk.Label(frame, text="Tekan tombol di bawah untuk membersihkan file sementara").pack(pady=10)

progress = ttk.Progressbar(frame, orient="horizontal", length=400, mode="determinate")
progress.pack(pady=10)

status_var = tk.StringVar()
status_label = ttk.Label(frame, textvariable=status_var, foreground="blue")
status_label.pack()

start_btn = ttk.Button(frame, text="Mulai Pembersihan", command=start_thread)
start_btn.pack(pady=10)

root.mainloop()
