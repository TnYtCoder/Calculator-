print("Please Select Operation ")
print("1. Add")
print("2. Sub")
print("3. Multiply")
print("4. Divide")

operation = input()

if operation == "1":
    sum1 = input("Select First Number : ")
    sum2 = input("Select Second Number : ")
    print("Your Answer Is : " + str(int(sum1) + int(sum2)))
elif operation == "2":
    sum1 = input("Select First Number : ")
    sum2 = input("Select Second Number : ")
    print("Your Answer Is : " + str(int(sum1) - int(sum2)))
elif operation == "3":
    sum1 = input("Select First Number : ")
    sum2 = input("Select Second Number : ")
    print("Your Answer Is : " + str(int(sum1) * int(sum2)))
elif operation == "4":
    sum1 = input("Select First Number : ")
    sum2 = input("Select Second Number : ")
    print("Your Answer Is : " + str(int(sum1) / int(sum2)))
    
else : print("Invalid Keyword !! Restart Again")