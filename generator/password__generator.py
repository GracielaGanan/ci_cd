# Lo que estamos haciendo es crear una funcion que genere una contraseña aleatoria
import random
import string
def generate_password(length=12):
    characters = (
        string.ascii_lowercase,
        string.ascii_uppercase,
        string.digits,
        string.punctuation
    )
    

    password = "".join(random.choice(characters) for _ in range(length))
    return password

# vamos agreagar pequeñas funciones que le podemos dar pequeñas funciones 
# donde le demos agregar numeros o que ocupe ciertos numeros. 
def has_uppercase (password):
    return any(c.isupper() for c in password)

def has_symbol(password):
    return any(c in string.punctuation for c in password)

def has_numbers(password):
    return any(c.isdigit() for c in password)

