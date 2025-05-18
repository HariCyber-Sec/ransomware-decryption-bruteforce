'''
Forage AIG Cybersecurity Program
Bruteforce starter template
'''

from zipfile import ZipFile
# Use a method to attempt to extract the zip file with a given password
# def attempt_extract(zf_handle, password):
def attempt_extract(zf_handle, password):
    try:
        # Try to extract all files using the password (must be bytes)
        zf_handle.extractall(pwd=password)
        return True
    except:
        return False



def main():
      
 # Iterate through password entries in rockyou.txt
 # Attempt to extract the zip file using each password
 # Handle correct password extract versus incorrect password attempt)
    print("[+] Beginning bruteforce ")
    with ZipFile('enc.zip') as zf:
        with open('rockyou.txt', 'rb') as f:
            for line in f:
                password = line.strip()  # Remove newline characters
                if attempt_extract(zf, password):
                    print(f"[+] Password found: {password.decode('utf-8')}")
                    return
    print("[-] Password not found in list")
           

if __name__ == "__main__":
    main()
     
