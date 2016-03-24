# Largest palindrome number from the product of two 3-digit numbers
# result 906609

number = ""
palindromenumbers = []

for x in range (100,999):
    for y in range (100,999):
        number = str(x*y)
        if len(number)==6: #With 5 digit palindrome numbers, result is 99999 ?!
             if number == number[::-1]:
                 palindromenumbers.append(number)


print(max(palindromenumbers))