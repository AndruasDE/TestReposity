def Code():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    userinput = input("Введите текст для шифрования: ")
    result = ""
    lag = int(input("Введите шаг сдвига: "))
    for i in userinput:
        iftrue = 0
        for a in alphabet:
            if i == a:
                result = result + alphabet[(alphabet.index(a)+lag)%26]
                iftrue = 1 
                continue 
        if iftrue == 0:
            result = result + userinput[userinput.index(i)]
    print(result)

def DeCode():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    userinput = input("Введите текст для расшифрововки: ")
    result = ""
    lag = 0
    #lag = int(input("Введите шаг сдвига: "))
    for char in alphabet:
        for i in userinput:
            iftrue = 0
            for a in alphabet:
                if i == a:
                    result = result + alphabet[(alphabet.index(a)+lag)%26]
                    iftrue = 1 
                    continue 
            if iftrue == 0:
                result = result + userinput[userinput.index(i)]
        print(result)
        result = ""
        lag = lag + 1
#Code()
DeCode()