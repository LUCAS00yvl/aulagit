from cadastro_animais import Animal

class Cachorro(Animal):
    def __init__(self, nome, idade, porte):
        super().__init__(nome, idade, porte)
    

    def setPorte(self,porte): 
        self.__porte=porte
    def getPorte(self):
        pass
    def mostrar(self):
        return (f"Cachorro de Nome: {self.getNome()}, Idade: {self.getIdade()}, e Porte: Médio") 
