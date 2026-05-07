CREATE DATABASE hotel_db;
USE hotel_db;

CREATE TABLE guests (
    guest_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(15),
    email VARCHAR(100)
);

CREATE TABLE rooms (
    room_id INT AUTO_INCREMENT PRIMARY KEY,
    room_type VARCHAR(50),
    price DECIMAL(10,2),
    status VARCHAR(20) DEFAULT 'Available'
);

CREATE TABLE bookings (
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    guest_id INT,
    room_id INT,
    check_in DATE,
    check_out DATE,
    FOREIGN KEY (guest_id) REFERENCES guests(guest_id),
    FOREIGN KEY (room_id) REFERENCES rooms(room_id)
);


INSERT INTO guests (name, phone, email) VALUES
('Rahul Sharma', '9876543210', 'rahul@gmail.com'),
('Priya Mehta', '9123456780', 'priya@gmail.com');

INSERT INTO rooms (room_type, price, status) VALUES
('Single', 1500, 'Available'),
('Double', 2500, 'Available'),
('Deluxe', 4000, 'Available');


