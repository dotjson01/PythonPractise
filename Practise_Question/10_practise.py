age = int (input("Enter the Age\n"))
height = float (input("Enter the Height\n"))
name = str(input("Enter the name\n"))
is_student = input("Are you a student ? Yes/No\n").strip().lower() in ("yes", "y", "true", "1")
is_student1 = None


print("Is student", is_student)
print(type(is_student))
print(age)
print(type(age))
print(height)
print(type(height))
print(name)
print(type(name))
print("Is student", is_student1)