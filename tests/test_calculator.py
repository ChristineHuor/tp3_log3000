import unittest
from backend.operators import add, subtract, multiply, divide


class TestCalculator(unittest.TestCase):
    """
    Suite de tests unitaires pour les fonctions arithmétiques
    du module backend.operators.

    Cette classe vérifie que chaque opération retourne le
    résultat attendu pour des valeurs valides.
    """

    def test_add(self):
        """
        Vérifie que la fonction add retourne la somme correcte
        de deux nombres positifs.
        """
        self.assertEqual(add(20, 35), 55)

    def test_subtract(self):
        """
        Vérifie que la fonction subtract retourne la différence correcte
        entre deux nombres positifs.
        """
        self.assertEqual(subtract(35, 20), 15)

    def test_multiply(self):
        """
        Vérifie que la fonction multiply retourne le produit correct
        de deux entiers.
        """
        self.assertEqual(multiply(5, 6), 30)

    def test_divide(self):
        """
        Vérifie que la fonction divide retourne un résultat
        flottant correct lors d'une division valide.
        """
        self.assertEqual(divide(20, 8), 2.5)


if __name__ == '__main__':
    unittest.main()
