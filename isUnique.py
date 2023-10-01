
# Dado un método que recibe una String, comprobar si todos los caracteres son únicos o no.

#  isUnique("abcde") => true;
#  isUnique("abcded") => false;

"""

a: b c d e
b: c d e
...

O(n^2)

Tabla hash

a b c d e _ 

for O(N)
consulta en la tabla O(1) ---> O(1)

"""


class IsUnique:
    def __init__(self, string):
        self.string = string

    def is_unique(self):
        number_of_chars = 128
        if len(self.string) > number_of_chars:
            return False
        char_set = set()
        for char in self.string:
            if char in char_set:
                return False
            char_set.add(char)
        return True
