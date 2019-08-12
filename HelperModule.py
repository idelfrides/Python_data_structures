

class HelperModule(object):

    def __init__(self):
        pass


    def app_info(self):
        print('''
            THIS APPLICATION IMPLEMENTS AA CRUD 
            OPERATIONS ON DATA STRUCTURES,
            LIKE: 
            ---- IMUTABLE ----------
                - TUPLE
                - STRING
            ---- MUTABLE -----------
                - LIST
                - DICTIONARY
                - FILE
                - SET     
                
        ********************************************   
        
        ''')


    def menu(self):
        print(' MENU \n\n 1 - Listas \n 2 - Dicionário \n 3 - Arquivos \n 4 - Conjuntos  \n 0 - Sair\n')
        aux = 1
        while aux == 1:
             opcao = int(input('Escolhe uma opcao:  '))
             if opcao in range(5):
                 return opcao
             else:
                 print('\n opcao: ', opcao)
                 print('\n WARNING: OPCAO INVALIDA!!!\n\n')


    def menu_atividade(self):
        print(' MENU DE ATIVIDADES CRUD: \n\n 1 - CREATE \n 2 - READ \n 3 - UPDATE \n 4 - DELETE  \n 0 - Sair de atividade\n\n')
        aux = True
        while aux is True:
            opcao = int(input('Escolhe uma opcao:  '))
            if opcao != 1 and opcao is not 2 and opcao != 3 and opcao is not 4 and opcao is not 0:
                print('AVISO: OPCAO INVALIDA!!!\n\n')
            else:
                aux = False
        return opcao


    def my_set(self, instance, value):
        if value == 1:
            self.lista = instance
        elif value == 2:
            self.dicio = instance
        elif value == 3:
            self.arq = instance
        elif value == 4:
            self.conj = instance
        else:
            pass


    def my_get(self, owner):
        if owner == 1:
            if self.lista:
                return 1
            else:
                return 0
        elif owner == 2:
            if self.dicio:
                return 1
            else:
                return 0
        elif owner == 3:
            print(self.arq)
            if self.arq > 0:
                return 1
            else:
                return 0
        elif owner == 4:
            if self.conj:
                return 1
            else:
                return 0
        else:
            pass


    def verif_estrut_exist(self, est):
        if est == 1:
           return  self.my_get(1)  # LIST
        elif est == 2:      # dictionary exist
            return self.my_get(2)  # DICT
        elif est == 3:      # list exist
            return self.my_get(3)  # FILE
        elif est == 4:
            return self.my_get(4)  # SET
        else:
            pass


    def info_structure(self, est):
        if est == 1:
            print('--------------------------------------\nVOCE ESCOLHEU TRABALHAR COM LISTAS\n')
        elif est == 2:
            print('--------------------------------------\nVOCE ESCOLHEU TRABALHAR COM DICIONARIO\n')
        elif est == 3:
            print('------------------------------------------\nVOCE ESCOLHEU TRABALHAR COM ARQUIVOS\n')
        elif est == 4:
            print('------------------------------------------\nVOCE ESCOLHEU TRABALHAR COM CONJUNTOS\n')
        else:
            pass



