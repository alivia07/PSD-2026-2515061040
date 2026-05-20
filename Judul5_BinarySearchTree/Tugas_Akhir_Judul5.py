class Node: 
    def __init__(self, key, nama_pasien): 
        self.key = key 
        self.nama_pasien = nama_pasien  
        self.left = None 
        self.right = None 
 
 
class UGDSystemBST: 
    def __init__(self): 
        self.root = None 
 
    def insert_node(self, root, key, nama_pasien): 
        if root is None: 
            return Node(key, nama_pasien) 
        if key < root.key: 
            root.left = self.insert_node(root.left, key, nama_pasien) 
        elif key > root.key: 
            root.right = self.insert_node(root.right, key, nama_pasien) 
        return root 
 
    def insert(self, key, nama_pasien): 
        self.root = self.insert_node(self.root, key, nama_pasien) 
 
    def find_min_node(self, root): 
        current = root 
        while current is not None and current.left is not None: 
            current = current.left 
        return current 
 
    def delete_node(self, root, key): 
        if root is None: 
            return None 
        if key < root.key: 
            root.left = self.delete_node(root.left, key) 
        elif key > root.key: 
            root.right = self.delete_node(root.right, key) 
        else: 
            if root.left is None and root.right is None: 
                return None 
            elif root.left is None: 
                return root.right 
            elif root.right is None: 
                return root.left 
            else: 
                successor = self.find_min_node(root.right) 
                root.key = successor.key 
                root.nama_pasien = successor.nama_pasien 
                root.right = self.delete_node(root.right, successor.key) 
        return root 
 
    def delete(self, key): 
        self.root = self.delete_node(self.root, key) 
 
    def level_order(self, root): 
        if root is None: 
            print("(Antrean kosong)") 
            return 
        queue = [] 
        queue.append(root) 
        while len(queue) > 0: 
            current = queue.pop(0) 
            print(f"[{current.nama_pasien} (Skor: {current.key})]", end=" -> ") 
            if current.left is not None: 
                queue.append(current.left) 
            if current.right is not None: 
                 queue.append(current.right) 
        print("Selesai") 
 
    def find_node(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self.find_node(root.left, key)
        return self.find_node(root.right, key)

    def find_successor(self, root, key): 
        target = self.find_node(root, key)
        if target is None:
            return None, False
        if target.right is not None:
            res = self.find_min_node(target.right)
            return res, True
        successor = None
        current = root
        while current is not None:
            if key < current.key:
                successor = current
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                break
        if successor is None:
            return None, False
        return successor, True
 
    def find_predecessor(self, root, key): 
        target = self.find_node(root, key)
        if target is None:
            return None, False  
        if target.left is not None:
            current = target.left
            while current.right is not None:
                current = current.right
            return current, True
        predecessor = None
        current = root
        while current is not None:
            if key > current.key:
                predecessor = current
                current = current.right
            elif key < current.key:
                current = current.left
            else:
                break
        if predecessor is None:
            return None, False
        return predecessor, True

def main(): 
    ugd = UGDSystemBST() 
    pilih = 0 
    while pilih != 5: 
        print("\n=== SISTEM ANTREAN UGD AUTOMATIC ===") 
        print("1. Daftarkan Pasien Baru (Insert)") 
        print("2. Tampilkan Struktur Antrean Kamar (Level-order)") 
        print("3. Panggil Pasien Setingkat Lebih Kritis (Successor & Auto-Delete)") 
        print("4. Panggil Pasien Setingkat Lebih Stabil (Predecessor & Auto-Delete)") 
        print("5. Keluar") 
        try: 
            pilih = int(input("Pilih Menu: ")) 
        except ValueError: 
            print("Input tidak valid!") 
            continue 
        if pilih == 1: 
            try: 
                nama = input("Masukkan nama pasien: ")
                x = int(input("Masukkan skor tingkat kekritisan (1-100): ")) 
                ugd.insert(x, nama) 
                print(f"Pasien {nama} dengan skor {x} berhasil masuk antrean.") 
            except ValueError: 
                print("Input tidak valid!") 
        elif pilih == 2: 
            print("Urutan Monitor UGD (Level-order): ", end="") 
            ugd.level_order(ugd.root) 
        elif pilih == 3: 
            try: 
                x = int(input("Masukkan skor acuan dokter: ")) 
                node_ans, found = ugd.find_successor(ugd.root, x) 
                if found and node_ans is not None: 
                    print(f"\n[DITEMUKAN] {node_ans.nama_pasien} (Skor: {node_ans.key}) langsung dipanggil ke penanganan dokter.") 
                    ugd.delete(node_ans.key)  
                    print(f"[SISTEM] Data {node_ans.nama_pasien} otomatis dihapus dari antrean.")
                else: 
                    print("Tidak ada pasien successor yang cocok (atau skor acuan tidak terdaftar).")
            except ValueError: 
                print("Input tidak valid!") 
        elif pilih == 4: 
            try: 
                x = int(input("Masukkan skor acuan dokter: ")) 
                node_ans, found = ugd.find_predecessor(ugd.root, x) 
                if found and node_ans is not None: 
                    print(f"\n[DITEMUKAN] {node_ans.nama_pasien} (Skor: {node_ans.key}) langsung dipanggil ke penanganan dokter.") 
                    ugd.delete(node_ans.key)  
                    print(f"[SISTEM] Data {node_ans.nama_pasien} otomatis dihapus dari antrean.")
                else: 
                    print("Tidak ada pasien predecessor yang cocok (atau skor acuan tidak terdaftar).") 
            except ValueError: 
                print("Input tidak valid!") 
        elif pilih == 5: 
            print("Sistem UGD selesai.") 
            break
        else: 
            print("Pilihan tidak valid!") 
 
if __name__ == "__main__": 
    main()
