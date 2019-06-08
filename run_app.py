import EstruturasDados as estd
import time as t


# ----------------- MAIN METHOD ----------------------
def main_app(run):
    est_d_ob = estd.EstruturasDados()
    est_d_ob.app_info()

    while run is True:
        opcao = est_d_ob.menu()
        if opcao == 1:
            est_d_ob.info_structure(1)
            metodoLitas()
        elif opcao is 2:
            est_d_ob.info_structure(2)
            metodoDicionario()
        elif opcao is 3:
            est_d_ob.info_structure(3)
            metodoArquivo()
        elif opcao == 4:
            est_d_ob.info_structure(4)
            metodoConjuntos()
        else:
            print('O(a) Sr(a), escolheu SAIR. A aplicacao sera encerrada. \n\n Grande abraço e Good bye.')
            t.sleep(7)
            run = False
    return

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


# -------------- MAIN METHOD ----------------------
def run_app(estado):
    if estado is 1:
        main_app(True)
    elif estado is 0:
        main_app(False)
    else:
       pass


# ------------------------------------
# THE METHOD THAT START RUNNING
# THE APPLICATIONS
# -----------------------------------
run_app(1)
