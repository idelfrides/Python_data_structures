from data_structures_lib import EstruturasDados as ds
from data_structures_lib import HelperModule as hm
import time as t, os


# ----------------------------------
#         MAIN METHOD
# ----------------------------------
def main_app(run):
    dso = ds.EstruturasDados()
    hmo = hm.HelperModule()

    hmo.app_info()

    while run is True:
        root_dir_path = os.path.dirname(os.path.abspath(__file__))
        # os.chdir(root_dir_path)
        print('CURRENT DIR: {}'.format(root_dir_path))
        # print('CURRENT DIR getcwd: {}'.format(os.getcwd()))
        opcao = hmo.menu()
        if opcao == 1:
            hmo.info_structure('lista')
            dso.metodoLitas(hmo)
        elif opcao is 2:
            hmo.info_structure('dicionario')
            dso.metodoDicionario(hmo)
        elif opcao is 3:
            hmo.info_structure('arquivo')
            dso.metodoArquivo(hmo, root_dir_path)
            dso.arq.clear()  # clear the controll list of files created
        elif opcao == 4:
            hmo.info_structure('conjunto')
            dso.metodoConjuntos(hmo)
        else:
            bye = """
            ------------------------------------
                O(a) Sr(a), escolheu SAIR. 
                A aplicacao sera encerrada.\n
                Grande abraço e Good bye.
            ------------------------------------ 
            """
            print('\n {}'.format(bye))
            print('\n\n\n')
            t.sleep(5)
            run = False
    return


# ------------------------------------
# START RUNNING THE APPLICATIONS
# ------------------------------------
if __name__ == "__main__":
    main_app(True)  
