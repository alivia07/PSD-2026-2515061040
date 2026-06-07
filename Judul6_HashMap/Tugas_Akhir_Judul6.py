class Node: 
    def __init__(self, key, value): 
        self.key = key 
        self.value = value 
        self.next = None 
 
 
class FilingCabinetHashMap: 
    def __init__(self, size=10): 
        self.SIZE = size
        self.table = [None] * self.SIZE 
 
    def hash_function(self, key): 
        return (key % self.SIZE + self.SIZE) % self.SIZE 
 
    def insert(self, key, value): 
        index = self.hash_function(key) 
        current = self.table[index] 
        while current is not None: 
            if current.key == key: 
                current.value = value 
                return 
            current = current.next 
        new_node = Node(key, value) 
        new_node.next = self.table[index] 
        self.table[index] = new_node 
 
    def search(self, key): 
        index = self.hash_function(key) 
        current = self.table[index] 
        while current is not None: 
            if current.key == key: 
                return current 
            current = current.next 
        return None 
 
    def remove_key(self, key): 
        index = self.hash_function(key) 
        current = self.table[index] 
        prev = None 
        while current is not None: 
            if current.key == key: 
                if prev is None: 
                    self.table[index] = current.next 
                else: 
                    prev.next = current.next 
                return True 
            prev = current 
            current = current.next 
        return False 
 
    def display(self): 
        print("\nIsi Laci Filing Cabinet (Separate Chaining):") 
        for i in range(self.SIZE): 
            print(f"Laci Ke-{i}: ", end="") 
            current = self.table[i] 
            while current is not None: 
                print(f"({current.key} -> {current.value}) | ", end="") 
                current = current.next 
            print("KOSONG/END") 
 
 
def main(): 
    cabinet = FilingCabinetHashMap() 
    
    cabinet.insert(13, "Berkas Katherina") 
    cabinet.insert(7, "Berkas Lina") 
    cabinet.insert(17, "Berkas Candra") 
    cabinet.insert(5, "Berkas Jaka")
    cabinet.insert(14, "Berkas Janice")
    cabinet.insert(25, "Berkas Ningning")
    cabinet.insert(6, "Berkas Edward")
    cabinet.insert(10, "Berkas Oliver")
    cabinet.insert(11, "Berkas Louis")
    cabinet.display() 
 
    x = int(input("\nMasukkan ID unik klien yang dicari: "))
    hasil = cabinet.search(x) 
    if hasil is not None: 
        print(f"\nberkas '{x}' ditemukan dengan Nama = {hasil.value}") 
    else: 
        print(f"\nberkas '{x}' tidak ditemukan") 
    
if __name__ == "__main__": 
    main()