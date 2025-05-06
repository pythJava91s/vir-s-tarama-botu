import os
import tkinter as tk
from tkinter import filedialog

# Şüpheli dosya uzantıları
suspicious_extensions = ['.exe', '.bat', '.vbs', '.js', '.dll']

def select_folder():
    root = tk.Tk()
    root.withdraw()  # Tkinter penceresini gizle
    folder_path = filedialog.askdirectory(title="Bir klasör seçin")  # Kullanıcıdan klasör seçmesi istenir
    return folder_path

def scan_files(folder_path):
    suspicious_files = []
    
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            if any(file_path.endswith(ext) for ext in suspicious_extensions):
                suspicious_files.append(file_path)
    
    return suspicious_files

def show_results(suspicious_files):
    if suspicious_files:
        print("Şüpheli Dosyalar Bulundu:")
        for file in suspicious_files:
            print(file)
    else:
        print("Şüpheli dosya bulunmadı.")

def main():
    print("Virüs Tarama Botu Başlatılıyor...")
    folder_path = select_folder()
    print(f"Tarama Başlatılıyor: {folder_path}")
    
    suspicious_files = scan_files(folder_path)
    
    show_results(suspicious_files)

if __name__ == "__main__":
    main()
