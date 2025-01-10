# Dictionary Attack

import hashlib

# Load dictionary file and crack the hash
def dictionary_attack(hash_to_crack, dictionary_path):
    try:
        with open(dictionary_path, 'r', encoding='latin-1') as file:
            for line in file:
                password = line.strip()
                # Hash the password
                hashed_password = hashlib.md5(password.encode()).hexdigest()
                
                # Compare hashes
                if hashed_password == hash_to_crack:
                    print(f"Password found: {password}")
                    return
        print("Password not found in the dictionary!")
    except FileNotFoundError:
        print("Dictionary file not found!")

# Input from user
md5_hash = input("Enter the MD5 hash to crack: ")
dictionary_path = r"C:\Users\Manas\Desktop\Winter Projects\MD5_Hash_Cracker\rockyou.txt"  
# Update with the actual path
dictionary_attack(md5_hash, dictionary_path)




# Some examples:

# Enter the MD5 hash to crack: 0f6f6b5416a836065f933e4857c31c9a
# Password found: ------



# Enter the MD5 hash to crack: e530700849717ca0f28f7bb3fe5bec2f
# Password found: timosha



# Enter the MD5 hash to crack: e10adc3949ba59abbe56e057f20f883e
# Password found: 123456