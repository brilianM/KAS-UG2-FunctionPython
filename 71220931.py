def tabung(r, t):
    pi = 3.14
    volume = pi * r ** 2 * t
    return volume

def kubus(sisi):
    volume = sisi ** 3
    return volume

def balok(p, l, t):
    volume = p * l * t
    return volume

print("=" * 18, "KALKULATOR PINTAR", "=" * 18)
print("Pilihlah bangun yang ingin anda hitung (inputan angka saja) :")
print("1. tabung")
print("2. kubus")
print("3. balok")
pilihan = int(input(""))

if pilihan == 1:
    r = int(input("masukkan diameter(cm): "))
    t = int(input("masukkan tinggi(cm): "))
    r /= 2
    print("volume tabung adalah", tabung(r, t))
elif pilihan == 2:
    sisi = int(input("masukkan sisi (cm): "))
    print("volume kubus adalah", kubus(sisi))
elif pilihan == 3:
    p = int(input("masukkan panjang (cm): "))
    l = int(input("masukkan lebar (cm): "))
    t = int(input("masukkan tinggi (cm): "))
    print("volume kubus adalah", balok(p, l, t))
else:
    print("Inputan yang anda masukkan salah !!")






    