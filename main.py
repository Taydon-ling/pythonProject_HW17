x = int(input("Give me a  4-digit number that is even and does not end with a 0: "))

if x >= 1000:
    if x <= 9999:
        if x%2 == 0:
            if not x%10 == 0:
                print("Thank you")
            else:
                print("No, it shouldn't end with 0")
        else:
            print("No, it is not even")
    else:
        print("No, it is too big")
else:
    print("No, it is too small")

quit()