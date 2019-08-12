
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
