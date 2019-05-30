from variavel import *

class Nivel(variavel):
    g = 9.81
    def calcular(self):
        print("1. Medição de nível por pressão hidrostática")
        print("2. Medição de nível por  pressão diferencial")
        escolha = int(input("\nDigite a opção de medição: "))
        if escolha == 1:
            print("O nível é:",self.hidrostatica, "mmH2O")
        elif escolha == 2:
            print("1. Tanque aberto")
            print("2. Tanque fechado")
            sit = int(input())
            self.diferencial(sit)
            
    def __init__(self, arBase, altLiq):
        self.altura = altLiq
        self.area = arBase
        
    def volume(self):
        return self.altura*self.area
    
    def massa(self):
        peso  = float(input("Digite o peso do produto: "))
        return self.area*peso/g
    
    def hidrostatica(self):
        densRel  = float(input("Digite a densidade relativa: "))
        return self.altura*densRel
    
    def diferencial(self,sit):
        #sit 2 para fechado e 1 para aberto
        masEsp = self.massa()/self.volume()
        if sit == 1:
            varPres = float(input("Digite a variação de pressão: "))
            
            h2 = varPress/(masEsp*g)
            print("O nivel do tanque aberto é: ", h2)
            
        elif sit == 2:
            varPeso = float(input("Digite a variação de peso: "))
            h2 = self.altura-varPeso/(masEsp*g)
            print("O nivel do tanque fechado é: ", h2)