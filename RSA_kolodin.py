def f(a):
    k = 0
    for i in range(2, a // 2 + 1):
        if (a % i == 0):
            k = k + 1
    if (k <= 0):
        return True
    else:
        return False


okno = int(input(" Выберите: \n 1. Зашифровать \n 2. Расшифровать \n use: "))

if (okno == 1):
    E = 1
    p = int(input("введите p: "))
    q = int(input("введите q: "))
    x = int(input("введите ваше сообщение: "))
    if (f(q) == True and f(p) == True):  
        print(f"{q}: число простое")
        print(f"{p}: число простое")
        n = p * q  
        fe = (p - 1) * (q - 1)
        e = 0
        d = 0
        print(f"Функция эйлера:{fe}")
        print(f"модуль p и q:{n}")
        for i in range(2, fe):
            if f(i) == True and fe % i != 0:
                e = i
                break
        print(f"открытая экспонента: {e}")
        # e,n-public key
        print(f"Открытый ключ: ({e}, {n})")
        if (x >= n):
            print("сообщение больше n,попробуйте заново")
        else:
            E = (pow(x, e)) % n
            print(f" Зашифрованное сообщение:{E}")
        for i in range(n):
            if ((e * i) % fe == 1) and i != e:
                d = i
                break

        print(f"закрытый ключ({d},{n})")
    elif (f(q) == f(p)):
        print("числа равны")
    else:
        print("числа не являются простыми")

elif (okno == 2):
    e = int(input("введите зашифровонное сообщение: "))
    d = int(input("введите число d: "))
    n = int(input("введите число n: "))
    kl = pow(e, d) % n
    print("Расшифрованное сообщение: ", kl)