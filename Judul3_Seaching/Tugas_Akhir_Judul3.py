def check_absence_record(data, n, target): 
    i = 0 
    counter = 0 
    while i < n: 
        if data[i] == target: 
            counter += 1 
        i += 1 
    return counter 
 
def main(): 
    data = [6123, 6144, 6157, 6123, 6188, 6123, 6157, 6199, 6101, 6188, 6123, 6199, 6123, 6157, 6188] 
    n = len(data) 
    print(f"Data catatan mahasiswa: {data}") 
    
    while True: 
        try: 
            target = int(input("Masukkan ID mahasiswa yang ingin dicek: ")) 
            break 
        except ValueError: 
            print("Input tidak valid, silakan masukkan angka!") 
            
    counter = check_absence_record(data, n, target) 
    
    if counter > 0: 
        print(f"ID {target} ditemukan sebanyak {counter} kali dalam data.") 
        if counter > 4:
            print(f"-> Status: Selalu hadir")
        elif counter < 4:
            print(f"-> Status: Jarang hadir")
    else: 
        print(f"ID {target} tidak ditemukan dalam catatan.") 
 
if __name__ == "__main__": 
    main()