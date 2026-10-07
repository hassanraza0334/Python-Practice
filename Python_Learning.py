# Dictionary Methods
# 1)  myDict.update()---> inserts the specified items to the dictionary

student={
    "Name":"Hassan Raza",
     "Subjects":["English","Math","Computer","Urdu"],
     "Age":25,
     "Marks":[78,89,88,99,],
     "CNIC":"Adults",
     "CGPA":3.2,

         }
student.update({"City":"Pattoki"})
print(student)