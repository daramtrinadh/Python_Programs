sample_dict = {
    "name": "John Doe",
    "age": 30,
    "email": "john.doe@example.com",
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "zipcode": "12345"
    },
    "hobbies": ["reading", "cycling", "traveling"],
    "is_active": True
}
print(sample_dict["name"])
print(sample_dict.get("address"))