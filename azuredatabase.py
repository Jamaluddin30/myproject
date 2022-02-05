import pyodbc
from datetime import datetime

server = 'attendancedata.database.windows.net'
database = 'attendance'
username = 'spattendance'
password = '$Patel123'
driver= '{ODBC Driver 17 for SQL Server}'

with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
    with conn.cursor() as cursor:
        def create_data():
            with conn:

                cursor.execute("""DROP TABLE IF EXISTS dbo.StudentAttendance
                                  CREATE TABLE dbo.StudentAttendance([Student_Name] nvarchar(20),[Date_Time] nvarchar(20))""")


        def insert_data(name, dtstring):
            with conn:
                cursor.execute("INSERT INTO dbo.StudentAttendance  (Student_Name , Date_Time)VALUES(?, ?)",  name,dtstring)

        def exist_name(name, d1):
            cursor.execute("SELECT Student_Name FROM dbo.StudentAttendance   ")
            row = cursor.fetchall()
            for ro in row:
                if (name == ro[0]):
                    return True
            return False
