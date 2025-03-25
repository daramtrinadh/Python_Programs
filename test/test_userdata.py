import pytest

def check_userdata(users):
    valid_users=[]
    for user in users:
        if "name" not in user or "age" not in user or "email" not in user:
            continue
        elif not isinstance(user['age'],int):
            continue
        valid_users.append(user)
    return valid_users

def test_alldata():
    user_data = [
        {"name": "Alice", "age": 30, "email": "alice@example.com"},
        {"name": "Bob", "age": "twenty-five", "email": "bob@example.com"},
        {"name": "Charlie", "email": "charlie@example.com"},
        {"name": "David", "age": 22, "email": "david@example.com"},
        {"name": "Eve", "age": 29, "email": "eve@example.com"}
    ]
    expected_output = [
        {"name": "Alice", "age": 30, "email": "alice@example.com"},
        {"name": "David", "age": 22, "email": "david@example.com"},
        {"name": "Eve", "age": 29, "email": "eve@example.com"}
    ]
    assert check_userdata(user_data)==expected_output

def test_process_user_data_empty():
    assert check_userdata([]) == []

def test_process_user_data_all_invalid():
    user_data = [
        {"name": "Alice", "age": "thirty", "email": "alice@example.com"},
        {"name": "Bob", "age": 25},
        {"age": 22, "email": "charlie@example.com"}
    ]
    assert check_userdata(user_data) == []