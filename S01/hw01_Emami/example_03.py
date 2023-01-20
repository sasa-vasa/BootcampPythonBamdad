num = int(input("Pls enter a two digit number: "))
first_dig = num % 10
second_dig = num // 10
print("1st digit to power of 2nd digit: ", first_dig**second_dig)
print("2nd digit to power of 1st digit: ", second_dig**first_dig)