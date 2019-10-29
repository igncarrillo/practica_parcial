#! /usr/bin/python3
import unittest
from parameterized import parameterized
from principal import Practica
import os

class Test_practica (unittest.TestCase):

    def setUp(self):
        self.ejemplo= Practica()

    @parameterized.expand([
        ('neuquen'),
        ('agita falsos usos la fatiga'),
    ])
    def test_Palindromo_true(self,frase):
        self.assertEqual(self.ejemplo.es_palindromo(frase),True)
    
    @parameterized.expand([
        ('mendoza'),
        ('la programacion requiere muchas horas de practica'),
    ])

    def test_esPalindromo_false(self,frase):
        self.assertEqual(self.ejemplo.es_palindromo(frase),False)

    @parameterized.expand([
        ('HOLA'),
        ('BUEN DIA'),
        ('PYTHON'),
    ])
    def test_mayusculas(self,frase):
        self.assertEqual(self.ejemplo.es_mayuscula(frase),True)
    
    @parameterized.expand([
        ('hola'),
        ('buEN DiA'),
        ('pYTHON'),
    ])

    def test_mayusculasFalse(self,frase):
        self.assertEqual(self.ejemplo.es_mayuscula(frase),False)

    @parameterized.expand([
        ('hola'),
        ('buen dia'),
        ('python'),
        ])

    def test_minusculas(self,frase):
        self.assertEqual(self.ejemplo.es_minusculas(frase),True)
    

if __name__=='__main__':
    os.system("clear")
    unittest.main()