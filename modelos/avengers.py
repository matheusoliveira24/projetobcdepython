class  Avengers:
 
    lista_de_avengers = []
 
    def __init__(self, nome_heroi='', nome_real='', categoria=[], poderes=[], poder_principal='', fraquezas=[], nivel_forca='', convocacao=False, tornozeleira=False , gps=False): # método construtor
        self.nome_heroi = nome_heroi # declaração de um atributo e atribuiçãode um valor
        self.nome_real = nome_real # variaveis de instância
        self.categoria = categoria
        self.poderes = poderes
        self.poder_principal = poder_principal
        self.fraquezas = fraquezas
        self.nivel_forca = nivel_forca
        self.convocacao = convocacao
        self.tornozeleira = tornozeleira
        self.gps = gps
        Avengers.lista_de_avengers.append(self)
 
    @classmethod
    def listar_avengers(cls):
 
        print(f'{'nome_heroi'.ljust(15)} | {'nome_real'.ljust(10)} | {'categoria'.ljust(15)} | {'poderes'.ljust(15)} | {'poder_principal'.ljust(15)} | {'fraquezas'.ljust(15)} | {'nivel_forca'.ljust(15)} | {'convocação'.ljust(15)} | {'tornozeleira'.ljust(15)} | {'gps'.ljust(15)}')
        for avengers in Avengers.lista_de_avengers:

            print(f'{str(avengers.nome_heroi).ljust(20)} | {str(avengers.nome_real).ljust(10)} | {str(avengers.categoria).ljust(15)} | {str(avengers.poderes).ljust(20)} | {str(avengers.poder_principal).ljust(20)} | {str(avengers.fraquezas).ljust(20)} | {str(avengers.nivel_forca).ljust(20)} | {str(avengers.convocacao).ljust(20)} | {str(avengers.tornozeleira).ljust(20)} | {str(avengers.gps).ljust(20)}')
 
 
    def __str__(self):
        return f'{'nome_heroi'.ljust(20)} | {'nome_real'.ljust(10)} | {'categoria'.ljust(15)} | {'poderes'.ljust(30)} | {'poder_principal'.ljust(20)} | {'fraquezas'.ljust(20)} | {'nivel_forca'.ljust(20)} {'convocaçao'.ljust(20)} | {'tornozeleira'.ljust(20)} | {'gps'.ljust(5)} \n{str(self.nome_heroi).ljust(20)} | {str(self.nome_real).ljust(10)} | {str(self.categoria).ljust(15)} | {str(self.poderes).ljust(30)} | {str(self.poder_principal).ljust(20)} | {str(self.fraquezas).ljust(20)} | {str(self.nivel_forca).ljust(20)} | {str(self.convocacao).ljust(20)} | {str(self.tornozeleira).ljust(20)} | {str(self.gps).ljust(5)}'
    
    @staticmethod
    def procurar_vingador(nome_heroi):
        '''Procurar um vingador pelo nome.'''
        for avengers in Avengers.lista_de_avengers:
            if avengers.nome_heroi.lower() == nome_heroi.lower():
                return avengers
        return None  

print(Avengers('Homem de Ferro', 'Tony Stark', 'Humano', ['Inteligência', 'Engenharia'], 'Armadura', 'Arrogância', 50, 'não', 'não', 'não'))
