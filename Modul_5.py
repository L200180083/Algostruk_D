#NO 1
class MhsTIF(object):
    def __init__(self,nama,nim,tinggal,us):
        self.nama = nama
        self.nim = nim
        self.tinggal = tinggal
        self.us = us

c0 = MhsTIF('rifqi', "L200180083", 'Kudus', 120000)
c1 = MhsTIF('aditya', "L200180125", 'Jogja', 146000)
c2 = MhsTIF('mahendra', "L200180304", 'Bali', 12500)
c3 = MhsTIF('djum', "L200180011", 'Makasar', 340000)
c4 = MhsTIF('bobi', "L200180023", 'Lampung', 450000)
c5 = MhsTIF('amron', "L200180055", 'Aceh', 460000)
c6 = MhsTIF('anto', "L200180081", 'Solo', 770000)
c7 = MhsTIF('cogan', "L200180003", 'Pati', 530000)
c8 = MhsTIF('dimas', "L200180213", 'Kudus', 235000)
c9 = MhsTIF('zein', "L200180040", 'Semarang', 450000)

Daftar=[c0,c1,c2,c3,c4,c5,c6,c7,c8,c9]
        
def swap(a,b,c):
    tmp=a[b]
    a[b]=a[c]
    a[c]=tmp
    
def ceknim(Daftar):
    for i in Daftar:
        print(i.nama,i.nim,i.tinggal)

def urutnim(a):
    n = len(a)
    for x in range(n-1):
        for y in range(n-x-1):
            if a[y].nim > a[y+1].nim:
                swap(a,y,y+1)



#NO 2
a = [1, 8, 22, 54, 89, 111, 102, 60]
b = [10, 2, 6, 12, 9, 23, 14, 33]

def urut(a,b):
    c = a +b
    for i in range(1,len(c)):
        nilai = c[i]
        pos = i
        while pos >0 and nilai<c[pos - 1]:
            c[pos]=c[pos-1]
            pos -=1
        c[pos]=nilai
    print(c)


#NO 3
def swap(A,p,q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp

def cariPosisiYangTerkecil(A, dariSini, sampaiSini):
    posisiTerkecil = dariSini
    for i in range(dariSini+1, sampaiSini):
        if A[1] < A[posisiTerkecil]:
            posisiTerkecil = 1
    return posisiTerkecil

def bubbleSort(A):
    n = len(A)
    for i in range(n-1):
        for j in range(n-i-1):
            if A[j] > A[j+1]:
                swap(A,j,j+1)

def selectionSort(A):
    n = len(A)
    for i in range(n-1):
        indexKecil = cariPosisiYangTerkecil(A, i, n)
        if indexKecil != i:
            swap(A, i, indexKecil)

def insertionSort(A):
    n = len(A)
    for i in range(1,n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos-1]:
            A[pos] = A[pos-1]
            pos = pos-1
        A[pos] = nilai
        
from time import time as detak
from random import shuffle as kocok

k = [i for i in range(1,6001)]
kocok(k)
u_bub = k[:]
u_sel = k[:]
u_ins = k[:]

aw = detak();bubbleSort(u_bub);ak=detak();print("Bubble    : %g detik"%(ak-aw));
aw = detak();selectionSort(u_sel);ak=detak();print("Selection : %g detik"%(ak-aw));
aw = detak();insertionSort(u_ins);ak=detak();print("Insertion : %g detik"%(ak-aw));
