import os

from data_structures_lib import EstruturasDados as ds
import time as t

class Crud_operation(object):

    def __init__(self):
        pass

   
    # ----------------------------------
    #           CRUD METHODS
    # ----------------------------------
    def create(self, tipo_estru, tipo, hmo):
        if tipo_estru == 1:    # create a list
            lista = []
            print('\n\n Sua LISTA foi criada com sucesso. \n Agora, vamos preenche-la.\n\n')
            hmo.my_set(lista, 1)
            if tipo is 1:
                hmo.all_values_lista()
                return
            else:
                pass
        elif tipo_estru == 2:   # create a dictionary
            dicionario = {}
            # hmo.feedback()
            print('\n\n Seu DICIONARIO foi criado com sucesso. \n Agora, vamos preenche-lo.\n\n')
            hmo.my_set(dicionario, 2)
            hmo.all_values_dict()
            return
        elif tipo_estru == 3:   # create a file
            file_name = hmo.get_file_name()
            print('CURRENT DIR: {}'.format(os.getcwd()))

            # hmo.change_dir(2)    # go to files_folder directory
            try:
                arquivo = open(file_name, 'w', encoding="utf-8")

                print('\n\n Seu ARQUIVO foi criado com sucesso. \n Agora, vamos preenche-lo.\n\n')
                t.sleep(4)
                preench = True
                hour = t.asctime()
                ind = 0
                while preench is True:
                    # ind = ind + 1
                    print('\n Informe um dado pra linha [%d] ou ( N ou n ) pra sair:  '%(ind))
                    dado = input('\n Informe um dado:  ')
                    if dado is not 'N' and dado is not 'n':
                       data = dado + '\n'
                       arquivo.writelines(data)
                       ind = ind + 1
                    else:
                        preench = False
                        arquivo.write(hour)
                        arquivo.close()
                        hmo.feedback()
                        # hmo.change_dir(1) # go to root dir
            except Exception as error:
                print('\n ERROR: ocorred when try crete a file --> {}.'.format(file_name))
                print('\n This is the error: {}'.format(error))
            return
        elif tipo_estru == 4:  # create a set
            conj = set()
            hmo.my_set(conj, 4)
            if tipo is 1:
                hmo.all_values_conj()
                return
            else:
                pass
        else:
            return


    def read(self, tipo_estru, hmo, file_name):
        dso = ds.EstruturasDados()
        if tipo_estru == 1:   # read the list
            my_lista = dso.lista
            print('\n\n APRESENTACAO DA LISTA \n')
            print(my_lista)
            print('\n\n')
            return
        elif tipo_estru == 2:  # read the dictionary
            my_dicio = dso.dicio
            print('\n\n APRESENTACAO DO DICIONARIO \n')
            print(my_dicio)
            print('\n\n')
            return
        elif tipo_estru == 3:  # read  the file
            print('\n\n LEITURA DE ARQUIVO --> {} \n\n'.format(file_name))
            arquivo = open(file_name, 'r', encoding="utf-8")
            # dados_arq = arquivo.readlines()
            for d in arquivo:
                # v = d.split()
                print(d)
                # print('\n')
            # hmo.my_set(1, 3)
            arquivo.close()
            print('\n\n')
            return
        elif tipo_estru == 4:  # read the set
            print('\n\n APRESENTACAO DO CONJUNTO \n')
            my_conj = dso.conj
            print(my_conj)
            print('\n\n')
            return
        else:
            pass


    def update(self, tipo_estru, hmo):
        dso = ds.EstruturasDados()

        if tipo_estru == 1:   # read a list
            my_lista = dso.lista
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
                        hmo.my_set(my_lista, 1)
                        return my_lista
            elif op is 2:
                k = int(input('\n Informe a posicao do elemento:  '))
                v = int(input('\n Informe o novo valor:  '))
                my_lista.pop(k)
                my_lista.insert(k, v)
                print(my_lista)
                print('\n\n\n')
                hmo.my_set(my_lista, 1)
                return
        elif tipo_estru == 2:  # create a dictionary
            my_dicio = dso.dicio
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
                        hmo.my_set(my_dicio, 1)
                        return
            elif op is 2:
                k = int(input('\n Informe a posicao do elemento:  '))
                v = int(input('\n Informe o novo valor:  '))
                my_dicio.pop(k)
                my_dicio.setdefault(k, v)
                print(my_dicio)
                print('\n\n\n')
                hmo.my_set(my_dicio, 1)
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
                    hmo.my_set(1, 3)
                    arquivo.close()
            return
        elif tipo_estru == 4:  # create a set
            print('\n\n ATUALIZACAO DO CONJUNTO \n')
            my_conj = dso.conj
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
                        hmo.my_set(my_conj, 4)
                        aux = False
                return
            elif op is 2:  #  Atualizar apenas um elemento
                old_value = int(input('\n Informe o valor atual:  '))
                new_value = int(input('\n Digite um novo valor:  '))
                my_conj.remove(old_value)
                my_conj.add(new_value)
                print(my_conj)
                print('\n\n\n')
                hmo.my_set(my_conj, 4)
                return
        else:
            pass


    def delete(self, tipo_estru, hmo):
        dso = ds.EstruturasDados()
        if tipo_estru == 1:  # read a list
            my_lista = dso.lista
            print('\n\n DELETE LISTA \n')
            my_lista.clear()
            print(my_lista)
            hmo.my_set(my_lista, 1)
            return
        elif tipo_estru == 2:  # create a dictionary
            my_dicio = dso.dicio
            print('\n\n DELETE DICIONARIO \n')
            my_dicio.clear()
            print(my_dicio)
            hmo.my_set(my_dicio, 1)
            return
        elif tipo_estru == 3:  # delete content in thefile
            print('\n\n DELETE: CONTEÚDO DE ARQUIVO \n')
            arquivo = open('arquivo.txt', 'w')
            arquivo.close()
            return
        elif tipo_estru == 4:  # create a set
            print('\n\n DELETE CONJUNTO \n')
            my_conju = dso.conj
            my_conju.clear()
            print(my_conju)
            hmo.my_set(my_conju, 4)
            return
        else:
            pass



    
