import mysql.connector
import streamlit as st

# Establish a connection to MySQL Server

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Admin@123",
    database="crud1"


)
mycursor=mydb.cursor()
print("Connection Established")

# Create Streamlit App

def main():
    st.title("Student Database Management System");

    # Display Options for CRUD Operations
    option=st.sidebar.selectbox("Access Information",("Insert record","Student data","Update record","Delete record"))
    # Perform Selected CRUD Operations
    if option=="Insert record":
        st.subheader("Insert a Record")
        Roll_no=st.number_input("Enter Roll Number")
        Name=st.text_input("Enter Name")
        Class=st.number_input("Enter Class")
        Percentage=st.number_input("Enter Percentage")
        Email=st.text_input("Enter Email")
        Address=st.text_input("Enter Permanent Address")

        if st.button("Insert Record"):
            sql= "insert into users(Roll_no,Name,Class,Percentage,Email,Address) values(%s,%s,%s,%s,%s,%s)"
            val= (Roll_no,Name,Class,Percentage,Email,Address)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Record Inserted Successfully!!!")



    elif option=="Student data":
        st.subheader("Read Records")
        mycursor.execute("select * from users")
        result = mycursor.fetchall()
        for row in result:
            st.write(row)



    elif option=="Update record":
        st.subheader("Update a Record")
        Roll_no=st.number_input("Enter ID",min_value=1)
        Name=st.text_input("Enter New Name")
        Class=st.number_input("Enter New Class")
        Percentage=st.number_input("Enter New Percentage")
        Email=st.text_input("Enter New Email")
        Address=st.text_input("Enter New Address")
        if st.button("Update"):
            sql="update users set Name=%s,Class=%s,Percentage=%s,Email=%s,Address=%s where Roll_no =%s"
            val=(Name,Class,Percentage,Email,Address,Roll_no)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Record Updated Successfully!!!")




    elif option == "Delete record":
        st.subheader("Delete a Record")
        Roll_no = st.number_input("Enter Roll Number", min_value=1)
        if st.button("Delete record"):
            sql = "delete from users where Roll_no = %s"
            val = (Roll_no,)
            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Record Deleted Successfully!!!")

    
    
    
    


if __name__ == "__main__":
    main()








