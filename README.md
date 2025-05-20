 # 🔐 Ransomware Decryption Bruteforce Tool

This project simulates a real-world ransomware response scenario where the encrypted file must be decrypted without paying ransom.  
Built during the **AIG Shields Up: Cybersecurity Job Simulation** hosted on Forage.

---

## 🎯 Objective

To write a Python script that bruteforces the decryption key of a ransomware-encrypted file using a provided password list (Rockyou subset).

---

## 💡 What It Does

- Loads a `.zip` encrypted file
- Iterates through a password list
- Attempts to extract the file using each password
- Logs and prints the correct password once found

---

## 🛠️ Tools & Technologies

- Python 3.8+
- `zipfile` and `itertools`
- Rockyou password list (small subset for testing)

---
 

