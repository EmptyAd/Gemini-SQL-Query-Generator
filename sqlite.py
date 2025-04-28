import sqlite3

# TO connect to SQLite database
connection = sqlite3.connect("store_office_v2.db")

# Cursor object to insert records and create tables
cursor = connection.cursor()

# Departments table
table_departments = """
CREATE TABLE IF NOT EXISTS Departments(
    DepartmentID INTEGER PRIMARY KEY AUTOINCREMENT,
    DepartmentName TEXT NOT NULL
);
"""
cursor.execute(table_departments)

# Employees table
table_employees = """
CREATE TABLE IF NOT EXISTS Employees(
    EmployeeID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Position TEXT NOT NULL,
    DepartmentID INTEGER,
    DateHired TEXT NOT NULL,
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
);
"""
cursor.execute(table_employees)

# Projects table
table_projects = """
CREATE TABLE IF NOT EXISTS Projects(
    ProjectID INTEGER PRIMARY KEY AUTOINCREMENT,
    ProjectName TEXT NOT NULL,
    DepartmentID INTEGER,
    StartDate TEXT NOT NULL,
    EndDate TEXT,
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
);
"""
cursor.execute(table_projects)

# Salaries table
table_salaries = """
CREATE TABLE IF NOT EXISTS Salaries(
    SalaryID INTEGER PRIMARY KEY AUTOINCREMENT,
    EmployeeID INTEGER,
    Amount REAL NOT NULL,
    PayDate TEXT NOT NULL,
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID)
);
"""
cursor.execute(table_salaries)

# Attendance table
table_attendance = """
CREATE TABLE IF NOT EXISTS Attendance(
    AttendanceID INTEGER PRIMARY KEY AUTOINCREMENT,
    EmployeeID INTEGER,
    Date TEXT NOT NULL,
    Status TEXT CHECK(Status IN ('Present', 'Absent', 'On Leave')) NOT NULL,
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID)
);
"""
cursor.execute(table_attendance)

# Sales table (Modified)
table_sales = """
CREATE TABLE IF NOT EXISTS Sales(
    SaleID INTEGER PRIMARY KEY AUTOINCREMENT,
    EmployeeID INTEGER,
    SaleAmount REAL NOT NULL,
    SaleDate TEXT NOT NULL,
    ProductID INTEGER NOT NULL,
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID)
);
"""
cursor.execute(table_sales)

# Insert into Departments
cursor.execute('''INSERT INTO Departments (DepartmentName) VALUES ('Sales')''')
cursor.execute('''INSERT INTO Departments (DepartmentName) VALUES ('Marketing')''')
cursor.execute('''INSERT INTO Departments (DepartmentName) VALUES ('HR')''')
cursor.execute('''INSERT INTO Departments (DepartmentName) VALUES ('Finance')''')
cursor.execute('''INSERT INTO Departments (DepartmentName) VALUES ('IT')''')

# Insert into Employees (15 employees)
cursor.execute('''INSERT INTO Employees (Name, Position, DepartmentID, DateHired) VALUES ('John Doe', 'Sales Manager', 1, '2022-05-01')''')
cursor.execute('''INSERT INTO Employees (Name, Position, DepartmentID, DateHired) VALUES ('Jane Smith', 'Marketing Lead', 2, '2023-06-15')''')
cursor.execute('''INSERT INTO Employees (Name, Position, DepartmentID, DateHired) VALUES ('Mark Johnson', 'HR Specialist', 3, '2021-03-12')''')
cursor.execute('''INSERT INTO Employees (Name, Position, DepartmentID, DateHired) VALUES ('Alice Brown', 'Finance Manager', 4, '2019-09-22')''')
cursor.execute('''INSERT INTO Employees (Name, Position, DepartmentID, DateHired) VALUES ('Bob White', 'IT Specialist', 5, '2020-11-30')''')
cursor.execute('''INSERT INTO Employees (Name, Position, DepartmentID, DateHired) VALUES ('Carol Green', 'Sales Associate', 1, '2023-01-14')''')
cursor.execute('''INSERT INTO Employees (Name, Position, DepartmentID, DateHired) VALUES ('Dave Black', 'Marketing Specialist', 2, '2024-02-01')''')
cursor.execute('''INSERT INTO Employees (Name, Position, DepartmentID, DateHired) VALUES ('Eva Blue', 'HR Assistant', 3, '2024-07-20')''')
cursor.execute('''INSERT INTO Employees (Name, Position, DepartmentID, DateHired) VALUES ('Frank Red', 'Finance Analyst', 4, '2022-12-03')''')
cursor.execute('''INSERT INTO Employees (Name, Position, DepartmentID, DateHired) VALUES ('Grace Yellow', 'IT Support', 5, '2023-04-06')''')
cursor.execute('''INSERT INTO Employees (Name, Position, DepartmentID, DateHired) VALUES ('Hannah Pink', 'Sales Associate', 1, '2023-11-19')''')
cursor.execute('''INSERT INTO Employees (Name, Position, DepartmentID, DateHired) VALUES ('Ian Violet', 'Marketing Assistant', 2, '2023-09-14')''')
cursor.execute('''INSERT INTO Employees (Name, Position, DepartmentID, DateHired) VALUES ('James Silver', 'HR Manager', 3, '2022-08-22')''')
cursor.execute('''INSERT INTO Employees (Name, Position, DepartmentID, DateHired) VALUES ('Katherine Brown', 'Finance Analyst', 4, '2023-05-25')''')
cursor.execute('''INSERT INTO Employees (Name, Position, DepartmentID, DateHired) VALUES ('Luke Green', 'IT Manager', 5, '2021-11-08')''')

