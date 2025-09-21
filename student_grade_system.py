# student grade system 

class student:
    def __init__ (self, student_id, name):
        self.student_id = student_id
        self.name= name
        self.subjects = {}

    def add_subject(self, subject_name, marks):
        self.subjects[subject_name] = marks
        

    def total_marks(self):
        return sum(self.subjects.values())
    
    def average(self):
        return self.total_marks()/len(self.subjects)
    
    def grade(self):
        avg = self.average()
        if avg>=90:
            return "A+"
        elif avg >= 80:
            return "A"
        elif avg >= 75:
            return "B+"
        elif avg >= 70:
            return "B"
        elif avg >= 50:
            return "C"
        else :
            return "fail"
    
class GradeManager:
    def __init__(self):
        self.students = {}
        

    def add_student(self, student_id, name):
        if student_id in self.students:
            print(f"{name} already exists.")
            return False
        self.students[student_id]= student(student_id, name)
        print(f"{name} successfully added with id {student_id}")
        
        return True

    def remove_student(self, student_id):
        if student_id in self.students:
            name = self.students[student_id].name 
            del self.students[student_id]
            print(f"{student_id} deleted succefully")
            return True
        else:
            print(f"{student_id} does not exists")
            return False
        
    def add_marks(self, student_id, subject, marks):
        if student_id not in self.students:
            print(f"{student_id} not found.")
            return False
        elif not (0 <= marks <=100 ):
            print("Enter marks between 0 to 100")
            return False 
        self.students[student_id].add_subject(subject,marks)
        print(f"{marks} successfully added in {subject}")
        return True
    
    def display_student(self, student_id):
        if student_id not in self.students:
            print(f"{student_id} not found!!")
            return False
        student = self.students[student_id]
        print("*"*50)
        print(f"student id: {student.student_id}   name: {student.name}")
        if not student.subjects:
            print("No subject added yet.")
            return False 
        for subject, marks in student.subjects.items():
            print(f"{subject} : {marks}")
        print(f"average = {student.average()}")
        print(f"total marks - {student.total_marks():.2f}")
        print(f"grade = {student.grade()}")

    def display_all_students(self):
        if not self.students:
            print("No student added yet.")
            return False
        print(f"{'id:':<6} {'name:':20} {'total:':<6} {'average:':<8} {'grade:':<6}   ")
        print("-"*50)
        for student in self.students.values():
            print(f"{student.student_id:<6}  {student.name:<20}"
                  f"{student.total_marks():<6}  {student.average():<8.2f}"
                  f"{student.grade():<6}")
            

def main():
    gm = GradeManager()
    while True:
        print("*"*50)
        print("Wlcm to Student Grade Management system!!!")
        print("*"*50)
        print("\n enter 1 to add student.")
        print("enter 2 for remove student.")
        print("enter 3 for add marks.")
        print("enter 4 for student detail.")
        print("enter 5 to see all students detail.")
        print("enter 6 to exit from program.")

        choice = int(input("Enter your choice(1-6):"))

        if choice == 1:
            name = input("enter student name:")
            sid = int(input("enter student id:"))
            gm.add_student(sid, name)
    
        elif choice ==2:
            sid = int(input("enter student id:"))
            gm.remove_student(sid)
        elif choice == 3:
            sid = int(input("enter the student id:"))
            sname = input("enter subject name:")
            marks = float(input("enter marks:"))
            gm.add_marks(sid, sname, marks)

        elif choice == 4:
            sid = int(input("enter the sudent id:"))
            gm.display_student(sid)

        elif choice == 5:
            gm.display_all_students()

        elif choice == 6:
            print("exiting program..............")
            break
        else :
            print("invalid choice please enter number between 1-6.........")

if __name__ == "__main__":
    main()