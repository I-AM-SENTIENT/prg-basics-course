# 5x5 cinema seating
# A = Available, B = Booked
cinema_seats = [
   ['A', 'A', 'B', 'A', 'A'],
   ['A', 'B', 'B', 'A', 'A'],
   ['A', 'A', 'A', 'A', 'B'],
   ['B', 'A', 'A', 'A', 'A'],
   ['A', 'B', 'A', 'A', 'A']
]

def seats_total(seats):
   size = 0
   for s in seats:
    for y in s:
        size+=1
   return size


def seats_available(seats):
    avav = 0
    for x in seats:
        for y in x:
            if y == 'A':
               avav+=1
    return avav

def seats_booked(seats):
    unav = 0
    for x in seats:
        for y in x:
            if y == 'B':
               unav+=1
    return unav

def seat_status(seats, row, place):
   if seats[row-1][place-1] == 'A':
      return 'Avav'
   elif seats[row-1][place-1] == 'B':
      return 'unav'


print('CINEMA INFORMATION TABLE')
print('Total seats:',seats_total(cinema_seats))
print('Seats available:',seats_available(cinema_seats))
print('Seats booked:', seats_booked(cinema_seats))
print('Seat in row 1, place 1:', seat_status(cinema_seats,1,1))
print('Seat in row 5, place 5:', seat_status(cinema_seats,5,5))
print('Seat in row 3, place 5:', seat_status(cinema_seats,3,5))