# Insert into Projects
cursor.execute('''INSERT INTO Projects (ProjectName, DepartmentID, StartDate, EndDate) VALUES ('Website Redesign', 5, '2025-04-01', '2025-06-30')''')
cursor.execute('''INSERT INTO Projects (ProjectName, DepartmentID, StartDate, EndDate) VALUES ('Marketing Campaign', 2, '2025-03-01', '2025-05-30')''')

# Insert into Salaries
cursor.execute('''INSERT INTO Salaries (EmployeeID, Amount, PayDate) VALUES (1, 5500, '2025-04-01')''')
cursor.execute('''INSERT INTO Salaries (EmployeeID, Amount, PayDate) VALUES (2, 4800, '2025-04-01')''')
cursor.execute('''INSERT INTO Salaries (EmployeeID, Amount, PayDate) VALUES (3, 4000, '2025-04-01')''')
cursor.execute('''INSERT INTO Salaries (EmployeeID, Amount, PayDate) VALUES (4, 6500, '2025-04-01')''')
cursor.execute('''INSERT INTO Salaries (EmployeeID, Amount, PayDate) VALUES (5, 5200, '2025-04-01')''')
cursor.execute('''INSERT INTO Salaries (EmployeeID, Amount, PayDate) VALUES (6, 3300, '2025-04-01')''')
cursor.execute('''INSERT INTO Salaries (EmployeeID, Amount, PayDate) VALUES (7, 4500, '2025-04-01')''')
cursor.execute('''INSERT INTO Salaries (EmployeeID, Amount, PayDate) VALUES (8, 3800, '2025-04-01')''')
cursor.execute('''INSERT INTO Salaries (EmployeeID, Amount, PayDate) VALUES (9, 7000, '2025-04-01')''')
cursor.execute('''INSERT INTO Salaries (EmployeeID, Amount, PayDate) VALUES (10, 4800, '2025-04-01')''')
cursor.execute('''INSERT INTO Salaries (EmployeeID, Amount, PayDate) VALUES (11, 3100, '2025-04-01')''')
cursor.execute('''INSERT INTO Salaries (EmployeeID, Amount, PayDate) VALUES (12, 4200, '2025-04-01')''')
cursor.execute('''INSERT INTO Salaries (EmployeeID, Amount, PayDate) VALUES (13, 4900, '2025-04-01')''')
cursor.execute('''INSERT INTO Salaries (EmployeeID, Amount, PayDate) VALUES (14, 6000, '2025-04-01')''')
cursor.execute('''INSERT INTO Salaries (EmployeeID, Amount, PayDate) VALUES (15, 5300, '2025-04-01')''')

# Insert into Attendance
cursor.execute('''INSERT INTO Attendance (EmployeeID, Date, Status) VALUES (1, '2025-04-01', 'Present')''')
cursor.execute('''INSERT INTO Attendance (EmployeeID, Date, Status) VALUES (2, '2025-04-01', 'Absent')''')
cursor.execute('''INSERT INTO Attendance (EmployeeID, Date, Status) VALUES (3, '2025-04-01', 'On Leave')''')

# Insert into Sales
cursor.execute('''INSERT INTO Sales (EmployeeID, SaleAmount, SaleDate, ProductID) VALUES (1, 500, '2025-04-01', 101)''')
cursor.execute('''INSERT INTO Sales (EmployeeID, SaleAmount, SaleDate, ProductID) VALUES (2, 300, '2025-04-02', 102)''')

# Commit changes to the database
connection.commit()

# Display all records
print("Departments:")
departments = cursor.execute('''SELECT * FROM Departments''')
for row in departments:
    print(row)

print("\nEmployees:")
employees = cursor.execute('''SELECT * FROM Employees''')
for row in employees:
    print(row)

print("\nProjects:")
projects = cursor.execute('''SELECT * FROM Projects''')
for row in projects:
    print(row)

print("\nSalaries:")
salaries = cursor.execute('''SELECT * FROM Salaries''')
for row in salaries:
    print(row)

print("\nAttendance:")
attendance = cursor.execute('''SELECT * FROM Attendance''')
for row in attendance:
    print(row)

print("\nSales:")
sales = cursor.execute('''SELECT * FROM Sales''')
for row in sales:
    print(row)

# Close the connection
connection.close()
