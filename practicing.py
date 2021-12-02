from random import*


tym1 = []
tym2 = []
tym3 = []



while True:
 meno = input("Meno:")
 tym = randint(0, 3)
 if tym == 0:
        tym1.append(meno)
 elif tym == 1:
    tym2.append(meno)
 elif tym == 2:
        tym3.append(meno)
 print("V týme 1 sú:", tym1)
 print("V týme 2 sú:", tym2)
 print("V týme 3 sú:", tym3)
 if meno == "koniec":
     break




