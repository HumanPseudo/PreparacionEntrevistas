import unittest
from twoSum import TwoSum  # Asegúrate de que este sea el nombre de tu archivo que contiene la clase TwoSum

class TestTwoSum(unittest.TestCase):

    def test_constructor(self):
        # Prueba para verificar que el constructor funcione correctamente
        nums = [2, 7, 11, 15]
        target = 9
        two_sum_obj = TwoSum(nums, target)
        self.assertEqual(two_sum_obj.nums, nums)
        self.assertEqual(two_sum_obj.target, target)

    def test_two_sum(self):
        # Prueba para verificar el método two_sum
        nums = [2, 7, 11, 15]
        target = 9
        two_sum_obj = TwoSum(nums, target)
        result = two_sum_obj.two_sum()  # Llama al método en la instancia
        self.assertEqual(result, (0, 1))  # Indices de los números que suman el objetivo

    def test_two_sum_no_solution(self):
        # Prueba para verificar el método two_sum cuando no hay solución
        nums = [2, 7, 11, 15]
        target = 100
        two_sum_obj = TwoSum(nums, target)
        result = two_sum_obj.two_sum()  # Llama al método en la instancia
        self.assertIsNone(result)  # No hay solución

if __name__ == '__main__':
    unittest.main()
