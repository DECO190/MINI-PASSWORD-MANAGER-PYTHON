import eng_func
from time import sleep
op=[1,2,3]
blok=0
while True:
    eng_func.cab('PASSWORD MANAGER')
    print('\033[1;33m1>\033[m \033[1;34mLOGIN\033[m')
    print('\033[1;33m2>\033[m \033[1;34mSIGN UP USER\033[m')
    print('\033[1;33m3>\033[m \033[1;34mEXIT\033[m')
    eng_func.linha()
    opi = int(input('\033[1;33mOPTION: \033[m'))
    if opi not in op:
        print('\033[1;31mINVALID OPTION!\033[m')
    if opi == 2:
        while True:
            eng_func.cab('SIGN UP')
            cu= str(input('\033[1;33m>\033[m \033[1;34mDIGIT YOUR USERNAME: \033[m'))
            cs= str(input('\033[1;33m>\033[m \033[1;34mDIGIT THE PASSWORD: \033[m'))
            if not eng_func.ex(f'{cu}.txt'):
                eng_func.cri(f'{cu}.txt')
                eng_func.cada(f'{cu}.txt',cs,'at')
                print('\033[1;32mUSER CREATED WITH SUCCESS!\033[m')
                break
            if eng_func.ex(f'{cu}.txt'):
                print("\033[1;31mINVALID USER NAME!")
                print('DIGIT ANOTHER ONE:\033[m')
    if opi == 3:
        print('\033[1;31mFINISHED SYSTEM!\033[m')
        break
    if opi == 1:
        while True:
            eng_func.cab('LOGIN')
            id= str(input('\033[1;33m> \033[m\033[1;34mDIGIT YOUR USER NAME: \033[m'))
            pas= str(input('\033[1;33m> \033[m\033[1;34mDIGIT THE PASSWORD: \033[m'))
            try:
                a = open(f'{id}.txt', 'rt')
            except:
                eng_func.linha()
                blok+=1
                print('\033[1;31mERROR: USER NOT FOUND!\033[m')
            else:
                rnh = a.readline().strip()
                if f'{rnh}' == f'{pas}':
                    eng_func.lar(f'{id}.txt')
                    break
                else:
                    blok+=1
                    print('\033[1;31mERROR: INCORRECT PASSWORD\033[m')
            if blok == 3:
                print('\033[1;31mACTIONS BLOCKED FOR 1min!\033[m')
                blok=0
                sleep(60)