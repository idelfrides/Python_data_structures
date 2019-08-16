import EstruturasDados as ds
import HelperModule as hm
import time as t


# ----------------------------------
#         MAIN METHOD
# ----------------------------------
def main_app(run):
    dso = ds.EstruturasDados()
    hmo = hm.HelperModule()

    hmo.app_info()

    while run is True:
        opcao = hmo.menu()
        if opcao == 1:
            hmo.info_structure('lista')
            dso.metodoLitas(hmo)
        elif opcao is 2:
            hmo.info_structure('dicionario')
            dso.metodoDicionario(hmo)
        elif opcao is 3:
            hmo.info_structure('arquivo')
            dso.metodoArquivo(hmo)
        elif opcao == 4:
            hmo.info_structure('conjunto')
            dso.metodoConjuntos(hmo)
        else:
            print('\n O(a) Sr(a), escolheu SAIR. \n A aplicacao sera encerrada. \n\n Grande abraço e Good bye. \n\n\n')
            t.sleep(7)
            run = False
    return


# ------------------------------------
# THE METHOD THAT START RUNNING
# THE APPLICATIONS
# -----------------------------------
if __name__ == "__main__":
    main_app(True)  
