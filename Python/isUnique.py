
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
        """
        Constructor de la clase IsUnique.

        Parameters:
            string (str): La cadena que se va a evaluar.
        """
        self.string = string

    def is_unique(self):
        """
        Verifica si la cadena contiene caracteres únicos.

        Returns:
            bool: True si la cadena tiene caracteres únicos, False si no.
        """
        # Número máximo de caracteres posibles en el juego de caracteres ASCII
        number_of_chars = 128

        # Verifica si la longitud de la cadena supera el número máximo de caracteres
        if len(self.string) > number_of_chars:
            return False

        # Conjunto para almacenar caracteres únicos
        char_set = set()

        # Itera a través de cada carácter en la cadena
        for char in self.string:
            # Si el carácter ya está en el conjunto, la cadena no tiene caracteres únicos
            if char in char_set:
                return False
            char_set.add(char)

        # Si no se encontraron caracteres duplicados, la cadena tiene caracteres únicos
        return True
