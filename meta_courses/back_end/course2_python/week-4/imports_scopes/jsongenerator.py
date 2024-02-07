import json
from employee import details, employee_name, age, title

def create_dict(name, age, title):
    dict_employee= {'first_name':str(name), 'age':int(age), 'title':str(title)}
    return dict_employee

def write_json_to_file(json_obj, output_file):
    with open(output_file,'w') as file:
        file.write(json_obj)

def main():
    # Print the contents of details() -- This should print the details of an employee
    details()

    # Create employee dictionary
    employee_dict = create_dict(employee_name, age, title)
    print("employee_dict: " + str(employee_dict))

    ''' 
    Use a function called dumps from the json module to convert employee_dict
    into a json string and store it in a variable called json_object.
    '''
    ### WRITE YOUR CODE BY MODIFYING THE LINE BELOW
    # In the line below replace the None keyword with your code. 
    # The format should look like: variable = json.dumps(dict)
    json_object = json.dumps(employee_dict)
    print("json_object: " + str(json_object))

    # Write out the json object to file
    write_json_to_file(json_object, "week-4/imports_scopes/employee.json")

if __name__ == "__main__":
    main()