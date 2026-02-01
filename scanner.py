import keyword
import os
import hashlib
from traceback import print_tb

from yaml import scan

# Supicious extensions commonly
SUSPICIOUS_EXTENSIONS = [".exe", ".scr", ".bat", ".ps1", ".vbs"]

# Suspicious File Name Keywords
SUSPICIOUS_KEYWORDS = ["invoice", "payment", "urgent", "password"]

def calculate_hash(file_path):
  sha256 = hashlib.sha256()
  try:
    with open(file_path, "rb") as f:
      while chunk := f.read(4096):
        sha256.update(chunk)
      return sha256.hexdigest()
  except:
    return None

def scan_folder(folder_path):
  print(f"\n SCANNING FOLDER : {folder_path}\n")

  for root, dirs, files in os.walk(folder_path):
    for file in files:
      file_path = os.path.join(root, file)
      risk = 0
      reasons = []

      # Extension Check
      if any(file.lower().endswith(ext) for ext in SUSPICIOUS_EXTENSIONS):
        risk += 1
        reasons.append("Suspicious Extension")

      # File Name keyword check
      if any(keyword in file.lower() for keyword in SUSPICIOUS_KEYWORDS):
        risk += 1
        reasons.append("Suspicious Filename")

      file_hash = calculate_hash(file_path)

      if risk > 0:
        print("SUSPICIOUS FILE FOUND")
        print(f"File : {file_path}")
        print(f"SHA256 : {file_hash}")
        print(f"Risk Level : {'HIGH' if risk >= 2 else 'MEDIUM'}")
        print(f"Reason : {', '.join(reasons)}\n")
      else:
        print("\n No SUSPICIOUS FILE FOUND.\n")

if __name__ == "__main__":
  folder = input("Enter Folder Path To SCAN : ")
  scan_folder(folder)
