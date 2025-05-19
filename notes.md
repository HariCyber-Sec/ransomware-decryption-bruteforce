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

- Built using Python 3 the script loops through a list of common passwords to crack an encrypted ZIP file.
- It automatically tries each password one by one until it finds the right one and unlocks the file.
- This mimics how a basic offline brute-force attack works, using a trimmed-down version of the popular RockYou password list.

---

## 📸 Screenshots

### 🔍 Start terminal
Here i started executing the file in terminal initial screenshot of the pathway of the folder and starting bruteforce.
![Terminal Screenshot](ransomware-decryption-bruteforce/screenshots/start.png)

### 🗂️ Executing the script (bruteforcing)
Here i executed the script and it iterated through every combination using rockyou password list and gave us the password.
![Encrypted File Structure](../screenshots/password.png)

### ✅ Successful Decryption Output
After successful bruteforceing we decrypted the enc.zip and got a word doc file.   
![Decryption Success](../screenshots/encrypted_contents.png)
Ransomware has thus been decrypted.

 

---

## 📚 Skills Practiced

- Learned how to write Python scripts to open and decrypt password-protected files.
- Got hands-on with brute-force logic and built in error-handling to deal with failed attempts.
- Practiced automating a common incident response task recovering files without paying ransom.
- Simulated a real-world blue team scenario involving ransomware recovery under pressure.

---

## 📌 Takeways

- Brute-force attacks can actually succeed when weak or common passwords are used for encryption.
- Relying on default tools or hiding system details isn’t real security  it’s just wishful thinking.
- Having regular backups, training employees, and staying on top of patches are must-haves to limit ransomware damage.
- Stopping attacks is great, but  incident response when things go wrong is just as important.

---

 

 
