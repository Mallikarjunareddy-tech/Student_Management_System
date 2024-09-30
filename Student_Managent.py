import pyodbc as odbc  # import the necessary Driver o Connect SQL Server
# Create a Connecting Object with Conn = pyodbc.connect(Truested_connection = "yes",driver = "{SQL Server}",Server ="replace with your server name",Database = "DatabaseName")
conn = odbc.connect(Trusted_connection='True',driver="{SQL Server}",Server='arjun\MSSQLSERVER2022',Database='StudentManagement',autocommit='yes')
cur = conn.cursor()  # Create a cursur object

# Create Rquire tables in Sql Server Management Studio 
# or
# Create Tables by using python code
# Create table Student
'''cur.execute(""" create table Student(
                                        Student_id  int primary key identity(1,1),
                                        first_name  varchar(50),
                                        last_name  varchar(50),
                                        Date_Of_Birth varchar(50),
                                        Email varchar(100)
                                        )""")'''
# Create Courses Table
'''cur.execute(""" create table Courses(
                            Course_id int primary key identity(1,1),
                            Course_name varchar(50),
                            Course_Description text)""")'''
# Create Grades table
'''cur.execute(create table Grade(
                            Grade_id int primary key identity(1,1),
                            Student_id int ,
                            Course_id int,
                            FOREIGN KEY (Student_id) REFERENCES Student(Student_id)
                            FOREIGN KEY (Course_id) REFERENCES Courses(Course_id)))'''

def add_Student(first_name,last_name,DOB,email): # Function to add student details
    cur.execute(""" insert into Students values(?,?,?,?) """,(first_name,last_name,DOB,email))
    print("Student added Successfully.")
    conn.commit()
def view_Students(): # Function that shows the content of the student table
    cur.execute("SELECT * FROM Students")
    rows= cur.fetchall()
    for row in rows:
        print(row)
    conn.commit()
    print("Those are all Students we Have")
def updateStudentsAllColumns(Student_id,first_name=None,last_name=None,Date_Of_Birth = None,E_mail=None): #Function that updates the all columns of the table Student
    cur.execute("""
                update Students
                set first_name = COALESCE(?,first_name),
                    last_name = COALESCE(?,last_name),
                    Date_Of_Birth = COALESCE(?,Date_Of_Birth),
                    E_mail = COALESCE(?,E_mail)
                where Student_id=? """,(first_name,last_name,Date_Of_Birth,E_mail,Student_id))
    conn.commit()
    print("Student Updated Successfully. ")
def updateStudentsFirstName(Student_id,first_name=None): # Creating a function that updates the first_name of the Student
    cur.execute("""
                update Students
                set first_name = COALESCE(?,first_name)
                where Student_id=? """,(first_name,Student_id))    
    conn.commit()
    print("Student Updated Successfully. ")
def updateStudentsLastName(Student_id,last_name=None):  # creating a function that updates student last name
    cur.execute("""
                update Students
                set last_name = COALESCE(?,last_name)
                where Student_id=? """,(last_name,Student_id))
    conn.commit()
    print("Student Updated Successfully. ") 
def updateStudentsDob(Student_id,Date_Of_Birth = None): # creating a function that updates the date of birth of the student 
    cur.execute("""
                update Students
                set Date_Of_Birth = COALESCE(?,Date_Of_Birth)
                where Student_id=? """,(Date_Of_Birth,Student_id))
    conn.commit()
    print("Student Updated Successfully. ")  
def updateStudentsE_mail(Student_id,E_mail=None): # creating the function that updates the e-mail of the student
    cur.execute("""
                update Students
                set E_mail = COALESCE(?,E_mail)
                where Student_id=? """,(E_mail,Student_id))
    conn.commit()
    print("Student Updated Successfully. ")             
def delete_Students(Student_id):      # creating a function that deletes the details of the function 
    cur.execute("DELETE FROM Students WHERE Student_id=?",(Student_id,))
    conn.commit()
    print("Student Deleted Successfully. ")
def add_courses(Course_name,Course_Description):  # Creating the function that adds the courses of the student
    cur.execute(""" insert into Courses values(?,?) """,(Course_name,Course_Description))
    conn.commit()
    print("Course added Successfully. ")
