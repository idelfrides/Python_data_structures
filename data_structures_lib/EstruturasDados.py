# ----------------------------------------
#           importing modules
# ----------------------------------------

from data_structures_lib import Crud_operation as cm
from data_structures_lib import HelperModule as hm
import os, time as t

# --------------------------------------------
# class contain CRUD METHODS and
# others methods
# --------------------------------------------
class EstruturasDados(object):
    hmo = hm.HelperModule()

    lista = []
    dicio = {}
    arq = []     # file holder - store all name of files exists in files_folder
    conj = set()

    def __init__(self):
        pass


    # ------------- DATA STRUCTURES METHODS --------------
    # ESTRUTURA DE DADO  LISTA. CÓDIGO 1
    def metodoLitas(self, hmo):
        cmo = cm.Crud_operation()
        run = 1
        while run is 1:
            operacao = hmo.menu_atividade()
            if operacao == 1:
                resp = hmo.verif_estrut_exist(1)   # return 1 or 0
                if resp == 1:  # list exist
                    print('\n\n AVISO: Lista já existe!\n')
                else:
                    print('\n\n AVISO: Lista NÃO existe!\n Deve ser criada. \n')
                    cmo.create(1, 1, hmo)  # create a list
            elif operacao == 2:
                resp = hmo.verif_estrut_exist(1)  # argument is number of data strucuture. return 1 or 0
                if resp == 1:  # list exist
                    cmo.read(1, 'notused')
                else:
                    print('\n\n AVISO: Lista NÃO existe!\n Deve ser criada. \n')
                    pass
                    #obj.create(1, 0)  # create a list # read a list
            elif operacao == 3:
                resp = hmo.verif_estrut_exist(1)  # argument is number of data strucuture. return 1 or 0
                if resp == 1:  # list exist
                    cmo.update(1, hmo, 'notused', 'notused')
                else:
                    print('\n\n AVISO: Lista NÃO existe!\n Deve ser criada. \n')
                    pass
                    # obj.create(1, 0)  # create a list # read a list
            elif operacao == 4:
                resp = hmo.verif_estrut_exist(1)  # argument is number of data strucuture. return 1 or 0
                if resp == 1:  # list exist
                    cmo.delete(1, hmo, 'notused')
                else:
                    print('\n\n AVISO: Lista NÃO existe!\n Deve ser criada. \n')
                    pass
                    # obj.create(1,0)
            else:
                print('\n\n O(a) Sr(a) escolheu VOLTAR\n\n!')
                run = 0
        return

    # ESTRUTURA DE DADO DICIONÁRIO. CÓDIGO  2
    def metodoDicionario(self, hmo):
        cmo = cm.Crud_operation()
        run = 1
        while run is 1:
            operacao = hmo.menu_atividade()
            if operacao == 1:    # create a dict
                resp = hmo.verif_estrut_exist(2)  # return 1 or 0
                if resp == 1:      # dict exist
                    print('\n\n AVISO: Dicionario já existe!\n')
                else:
                    print('\n\n AVISO: Dicionario NÃO existe!\n Deve ser criado. \n')
                    cmo.create(2, 0, hmo)  # create a dict
            elif operacao == 2:    # read the dict
                resp = hmo.verif_estrut_exist(2)  # argument is number of data strucuture. return 1 or 0
                if resp == 1:      # dict exist
                    cmo.read(2, 'notused')    # read the dict
                else:
                    print('\n\n AVISO: Dicionario NÃO existe!\n Deve ser criado. \n')
                    pass
                    # obj.create(2,0)
            elif operacao == 3:    # update a dict
                resp = hmo.verif_estrut_exist(2)  # argument is number of data strucuture. return 1 or 0
                if resp == 1:      # dict exist
                    cmo.update(2, hmo, 'notused','notused')  # update dict
                else:
                    print('\n\n AVISO: Dicionario NÃO existe!\n Deve ser criado. \n')
                    pass
                    # obj.create(2,0)  # create a dict
            elif operacao == 4:    # delete the dict
                resp = hmo.verif_estrut_exist(2)  # argument is number of data strucuture. return 1 or 0
                if resp == 1:      # dict exist
                    cmo.delete(2, hmo, 'obama')  # delete the dict
                else:
                    print('\n\n AVISO: Dicionario NÃO existe!\n Deve ser criado. \n')
                    pass
                    # obj.create(2,0)
            else:
                print('\n\n O(a) Sr(a) escolheu VOLTAR\n\n')
                run = 0
        return

    # ESTRUTURA DE DADO ARQUIVO. CÓDIGO  3
    def metodoArquivo(self, hmo):
        # print('CURRENT DIR: {}'.format(os.getcwd()))
        cmo = cm.Crud_operation()
        hmo.change_dir(2)
        hmo.prepare2read()
        # hmo.change_dir(2)
        run = True
        while run is True:
            operacao = hmo.menu_atividade()
            if operacao == 1:     # create a file
                resp = hmo.verif_estrut_exist(3)  # return 1 or 0
                if resp == 1:     # file exist
                    info="""
                     ***************************************
                        FEEDBACK: Arquivo(s) existente(s)
                     ***************************************
                        Foram encontrados os seguintes
                        arquivos:
                     
                     """
                    print('{}'.format(info))

                    for f in self.arq:
                        print('\n File --> {}'.format(f))

                    ans = hmo.oper_or_new_file()

                    if ans == 'operar':
                        pass
                    elif ans == 'novo':
                        cmo.create(3, 0, hmo)
                    elif ans == 'quit':
                        run = True # go back to menu of activities
                    else:
                        pass
                else:
                    print('\n\n AVISO: Arquivo NÃO existe!\n Deve ser criado.')
                    cmo.create(3, 0, hmo) # create a file
            elif operacao == 2:   # read the file
                resp = hmo.verif_estrut_exist(3)  # argument is number of data strucuture. return 1 or 0
                if resp == 1:     # file exist
                    file = hmo.file2oper()
                    if file != 'quit':
                        cmo.read(3, file)
                    elif file =='quit':
                        run = True
                    else:
                        pass
                else:
                    warning = """
                    ************************************
                        WARNING: NOTAS NAO REGISTRADA
                    ************************************
                       Nenhuma nota foi encontrada.
                       Crie um nova pra operar. 
                       No menu a seguir escolhe opcao
                        --> CREATE
                    """
                    t.sleep(4)
                    print('{}'.format(warning))
                    pass
                    # obj.create(3) # create a file
            elif operacao == 3:   # update a file
                resp = hmo.verif_estrut_exist(3)  # argument is number of data strucuture. return 1 or 0
                if resp == 1:     # file exist
                    file = hmo.file2oper()
                    up_type = hmo.update_type()
                    if file != 'quit':
                        cmo.update(3, hmo, file, up_type)
                    elif file == 'quit' or up_type == 'quit':
                        run = True
                    else:
                        pass

                else:
                    print('\n\n AVISO: Arquivo NÃO existe!\n Deve ser criado.')
                    pass
                    # obj.create(3) # create a file
            elif operacao == 4:   # delete the file
                resp = hmo.verif_estrut_exist(3)  # argument is number of data strucuture. return 1 or 0
                if resp is 1:     # file
                    file = hmo.file2oper()
                    if file != 'quit':
                        cmo.delete(3, hmo, file)
                    elif file == 'quit':
                        run = True
                    else:
                        pass
                else:
                    print('\n\n AVISO: Arquivo NÃO existe!\n Deve ser criado.')
                    pass
                    # obj.create(3)
            else:
                print('\n\n O(a) Sr(a) escolheu VOLTAR\n\n')
                run = 0
        hmo.change_dir(1)
        return


    # ESTRUTURA DE DADO CONJUNTO. CÓDIGO  4
    def metodoConjuntos(self, hmo):
        cmo = cm.Crud_operation()
        run = 1
        while run is 1:
            operacao = hmo.menu_atividade()
            if operacao == 1:
                resp = hmo.verif_estrut_exist(4)  # return 1 or 0
                if resp == 1:  # list exist
                    print('\n\n AVISO: Conjunto já existe!\n')
                else:
                    print('\n\n AVISO: Conjunto NÃO existe!\n Deve ser criado. \n ')
                    cmo.create(4, 1, hmo)  # create a list
            elif operacao == 2:
                resp = hmo.verif_estrut_exist(4)  # argument is number of data strucuture. return 1 or 0
                if resp == 1:  # list exist
                    cmo.read(4, 'file')
                else:
                    print('\n\n AVISO: Conjunto NÃO existe!\n Deve ser criado.\n')
                    pass
                    # obj.create(4)  # create a list # read a list
            elif operacao == 3:
                resp = hmo.verif_estrut_exist(4)  # argument is number of data strucuture. return 1 or 0
                if resp == 1:  # list exist
                    cmo.update(4, hmo, 'notused', 'notused')
                else:
                    print('\n\n AVISO: Conjunto NÃO existe!\n Deve ser criado.\n')
                    pass
                    # obj.create(4)  # create a list # read a list
            elif operacao == 4:
                resp = hmo.verif_estrut_exist(4)  # argument is number of data strucuture. return 1 or 0
                if resp == 1:  # list exist
                    cmo.delete(4, hmo, 'notused')
                else:
                    print('\n\n AVISO: Conjunto NÃO existe!\n Deve ser criado.\n')
                    pass
                    # obj.create(4)
            else:
                print('\n\n O(a) Sr(a) escolheu VOLTAR\n\n')
                run = 0
        return