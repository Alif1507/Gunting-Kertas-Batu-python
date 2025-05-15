import random

opsi = ("gunting", "kertas", "batu")
percobaan = 0
skorBot = 0
print("========================================")
print("           Gunting Kertas Batu          ")
while True:

  print("ketik q untuk keluar")
  pilihan = input("ayo main Gunting kertas batu: ").lower()
  pilihanBot = random.choice(opsi)

  if pilihan == opsi[0] or pilihan == opsi[1] or pilihan == pilihan == opsi[2]:

    
    if pilihan == pilihanBot:
      print("Benar!!")
      print(f"{pilihan}, Bot {pilihanBot}")
      percobaan += 1
    else:
      print("salah!")
      print(f"{pilihan}, Bot {pilihanBot}")
      skorBot += 1

  elif pilihan == "q":
    break

  else:
    print("Silakan Ketik 'Gunting', 'Kertas', 'Batu' ")

print("+======================+")
print(f"skor: {percobaan}")
print(f"skor Bot: {skorBot}")
print("+======================+")

  
