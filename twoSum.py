"""

 * Dado un array de números enteros y un target, retorna los índices de dos
 * números para los que la suma de ambos sea igual al target.
 *
 * Puedes asumir que hay solamente una solución.
 *
 * Ejemplo 1:
 *  Input: nums = [9,2,5,6], target = 7
 *  Output: [1,2]
 *  Explicación: nums[1] + nums[2] == 7, devolvemos [1, 2].
 *
 * Ejemplo 2:
 *  Input: nums = [9,2,5,6], target = 100
 *  Output: null
 * 
 * [(-2 <- complemento para 9 sumar 7, indice), 5, ] -> O(N)
 *
 *
 *
"""
class TwoSum:
    """
    La clase TwoSum busca pares de números en una lista que sumen un objetivo dado.

    Args:
        nums (list[int]): Una lista de números enteros.
        target (int): El objetivo para la suma de dos números.

    Attributes:
        nums (list[int]): La lista de números proporcionada.
        target (int): El objetivo para la suma de dos números.

    Methods:
        two_sum(): Encuentra dos índices que suman el objetivo dado.

    Example:
        Ejemplo de uso de la clase TwoSum:
        ```
        nums = [2, 7, 11, 15]
        target = 9
        two_sum_instance = TwoSum(nums, target)
        indices = two_sum_instance.two_sum()
        print("Índices de los números que suman el objetivo:", indices)
        ```

    """

    def __init__(self, nums, target):
        """
        Inicializa una instancia de TwoSum.

        Verifica si la lista de números es válida y establece los atributos.

        Args:
            nums (list[int]): Una lista de números enteros.
            target (int): El objetivo para la suma de dos números.
        
        Returns:
            None
        """
        self.nums = nums
        self.target = target
        if nums is None or len(nums) < 2:
            # La lista no es válida, no se puede encontrar la suma
            return None

    def two_sum(self):
        """
        Encuentra dos índices que suman el objetivo dado.

        Utiliza un diccionario para almacenar los números y sus índices
        para buscar rápidamente el complemento necesario.

        Returns:
            tuple: Una tupla con los índices de los números que suman el objetivo,
                   o None si no se encuentra ninguna solución.
        """
        complement_map = {}  # Diccionario para almacenar el complemento y su índice

        for i, num in enumerate(self.nums):
            complement = self.target - num

            if complement in complement_map:
                # Se encontró una solución
                return complement_map[complement], i

            # Guarda el índice actual junto con el número en el diccionario
            complement_map[num] = i

        # No se encontró ninguna solución
        return None
