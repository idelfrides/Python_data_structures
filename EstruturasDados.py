
# ----------------------------------------------
# class contain CRUD METHODS and
# others methods
# -----------------------------------------------
class EstruturasDados(object):

    lista = []
    dicio = {}
    arq = 0
    conj = set()

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


# ------------ CRUD METHODS -------------------------
    def create(self, tipo_estru, tipo):

        if tipo_estru == 1:    # create a list
            lista = []
            print('\n\n Sua LISTA foi criada com sucesso. \n Agora, vamos preenche-la.\n\n')
            self.my_set(lista, 1)
            if tipo is 1:
                resp = self.int_values_lista()
                if resp is -1:      # trocar pra string
                    resp2 = self.string_value_lista()  # return '0'
                    if resp2 is '0':
                        return
                        # self.create(1, 1)  # recursive call
                else:
                    return  # 0 sair
            else:
                pass

        elif tipo_estru == 2:  # create a dictionary
            dicionario = {}
            print('\n\n Seu DICIONARIO foi criado com sucesso. \n Agora, vamos preenche-lo.\n\n')
            preench = True
            ind = 0
            while preench is True:
                ind = ind + 1
                valor = int(input('Informe um valor p/ [%d] ou 0 pra sair:  '%(ind)))
                if valor is not 0:
                    dicionario[(ind)] = valor
                    print(dicionario)
                else:
                    preench = False
                    self.my_set(dicionario, 2)
            return

        elif tipo_estru == 3:   # create a file
            arquivo = open('arquivo.txt', 'w', encoding="utf8")
            print('\n\n Seu ARQUIVO foi criado com sucesso. \n Agora, vamos preenche-lo.\n\n')
            preench = True
            ind = 0
            while preench is True:
                ind = ind + 1
                dado = input('Informe um dado pra linha [%d] ou N pra sair:  '%(ind))
                if dado is not 'N' and dado is not 'n':
                   arquivo.writelines(dado)
                else:
                    preench = False
                    self.my_set(1, 3)
                    arquivo.close()
            return

        elif tipo_estru == 4:  # create a set
            conj = set()
            self.my_set(conj, 4)
            if tipo is 1:
                resp = self.int_values_conj()
                if resp is -1:  # trocar pra string
                    resp2 = self.string_value_conj() # return '0'
                    if resp2 is '0':  # exit
                        return
                    else:
                        pass
                else:
                    return  # 0 sair
            else:
                pass
        else:
            return


    def read(self, tipo_estru):
        if tipo_estru == 1:   # read the list
            my_lista = self.lista
            print('\n\n APRESENTACAO DA LISTA \n')
            print(my_lista)
            print('\n\n')
            return
        elif tipo_estru == 2:  # read the dictionary
            my_dicio = self.dicio
            print('\n\n APRESENTACAO DO DICIONARIO \n')
            print(my_dicio)
            print('\n\n')
            return
        elif tipo_estru == 3:  # read  the file
            print('\n\n LEITURA DE ARQUIVO \n')
            arquivo = open('arquivo.txt', 'r', encoding="utf-8")
            dados_arq = arquivo.readlines()

            for d in dados_arq:
                # v = d.split()
                print(d)
                print('\n')
            self.my_set(1, 3)
            arquivo.close()
            print('\n\n')
            return
        elif tipo_estru == 4:  # read the set
            print('\n\n APRESENTACAO DO CONJUNTO \n')
            my_conj = self.conj
            print(my_conj)
            print('\n\n')
            return
        else:
            pass


    def update(self, tipo_estru):
        if tipo_estru == 1:  # read a list
            my_lista = self.lista
            print('\n\n ATUALIZACAO \n')
            op = int(input(' 1 -> Atualizar lista interia \n 2 -> Apenas um elemento \n\n  Sua opcao aqui:   '))
            print('\r')
            if op is 1:
                aux = True
                k = 0
                tam = my_lista.__len__()
                while aux is True:
                    valor = int(input('\n Informe um valor p/ [%d] ou 0 pra sair:  '%(k)))
                    if type(valor) is int and valor != 0 and k < tam:
                        my_lista.pop(k)
                        my_lista.insert(k, valor)
                        k = k + 1
                        print(my_lista)
                    elif type(valor) is int and valor != 0 and k >= tam:
                        my_lista.append(valor)
                        k = k + 1
                        print(my_lista)
                    else:
                        self.my_set(my_lista, 1)
                        return my_lista
            elif op is 2:
                k = int(input('\n Informe a posicao do elemento:  '))
                v = int(input('\n Informe o novo valor:  '))
                my_lista.pop(k)
                my_lista.insert(k, v)
                print(my_lista)
                print('\n\n\n')
                self.my_set(my_lista, 1)
                return
        elif tipo_estru == 2:  # create a dictionary
            my_dicio = self.dicio
            print('\n\n ATUALIZACAO \n')
            op = int(input(' 1 -> Atualizar dicionario interio \n 2 -> Apenas um elemento \n\n  Sua opcao aqui:   '))
            print('\r')
            if op is 1:
                aux = True
                tam = my_dicio.__len__()
                k = 1
                while aux is  True:
                    valor = int(input('\n Informe um valor p/ [%d] ou 0 pra sair:  ' % (k)))
                    if type(valor) is int and valor != 0 and k <= tam:
                        my_dicio.pop(k)
                        my_dicio.setdefault(k, valor)
                        k = k + 1
                        print(my_dicio)
                    elif type(valor) is int and valor != 0 and k > tam:
                        my_dicio.setdefault(k, valor)
                        k = k + 1
                        print(my_dicio)
                    else:
                        self.my_set(my_dicio, 1)
                        return
            elif op is 2:
                k = int(input('\n Informe a posicao do elemento:  '))
                v = int(input('\n Informe o novo valor:  '))
                my_dicio.pop(k)
                my_dicio.setdefault(k, v)
                print(my_dicio)
                print('\n\n\n')
                self.my_set(my_dicio, 1)
                return
        elif tipo_estru == 3:  # create a file
            print('\n\n ATUALIZACAO DE ARQUIVO \n')
            arquivo = open('arquivo.txt', 'w', encoding="utf-8")
            preench = True
            ind = 0
            while preench is True:
                ind = ind + 1
                dado = input('Informe um dado pra linha [%d] ou N pra sair:  ' % (ind))
                if dado is not 'N' and dado is not 'n':
                    # arquivo.writelines(dado)
                    arquivo.writelines(dado)
                    # d.append(dado)
                else:
                    preench = False
                    self.my_set(1, 3)
                    arquivo.close()
            return
        elif tipo_estru == 4:  # create a set
            print('\n\n ATUALIZACAO DO CONJUNTO \n')
            my_conj = self.conj
            op = int(input(' 1 -> Atualizar CONJUNTO interio \n 2 -> Apenas um elemento \n\n  Sua opcao aqui:   '))
            print('\r')
            if op is 1:   # 1 Atualizar CONJUNTO interio
                aux = True
                tam = my_conj.__len__()
                k = 1
                while aux is True:
                    valor = int(input('\n Informe um inteiro p/ set[%d] ou 0 pra sair:  ' %(k)))
                    if type(valor) is int and valor != 0 and k <= tam:
                        my_conj.pop()
                        my_conj.add(valor)
                        k = k + 1
                        print(my_conj)
                    elif type(valor) is int and valor != 0 and k > tam:
                        my_conj.add(valor)
                        k = k + 1
                        print(my_conj)
                        # self.create(4, 1)
                        # aux = False
                        # self.my_set(my_conj, 4)
                    else:
                        self.my_set(my_conj, 4)
                        aux = False
                return
            elif op is 2:  #  Atualizar apenas um elemento
                old_value = int(input('\n Informe o valor atual:  '))
                new_value = int(input('\n Digite um novo valor:  '))
                my_conj.remove(old_value)
                my_conj.add(new_value)
                print(my_conj)
                print('\n\n\n')
                self.my_set(my_conj, 4)
                return
        else:
            pass


    def delete(self, tipo_estru):
        if tipo_estru == 1:  # read a list
            my_lista = self.lista
            print('\n\n DELETE LISTA \n')
            my_lista.clear()
            print(my_lista)
            self.my_set(my_lista, 1)
            return
        elif tipo_estru == 2:  # create a dictionary
            my_dicio = self.dicio
            print('\n\n DELETE DICIONARIO \n')
            my_dicio.clear()
            print(my_dicio)
            self.my_set(my_dicio, 1)
            return
        elif tipo_estru == 3:  # delete content in thefile
            print('\n\n DELETE: CONTEÚDO DE ARQUIVO \n')
            arquivo = open('arquivo.txt', 'w')
            arquivo.close()
            return
        elif tipo_estru == 4:  # create a set
            print('\n\n DELETE CONJUNTO \n')
            my_conju = self.conj
            my_conju.clear()
            print(my_conju)
            self.my_set(my_conju, 4)
            return
        else:
            pass


    def int_values_conj(self):
        conj = self.conj
        preench = True
        ind = conj.__len__()
        while preench is True:
            ind = ind + 1
            valor = int(input('Informe um inteiro pra set{%d} ou -1 pra "caracteres" ou "0" pra sair:  ' % (ind)))
            if valor is not 0 and valor > 0:
                conj.add(valor)
                print(conj)
            else:
                preench = False
                self.my_set(conj, 4)
        return valor


    def string_value_conj(self):
        conju = self.conj
        preench = True
        ind = conju.__len__()
        while preench is True:
            ind = ind + 1
            dado = input('\n Informe um dado pra set{%d} ou 0 pra sair:  ' % (ind))
            if dado is not '0':
                conju.add(dado)
                print(conju)
            else:
                preench = False
                self.my_set(conju, 4)
        return dado


    def int_values_lista(self):
        lista = self.lista
        preench = True
        ind = lista.__len__()
        while preench is True:
            valor = int(input('Informe um inteiro pra Lista[%d] ou -1 pra "caracteres" ou "0" pra sair:  ' % (ind + 1)))
            if valor is not 0 and valor > 0:
                lista.append(valor)
                print(lista)
                ind = ind + 1
            else:
                preench = False
                self.my_set(lista, 1)
        return valor


    def string_value_lista(self):
        lista = self.lista
        preench = True
        ind = lista.__len__()
        while preench is True:
            ind = ind + 1
            dado = input('\n Informe um dado pra set{%d} ou 0 pra sair:  ' % (ind))
            if dado is not '0':
                lista.append(dado)
                print(lista)
            else:
                preench = False
                self.my_set(lista, 1)
        return dado
