class PrinterSpoolQueue:
    def __init__(self, maxsize=100):
        self.MAXN = maxsize
        self.q = [None] * self.MAXN
        self.frontidx = -1
        self.rearidx = -1

    def is_empty(self):
        return self.frontidx == -1

    def is_full(self):
        return self.rearidx + 1 == self.MAXN or (self.rearidx + 1 == self.frontidx)

    def enqueue(self, x):
        if self.is_full():
            print("Spool printer sudah mencapai batas maksimal")
            return
        if self.is_empty():
            self.frontidx = 0
            self.rearidx = 0
        else:
            self.rearidx = (self.rearidx + 1) % self.MAXN
        self.q[self.rearidx] = x
        print(f"Permintaan cetak '{x}' berhasil ditambahkan ke antrean")

    def dequeue(self):
        if self.is_empty():
            print("Tidak ada dokumen yang siap dicetak")
            return
        print(f"Dokumen '{self.q[self.frontidx]}' berhasil dicetak")
        if self.frontidx == self.rearidx:
            self.frontidx = -1
            self.rearidx = -1
        else:
            self.frontidx = (self.frontidx + 1) % self.MAXN

    def peek(self):
        if self.is_empty():
            print("Tidak ada dokumen yang siap dicetak")
            return
        print(f"Dokumen pertama siap dicetak: '{self.q[self.frontidx]}'")

    def display(self):
        if self.is_empty():
            print("Tidak ada dokumen dalam spool printer")
            return
        print("Isi antrean printer (depan ke belakang): ", end="")
        i = self.frontidx
        while True:
            print(self.q[i], end=" ")
            if i == self.rearidx:
                break
            i = (i + 1) % self.MAXN
        print()

def main():
    printer_queue = PrinterSpoolQueue()
    pilih = 0
    while pilih != 5:
        print("\n=== SISTEM MANAGEMENT PRINTER (PRINTER SPOOLING) ===")
        print("1. Tambah Permintaan Cetak (Enqueue)")
        print("2. Proses Cetak (Dequeue)")
        print("3. Lihat Dokumen Depan (Peek)")
        print("4. Tampilkan Antrean")
        print("5. Keluar")
        try:
            pilih = int(input("Pilih: "))
        except ValueError:
            print("Input tidak valid!")
            continue

        if pilih == 1:
            try:
                dokumen = input("Masukkan nama dokumen: ")
                printer_queue.enqueue(dokumen)
            except:
                print("Input tidak valid!")
        elif pilih == 2:
            printer_queue.dequeue()
        elif pilih == 3:
            printer_queue.peek()
        elif pilih == 4:
            printer_queue.display()
        elif pilih == 5:
            print("Mematikan sistem spooler.")
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()