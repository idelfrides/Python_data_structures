
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
       
     
    
    
    
# ------------- DATA STRUCTURES METHODS --------------
# ESTRUTURA DE DADO  LISTA. CÓDIGO 1
def metodoLitas():
    obj = estd.EstruturasDados()
    run = 1
    while run is 1:
        operacao = obj.menu_atividade()
        if operacao == 1:
            resp = obj.verif_estrut_exist(1)   # return 1 or 0
            if resp == 1:  # list exist
                print('\n\n AVISO: Lista já existe!\n')
            else:
                print('\n\n AVISO: Lista NÃO existe!\n Deve ser criada. \n')
                obj.create(1, 1)  # create a list
        elif operacao == 2:
            resp = obj.verif_estrut_exist(1)  # argument is number of data strucuture. return 1 or 0
            if resp == 1:  # list exist
                obj.read(1)
            else:
                print('\n\n AVISO: Lista NÃO existe!\n Deve ser criada. \n')
                pass
                #obj.create(1, 0)  # create a list # read a list
        elif operacao == 3:
            resp = obj.verif_estrut_exist(1)  # argument is number of data strucuture. return 1 or 0
            if resp == 1:  # list exist
                obj.update(1)
            else:
                print('\n\n AVISO: Lista NÃO existe!\n Deve ser criada. \n')
                pass
                # obj.create(1, 0)  # create a list # read a list
        elif operacao == 4:
            resp = obj.verif_estrut_exist(1)  # argument is number of data strucuture. return 1 or 0
            if resp == 1:  # list exist
                obj.delete(1)
            else:
                print('\n\n AVISO: Lista NÃO existe!\n Deve ser criada. \n')
                pass
                # obj.create(1,0)
        else:
            print('O(a) Sr(a), escolheu SAIR DA APLICACAO. \n Grande abraço!')
            run = 0
    return


# ESTRUTURA DE DADO DICIONÁRIO. CÓDIGO  2
def metodoDicionario():
    obj = estd.EstruturasDados()
    run = 1
    while run is 1:
        operacao = obj.menu_atividade()
        if operacao == 1:    # create a dict
            resp = obj.verif_estrut_exist(2)  # return 1 or 0
            if resp == 1:      # dict exist
                print('\n\n AVISO: Dicionario já existe!\n')
            else:
                print('\n\n AVISO: Dicionario NÃO existe!\n Deve ser criado. \n')
                obj.create(2, 0)  # create a dict
        elif operacao == 2:    # read the dict
            resp = obj.verif_estrut_exist(2)  # argument is number of data strucuture. return 1 or 0
            if resp == 1:      # dict exist
                obj.read(2)    # read the dict
            else:
                print('\n\n AVISO: Dicionario NÃO existe!\n Deve ser criado. \n')
                pass
                # obj.create(2,0)
        elif operacao == 3:    # update a dict
            resp = obj.verif_estrut_exist(2)  # argument is number of data strucuture. return 1 or 0
            if resp == 1:      # dict exist
                obj.update(2)  # update dict
            else:
                print('\n\n AVISO: Dicionario NÃO existe!\n Deve ser criado. \n')
                pass
                # obj.create(2,0)  # create a dict
        elif operacao == 4:    # delete the dict
            resp = obj.verif_estrut_exist(2)  # argument is number of data strucuture. return 1 or 0
            if resp == 1:      # dict exist
                obj.delete(2)  # delete the dict
            else:
                print('\n\n AVISO: Dicionario NÃO existe!\n Deve ser criado. \n')
                pass
                # obj.create(2,0)
        else:
            print('O(a) Sr(a), escolheu SAIR DA APLICACAO. \n Grande abraço!')
            run = 0
    return


# ESTRUTURA DE DADO ARQUIVO. CÓDIGO  3
def metodoArquivo():
    obj = estd.EstruturasDados()
    run = 1
    while run is 1:
        operacao = obj.menu_atividade()
        if operacao == 1:     # create a file
            resp = obj.verif_estrut_exist(3)  # return 1 or 0
            if resp == 1:     # file exist
                print('\n\n AVISO: Arquivo já existe!\n')
            else:
                print('\n\n AVISO: Arquivo NÃO existe!\n Deve ser criado.')
                obj.create(3, 0) # create a file
        elif operacao == 2:   # read the file
            resp = obj.verif_estrut_exist(3)  # argument is number of data strucuture. return 1 or 0
            if resp == 1:     # file exist
                obj.read(3)
            else:
                print('\n\n AVISO: Arquivo NÃO existe!\n Deve ser criado.')
                pass
                # obj.create(3) # create a file
        elif operacao == 3:   # update a file
            resp = obj.verif_estrut_exist(3)  # argument is number of data strucuture. return 1 or 0
            if resp == 1:     # file exist
                obj.update(3)
            else:
                print('\n\n AVISO: Arquivo NÃO existe!\n Deve ser criado.')
                pass
                # obj.create(3) # create a file
        elif operacao == 4:   # delete the file
            resp = obj.verif_estrut_exist(3)  # argument is number of data strucuture. return 1 or 0
            if resp is 1:     # file exist
                obj.delete(3)
            else:
                print('\n\n AVISO: Arquivo NÃO existe!\n Deve ser criado.')
                pass
                # obj.create(3)
        else:
            print('O(a) Sr(a), escolheu SAIR DA APLICACAO. \n Grande abraço!')
            run = 0
    return


# ESTRUTURA DE DADO CONJUNTO. CÓDIGO  4
def metodoConjuntos():
    obj = estd.EstruturasDados()
    run = 1
    while run is 1:
        operacao = obj.menu_atividade()
        if operacao == 1:
            resp = obj.verif_estrut_exist(4)  # return 1 or 0
            if resp == 1:  # list exist
                print('\n\n AVISO: Conjunto já existe!\n')
            else:
                print('\n\n AVISO: Conjunto NÃO existe!\n Deve ser criado. \n ')
                obj.create(4, 1)  # create a list
        elif operacao == 2:
            resp = obj.verif_estrut_exist(4)  # argument is number of data strucuture. return 1 or 0
            if resp == 1:  # list exist
                obj.read(4)
            else:
                print('\n\n AVISO: Conjunto NÃO existe!\n Deve ser criado.\n')
                pass
                # obj.create(4)  # create a list # read a list
        elif operacao == 3:
            resp = obj.verif_estrut_exist(4)  # argument is number of data strucuture. return 1 or 0
            if resp == 1:  # list exist
                obj.update(4)
            else:
                print('\n\n AVISO: Conjunto NÃO existe!\n Deve ser criado.\n')
                pass
                # obj.create(4)  # create a list # read a list
        elif operacao == 4:
            resp = obj.verif_estrut_exist(4)  # argument is number of data strucuture. return 1 or 0
            if resp == 1:  # list exist
                obj.delete(4)
            else:
                print('\n\n AVISO: Conjunto NÃO existe!\n Deve ser criado.\n')
                pass
                # obj.create(4)
        else:
            print('O(a) Sr(a), escolheu SAIR DA APLICACAO. \n Grande abraço!')
            run = 0
    return

