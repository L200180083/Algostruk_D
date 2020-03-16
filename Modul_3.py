###1
import numpy as np
class pertama(object):
    def konsisten(self,a):
        k = len(a[0])
        z = 0
        for i in range(len(a)):
            if (len(a[i]) == k):
               z+=1
        if(z == len(a)):
            print("matriks konsisten")
        else:
            print("matrik tidak konsisten")
        for x in a:
            for i in x:
                assert isinstance(i,int),"harus integer"     
            return True
       
    def ukuran(self,a):
        return("Ukuran Matrix berordo "+str(len(a))+" x "+str(len(a[0])))
    def Jml(self,a,b):
        q = np.array(a)
        w= np.array(b)
        Ukuran1 = len(a) + len(a[0])
        Ukuran2 = len(b) + len(b[0])
        if Ukuran1 == Ukuran2:
            return q+w
            
        else:
            print("tidak konsisten")
    def Kali(self,a,b):
        hsl = []
        Ukuran1 = len(a) + len(a[0])
        Ukuran2 = len(b) + len(b[0])
        if Ukuran1 == Ukuran2:
            for i in range(0,len(a)):
                save=[]
                for j in range(0,len(a[0])):
                    jml=0
                    for k in range(len(a)):
                        jml += (a[i][k]*b[k][j])
                    save.append(jml)
                hsl.append(save)
            return hsl

        else:
            print("Matriks Tidak Sesuai")
    def det(self,a):
        if len(a)==len(a[0]):
            a = np.array(a)
            return(np.linalg.det(a))
        else:
            print("harus bujur sangkar")
###2
class kedua(object):
    def buatNol(self,m,n):
        print([[0 for i in range(m)]for g in range(n)])
    def buatnol(self,m):
        print([[0 for i in range (m)]for g in range(m)])
    def buatIdentitas(self,m):
        print([[1 if i == j else 0 for i in range(m) ]for j in range(m)])

###3
class linkedList(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedList():
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail
        
    def listprint(self):
        printval = self.head
        hasil = []
        while printval is not None:
            hasil.append(printval.data)
            printval = printval.next
        print(hasil)

    def cari(self, nilai):
            cek = self.head
            a = 1
            while cek is not None:
                if cek.data == nilai:
                    print("terdapat pada urutan ke-"+str(a))
                    break
                if cek.data != nilai:
                    a += 1
                    cek = cek.next
                    
    def tambahDepan(self, b):
        b.next = self.head
        self.head = b
        
    def tambahAkhir(self, c):
        self.tail.next = c
        self.tail = c
        
    def tambah(self, d, posisi):
        if posisi == 1:
            d.next = self.head
            self.head = d
        if posisi == 7:
            self.tail.next = d
            self.tail = d
        if posisi == 2:
            d.next = self.head.next
            self.head.next = d
        if posisi == 3:
            d.next = self.head.next.next
            self.head.next.next = d
        if posisi == 4:
            d.next = self.head.next.next.next
            self.head.next.next.next = d
        if posisi == 5:
            d.next == self.head.next.next.next.next
            self.head.next.next.next.next = d
        if posisi == 6:
            d.next == self.head.next.next.next.next.next
            self.head.next.next.next.next.next = d
        if posisi > 7 or posisi < 0:
            raise AssertionError("Posisi harus direntang 0 sampai 7")
    def hapus(self, posisi): 
        hapus = self.head 
        if posisi == 0: 
            self.head = temp.next
            hapus = None
        for i in range(posisi-1): 
            hapus = hapus.next
            if hapus is None: 
                break
        next = hapus.next.next
        hapus.next = next

###4
class Node: 
    def __init__(self, data): 
        self.data = data 
        self.prev = None
class DoublyLinkedList: 
    def __init__(self): 
        self.head = None
    def awal(self, new_data):
        print("menambah pada awal", new_data)
        new_node = Node(new_data) 
        new_node.next = self.head 
        if self.head is not None: 
            self.head.prev = new_node 
        self.head = new_node 
    def akhir(self, new_data):
        print("menambah pada akhir", new_data)
        new_node = Node(new_data) 
        new_node.next = None
        if self.head is None: 
            new_node.prev = None
            self.head = new_node 
            return 
        last = self.head 
        while(last.next is not None): 
            last = last.next
        last.next = new_node 
        new_node.prev = last 
        return
    def printList(self, node): 
        print("\nDari Depan :")
        while(node is not None): 
            print(" % d" %(node.data))
            last = node 
            node = node.next
        print("\nDari Belakang :")
        while(last is not None): 
            print(" % d" %(last.data)) 
            last = last.prev

