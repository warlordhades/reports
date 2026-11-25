students = [
    ("Alice", 88, 92, 85),
    ("Bob", 76, 81, 79),
    ("Charlie", 95, 90, 93)
]

choice = input("Enter student name (Alice, Bob, Charlie): ")

for student in students:
    name, math, science, english = student
    
    if name == choice:
        print("Name:", name)
        print("Math:", math)
        print("Science:", science)
        print("English:", english)
