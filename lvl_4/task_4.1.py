# Задача 4.1.
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:

import sqlite3
# 1
# connection = sqlite3.connect(r'C:\Users\natah\envs\homeworks\lvl_4\teatchers.db') 
# cursor = connection.cursor()                
# sqlquery = """CREATE TABLE Students (
# Student_Id INTEGER,
# Student_Name TEXT, 
# School_Id INTEGER NOT NULL PRIMARY KEY);"""
# cursor.execute(sqlquery)                   
# connection.commit()              
# connection.close() 

# 2
# connection = sqlite3.connect(r'C:\Users\natah\envs\homeworks\lvl_4\teatchers.db') 
# cursor = connection.cursor()                
# sqlquery = """INSERT INTO Students (Student_Id, Student_Name, School_Id)
# VALUES
# (201, 'Иван', 1),
# (202, 'Петр', 2),
# (203, 'Анастасия', 3),
# (204, 'Игорь', 4);"""
# cursor.execute(sqlquery)                    
# connection.commit()                
# connection.close()

# 3
def get_connection():
  connection = sqlite3.connect(r'C:\Users\natah\envs\homeworks\lvl_4\teatchers.db')
  return connection

def close_connection(connection):
  if connection:
    connection.close()

def get_student_info(Student_Id):
  try:
    connection = get_connection()
    cursor = connection.cursor()
    select_query = """SELECT Students.Student_Id, Students.student_name, School.School_Id, School.School_Name
From Students
JOIN School ON Students.School_Id = School.School_Id
WHERE Student_Id = ?;"""
    cursor.execute(select_query, (Student_Id,))
    records = cursor.fetchall()
    close_connection(connection)
    for row in records:
      print("ID Студента:", row[0])
      print("Имя студента:", row[1])
      print("ID школы:", row[2])
      print("Название школы:", row[3])
  except (Exception, sqlite3.Error) as error:
    print("Ошибка в получении данных: ", error) 

get_student_info(201)