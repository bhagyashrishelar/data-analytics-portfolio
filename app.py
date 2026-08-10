import streamlit as st
import sqlite3

# Connect to database
conn = sqlite3.connect("data.db")
c = conn.cursor()
# create table
c.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER
)
""")

st.title("Student CRUD App")

menu = ["Create", "Read", "Update", "Delete"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Create":
    st.subheader("Add New Student")

    name = st.text_input("Enter Name")
    age = st.number_input("Enter Age", 0, 100)

    if st.button("Add"):
        c.execute("INSERT INTO students(name, age) VALUES(?, ?)", (name, age))
        conn.commit()
        st.success("Student Added Successfully!")

elif choice == "Read":
    st.subheader("View Students")

    c.execute("SELECT * FROM students")
    data = c.fetchall()
    st.write(data)

elif choice == "Update":
    st.subheader("Update Student")

    c.execute("SELECT * FROM students")
    data = c.fetchall()
    ids = [row[0] for row in data]

    selected_id = st.selectbox("Select Student ID", ids)
    new_name = st.text_input("New Name")
    new_age = st.number_input("New Age", 0, 100)

    if st.button("Update"):
        c.execute("UPDATE students SET name=?, age=? WHERE id=?",
                  (new_name, new_age, selected_id))
        conn.commit()
        st.success("Student Updated Successfully!")

elif choice == "Delete":
    st.subheader("Delete Student")

    c.execute("SELECT * FROM students")
    data = c.fetchall()
    ids = [row[0] for row in data]

    selected_id = st.selectbox("Select Student ID to Delete", ids)

    if st.button("Delete"):
        c.execute("DELETE FROM students WHERE id=?", (selected_id,))
        conn.commit()
        st.success("Student Deleted Successfully!")