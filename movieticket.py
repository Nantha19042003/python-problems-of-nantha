Movie Ticket Booking

Question:
A theater has 50 seats. Write a program to book tickets until all seats are filled.

Answer:

seats = 50

while seats > 0:
    ticket = int(input("Number of Tickets: "))

    if ticket <= seats:
        seats -= ticket
        print("Booking Successful")
        print("Remaining Seats:", seats)
    else:
        print("Only", seats, "Seats Available")

    if seats == 0:
        print("House Full")
