class Recipiente:
  
    def __init__(self,tamanho):
        
        self.tamanho=float(tamanho) if tamanho > 0 else 0
        self.conteudo=float(0)
        self.limpo=True


    def esvaziar(self):
        self.conteudo=0


    def esta_vazio(self):
        if self.conteudo==0:
           return True
        return False


    def lavar(self):
        self.conteudo=0
        self.limpo=True


    def esta_limpo(self):
        if self.limpo==True:
            return True
        return False 


    def estado(self):
        if self.limpo:
            return 'limpo'
        return 'sujo'


    def sujar(self):
        self.limpo=False


    def __str__(self) -> str:
        return f'Um recipiente {self.estado()} não especificado'


    def __repr__(self) -> str:
        return f'Um recipiente {self.estado()} não especificado'


