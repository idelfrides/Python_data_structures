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
            print('zn O(a) Sr(a), escolheu SAIR. \n A aplicacao sera encerrada. \n\n Grande abraço e Good bye. \n\n\n')
            t.sleep(7)
            run = False
    return


# ------------------------------------
# THE METHOD THAT START RUNNING
# THE APPLICATIONS
# -----------------------------------
if __name__ == "__main__":
    main_app(True)  
