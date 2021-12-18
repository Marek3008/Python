def kalkulacka():
       while True:
              number1 = int(input("Zadaj prvé číslo: "))
              operacia = input("Zadaj počtovú operáciu: ")
              number2 = int(input("Zadaj druhé číslo: "))
              vysledok = "Výsledok je "

              if operacia == "+":
                     print(vysledok, number1 + number2)
              if operacia == "-":
                     print(vysledok, number1 - number2)
              if operacia == "*":
                     print(vysledok, number1 * number2)
              if operacia == "/":
                     print(vysledok, number1 / number2)
              pokracovanie = input("Chceš pokračovať? ")
              if pokracovanie == "áno":
                     False
              if pokracovanie == "nie":
                     break

kalkulacka()





