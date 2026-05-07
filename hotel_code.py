import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ENTER_YOUR_PASSWORD_HERE",#ITS GENERALLY 12345678 or admin123
    database="hotel_db"
)

cursor = conn.cursor()


#ADDING GUEST
def add_guest(name, phone, email):
    sql = "INSERT INTO guests (name, phone, email) VALUES (%s, %s, %s)"
    values = (name, phone, email)
    cursor.execute(sql, values)
    conn.commit()
    print("Guest added successfully")


#Adding ROOM
def add_room(room_type, price):
    sql = "INSERT INTO rooms (room_type, price) VALUES (%s, %s)"
    values = (room_type, price)
    cursor.execute(sql, values)
    conn.commit()
    print("Room added successfully")



#VIEW Available Rooms
def show_rooms():
    cursor.execute("SELECT * FROM rooms WHERE status='Available'")
    rooms = cursor.fetchall()

    for room in rooms:
        print(room)


#BOOK ROOM
def book_room(guest_id, room_id, check_in, check_out):
    
    # check if room available
    cursor.execute("SELECT status FROM rooms WHERE room_id=%s", (room_id,))
    status = cursor.fetchone()

    if status[0] != "Available":
        print("Room not available")
        return

    # insert booking
    sql = "INSERT INTO bookings (guest_id, room_id, check_in, check_out) VALUES (%s, %s, %s, %s)"
    values = (guest_id, room_id, check_in, check_out)
    cursor.execute(sql, values)

    # update room status
    cursor.execute("UPDATE rooms SET status='Booked' WHERE room_id=%s", (room_id,))

    conn.commit()
    print("Room booked successfully")



#CANCEL BOOKING
def cancel_booking(booking_id):
    
    cursor.execute("SELECT room_id FROM bookings WHERE booking_id=%s", (booking_id,))
    room = cursor.fetchone()

    if room:
        room_id = room[0]

        cursor.execute("DELETE FROM bookings WHERE booking_id=%s", (booking_id,))
        cursor.execute("UPDATE rooms SET status='Available' WHERE room_id=%s", (room_id,))

        conn.commit()
        print("Booking cancelled")


#VIEW BOOKINGs
def show_bookings():
    cursor.execute("""
        SELECT b.booking_id, g.name, r.room_type, b.check_in, b.check_out
        FROM bookings b
        JOIN guests g ON b.guest_id = g.guest_id
        JOIN rooms r ON b.room_id = r.room_id
    """)

    for row in cursor.fetchall():
        print(row)


#Menu SYSTEM(MAIN PROGRAM)

while True:
    print("\n--- HOTEL MANAGEMENT SYSTEM ---")
    print("1. Add Guest")
    print("2. Add Room")
    print("3. Show Available Rooms")
    print("4. Book Room")
    print("5. Cancel Booking")
    print("6. Show Bookings")
    print("7. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        add_guest(name, phone, email)

    elif choice == 2:
        room_type = input("Room Type: ")
        price = float(input("Price: "))
        add_room(room_type, price)

    elif choice == 3:
        show_rooms()

    elif choice == 4:
        guest_id = int(input("Guest ID: "))
        room_id = int(input("Room ID: "))
        check_in = input("Check-in (YYYY-MM-DD): ")
        check_out = input("Check-out (YYYY-MM-DD): ")
        book_room(guest_id, room_id, check_in, check_out)

    elif choice == 5:
        booking_id = int(input("Booking ID: "))
        cancel_booking(booking_id)

    elif choice == 6:
        show_bookings()

    elif choice == 7:
        break
