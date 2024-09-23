import random


print("Permainan Gunting, Batu, dan Kertas")

game = ("Gunting", "Batu", "Kertas")

while True:
    player = input("Pilih Gunting, Batu, Kertas=  ").capitalize()
    
    if player not in game:
        print("Pilihan Eror, Coba lagi")
        continue
    
    komputer = random.choice(game)
    print(f"Komputer Memilih:  {komputer}")
    
    if player == komputer:
        print("Seri!!")
    elif (player == "Gunting" and komputer == "Kertas") or \
         (player == "Batu" and komputer == "Gunting") or \
         (player == "Kertas" and komputer == "Batu"):
             print("Congratulation You Beat AI!")
    else:
        print("AI beat Human!")
        
    main_lagi = input("ingin bermain lagi? (y/n): ").lower()
    if main_lagi != 'y':
        print("Terimakasih Telah Bermain!")
        break
        

<!---
Caramaderies/Caramaderies is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->
