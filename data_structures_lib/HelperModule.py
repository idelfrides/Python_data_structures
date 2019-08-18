# ----------------------------------------
#           importing modules
# ----------------------------------------
import glob, os
import time as t

from data_structures_lib import EstruturasDados as ds


# ----------------------------------
# THIS METHOD CONTAIN METHODS USED
# LIKE COMPLEMEN
# ----------------------------------


class HelperModule(object):

    def __init__(self):
        pass


    def app_info(self):
        print('''
        *********************************************
            THIS APPLICATION IMPLEMENTS A CRUD 
            OPERATIONS ON DATA STRUCTURES,
            LIKE: 
            ---- IMUTABLE ----------
                - TUPLE
                - STRING
            ---- MUTABLE -----------
                - LIST
                - DICTIONARY
                - FILE
                - SET     
                
        ********************************************  
        ''')

    def menu(self):
        print(' MENU \n\n 1 - Listas \n 2 - Dicionário \n 3 - Arquivos \n 4 - Conjuntos  \n 0 - Sair\n')
        yes_option = False
        option = None
        while yes_option is False:
            try:
                option = int(input('\n Enter an option:  '))
                if option in range(5):
                    yes_option = True
                else:
                    print('\n opcao: ', option)
                    print('\n WARNING: OPCAO INVALIDA!!!\n\n')
            except Exception as error:
                print('\n You entered a CARACTER or a STRING')
                print('\n WARNING: INVALID OPTION!!!')
                print('\n PYTHON SAID: {}'.format(error))
        return option

    def menu_atividade(self):
        print('\n MENU DE ATIVIDADES CRUD: \n'
              '\n 1 - CREATE '
              '\n 2 - READ '
              '\n 3 - UPDATE '
              '\n 4 - DELETE  '
              '\n 0 - Voltar\n')
        yes_act = False
        option = None
        while yes_act is False:
            try:
                option = int(input('\n Enter an action to perform:  '))
                if option in range(5):
                    yes_act = True
                else:
                    print('\n You entered --> {} '.format(option))
                    print('AVISO: OPCAO INVALIDA!!!\n\n')
            except Exception as error:
                print('\n You entered a CARACTER or a STRING')
                print('\n WARNING: INVALID OPTION!!!')
                print('\n PYTHON SAID: {}'.format(error))
        return option


    def my_set(self, instance, value):
        dso = ds.EstruturasDados()
        if value == 1:
            dso.lista = instance
        elif value == 2:
            dso.dicio = instance
        elif value == 3:
            dso.arq = instance
        elif value == 4:
            dso.conj = instance
        else:
            pass


    def my_get(self, owner):
        dso = ds.EstruturasDados()
        if owner == 1:
            if dso.lista:
                return 1
            else:
                return 0
        elif owner == 2:
            if dso.dicio:
                return 1
            else:
                return 0
        elif owner == 3:
            # print(dso.arq)
            if dso.arq.__len__() > 0:
                return 1
            else:
                return 0
        elif owner == 4:
            if dso.conj:
                return 1
            else:
                return 0
        else:
            pass


    def verif_estrut_exist(self, est):
        if est == 1:
           return  self.my_get(1)  # LIST
        elif est == 2:             # dictionary exist
            return self.my_get(2)  # DICT
        elif est == 3:             # list exist
            return self.my_get(3)  # FILE
        elif est == 4:
            return self.my_get(4)  # SET
        else:
            pass


    def info_structure(self, est):
        info = """
        --------------------------------------
            VOCE ESCOLHEU TRABALHAR COM ...
        --------------------------------------        
        """
        struc_upper = est.upper()
        if est == 'lista':
            print('{} {}'.format(info, struc_upper))
        elif est == 'dicionario':
            print('{} {}'.format(info, struc_upper))
        elif est == 'arquivo':
            print('{}{}'.format(info, struc_upper))
        elif est == 'conjunto':
            print('{}{}'.format(info, struc_upper))
        else:
            pass
        

    def all_values_lista(self):
        dso = ds.EstruturasDados()
        lista = dso.lista
        preench = True
        ind = lista.__len__()
        valor = None
        while preench is True:
            print('\n Informe um numero, caractere ou palavra pra Lista[%d]' %(ind + 1))
            print('\n quit -> pra sair')
            help_value = input('\n Enter some: ')
            if help_value.isnumeric():
                valor = int(help_value)
                lista.append(valor)
                print(lista)
                ind = ind + 1
            elif help_value.isalpha() and (help_value != 'QUIT' and help_value != 'quit'):
                lista.append(help_value)
                print(lista)
                ind = ind + 1
            elif help_value == 'QUIT' or help_value == 'quit':
                preench = False
                self.my_set(lista, 1)
            elif help_value.isalnum():
                preench = True
            else:
                pass
        return


    def all_values_dict(self):
        dso = ds.EstruturasDados()
        dicio = dso.dicio
        preench = True
        ind = dicio.__len__()
        valor = None
        while preench is True:
            print('\n Informe um numero, caractere ou palavra pra Dicionario[%d]' %(ind + 1))
            print('\n quit -> pra sair')
            help_value = input('\n Enter some: ')

            if help_value.isnumeric():
                ind = ind + 1
                valor = int(help_value)
                dicio[(ind)] = valor
                print(dicio)
            elif help_value.isalpha() and (help_value != 'QUIT' and help_value != 'quit'):
                ind = ind + 1
                dicio[(ind)] = help_value
                print(dicio)
            elif help_value == 'QUIT' or help_value == 'quit':
                preench = False
                self.my_set(dicio, 2)
            elif help_value.isalnum():
                preench = True
            else:
                pass
        return


    def all_values_conj(self):
        dso = ds.EstruturasDados()
        conj = dso.conj
        preench = True
        ind = conj.__len__()
        valor = None
        while preench is True:
            ind = ind + 1
            print('\n Informe um numero, caractere ou palavra pra Conjunto[%d]' % (ind + 1))
            print('\n quit -> pra sair')
            help_value = input('\n Enter some: ')
            if help_value.isnumeric():
                valor = int(help_value)
                conj.add(valor)
                print(conj)
                ind = ind + 1
            elif help_value.isalpha() and (help_value != 'QUIT' and help_value != 'quit'):
                conj.add(help_value)
                print(conj)
                ind = ind + 1
            elif help_value == 'QUIT' or help_value == 'quit':
                preench = False
                self.my_set(conj, 1)
            elif help_value.isalnum():
                preench = True
            else:
                pass
        return

    def get_file_name(self):
        file_name = 'wmfile'
        yes_name = False
        while yes_name is False:
            try:
                file_name = input('\n Enter your file name with 5 or more caracters:  ')
                if file_name.isalpha() and file_name.__len__() >= 5:
                    yes_name = True
                else:
                    print('\n You entered --> {}'.format(file_name))
                    print('\n WARNING: INVALID NAME!!!')
                    print('\n You entered a STRING under 5 CARACTERS or an number')
            except Exception as error:
                print('\n You entered a STRING under 5 CARACTERS')
                print('\n WARNING: INVALID NAME!!!')
                print('\n PYTHON SAID: {}'.format(error))
        complete_file = file_name + '.txt'
        # complete_file = file_name + '.' + 'txt'
        return  complete_file


    def change_dir(self, code):
        if code is 'root':
            os.chdir('ESTRUTURAS_DADOS')
        elif code is 1:     # go to root dir
            current_dir_path = os.path.dirname(os.path.abspath(__file__))
            os.chdir(current_dir_path)
            print(os.getcwd())
        elif code is 2:   # go to files_folder dir
            # self.change_dir('root')
            os.chdir('files_folder')
            # print(os.getcwd())
        else:
            pass

    def prepare2read(self):
        dso = ds.EstruturasDados()
        # self.change_dir(2)
        for file in glob.glob('*.txt'):
            dso.arq.append(file)

        # self.change_dir(1)

    def oper_or_new_file(self):
        option = None
        yes_name = False
        while yes_name is False:
            print('\n\n  MENU ACTION \n'
                  '\n operar -> Operar sobre um arquivo existe'
                  '\n novo -> Criar um novo arquivo'
                  '\n quit -> Abandonar')
            try:
                option = input('\n Enter your choice:  ')
                actions = ['operar', 'novo', 'quit']
                if option in actions:
                    yes_name = True
                elif option.isnumeric():
                    raise Exception
                else:
                    print('\n You entered --> {}'.format(option))
                    print('\n WARNING: INVALID OPTION!!!')
                    print('\n You entered a STRING do not listed on MENU ACTION or a number')
            except Exception as error:
                print('\n WARNING: INVALID OPTION!!!')
                print('\n You entered a NUMBER/NUMERIC')
                print('\n PYTHON SAID: {}'.format(error))
        return option

    def file2oper(self):
        dso = ds.EstruturasDados()
        len = dso.arq.__len__()
        # real_len = len - 1
        print('\n ARQUIVOS DISPONÍVEIS PRA OPERAR \n')

        # file = None
        yes_file = False
        while yes_file is False:
            for ind in range(len):
                p = ind + 1
                print('\n [{}] -> {}'.format(p, dso.arq[ind]))
            quit = 'quit'
            zero = 0
            print('\n [{}] -> {}'.format(zero, quit))
            try:
                option =  int(input('\n Enter your option:  '))
                if option in range(1, len + 1):
                    file = dso.arq[option-1]
                    yes_file = True
                elif option is 0:
                    file = 'quit'
                    yes_file = True
                else:
                    print('\n You entered --> {}'.format(option))
                    print('\n WARNING: INVALID OPTION!!!')
                    print('\n You entered a NUMBER do not listed on MENU ABOUVE\n')
            except Exception as error:
                print('\n WARNING: INVALID OPTION!!!')
                print('\n You entered a STRING/CARACTER')
                print('\n PYTHON SAID: {}'.format(error))
        return file

    def feedback(self):
        print('\n\n -------------------------------------------')
        print('\n\t    OPERATION DONE SUCCESSFULLY')
        print('\n -------------------------------------------')

    def update_type(self):
        option = None
        yes_type = False
        while yes_type is False:
            print('\n\n  MENU TYPE UPDATE \n'
                '\n add -> UPDATE ADD: Adicionar novo conteúdo ao já existente no arquivo'
                '\n replace -> UPDATE REPLACE: Substituir o conteúdo existente'
                '\n quit -> Abandonar')
            try:
                option = input('\n Enter your choice:  ')
                myoptions = ['add', 'replace', 'quit']
                if option in myoptions:
                    yes_type = True
                elif option.isnumeric():
                    raise Exception
                else:
                    print('\n You entered --> {}'.format(option))
                    print('\n WARNING: INVALID OPTION!!!')
                    print('\n You entered a STRING do not listed on MENU TYPE UPDATE or a number')
            except Exception as error:
                print('\n WARNING: INVALID OPTION!!!')
                print('\n You entered a NUMBER/NUMERIC')
                print('\n PYTHON SAID: {}'.format(error))
        return option

    def generate_menu(self, options):
        """
             parameters definition
        -------------------------------------
        :param options - a list of options
            ex.: options['create', 'read', 'update',  'delete']

        """
        print('\n I AM GENERATEMENU \n\n')
        n = options.__len__()

        print('\n MENU DE OPTIONS \n')
        for ind in range(n):
            choice = ind + 1
            op = options[ind].upper()
            print('\n {} --> {}'.format(choice, op))

        choice = 'quit'
        op = 'Sair'
        print('\n {} --> {}'.format(choice, op))

        yes_act = False
        option = None
        while yes_act is False:
            try:
                option = int(input('\n\n Enter an option to perform:  '))
                if option in range(1, n + 1):
                    yes_act = True  # option is valid
                elif option == 'quit':
                    yes_act = True
                else:
                    print('\n You entered --> {} '.format(option))
                    print('\n WARNING: INVALID OPTION!!\n\n')
            except Exception as error:
                print('\n You entered a CARACTER or a STRING')
                print('\n WARNING: INVALID OPTION!!!')
                print('\n PYTHON SAID: {}'.format(error))
        return option

    def getting_values(self, struct, type_struct, type_data):
        """
             parameters definition
        -------------------------------------
        :param type_data - define the type of data user expected.
            It can be 'numeric', 'alpha' or 'both'
        """
        if type_data == 'numeric':
            struct = self.get_numeric_values(struct, type_struct)
        elif type_data == 'alpha':
            pass
            # struct = self.get_alpha_values(struct, type_struct)
        elif type_data == 'both':
            pass
            # struct = self.get_all_values(struct, type_struct)
        else:
            print('\n\n INVALID TYPE OF DATA \n This task will not performed \n\n')
            t.sleep(4)
        return struct

    def get_numeric_values(self, struct, type_struct):

        if type_struct == 'list':
            info = """
            ***************************************
                FILL YOUR DATA STRUCTURE 
                WITH NUMERIC VALUES
            ****************************************
            """
            print('{} --> {}'.format(info, struct))

            yes_act = False
            option = None
            n = struct.__len__()
            ind = n
            while yes_act is False:
                try:
                    ind = ind + 1
                    print('\n\n Enter a value to position [%d] of your LIST' %(ind))
                    print('\n quit --> Sair')
                    value = input('\n\n Enter a value:  ')
                    if value.isnumeric():
                        struct.append(float(value))

                    elif value.isalpha() and value == 'quit':
                        yes_act = True    # quit
                    else:  # invalid value
                        print('\n You entered --> {} '.format(option))
                        raise Exception
                        #print('\n WARNING: INVALID OPTION!!\n\n')
                except Exception as error:
                    print('\n You entered a CARACTER or a STRING')
                    print('\n WARNING: INVALID VALUE!!!')
                    print('\n PYTHON SAID: {}'.format(error))
        elif type_struct == 'set':
            pass
        else:
            pass

        return struct

    def get_alpha_values(self):
        pass

    def get_all_values(self):
        pass
