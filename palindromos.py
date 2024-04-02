import unittest

def palindrome(x):
    x = x.lower()
    if x == x[::-1]:
        return True
    else:
        return False
    
""""    
palabra = input('Palabra: ')
resultado = palindrome(palabra)
print(resultado)

"""

class TestIsPalindrome(unittest.TestCase):
    def test_with_a(self):
        input = "a"
        result = palindrome(input)
        self.assertTrue(result)

    def test_with_ala(self):
        input = "ala"
        result = palindrome(input)
        self.assertTrue(result)

    def test_with_neuquen(self):
        input = "neuquen"
        result = palindrome(input)
        self.assertTrue(result)

    def test_with_hola(self):
        input = "hola"
        result = palindrome(input)
        self.assertFalse(result)


unittest.main()
