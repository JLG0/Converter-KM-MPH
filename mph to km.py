user = True

letter_k = "k"

letter_K = "K"

letter_m = "m"

letter_M = "M"

to_miles = 0.621371192

to_kilometers = 1.609344

print ("SPEED CONVERTER 1.02")


while user:
    letter = (raw_input ("For Miles to Kilometers press letter K \nFor Kilometers to Miles press letter M: "))
    if letter == letter_k:
        print("")
        answer = to_kilometers * int(raw_input("Add a number of Miles: "))
        print("That equals to"), answer, ("kilometers")
        print("")

    elif letter == letter_m:
        print("")
        answer = to_miles * int(raw_input("Add a number of Kilometers: "))
        print("That equals to"), answer, ("miles")
        print("")

    elif letter == letter_K:
        print("")
        answer = to_kilometers * int(raw_input("Add a number of Miles: "))
        print("That equals to"), answer, ("kilometers")
        print("")

    elif letter == letter_M:
        print("")
        answer = to_miles * int(raw_input("Add a number of Kilometers: "))
        print("That equals to"), answer, ("miles")
        print("")
     
    else:
        print("")
        print("Please choose between letter K and letter M")
        print("")

