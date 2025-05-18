 # 🧠 Ransomware Decryption Bruteforce – Project Notes

This project was completed as part of the **AIG Shields Up: Cybersecurity Virtual Experience** on Forage.

---

## 🎯 Objective

Simulate a real-world ransomware recovery scenario by **writing a Python script to bruteforce a decryption key** for a zip file encrypted by a ransomware variant.

The task emphasized breaking the encryption **ethically** using known password lists, rather than paying the ransom, as per the internal policy of the simulated organization.

---

## 💻 Scenario

- An attacker exploited a zero-day vulnerability (Log4j) in a product staging server.
- The ransomware was only partially deployed, encrypting a single `.zip` file.
- The goal was to recover the file **without paying** the attacker.

---

## 🔧 Technical Summary

- Used **Python 3** with the built-in `zipfile` module to iterate over a provided wordlist.
- The script attempted each password until it successfully extracted the contents.
- This simulates a basic form of **offline brute force attack** using a subset of the popular RockYou wordlist.

---

## 📸 Screenshots

### 🔍 Script in Action
![Terminal Screenshot](../screenshots/terminal-demo.png)

### 🗂️ Encrypted Zip File and Wordlist
![Encrypted File Structure](../screenshots/encrypted-folder.png)

### ✅ Successful Decryption Output
![Decryption Success](../screenshots/success-output.png)

> _Note: Replace the above image paths with your actual screenshots under `/screenshots/` folder._

---

## 📚 Key Skills Practiced

- Writing and running Python scripts to handle encrypted archives
- Understanding brute-force logic and handling exceptions
- Automation of security tasks in incident response situations
- Simulating real-world blue team scenarios

---

## 📌 Lessons Learned

- Brute-force attacks can work on weak encryption if poor passwords are used.
- Organizations should not rely on security through obscurity or default tooling.
- Regular backups, employee awareness, and proper patching are essential to reduce ransomware impact.
- Prevention is key, but **preparation for incident response** is just as important.

---

## 🤝 Acknowledgements

- AIG Cybersecurity Team (Virtual Scenario)
- Forage (Platform)
- Wordlist: Subset from RockYou

---
