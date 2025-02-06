sample_dict = {
    "student": {
        "name": "Alice",
        "age": 20,
        "courses": {
            "math": "A",
            "science": "B",
            "english": "A"
        }
    },
    "teacher": {
        "name": "Mr. Smith",
        "age": 45,
        "subjects": ["math", "science", "history"]
    }
}

student_course=sample_dict["student"]
student_teacher=sample_dict["teacher"]
print(student_course["courses"])
print(student_teacher["name"])