while True:
    print(100*"\n")

    print("Menu Kalkulator")
    print("1. Pertambahan")
    print("2. Perkurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Keluar")
    pilihan = input("Pilih operator kamu: ")
    if pilihan not in ['1','2','3','4','5']:
        print("Pilihan Error Tolong Masukan Pilihan Yang Valid")
        input("Press Enter to Continue")
        continue
    if pilihan == '5':
        print("Terimakasih Telah Menggunakan Kalkulator ini")
        input("Tekan Enter Untuk Keluar")
        break
    operand1 = float(input("Masukan angka: "))
    operand2 = float(input("Masukan angka kedua: "))
    result = 0
    if pilihan == "1":
        result = operand1 + operand2
    elif pilihan == "2":
        result = operand1 - operand2
    elif pilihan == "3":
        result = operand1 * operand2
    elif pilihan == "4": 
        result =  operand1 / operand2
        
        
    print(f"Hasilnya adalah {result}")
    input("Press Enter to Continue")
         
