print("This program will ask for two integers and then print the even and odd integers between them.")

# this loop will keep on asking the user for correct input
while True:
    starting_int = int(input("Starting integer: "))
    ending_int = int(input("Ending integer: " ))
    if starting_int > ending_int:
        print("Invalid case. Try again.")
        continue
    
    print("Even numbers: ")
    for i in range(starting_int, ending_int + 1):
        if i % 2 == 0:
            print(i)
    
    print("Odd numbers: ")
    for i in range(starting_int, ending_int + 1):
        if i % 2 != 0:
            print(i)
            
    break
