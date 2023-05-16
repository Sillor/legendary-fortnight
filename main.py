import random, json

with open('config.json', encoding = "utf-8", mode = "r") as f:
    config = json.load(f)
nextWordChance = config["nextWordChance"] - 1;
randomWordChance = config["randomWordChance"] - 1;
minSymbols = config["minSymbols"];
maxSymbols = config["maxSymbols"];
enterAfterSymbolsChance = config["enterAfterSymbolsChance"] - 1;
randomSymbolChance = config["randomSymbolChance"] - 1;

def inputFile(name):
    f = open(name, encoding = "utf-8", mode = "r")
    lines = f.read()
    lines = lines.split()
    f.close()
    return lines

def randCapitalize(str):
    outer = True
    inner = True
    while outer:
        i = random.randint(0, len(str) - 1)
        str[i] = str[i].upper()
        while inner:
            j = random.randint(0,nextWordChance)
            if j != 0:
                if (i + j) < len(str):
                    str[i + 1] = str[i + 1].upper()
                    i += 1
            else:
                inner = False
        i = random.randint(0,randomWordChance)
        if i == 0:
            outer = False

def combineList(str):
    newStr = ""
    for i in range(len(str)):
        newStr += str[i]
        if i!= len(str) - 1:
            newStr += " "
    return newStr

def symbolizer(str):
    pos = random.randint(0, len(str) - 1)
    count = 0

    for i in range(len(str)):
        if str[i] == " ":
            count += 1
    spaces = random.randint(1, count)
    count = 0
    for i in range(len(str)):
        if str[i] == " ":
            count += 1
        if count == spaces:
            pos = i
            break
                
    symbols = ["=", "!", ".", "?"]
    str = str[:pos] + (symbols[random.randint(0, len(symbols) - 1)] * random.randint(minSymbols,maxSymbols)) + ('\n' if (random.randint(0,enterAfterSymbolsChance) != 0) else '') + str[pos:]
    return str

def addSymbols(str):
    flag = True
    while flag:
        str = symbolizer(str)
        i = random.randint(0,randomSymbolChance)
        if i == 0:
            flag = False
    return str

# def userChoice():
#     print("Из файла или вручную? (Введите 1 или 2)")
#     choice = input()
#     if choice == "1":
#         lines = inputFile("input.txt")
#     elif choice == "2":
#         lines = input("Введите текст (2 или более слов): ").split()
#     else:
#         print("Неправильный ввод")
#         return userChoice()
#     return lines

def main():
    print ("Для выхода напишите '0 0'\n")
    while True:
        valid = False
        while not valid:
            lines = input("Введите текст (2 или более слов): ").split()
            if len(lines) < 2:
                print("Неправильный ввод")
            else:
                valid = True
        if lines[0] == "0" and lines[1] == "0":
            break
        randCapitalize(lines)
        lines = combineList(lines)
        lines = addSymbols(lines)
        print('\n' + lines)


if __name__ == "__main__":
    main()
