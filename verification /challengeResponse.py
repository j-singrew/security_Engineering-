from cryptography.fernet import Fernet
import secrets

key = Fernet.generate_key()
f = Fernet(key)

def generate_challenge():
    return secrets.token_urlsafe(32)

"""
Engine controller ~ E

challenge  ~ N

E -> T : N 

"""
def engine_controller():
    N = generate_challenge()
    encrypted_challenge = transponder(N.encode())

    decrypted = f.decrypt(encrypted_challenge)
    transponder_n, returned_nonce = decrypted.decode().split("-")
    if returned_nonce == N:
        print(transponder_n ," Match")
    else:
        print("Authentication failed")




"""

Key Trandsponder ~ T
K ~ Enrypted key 

T ->E :T {T,N}k
"""
def transponder(challenge):
    transponder_id="transponer_46"
    return f.encrypt(transponder_id+"-"+challenge)

    



engine_controller()