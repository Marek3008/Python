def priklad():
    priklad.has_been_called = True

priklad.has_been_called = False
priklad()
if priklad.has_been_called == True:
    print("gg")