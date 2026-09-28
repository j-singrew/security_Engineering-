
import string 
from cryptography.fernet import Fernet
import secrets


"""
2 Agents guarage 

authenticator 

GUARGE agent properties:
    histrorical nonce values 
"""

key = Fernet.generate_key()
f = Fernet(key)

nonce_history = []
user_db = ("user#123124")

"""
nonce Generator ~ N
"""

def nonce_generator():
    return ''.join(
        secrets.choice(string.ascii_letters + string.digits)
        for _ in range(32)
    )

    

"""
Simple verification
"""
def nonce_verification(nonce_value):
    if nonce_value not in nonce_history:
        nonce_history.append(nonce_value)
        return True
    return False





def gaurage(token):

    token = f.decrypt(token).decode()
    token_split  = token.split("-")
    user = token_split[0]
    nonce = token_split[1]

    if  nonce_verification(nonce):
        if user in user_db:

            return "user Authentication confirmed"
        else:
            return "user Authentication denied"






"""
T ~ Token 
G ~name
N ~ nonce

T -> G ∶ T, {T, N}KT
"""

def auth_agent():
    name = "user#123124"
    nonce = nonce_generator()
    unencrypted_token  =  name+"-"+nonce
    T = unencrypted_token.encode()

    encrypted_token = f.encrypt(T)
    i = gaurage(encrypted_token)
    print(i)




auth_agent()















