print("Cezazova sifra: ")

ZNAKY = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while True:
    print("Chces zasifrovat spravu alebo ju odsifrovat?: zadaj s - pre sifrovanie a o - pre odsifrovanie")
    odpoved = input().lower()
    if odpoved.startswith("s"):
        mod = "sifrovanie"
        break
    elif odpoved.startswith("o"):
        mod = "odsifrovanie"
        break
    print("Prosim zadaj len pismena s alebo o")

while True:
    maxKluc = len(ZNAKY) - 1
    print("Zadaj velkost kluca pre sifrovanie od (0 po {}): ".format(maxKluc))
    odpoved = input("-> ")
    
    if not odpoved.isdecimal():
        continue
    
    if 0 <= int(odpoved) < len(ZNAKY):
        kluc = int(odpoved)
        break

print("Zadaj spravu pre {}: ".format(mod))
sprava = input("-> ")
sprava = sprava.upper()

preklad = ""

for symbol in sprava:
    if symbol in ZNAKY:
        num = ZNAKY.find(symbol)
        if mod == "sifrovanie":
            num = (num + kluc) % len(ZNAKY)
        elif mod == "odsifrovanie":
            num = (num - kluc) % len(ZNAKY)
        preklad += ZNAKY[num]
    else:
        preklad += symbol

print(preklad)
