student_id=int(input("Enter the Student id:"))
student_records={
    101: {'name': 'Alice', 'age': 20, 'grade': 'A'},
    102: {'name': 'Bob', 'age': 22, 'grade': 'B'},
    103: {'name': 'Charlie', 'age': 21, 'grade': 'A'}
}

if student_id in student_records:
    print(student_records[student_id])
else:
    print(f"Invalid Student Id {student_id}")