def view_Courses():                # Creating function that fetches the all details of the courses
    rows=cur.execute("select * from Courses")
    for row in rows:
        print(row)
    conn.commit()
    print("These are all Courses we Have")
def updateCoursesAllColumns(Course_id,Course_name= None,Course_Description=None):   # creating a function that updates the all details of the courses table
    cur.execute("""
                update Courses
                set Course_name = COALESCE(?,Course_name),
                    Course_Description = COALESCE(?,Course_Description)
                where Course_id=? """,(Course_name,Course_Description,Course_id))
def updateCourseName(Course_id,Course_name= None):   # creating the function that updates the course name.
    cur.execute("""
                update Courses
                set Course_name = COALESCE(?,Course_name)
                where Course_id=? """,(Course_name,Course_id))    
                      
    conn.commit()
    print("Course Updated Successfully. ")
def updateCourseDescription(Course_id,Course_Description=None):      # Creating a function that updates the course description
    cur.execute("""
                update Courses
                set Course_Description = COALESCE(?,Course_Description)
                where Course_id=? """,(Course_Description,Course_id))    

def delete_Courses(Course_id):                            # creating a function that delete the courses bassed on id.
    cur.execute("dalete from Courses where Course_id=? ",(Course_id,)) 
    conn.commit()
    print("Course Deleted Successfully. ")
def add_Grades(Student_id,Course_id,Grade):       # creating a function that adds the grades to the table.
    cur.execute(""" insert into Grades values(?,?,?) """,(Student_id,Course_id,Grade))
    conn.commit()
    print("Grade added Successfully. ")
def view_Grades():            # creating the function that fetch the all grade details
    rows=cur.execute("SELECT * FROM Grades")
    for row in rows:
        print(row)
    conn.commit()
    print("These are all Grades we Have")   
def UpdateGradesAllColumns(Grade_id,Student_id=None,Course_id=None,Grade=None):       # creating the function that updates the all details of the table
    cur.execute(""" 
                update Grades
                set Student_id = COALESCE(?,Student_id),
                    Course_id = COALESCE(?,Course_id),
                    Grade = COALESCE(?,Grade)
                where Grade_id = ? """,(Student_id,Course_id,Grade,Grade_id))
    conn.commit()
    print("Grade Updated Successfully. ")
def UpdateGradesStudentID(Grade_id,Student_id=None,):      # creating the function that updates the studentID
    cur.execute(""" 
                update Grades
                set Student_id = COALESCE(?,Student_id)
                where Grade_id = ? """,(Student_id,Grade_id))
    conn.commit()
    print("Grade Updated Successfully. ") 
def UpdateGradesCourseID(Grade_id,Course_id=None):     # creating the function that updates the courseID
    cur.execute(""" 
                update Grades
                set Course_id = COALESCE(?,Course_id)
                where Grade_id = ? """,(Course_id,Grade_id))
    conn.commit()
    print("Grade Updated Successfully. ") 
def UpdateGradesColGrade(Grade_id,Grade=None):    # creating the function taht updates the grade column
    cur.execute(""" 
                update Grades
                set Grade = COALESCE(?,Grade)
                where Grade_id = ? """,(Grade,Grade_id))
    conn.commit()
    print("Grade Updated Successfully. ")          
def delete_Grades(Grade_id):          # creating the function that delete the details of the grade column.
    cur.execute("DELETE FROM Grades WHERE Grade_id=?",(Grade_id,))
    conn.commit()
    print("Grade Deleted Successfully. ")


