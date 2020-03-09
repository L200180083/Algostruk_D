#1
class pesan(object):
    def __init__(self,a):
        self.a = a
    def apakahterkandung(self, b):
        return b in self.a
    def hitungkonsonan(self):
        itung = 0
        vokal = ["a","i","u","e","o","A","I","U","E","O"]
        for i in self.a:
            if i not in vokal:
                itung+=1
        return itung
    def hitungvokal(self):
        itung = 0
        vokal = ["a","i","u","e","o","A","I","U","E","O"]
        for i in self.a:
            if i in vokal:
                itung+=1
        return itung

#2
class manusia(object):
    keadaan = "lapar"
    def __init__(self,nama):
        self.nama = nama
    def ucapkansalam(self):
        print("salam, namaku", self.nama)
    def makan(self,s):
        print("saya baru saja makan",s)
        self.keadaan = "kenyang"
    def olahraga(self,o):
        print("saya baru saja latihan",o)
        self.keadaan = "lapar"
    def mengalikandengandua(self,n):
        return n*2
class mahasiswa(manusia):
    def __init__(self,nama,nim,kota,us):
        self.nama = nama
        self.nim = nim
        self.kota = kota
        self.uangsaku = us
    def __str__(self):
        s = self.nama + ',Nim'+str(self.nim)+',kota'+self.kota+',uang saku'+self.uangsaku+'/bulan'
        return s
    def ambilnama(self):
        return self.nama
    def ambilnim(self):
        return self.nim
    def ambilkotatinggal(self):
        return self.kota
    def ambiluangsaku(self):
        return self.uangsaku
    def makan(self,s):
        print ("saya baru saja makan",s,"sambil belajar")
        self.keadaan = "kenyang"
    def perbaruikotatinggal(self,b):
        self.kota=b
    def tambahuangsaku(self,c):
        self.uangsaku+=c

#3
class manusia(object):
    keadaan = "lapar"
    def __init__(self,nama):
        self.nama = nama
    def ucapkansalam(self):
        print("salam, namaku", self.nama)
    def makan(self,s):
        print("saya baru saja makan",s)
        self.keadaan = "kenyang"
    def olahraga(self,o):
        print("saya baru saja latihan",o)
        self.keadaan = "lapar"
    def mengalikandengandua(self,n):
        return n*2
class mahasiswa(manusia):
    def __init__(self,nama,nim,kota,us):
        self.nama = nama
        self.nim = nim
        self.kota = kota
        self.uangsaku = us
    def __str__(self):
        s = self.nama + ',Nim'+str(self.nim)+',kota'+self.kota+',uang saku'+self.uangsaku+'/bulan'
        return s
    def ambilnama(self):
        return self.nama
    def ambilnim(self):
        return self.nim
    def ambilkotatinggal(self):
        return self.kota
    def ambiluangsaku(self):
        return self.uangsaku
    def makan(self,s):
        print ("saya baru saja makan",s,"sambil belajar")
        self.keadaan = "kenyang"
    def perbaruikotatinggal(self,b):
        self.kota=b
    def tambahuangsaku(self,c):
        self.uangsaku+=c
a = input("nama :")
b= input("nim :")
c = input("kota :")
d = input("uang saku per bulan :")
x = mahasiswa(a,b,c,d)
print("data mahasiswa :",x)

#no 4&5
class manusia(object):
    keadaan = "lapar"
    def __init__(self,nama):
        self.nama = nama
    def ucapkansalam(self):
        print("salam, namaku", self.nama)
    def makan(self,s):
        print("saya baru saja makan",s)
        self.keadaan = "kenyang"
    def olahraga(self,o):
        print("saya baru saja latihan",o)
        self.keadaan = "lapar"
    def mengalikandengandua(self,n):
        return n*2
class mahasiswa(manusia):
    def __init__(self,nama,nim,kota,us,lk=[]):
        self.nama = nama
        self.nim = nim
        self.kota = kota
        self.uangsaku = us
        self.lk = lk
    def __str__(self):
        s = self.nama + ',Nim'+str(self.nim)+',kota'+self.kota+',uang saku'+self.uangsaku+'/bulan'
        return s
    def ambilnama(self):
        return self.nama
    def ambilnim(self):
        return self.nim
    def ambilkotatinggal(self):
        return self.kota
    def ambiluangsaku(self):
        return self.uangsaku
    def makan(self,s):
        print ("saya baru saja makan",s,"sambil belajar")
        self.keadaan = "kenyang"
    def perbaruikotatinggal(self,b):
        self.kota=b
    def tambahuangsaku(self,c):
        self.uangsaku+=c
#4
    def listkuliah(self):
        return self.lk
    def ambilkuliah(self,b):
        self.lk.append(b)
#5        
    def hapusmatakuliah(self,d):
        for x in self.lk:
            if d in self.lk:
                self.lk.remove(d)
            else:
                print("maaf anda tidak dapat menghapus matkul tersebut karena matkul tersebut tidak ada")

#6
from datetime import date
class manusia(object):
    keadaan = "lapar"
    def __init__(self,nama):
        self.nama = nama
    def ucapkansalam(self):
        print("salam, namaku", self.nama)
    def makan(self,s):
        print("saya baru saja makan",s)
        self.keadaan = "kenyang"
    def olahraga(self,o):
        print("saya baru saja latihan",o)
        self.keadaan = "lapar"
    def mengalikandengandua(self,n):
        return n*2

class SiswaSMA(manusia):
    def __init__(self, nama, nis, umur, us):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia"""
        self.nama = nama
        self.nis = nis
        self.umur = umur
        self.us = us
        
    def __str__(self):
        s = self.nama +', NIS '+str(self.nis)\
            +'. Berumur '+ str(self.umur) \
            +'. Uang saku Rp. '+ str(self.us)\
            +' tiap harinya.'
        return s
    def ambilnama(self):
        return self.nama
    def ambilnim(self):
        return self.nis
    def ambilumur(self):
        return self.umur
    def ambiluangsaku(self):
        return self.us

    def tahunlahir(self):
        thnskr = date.today().year
        tl = thnskr - self.umur
        return tl
#7
class MhsTIF(mahasiswa):
    def katakanPy(self):
        print("python is cool.")
