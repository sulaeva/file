def cal():
    while True:          #это бесконечный цикл пока она является истиной (True)
        print("0 '+' ")
        print("1 '-' ")
        print("2 '*' ")
        print("3 '/' ")
        print("4 'stop' ")
        try:
            ch = eval(input("enter num 1:"))
            oper = int(input("enter operators:"))
            ch2 = eval(input("enter num 2:"))

            if oper == 0:
                res = ch + ch2
                print(f"Результат: {res}")
            elif oper == 1:
                res = ch - ch2
                print(f"Результат: {res}")
            elif oper == 2:
                res = ch * ch2
                print(f"Результат: {res}")
            elif oper == 3:
                res = ch / ch2
                print(f"Результат: {res}")
            elif oper == 4:
                print("stop")
                break
            else:
                print('не верная операция')
        except:                # сработает при ошибке
            print("Ошибка введите число")
cal()