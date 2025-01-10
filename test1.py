# Brute Force Attack

import hashlib
import itertools
import string

# Brute force function
def brute_force_attack(hash_to_crack, max_length=6):
    chars = string.ascii_lowercase + string.digits  # Define character set
    for length in range(1, max_length + 1):
        for combo in itertools.product(chars, repeat=length):
            password = ''.join(combo)
            hashed_password = hashlib.md5(password.encode()).hexdigest()
            if hashed_password == hash_to_crack:
                print(f"Password found: {password}")
                return
    print("Password not found using brute force!")

# Input from user
md5_hash = input("Enter the MD5 hash to crack: ")
brute_force_attack(md5_hash)




# Some examples:

# 900150983cd24fb0d6963f7d28e17f72 - abc

# e2fc714c4727ee9395f324cd2e7f331f - abcd

# ab56b4d92b40713acc5af89985d4b786 - abcde

# e80b5017098950fc58aad83c8c14978e - abcdef

