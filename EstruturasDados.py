# ----------------------------------------
#           importing modules
# ----------------------------------------

import HelperModule as hm
import Crud_operation as cm

# --------------------------------------------
# class contain CRUD METHODS and
# others methods
# --------------------------------------------
class EstruturasDados(object):
    hmo = hm.HelperModule()

    lista = []
    dicio = {}
    arq = 0
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
                    cmo.read(1, hmo)
                else:
                    print('\n\n AVISO: Lista NÃO existe!\n Deve ser criada. \n')
                    pass
                    #obj.create(1, 0)  # create a list # read a list
            elif operacao == 3:
                resp = hmo.verif_estrut_exist(1)  # argument is number of data strucuture. return 1 or 0
                if resp == 1:  # list exist
                    cmo.update(1, hmo)
                else:
                    print('\n\n AVISO: Lista NÃO existe!\n Deve ser criada. \n')
                    pass
                    # obj.create(1, 0)  # create a list # read a list
            elif operacao == 4:
                resp = hmo.verif_estrut_exist(1)  # argument is number of data strucuture. return 1 or 0
                if resp == 1:  # list exist
                    cmo.delete(1, hmo)
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
                    cmo.read(2, hmo)    # read the dict
                else:
                    print('\n\n AVISO: Dicionario NÃO existe!\n Deve ser criado. \n')
                    pass
                    # obj.create(2,0)
            elif operacao == 3:    # update a dict
                resp = hmo.verif_estrut_exist(2)  # argument is number of data strucuture. return 1 or 0
                if resp == 1:      # dict exist
                    cmo.update(2, hmo)  # update dict
                else:
                    print('\n\n AVISO: Dicionario NÃO existe!\n Deve ser criado. \n')
                    pass
                    # obj.create(2,0)  # create a dict
            elif operacao == 4:    # delete the dict
                resp = hmo.verif_estrut_exist(2)  # argument is number of data strucuture. return 1 or 0
                if resp == 1:      # dict exist
                    cmo.delete(2, hmo)  # delete the dict
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
        cmo = cm.Crud_operation()
        run = 1
        while run is 1:
            operacao = hmo.menu_atividade()
            if operacao == 1:     # create a file
                resp = hmo.verif_estrut_exist(3)  # return 1 or 0
                if resp == 1:     # file exist
                    print('\n\n AVISO: Arquivo já existe!\n')
                else:
                    print('\n\n AVISO: Arquivo NÃO existe!\n Deve ser criado.')
                    cmo.create(3, 0, hmo) # create a file
            elif operacao == 2:   # read the file
                resp = hmo.verif_estrut_exist(3)  # argument is number of data strucuture. return 1 or 0
                if resp == 1:     # file exist
                    cmo.read(3, hmo)
                else:
                    print('\n\n AVISO: Arquivo NÃO existe!\n Deve ser criado.')
                    pass
                    # obj.create(3) # create a file
            elif operacao == 3:   # update a file
                resp = hmo.verif_estrut_exist(3)  # argument is number of data strucuture. return 1 or 0
                if resp == 1:     # file exist
                    cmo.update(3, hmo)
                else:
                    print('\n\n AVISO: Arquivo NÃO existe!\n Deve ser criado.')
                    pass
                    # obj.create(3) # create a file
            elif operacao == 4:   # delete the file
                resp = hmo.verif_estrut_exist(3)  # argument is number of data strucuture. return 1 or 0
                if resp is 1:     # file exist
                    cmo.delete(3, hmo)
                else:
                    print('\n\n AVISO: Arquivo NÃO existe!\n Deve ser criado.')
                    pass
                    # obj.create(3)
            else:
                print('\n\n O(a) Sr(a) escolheu VOLTAR\n\n')
                run = 0
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
                    cmo.read(4, hmo)
                else:
                    print('\n\n AVISO: Conjunto NÃO existe!\n Deve ser criado.\n')
                    pass
                    # obj.create(4)  # create a list # read a list
            elif operacao == 3:
                resp = hmo.verif_estrut_exist(4)  # argument is number of data strucuture. return 1 or 0
                if resp == 1:  # list exist
                    cmo.update(4, hmo)
                else:
                    print('\n\n AVISO: Conjunto NÃO existe!\n Deve ser criado.\n')
                    pass
                    # obj.create(4)  # create a list # read a list
            elif operacao == 4:
                resp = hmo.verif_estrut_exist(4)  # argument is number of data strucuture. return 1 or 0
                if resp == 1:  # list exist
                    cmo.delete(4, hmo)
                else:
                    print('\n\n AVISO: Conjunto NÃO existe!\n Deve ser criado.\n')
                    pass
                    # obj.create(4)
            else:
                print('\n\n O(a) Sr(a) escolheu VOLTAR\n\n')
                run = 0
        return