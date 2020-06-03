op=[1,2,3]


def linha(a='=',b=40):
    print(a*b)


def cab(a):
    linha()
    print(f'\033[1;35m{a}\033[m'.center(47))
    linha()


def cri(nome):
    try:
        a= open(nome,'wt+')
        a.close()
    except:
        print('\033[1;31mERROR! Was not possible create the file!\033[m')
    else:
        print('\033[1;32mFile created with SUCCESS!\033[m')


def ex(nome):
    try:
        a= open(nome,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def cada(ar,sen,id = 0):
    try:
        a= open(ar,'at')
    except:
        print('There was a problem to open the file')
    else:
        a.write(f'{sen}')
        a.close()


def lar(arq):
        while True:
            cab('MENU DO USUARIO')
            print('\033[1;33m1>\033[m \033[1;34mSEE PASSWORDS\033[m')
            print('\033[1;33m2>\033[m \033[1;34mSIGN UP PASSWORD\033[m')
            print('\033[1;33m3>\033[m \033[1;34mEXIT\033[m')
            opi=int(input('\033[1;33mOPTION: \033[m'))
            if opi not in op:
                print('\033[1;31mINVALID PASSWORD\033[m')
            else:
                if opi == 1:
                    linha('-')
                    print('\033[1;32mPASSWORDS:\033[m')
                    try:
                        c = open(arq, 'rt')
                    except:
                        print('ERROR TO READ THE FILE ')
                    else:
                        print(c.read())
                        c.close()

                if opi == 2:
                    cab('NOVA SENHA')
                    ser=str(input('\033[1;33m>\033[m \033[1;34mSERVICE: \033[m'))
                    usa=str(input('\033[1;33m>\033[m \033[1;34mUSERNAME: \033[m'))
                    pah=str(input('\033[1;33m>\033[m \033[1;34mPASSWORD: \033[m'))
                    try:
                        c= open(arq, 'at')
                    except:
                        print('ERROR TO READ THE FILE ')
                    else:
                        c.write(f'\nSERVICE: {ser}, USERNAME: {usa}, PASSWORD: {pah} ')
                        c.close()
                if opi == 3:
                    break