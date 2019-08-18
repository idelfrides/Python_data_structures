#-------------------------------------
# importing my own modules
# ------------------------------------
from data_structures_lib import EstruturasDados as ds

#-------------------------------------
# importing python modules
# ------------------------------------
import glob, os
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
            # print('CURRENT DIR: {}'.format(os.getcwd()))

            content = list()
            try:
                arquivo = open(file_name, 'w', encoding="utf-8")

                print('\n\n Seu ARQUIVO foi criado com sucesso. \n Agora, vamos preenche-lo.\n\n')
                t.sleep(4)
                preench = True
                hour = t.asctime()
                ind = 1
                while preench is True:
                    # ind = ind + 1
                    print('\n Informe um dado pra linha [%d] ou ( N ou n ) pra sair:  '%(ind))
                    dado = input('\n Informe um dado:  ')
                    if dado is not 'N' and dado is not 'n':
                       data = dado + '\n'
                       content.append(data)
                       ind = ind + 1
                    else:
                        arquivo.writelines(content)
                        preench = False
                        arquivo.write(hour)
                        arquivo.write('\n')
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


    def read(self, tipo_estru, file_name):
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
                print(d)
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


    def update(self, tipo_estru, hmo, file_name, up_type):
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

            # op = int(input(' 1 -> Atualizar dicionario interio \n 2 -> Apenas um elemento \n\n  Sua opcao aqui:   '))
            options = ['Atualizar dicionario interio','Apenas um elemento']
            op = hmo.generate_menu(options)
            print('\r')
            if op is 1:   # Atualizar dicionario interio
                aux = True
                tam = my_dicio.__len__()
                k = 1
                while aux is  True:
                    valor = input('\n Informe um valor p/ [%d] ou "quit" pra sair:  ' % (k))
                    if  valor.isalpha() and  valor != 'quit' and k <= tam:
                        my_dicio.pop(k)
                        my_dicio.setdefault(k, valor)
                        k = k + 1
                        print(my_dicio)
                    elif valor.isnumeric() and valor != 0 and k <= tam:
                        my_dicio.pop(k)
                        my_dicio.setdefault(k, int(valor))
                        k = k + 1
                    elif valor.isnumeric() and valor != 0 and k > tam:
                        real_value = int(valor)
                        my_dicio.setdefault(k, real_value)
                        k = k + 1
                        print(my_dicio)
                    elif valor.isalpha() and valor != 'quit' and k > tam:
                        my_dicio.setdefault(k, valor)
                        k = k + 1
                        print(my_dicio)
                    elif valor == 'quit':
                        hmo.my_set(my_dicio, 1)
                        return
                    else:
                        pass

            elif op is 2: # Apenas um elemento
                k = int(input('\n Informe a posicao do elemento:  '))
                v = input('\n Informe o novo valor/dado:  ')
                if k <= 0 or k > my_dicio.__len__():
                    print('\n\n WARNING: INVALID POSITION \n THIS ACTION WILL BE QUITED \n\n')
                    t.sleep(4)
                    return
                elif v.isnumeric():
                    my_dicio.pop(k)
                    my_dicio.setdefault(k, float(v))

                    print(my_dicio)
                    print('\n\n\n')
                    hmo.my_set(my_dicio, 1)
                    return
                elif v.isalpha():
                    my_dicio.pop(k)
                    my_dicio.setdefault(k, v)

                    print(my_dicio)
                    print('\n\n\n')
                    hmo.my_set(my_dicio, 1)
                    return
                else:
                    print('\n\n WARNING: INVALID VALUE \n THIS ACTION WILL BE QUITED \n\n')
                    t.sleep(4)
                    return
        elif tipo_estru == 3:  # update a file
            print('\n\n ATUALIZACAO DE ARQUIVO --> {}\n'.format(file_name))
            if up_type == 'add':
                self.update_add(hmo, file_name)
                return
            elif up_type == 'replace':
                self.update_replace(hmo, file_name)
                return
            else:
                pass
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


    def delete(self, tipo_estru, hmo, file_name):
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
            print('\n\n DELETANDO O ARQUIVO -> {} \n'.format(file_name))
            all_files = glob.glob('*.txt')
            if file_name in all_files:
                os.unlink(file_name)
            hmo.feedback()
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


    def update_add(self, hmo, file_name):
        old_content = list()
        try:
            # arq = open(file_name, 'r', encoding="utf-8")
            # t.sleep(4)
            # for d in arq:
            # old_content.append(d)
            # arq.close()
            # t.sleep(3)

            arquivo = open(file_name, 'a', encoding='utf-8')

            # arquivo.writelines(old_content)
            preench = True
            hour = t.asctime()
            ind = 0
            while preench is True:
                print('\n Informe um dado pra linha [%d] ou ( N ou n ) pra sair:  ' % (ind))
                dado = input('\n Informe um dado:  ')
                if dado is not 'N' and dado is not 'n':
                    data = dado + '\n'
                    old_content.append(data)
                    # arquivo.writelines(data)
                    ind = ind + 1
                else:
                    arquivo.writelines(old_content)
                    preench = False
                    arquivo.write(hour)
                    arquivo.write('\n')
                    arquivo.close()
                    hmo.feedback()
        except Exception as error:
            print('\n ERROR: ocorred when try to open file --> {}'.format(file_name))
            print('\n PYTHON SAYD: {}'.format(error))


    def update_replace(self, hmo, file_name):
        content = list()
        try:
            arq = open(file_name, 'w', encoding="utf-8")
            """ this clear the current 
            content inside the file"""
            # arq.close()

            # t.sleep(4)
            preench = True
            hour = t.asctime()
            ind = 0
            print('\n NOVOS DADOS PRA O SEU ARQUIVO {}\n\n'.format(file_name))
            while preench is True:
                print('\n Informe um dado pra linha [%d] ou ( N ou n ) pra sair:  ' % (ind))
                dado = input('\n Informe um dado:  ')
                if dado is not 'N' and dado is not 'n':
                    data = dado + '\n'
                    content.append(data)
                    ind = ind + 1
                else:
                    arq.writelines(content)
                    preench = False
                    arq.write(hour)
                    arq.write('\n')
                    arq.close()
                    hmo.feedback()
        except Exception as error:
            print('\n ERROR: ocorred when try open a file --> {}.'.format(file_name))
            print('\n PYTHON SAYD: {}'.format(error))
