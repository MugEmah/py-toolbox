# -*- coding: utf-8 -*-
"""
Created on Wed Sep  3 21:49:42 2025

@author: mugee
"""


import os
import tarfile
import zipfile
import time
import sys

SOURCE_DIR = r"D:\www.bemyone.com"    #Change to your source folder
BACKUP_DIR = r"C:\Users\mugee\Desktop\Python projects\BK"  #Change to your backup folder
MAX_BACKUPS = 5   # How many backups to keep
BACKUP_FORMAT = "zip"   # "zip" for windows machines or "tar.gz" for Linux/macOS

def create_tar_backup(backup_path):
    with tarfile.open(backup_path, "w:gz", encoding="utf-8") as tar:
        tar.add(SOURCE_DIR, arcname=os.path.basename(SOURCE_DIR), recursive=True)

def create_zip_backup(backup_path):
    with zipfile.ZipFile(backup_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(SOURCE_DIR):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, os.path.dirname(SOURCE_DIR))
                zipf.write(file_path, arcname)
    
def create_backup():
    os.makedirs(BACKUP_DIR, exist_ok=True)
    
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    ext = "zip" if BACKUP_FORMAT == "zip" else "tar.gz"
    backup_filename = f"backup_{timestamp}.{ext}"
    backup_path = os.path.join(BACKUP_DIR, backup_filename)
    
    print(f"[+] Creating {BACKUP_FORMAT} backup: {backup_path}")

    if BACKUP_FORMAT == "zip":
        create_zip_backup(backup_path)
    else:
        create_tar_backup(backup_path)
        
    print("[+] Backup created successfully.")
    
def cleanup_backups():
    backups = sorted(
        [f for f in os.listdir(BACKUP_DIR) if f.startswith("backup_") and (f.endswith(".zip") or f.endswith(".tar.gz"))]
        )
    
    if len(backups) > MAX_BACKUPS:
        to_remove = len(backups) - MAX_BACKUPS
        print(f"[!] Removing {to_remove} old backups(s).")
        for old_backup in backups[:to_remove]:
            old_path = os.path.join(BACKUP_DIR, old_backup)
            os.remove(old_path)
            print(f"[x] Removed {old_path}")
            
def main():
    try:
        create_backup()
        cleanup_backups()
    except Exception as e:
        print(f"[!] Error: {e}")
        sys.exit(1)
    
if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    