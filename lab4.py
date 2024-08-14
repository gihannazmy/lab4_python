# import mysql.connector
# from mysql.connector import Error

# def connect_db():
#     try:
#         connection = mysql.connector.connect(
#             host='localhost',
#             database='iti',
#             user='helana',
#             password='1993'
#         )
#         if connection.is_connected():
#             print("Connected to the database")
#         return connection
#     except Error as e:
#         print(f"Error: {e}")
#         return None

# def insert_record(table, data):
#     connection = connect_db()
#     if connection is None:
#         return "Connection failed"
    
#     cursor = connection.cursor()
#     if table == 'trainee':
#         query = "INSERT INTO trainee (name, age, track_id) VALUES (%s, %s, %s)"
#     elif table == 'track':
#         query = "INSERT INTO track (name, duration) VALUES (%s, %s)"
#     else:
#         return "Invalid table"
    
#     try:
#         cursor.execute(query, data)
#         connection.commit()
#         return "Record inserted successfully"
#     except Error as e:
#         return f"Error: {e}"
#     finally:
#         cursor.close()
#         connection.close()

# def update_record(table, data, condition):
#     connection = connect_db()
#     if connection is None:
#         return "Connection failed"
    
#     cursor = connection.cursor()
#     if table == 'trainee':
#         query = "UPDATE trainee SET name = %s, age = %s, track_id = %s WHERE " + condition
#     elif table == 'track':
#         query = "UPDATE track SET name = %s, duration = %s WHERE " + condition
#     else:
#         return "Invalid table"
    
#     try:
#         cursor.execute(query, data)
#         connection.commit()
#         return "Record updated successfully"
#     except Error as e:
#         return f"Error: {e}"
#     finally:
#         cursor.close()
#         connection.close()

# def select_records(table, condition=None):
#     connection = connect_db()
#     if connection is None:
#         return "Connection failed"
    
#     cursor = connection.cursor(dictionary=True)
#     query = f"SELECT * FROM {table}"
#     if condition:
#         query += " WHERE " + condition
    
#     try:
#         cursor.execute(query)
#         records = cursor.fetchall()
#         return records
#     except Error as e:
#         return f"Error: {e}"
#     finally:
#         cursor.close()
#         connection.close()

# def delete_record(table, condition):
#     connection = connect_db()
#     if connection is None:
#         return "Connection failed"
    
#     cursor = connection.cursor()
#     query = f"DELETE FROM {table} WHERE {condition}"
    
#     try:
#         cursor.execute(query)
#         connection.commit()
#         return "Record deleted successfully"
#     except Error as e:
#         return f"Error: {e}"
#     finally:
#         cursor.close()
#         connection.close()

# import dbconnection

# # Insert 
# result = dbconnection.insert_record('trainee', ('John Doe', 25, 1))
# print(result)

# # Update
# result = dbconnection.update_record('trainee', ('John Smith', 26, 1), "name = 'John Doe'")
# print(result)

# # Select 
# records = dbconnection.select_records('trainee')
# print(records)

# # Delete 
# result = dbconnection.delete_record('trainee', "name = 'John Smith'")
# print(result)

# ////////////////////////////////////////////////////////////////////////////////////////////////////////
# ////////////////////////////////(2)//////////////////////////////////////////////////////////////////////
# create class human--->defin classvar,instnacevar,method
class Human:

    def __init__(self, name, age, gender, nationalId):
        self.name = name
        self.age = age
        self.gender = gender
    # Instance method
    def introduce(self):
        """
        Introduces the human with their name, age, and gender.
        """
        return f"Hello, my name is {self.name}. I am a {self.age}-year-old {self.gender}."
    def is_adult(age):
        """
        Determines if the human is an adult based on their age.
        """
        return age >= 18
    

class Employee():
    company = "Concentrix"
    def __init__(self, name, age, gender, national_id, employee_id, position, salary):
      
        self.name = name
        self.age = age
        self.gender = gender
        self.national_id = national_id
        self.employee_id = employee_id
        self.position = position
        self.salary = salary
    def introduce(self):
        """
        Introduces the employee, including their job-related information.
        """
        return f"Hello, my name is {self.name}. I am a {self.age}-year-old {self.gender}. My postion is {self.position}. My salary is {self.salary}"

    def work(self):
        """
        Describes the employee working at their job.
        """
        return f"{self.name} is working as a {self.position} at {self.company}."
    