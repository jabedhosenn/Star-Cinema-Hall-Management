class Star_Cinema:
    _hall_list = []

    @classmethod
    def entry_hall(cls, hall):
        cls._hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.__seats = {}
        self.__show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        Star_Cinema.entry_hall(self)

    def entry_show(self, id, movie_name, time):
        self.__show_list.append((id, movie_name, time))
        self.__seats[id] = [['F' for _ in range(self._cols)] for _ in range(self._rows)]
        print(f"Show with ID {id} added successfully.")

    def book_seats(self, show_id, seat_list):
        if show_id not in self.__seats:
            print("Invalid show ID!")
            return
        for seat in seat_list:
            row, col = seat
            if row < 0 or row >= self._rows or col < 0 or col >= self._cols:
                print("Invalid seat number!")
                return
            if self.__seats[show_id][row][col] == 'F':
                self.__seats[show_id][row][col] = 'B'
                print(f"Seat ({row}, {col}) booked successfully.")
            else:
                print(f"Seat ({row}, {col}) is already booked.")

    def view_show_list(self):
        if not self.__show_list:
            print("No shows available.")
        else:
            print("Current Shows:")
            for id, movie_name, time in self.__show_list:
                print(f"ID: {id}, Movie: {movie_name}, Time: {time}")

    def view_available_seats(self, show_id):
        if show_id not in self.__seats:
            print("Invalid show ID!")
            return
        seats = self.__seats[show_id]
        print("Available Seats:")
        for i, row in enumerate(seats):
            print(f"Row {i}: {' '.join(row)}")


hall = Hall(5, 5, 2)

while True:
    print("\n-----Welcome to Star Cinema-----\n")
    print("1. Add Show")
    print("2. View Shows")
    print("3. Book Seats")
    print("4. View Available Seats")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == '1':
        show_id = int(input("Enter show ID: "))
        movie_name = input("Enter movie name: ")
        show_time = input("Enter show time: ")
        hall.entry_show(show_id, movie_name, show_time)

    elif choice == '2':
        hall.view_show_list()

    elif choice == '3':
        show_id = int(input("Enter show ID: "))
        num_seats_to_book = int(input("Number of seats to book: "))
        seats_to_book = []
        for _ in range(num_seats_to_book):
            row = int(input("Enter row: "))
            col = int(input("Enter column: "))
            seats_to_book.append((row, col))
        hall.book_seats(show_id, seats_to_book)

    elif choice == '4':
        show_id = int(input("Enter show ID: "))
        hall.view_available_seats(show_id)

    elif choice == '5':
        print("Exiting...")
        print("Thanks for visiting us.")
        print("Come again.")
        break

    else:
        print("Invalid choice. Please choose again.")
