#UAS STRUKTUR DATA 71210776
class Node:
    def __init__(self,data,priority):
        self._data = data
        self._priority = priority
        self._next = None
        self._prev = None

class PQSTugas:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def isEmpty(self) -> bool:
        if self._size == 0:
            return True
        else:
            return False

    def __len__(self):
        return self._size

    def printAll(self):
        print("\n=== Prioritas : Tugas ===")
        if self.isEmpty() == True:
            print("Priority queue is empty")
        else:
            bantu = self._head
            while bantu != None:
                print(bantu._data, bantu._priority, end='')
                bantu = bantu._next
            print()

    def _addHead(self, newNode):
        data = [int(newNode), data]
        self._data.append(data)
        self._data.sort()
        self._size += 1
        
    def _addTail(self, newNode):
        #isi kode anda
        pass
    def _addMiddle(self, newNode):
        #isi kode anda
        pass

    def add(self, data, priority):
        baru = Node(data, priority)
        if self.isEmpty():
             self._head = baru
             self._tail = baru
        elif self._size == 1:
             if self._head._priority > priority:
                 baru._next = self._head
                 self._head._prev = baru
                 self._head = baru
             else:
                 self._head._next = baru
                 baru._prev = self._head
                 self._tail = baru
        else:
             if self._head._priority > priority:
                 baru._next = self._head
                 self._head._prev = baru
                 self._head = baru
             elif self._tail._priority <= priority:
                 self._tail._next = baru
                 baru._prev = self._tail
                 self._tail = baru
                 self._tail._next = None
             else:
                 bantu = self._head
                 while bantu._priority < priority:
                     bantu = bantu._next
                 baru._next = bantu
                 bantu._prev = baru
                 bantu._prev._next = baru
                 baru._prev = bantu._prev
             self._size = self._size + 1
             
    def remove(self):
        if self.isEmpty() == False:
            hapus = self._head
            if self._size == 1:
                self._head = None
            else:
                self._head = self._head._next
                self._head._prev = None
            del hapus
            self._size = self._size -1

    def removePriority(self, priority):
        lst = []
        for i in range(len(self._data)):
            if self._data[i][0] == priority:
                del self._data[i][1]
        for x in range(len(self._data)):
            if len(self._data[x]) == 1:
                pass
            else:
                lst.append(self._data)
        self._data = lst
        self._size -= 1


if __name__ == "__main__":
    tugasKu = PQSTugas()
    tugasKu.add("StrukDat",1)
    tugasKu.add("Menyapu", 5)
    tugasKu.add("Cuci Baju", 4)
    tugasKu.add("Beli Alat Tulis", 3)
    tugasKu.add("Cuci Sepatu", 4)
    tugasKu.printAll()
    tugasKu.remove()
    tugasKu.printAll()
    #tugasKu.removePriority(2)
    #tugasKu.removePriority(4)
    tugasKu.printAll()