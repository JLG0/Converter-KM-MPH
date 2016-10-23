user = True

letter_k = "k"

letter_K = "K"

letter_m = "m"

letter_M = "M"

to_miles = 0.621371192

to_kilometers = 1.609344

print ("SPEED CONVERTER 1.01")


while user:
    letter = (raw_input ("For miles to kilometers press letter K \nFor kilometers to miles press letter M: "))
    if letter == letter_k:
        print
        print to_kilometers * int(raw_input("Add a number of kilometers: "))
        print 

    elif letter == letter_m:
        print
        print to_miles * int(raw_input("Add a number of miles: "))
        print 

    elif letter == letter_K:
        print
        print to_kilometers * int(raw_input("Add a number of kilometers: "))
        print

    elif letter == letter_M:
        print
        print to_miles * int(raw_input("Add a number of miles: "))
        print
     
    else:
        print
        print("Please choose between letter K and letter M")
        print

