#! usr/bin/python3
import string
import os

class Practica():

    def init(self,frase):
        pass

    def menu(self):
        while(True):
            decision=int(input("""
                        1-Averiguar si es palindromo 
                        2-Averiguar si esta en mayusculas
                        3-Averiguar si esta en minusculas
                        4-Salir

                        Ingrese que desea hacer:"""))
            if(decision==1):
                frase=str(input("Ingrese la frase: "))
                ejemplo1.es_palindromo(frase)
            else:
                return False

    def es_palindromo(self,frase):
        frase=frase.replace(' ','')
        frase_invertida=frase[::-1]
        if(frase_invertida==frase):
            print("\n{} Es palindromo".format(frase))
            return True
        else:
            print("\n{} No es palindromo".format(frase))
            return False
    
    def es_mayuscula(self,frase):
        frase_may=frase.upper()
        if(frase_may==frase):
            return True
        else:
            return False
    
    def es_minusculas(self,frase):
        frase_min = frase.lower()
        if(frase_min==frase):
            return True
        else:
            return False


ejemplo1=Practica()
ejemplo1.menu()
os.system("clear")