from modelos.database import Database
class  Avengers:
 
    lista_de_avengers = []
 
    def __init__(self, id, nome_heroi='', nome_real='', categoria=[], poderes=[], poder_principal='', fraquezas=[], nivel_forca='', convocacao=False, tornozeleira=False , gps=False): # método construtor
        self.id=id
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
 
        print(f'{'nome_heroi'.ljust(20)} | {'nome_real'.ljust(10)} | {'categoria'.ljust(15)} | {'poderes'.ljust(20)} | {'poder_principal'.ljust(20)} | {'fraquezas'.ljust(20)} | {'nivel_forca'.ljust(20)} | {'convocação'.ljust(20)} | {'tornozeleira'.ljust(20)} | {'gps'.ljust(5)}')
        for avengers in Avengers.lista_de_avengers:

            print(f'{str(avengers.nome_heroi).ljust(20)} | {str(avengers.nome_real).ljust(10)} | {str(avengers.categoria).ljust(15)} | {str(avengers.poderes).ljust(20)} | {str(avengers.poder_principal).ljust(20)} | {str(avengers.fraquezas).ljust(20)} | {str(avengers.nivel_forca).ljust(20)} | {str(avengers.convocacao).ljust(20)} | {str(avengers.tornozeleira).ljust(20)} | {str(avengers.gps).ljust(5)}')
 
 
    def __str__(self):
        return f'{'nome_heroi'.ljust(20)} | {'nome_real'.ljust(10)} | {'categoria'.ljust(15)} | {'poderes'.ljust(20)} | {'poder_principal'.ljust(20)} | {'fraquezas'.ljust(20)} | {'nivel_forca'.ljust(20)} | {'convocaçao'.ljust(20)} | {'tornozeleira'.ljust(20)} | {'gps'.ljust(5)} \n{str(self.nome_heroi).ljust(20)} | {str(self.nome_real).ljust(10)} | {str(self.categoria).ljust(15)} | {str(self.poderes).ljust(20)} | {str(self.poder_principal).ljust(20)} | {str(self.fraquezas).ljust(20)} | {str(self.nivel_forca).ljust(20)} | {str(self.convocacao).ljust(20)} | {str(self.tornozeleira).ljust(20)} | {str(self.gps).ljust(5)}'
    
    @staticmethod
    def procurar_vingador(nome_heroi):
        '''Procurar um vingador pelo nome.'''
        for avengers in Avengers.lista_de_avengers:
            if avengers.nome_heroi.lower() == nome_heroi.lower():
                return avengers
        return None  
    
    # mudança de estado

    @property
    def convocacao(self):
        return 'Sim' if self._convocacao else 'Não'
    
    @convocacao.setter
    def convocacao(self, valor):
        self._convocacao = valor

    @property
    def tornozeleira(self):
        return 'Sim' if self._tornozeleira else 'Não'

    @tornozeleira.setter
    def tornozeleira(self, valor):
        self._tornozeleira = valor

    # fim mudança de estado

    
    # Funções de convocação, aplicar tornozeleira e gps
    def convocar(self):
        self.convocacao = True
        return f'{self.nome_heroi} convocado!'
    
    def aplicar_tornozeleira(self):
        if self._convocacao:
            if self.nome_heroi == 'Thor':
                return '"Eu sou Thor, Deus do Trovão, filho de Odin! Nenhuma corrente ou restrição pode me controlar. \nTentem colocar-me uma tornozeleira, e verão o que acontece quando um deus é desafiado..."'
            elif self.nome_heroi == 'Hulk':
                return '"Hulk esmaga! Hulk mais forte tornozeira!"'
            self.tornozeleira = True
            return 'Tornozeleira aplicada com sucesso!'
        return f'{self.nome_heroi} não foi convocado ainda.'
    
    #Fim da funções 
    



    def carregar_herois():
        try:
            db = Database()
            db.connect()

            query = 'SELECT nome_heroi, nome_real, categoria, poderes, poder_principal, fraquezas, nivel_forca FROM heroi'
            herois = db.select(query)
            for heroi in herois:
                Avengers(*heroi)
        except Exception as e:
            print(f'Error: {e}')
        finally:
            db.disconnect()