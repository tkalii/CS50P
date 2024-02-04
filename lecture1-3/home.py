students = [
    {"name":"Hermione", "house":"Gryffindor"},
    {"name":"Harry", "house":"Gryffindor"},
    {"name":"Ron", "house":"Gryffindor"}
    ]

# print(students["Hermione"])
# print(students["Harry"])
# print(students["Ron"])
# print(students["Draco"])
for student in  students:
    print(student["name"], student["house"], sep = ", ")