# Largest palindrome number from the product of two 3-digit numbers
# result 906609

zahl = ""
palindromzahlen = []

for x in range (100,999):
    for y in range (100,999):
        zahl = str(x*y)
        if len(zahl)==6: #With 5 digit palindrome numbers, result is 99999 ?!
             if zahl == zahl[::-1]:
                 palindromzahlen.append(zahl)


print(max(palindromzahlen))