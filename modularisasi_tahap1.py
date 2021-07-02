""""
Program menghitung luas segitiga
luas segitiga = alas * tinggi /2

"""

print('menghitung luas segitiga 1')
alas = 10
tinggi = 6
menghitung_luas_segitiga = alas * tinggi /2
print(f' segitiga yang memliki tinggi ={tinggi} dan memiliki alas={alas} adalah ={menghitung_luas_segitiga}')

print('menghitung luas segitiga 2 dengan copy paste')
alas = 11
tinggi = 7
menghitung_luas_segitiga = alas * tinggi /2
print(f' segitiga yang memliki tinggi ={tinggi} dan memiliki alas={alas} adalah ={menghitung_luas_segitiga}')

print('\n membuat fungsi hitung luas segitiga')
def hitung_luas_segitiga(alas,tinggi):
    hitung_alas = alas * tinggi / 2
    return  hitung_alas
print(f'luas segitiga yang memnggunakan fungsi dengan alas = 10 dan tinggi =6 adalah {hitung_luas_segitiga(10,6)}')