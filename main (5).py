class Student:
  def __init__(self,name,roll_number,cgpa):
    self.name=name
    self.roll_number=roll_number
    self.cgpa=cgpa

def sort_student (student_list):
  sorted_students=sorted(student_list, key=lambda student:student.cgpa,reverse =True)
  return sorted_students 

  #example usage:
student1 = Student("alice","S123",3.7)
student2 = Student("bob","S124",3.9)
student3 = Student("charlie","S125",3.5)
student4 = Student("David","S126",3.8)


students =[student1,student2,student3,student4]

sorted_students = sort_student(students)

#print the the sorted list of students by CGPA in ascending order
for student in sorted_students :
  print(f"Name:{student.name},Roll Number. {student.roll_number},CGPA:{student.cgpa}")




  
  
    