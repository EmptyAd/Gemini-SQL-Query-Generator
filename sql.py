import streamlit as st
import sqlite3
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()  # Make sure to set your GOOGLE_API_KEY in your .env file

# Configure Google Gemini API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to retrieve data from SQLite DB
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    try:
        cur.execute(sql)
        rows = cur.fetchall()
        conn.commit()
        conn.close()
        return rows
    except sqlite3.Error as e:
        conn.close()
        st.error(f"SQL Error: {e}")
        return []
    
def get_column_names(table, db):
    query = f"PRAGMA table_info({table});"
    result = read_sql_query(query, db)
    column_names = [column[1] for column in result]
    return column_names



# Function to get Gemini response (SQL generation)
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('models/gemini-1.5-pro-latest')
    response = model.generate_content([prompt, question])  # Gemini generates the response
    sql_code = response.text.strip()

    # Clean up the response to extract valid SQL
    if "```sql" in sql_code:
        sql_code = sql_code.split("```sql")[-1]
    if "```" in sql_code:
        sql_code = sql_code.split("```")[0]

    lines = sql_code.splitlines()
    valid_lines = []
    started = False
    for line in lines:
        line_strip = line.strip()
        if not started:
            if any(line_strip.upper().startswith(kw) for kw in ["SELECT", "WITH", "INSERT", "UPDATE", "DELETE"]):
                started = True
                valid_lines.append(line_strip)
        else:
            valid_lines.append(line_strip)

    final_sql = " ".join(valid_lines)
    return final_sql.strip()


system_prompt = """
You are an expert in converting natural language questions into correct and advanced SQL queries for an SQLite database.

Important Instructions:
- The database is an **SQLite** database.
- The database contains the following tables:

  1. **Departments**:
     - **DepartmentID** (INTEGER): Unique identifier for each department.
     - **DepartmentName** (TEXT): Name of the department.

  2. **Employees**:
     - **EmployeeID** (INTEGER): Unique identifier for each employee.
     - **Name** (TEXT): Name of the employee.
     - **Position** (TEXT): Job title of the employee.
     - **DepartmentID** (INTEGER): ID of the department to which the employee belongs (foreign key).
     - **DateHired** (TEXT): Date the employee was hired.

  3. **Projects**:
     - **ProjectID** (INTEGER): Unique identifier for each project.
     - **ProjectName** (TEXT): Name of the project.
     - **DepartmentID** (INTEGER): ID of the department handling the project (foreign key).
     - **StartDate** (TEXT): Start date of the project.
     - **EndDate** (TEXT): End date of the project.

  4. **Salaries**:
     - **SalaryID** (INTEGER): Unique identifier for each salary record.
     - **EmployeeID** (INTEGER): ID of the employee (foreign key).
     - **Amount** (REAL): Salary amount.
     - **PayDate** (TEXT): Date the salary was paid.

  5. **Attendance**:
     - **AttendanceID** (INTEGER): Unique identifier for each attendance record.
     - **EmployeeID** (INTEGER): ID of the employee (foreign key).
     - **Date** (TEXT): Date of attendance.
     - **Status** (TEXT): Status of the employee (e.g., 'Present', 'Absent', 'On Leave').

  6. **Sales**:
     - **SaleID** (INTEGER): Unique identifier for each sale.
     - **EmployeeID** (INTEGER): ID of the employee involved in the sale (foreign key).
     - **SaleAmount** (REAL): Amount of money involved in the sale.
     - **SaleDate** (TEXT): Date the sale took place.
     - **ProductID** (INTEGER): ID of the product sold.

- Your goal is to generate a correct **SQLite query** based on the user's natural language question.

- If the user asks for the **columns** of a table (example: "what are the columns of Employees", "list columns of Salaries"),  
  output:

    PRAGMA table_info(TableName);

  (Replace **TableName** with the requested table name.)

- For all other questions, generate correct **SQLite SELECT** queries, using appropriate **JOINs, WHERE, GROUP BY, HAVING, ORDER BY, subqueries, aggregate functions, and filtering**.

- **Use only valid SQLite syntax.**

- **Do not** use system tables, INFORMATION_SCHEMA, or any metadata sources.

- **Only output the SQL query.**  
  **No extra explanations, no commentary, no backticks (`).**

---

### Example SQL Queries:

1. **Get all employees and their department names:**

   SELECT Employees.Name, Departments.DepartmentName
   FROM Employees
   INNER JOIN Departments ON Employees.DepartmentID = Departments.DepartmentID;

2. **Get total sales made by each employee:**

   SELECT Employees.Name, SUM(Sales.SaleAmount) AS TotalSales
   FROM Sales
   INNER JOIN Employees ON Sales.EmployeeID = Employees.EmployeeID
   GROUP BY Employees.Name;

3. **What are the columns of Employees table?**

   PRAGMA table_info(Employees);

4. **Find employees who were absent today:**

   SELECT Employees.Name
   FROM Employees
   INNER JOIN Attendance ON Employees.EmployeeID = Attendance.EmployeeID
   WHERE Attendance.Date = date('now') AND Attendance.Status = 'Absent';

5. **List projects that ended before today:**

   SELECT ProjectName, EndDate
   FROM Projects
   WHERE EndDate < date('now');

6. **Get average salary by department:**

   SELECT Departments.DepartmentName, AVG(Salaries.Amount) AS AverageSalary
   FROM Salaries
   INNER JOIN Employees ON Salaries.EmployeeID = Employees.EmployeeID
   INNER JOIN Departments ON Employees.DepartmentID = Departments.DepartmentID
   GROUP BY Departments.DepartmentName;

"""


# Streamlit app setup
st.set_page_config(page_title="SQL Query Generator")
st.header("Gemini SQL Query Generator")

# Input field for the user's question
question = st.text_input("Ask a question", "")

# Button to trigger the generation of SQL query
submit = st.button("Generate SQL Query")

# If button is clicked, process the user's question
if submit:
    if question:
        if "column names" in question.lower():
            # Get column names from the Employees table
            column_names = get_column_names("Employees", "store_office.db")
            st.subheader("Column Names")
            st.write(", ".join(column_names))
        else:
            # Call Gemini to generate SQL query
            sql_query = get_gemini_response(question, system_prompt)
            st.subheader("Generated SQL Query")
            st.code(sql_query, language="sql")

            # Execute SQL query and display results
            try:
                result = read_sql_query(sql_query, "store_office.db")
                st.subheader("Query Result")
                for row in result:
                    st.write(row)
            except Exception as e:
                st.error(f"Error executing query: {e}")
    else:
        st.warning("Please enter a question.")
