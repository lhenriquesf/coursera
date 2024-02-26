employee_dict = {
    12345: {
        "id": "12345",
        "name": "John", 
        "department": "Kitchen"    
    },
    12458: {
        "id": "12458",
        "name": "Paul", 
        "department": "House Floor"    
    }
}

def get_employee_from_dict(id):
    return employee_dict[id]['id']


print(get_employee_from_dict(12458))

