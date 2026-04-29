def tukar(antrean, i, j): 
    temp = antrean[i] 
    antrean[i] = antrean[j] 
    antrean[j] = temp 

def bubble_sort_tiket(antrean): 
    n = len(antrean)
    for i in range(n - 1): 
        for j in range(n - i - 1): 
            if antrean[j]['nomor'] > antrean[j + 1]['nomor']: 
                tukar(antrean, j, j + 1) 

def main(): 
    try: 
        n = int(input("Masukkan jumlah orang dalam antrean: ")) 
    except ValueError: 
        print("Input jumlah tidak valid!") 
        return

    antrean = [] 
    print("Masukkan data antrean (nama dan nomor tiket):") 
    for i in range(n): 
        nama = input(f"Nama orang ke-{i+1}: ")
        while True: 
            try: 
                nomor = int(input(f"Nomor tiket orang ke-{i+1}: ")) 
                antrean.append({'nama': nama, 'nomor': nomor}) 
                break 
            except ValueError: 
                print("Nomor tiket harus berupa angka!") 

    print(f"\nAntrean sebelum diurutkan: {antrean}") 
    bubble_sort_tiket(antrean) 
    
    print("\nAntrean setelah diurutkan (berdasarkan nomor tiket):") 
    for orang in antrean: 
        print(f"Nama: {orang['nama']}, Nomor Tiket: {orang['nomor']}") 

if __name__ == "__main__": 
    main()