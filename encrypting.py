from cryptography.fernet import Fernet
key = Fernet.generate_key()

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
        
def load_key():
    return open("key.key", "rb").read()

write_key()
key = load_key()
def encrypt(filename, key):
    f = Fernet(key)
    
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)
def decrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(filename, "wb") as file:
        file.write(decrypted_data)
file = "university_records.csv"
encrypt(file, key)
decrypt(file, key)