from base64 import encode
import hashlib
import bcrypt
class HashTools:
    
    def HashPassword(password):
        uniquehash = bcrypt.gensalt(rounds=12)
        password = password.encode()
        passwd = bcrypt.hashpw(
            password,
            uniquehash
        )
        passwd = passwd.decode('utf-8')
        return passwd

    def CheckHash(password, hash):
        password = password.encode()
        hash = hash.encode()
        if bcrypt.hashpw(password, hash) == hash:
            #print("----- HASH MATCH -----")
            return True
        else:
            #print("----- HASH MISMATCH -----")
            return False