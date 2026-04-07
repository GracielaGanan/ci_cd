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


def test_has_uppercase():
    assert has_uppercase("Abc") is True


def test_has_number():
    assert has_number("abc1") is True


def test_has_symbol():
    assert has_symbol("abc!") is True


def test_generated_password_length_range():
    for length in range(4, 20):
        password = generate_password(length)
        assert len(password) == length