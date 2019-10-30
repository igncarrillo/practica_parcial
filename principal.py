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
                frase=str(input("\nIngrese la frase: "))
                ejemplo1.es_palindromo(frase)
            elif(decision==2):
                frase=str(input("\nIngrese la frase: "))
                ejemplo1.es_mayuscula(frase)
            elif(decision==3):
                frase=str(input("\nIngrese la frase: "))
                ejemplo1.es_minusculas(frase)
            elif(decision==4):
                print("\nSaliendo...")
                return False
            else:
                print("\nOpcion incorrecta - Intente nuevamente...\n")

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
            print("\n{} está totalmente en mayuscula".format(frase))
            return True
        else:
            print("\n{} no está totalmente en mayuscula".format(frase))
            return False
    
    def es_minusculas(self,frase):
        frase_min = frase.lower()
        if(frase_min==frase):
            print("\n{} está totalmente en minuscula".format(frase))
            return True
        else:
            print("\n{} no está totalmente en minuscula".format(frase))
            return False

os.system("clear")
ejemplo1=Practica()
ejemplo1.menu()