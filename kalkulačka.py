def kalkulacka():
       while True:
              number1 = int(input("Zadaj prvé číslo: "))
              operacia = input("Zadaj počtovú operáciu: ")
              number2 = int(input("Zadaj druhé číslo: "))
              vysledok = "Výsledok je "

              if operacia == "+":
                     print(vysledok, number1 + number2)
              if operacia == "-":
                     ktore_cislo1 = input("Od ktorého čísla chceš odčítať? ")
                     if ktore_cislo1 == "od prvého":
                            print(vysledok, number1 - number2)
                     if ktore_cislo1 == "od druhého":
                            print(vysledok, number2 - number1)
              if operacia == "*":
                     print(vysledok, number1 * number2)
              if operacia == "/":
                     ktore_cislo2 = input("Ktorým číslom chceš deliť? ")
                     if ktore_cislo2 == "prvým":
                            print(vysledok, number2 / number1)
                     if ktore_cislo2 == "druhým":
                            print(vysledok, number1 / number2)
              pokracovanie = input("Chceš pokračovať? ")
              if "áno" in pokracovanie:
                     False
              if "nie" in pokracovanie:
                     break

kalkulacka()





