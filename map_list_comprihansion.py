# Input data: List of dictionaries
employee_list = [
    {"id": 12345, "name": "John", "department": "Kitchen"},
    {"id": 12456, "name": "Paul", "department": "House Floor"},
    {"id": 12478, "name": "Sarah", "department": "Management"},
    {"id": 12434, "name": "Lisa", "department": "Cold Storage"},
    {"id": 12483, "name": "Ryan", "department": "Inventory Mgmt"},
    {"id": 12419, "name": "Gill", "department": "Cashier"}
]


"Function to be passed to the map() function."
def mod(employee_list):
    temp = employee_list['name'] + "_" + employee_list["department"]
    return temp


"list - A list of strings consisting of name + department."
def to_mod_list(employee_list):
    map_list = map(mod, employee_list)
    return list(map_list)

" list - A list of usernames consisting of name + department delimited by underscores."

def generate_usernames(mod_list):
    username = [x.replace(' ', '_') for x in mod_list]
    return username


"  dict - A dictionary mapping an employee's id (value) to their first initial (key)."

def map_id_to_initial(employee_list):
    id_to_name = {employer['name'][0]: employer['id'] for employer in employee_list}
    return id_to_name



def main():
    mod_emp_list = to_mod_list(employee_list)
    print("Modified employee list: " + str(mod_emp_list) + "\n")

    print(f"List of usernames: {generate_usernames(mod_emp_list)}\n")

    print(f"Initials and ids: {map_id_to_initial(employee_list)}")


if __name__ == "__main__":
    main()