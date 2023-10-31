

from prime_qg2218.prime import is_prime

def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(4) == False
    assert is_prime(5) == True
    assert is_prime(7) == True
