# Student Database Management System

A simple web-based Student Database Management System built with **Streamlit** and **MySQL**. This application allows users to perform basic CRUD (Create, Read, Update, Delete) operations on student records stored in a MySQL database.

---

## Features

- **Insert Record:** Add new student details including Roll Number, Name, Class, Percentage, Email, and Address.
- **View Records:** Display all student records from the database.
- **Update Record:** Modify existing student information using the Roll Number as the identifier.
- **Delete Record:** Remove student records by Roll Number.

---

## Technologies Used

- Python
- Streamlit (for building the web interface)
- MySQL (database backend)
- mysql-connector-python (MySQL connector library for Python)

---

## Prerequisites

- Python 3.x installed on your system
- MySQL Server installed and running
- Streamlit installed (`pip install streamlit`)
- MySQL Connector installed (`pip install mysql-connector-python`)

---

# Student Database Management System

A simple web-based Student Database Management System built with **Streamlit** and **MySQL**. This application allows users to perform basic CRUD (Create, Read, Update, Delete) operations on student records stored in a MySQL database.

---

## Features

- **Insert Record:** Add new student details including Roll Number, Name, Class, Percentage, Email, and Address.
- **View Records:** Display all student records from the database.
- **Update Record:** Modify existing student information using the Roll Number as the identifier.
- **Delete Record:** Remove student records by Roll Number.

---

## Technologies Used

- Python
- Streamlit (for building the web interface)
- MySQL (database backend)
- mysql-connector-python (MySQL connector library for Python)

---

## Prerequisites

- Python 3.x installed on your system
- MySQL Server installed and running
- Streamlit installed (`pip install streamlit`)
- MySQL Connector installed (`pip install mysql-connector-python`)

---

## Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/MrunalRD/Student-Database-Management-System.git
   cd Student-Database-Management-System

2. **Create MySQL database and table**
   CREATE DATABASE crud1;

   USE crud1;

   CREATE TABLE users (
   
    Roll_no INT PRIMARY KEY,
   
    Name VARCHAR(255),
   
    Class INT,
   
    Percentage FLOAT,
   
    Email VARCHAR(255),
   
    Address VARCHAR(255)
   
   );

 4. **Run the Streamlit app**
     python -m streamlit run directory path filename.py


