from classes.recipiente import Recipiente

class Copo(Recipiente):


    def __init__(self,tamanho):
        super().__init__(tamanho)


    def encher(self,string="água"):
        if not self.limpo:
            return "Não se pode encher um copo sujo"
        self.sujar()
        self.conteudo=self.tamanho
        self.bebida=string


    def beber(self,quantidade):
        if quantidade <0:
            return 'Quantidade deve ser positiva'
        if quantidade>self.conteudo:
            return 'Não há bebida suficiente no copo'
        self.conteudo=self.conteudo-float(quantidade)


    def lavar(self):
        self.bebida=None
        self.limpo=True
        self.conteudo=0


    def __str__(self) -> str:
        if self.conteudo == 0:
            return f'Um copo vazio de {self.tamanho}ml'
        return f'Um copo de {self.tamanho}ml contendo {self.conteudo}ml de {self.bebida}'
        
            
    def __repr__(self) -> str:
        if self.conteudo == 0:
            return f'Um copo vazio de {self.tamanho}ml'
        return f'Um copo de {self.tamanho}ml contendo {self.conteudo}ml de {self.bebida}' 

