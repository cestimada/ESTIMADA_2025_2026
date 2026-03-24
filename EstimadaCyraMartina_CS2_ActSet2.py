students= []
for i in range(3):
    dicti= {}
    dicti["name"]=input("Enter Name: ")
    dicti["age"]=input("Enter Age: ")
    dicti["grade"]=input("Enter Grade: ")
    print("\n")
    students.append(dicti)

print("Class Directory: ") 
for i in students:
    print("", i["name"], "| Age: ", i["age"], "| Grade:", i["grade"])
          