def Main_menu():
    while True:
        print("1.Add Students")
        print("2.View Students")
        print("3.Update Students")
        print("4.Delete Students")
        print("5.Add Courses")
        print("6.View Courses")
        print("7.Update Courses")
        print("8.Delete Courses")
        print("9.Add Grades")
        print("10.View Grades")
        print("11.Update Grades")
        print("12.Delete Grades")
        print("13.Exit")
        choice = input("Enter your choice in numbers: ")
        if choice == "1":
            first_name = input("Enter the firstName: ")
            last_name = input("enter the lastName: ")
            dob = input("Enter the Date of Birth(YYYY-MM-DD): ")
            email = input("Enter the E-mail Address: ")
            add_Student(first_name,last_name,dob,email)
        elif choice == "2":
            view_Students()
        elif choice == "3":
            print("the columns in a table are: ")
            print("1.first_name")
            print("2.last_name")
            print("3.Date of Birth")
            print("4.E-mail")
            print("5.update all columns")
            Column = input("enter the Column would be update(Enter in column numbers): ")
            if Column == "1":
                Student_id = int(input("Enter the student_id: "))
                first_name= input("Enter the updated firstName /None: ")
                updateStudentsFirstName(Student_id,first_name)
            elif Column == "2":
                Student_id = int(input("Enter the student_id: "))
                last_name = input("Enter the updated lastName/ None: ")
                updateStudentsLastName(Student_id,last_name)
            elif Column == '3':
                Student_id = int(input("Enter the student_id: "))
                Date_Of_Birth = input("Enter the updated DOB(YYYY-MM-DD) / None:  ")    
                updateStudentsDob(Student_id,Date_Of_Birth)
            elif Column == "4":
                Student_id = int(input("Enter the student_id: ")) 
                E_mail = input("Enter the updated e-mail / None: ")   
                updateStudentsE_mail(Student_id,E_mail)
            elif Column == "5":
                Student_id = int(input("Enter the student_id: ")) 
                first_name= input("Enter the updated firstName /None: ") 
                last_name = input("Enter the updated lastName/ None: ")
                Date_Of_Birth = input("Enter the updated DOB(YYYY-MM-DD) / None:  ") 
                E_mail = input("Enter the updated e-mail / None: ") 
                updateStudentsAllColumns(Student_id,first_name,last_name,Date_Of_Birth,E_mail)

                
            
        elif choice == "4":
            Student_id = int(input("Enter the student_id: "))
            delete_Students(Student_id)
        elif choice == "5":
            CourseName = input("Enter the Course name: ")
            CourseDescription = input("Enter the Description: ")
            add_courses(CourseName,CourseDescription)
        elif choice == '6':
            view_Courses()
        elif choice == '7':
            print("the columns in a table are: ")
            print("1.Course name")
            print("2.Course Description")
            print("3.update all columns")
            Column = input("enter the Column would be update(Enter in column numbers): ")
            if Column == "1":
                Course_id = int(input("Enter the course_id: "))
                CourseName = input("enter the Course name: ")
                updateCourseName(Course_id,CourseName)
            elif Column =='2':
                Course_id = int(input("Enter the Course_id: "))
                CourseDescription = input("Enter the Description: ")
                updateCourseDescription(Course_id,CourseDescription)
            elif Column =='3':
                Course_id = int(input("Enter the Course_id: "))
                CourseName = input("Enter the course name: ")
                CourseDescription = input("Enter the Description: ")
                updateCoursesAllColumns(Course_id,CourseName,CourseDescription)
        elif choice =='8':
            Course_id = int(input("Enter the Course_id: "))
            delete_Courses(Course_id)
        elif choice == '9':
            Student_id = int(input("Enter the Student_id: "))
            Course_id = int(input("Enter the Course_id: "))
            Grade = input("Enter the Grade: ")
            add_Grades(Student_id,Course_id,Grade)
        elif choice == '10':
            view_Grades()
        elif choice == '11':
            print("the Columns in table are: ")
            print("1.Student_id")
            print("2.Course_id")
            print("3.Grade")
            Column = input("Enter the Column would be update(Enter in column numbers): ")
            if Column =='1':
                Grade_id = int(input("Enter the GradeID: "))
                Student_id = int(input("Enter the Student_id: "))
                UpdateGradesStudentID(Grade_id,Student_id)
            elif Column =='2':
                Grade_id = int(input("Enter the GradeID: "))
                Course_id = int(input("Enter the Course_id: "))
                UpdateGradesCourseID(Grade_id,Course_id)
            elif Column =='3':
                Grade_id = int(input("Enter the GradeID: "))
                Grade = input("Enter the Grade: ")
                UpdateGradesColGrade(Grade_id,Grade)

        elif choice == '12':
            Grade_id = int(input("Enter the GradeID: "))
            delete_Grades(Grade_id)
        elif choice == '13':
            print("Exiting.....")
            break
        else:
            print("Invalid Valid Choice. Please try again..")    
Main_menu()                        











































            