from generator.password__generator import (generate_password
,has_uppercase 
,has_symbol
,has_numbers

)
# creamos funciones q van a testear

def test_password_length():
    password = generate_password()
    assert len(password) == 12

def test_password_is_string():
    password = generate_password(10)
    assert isinstance(password, str)


    