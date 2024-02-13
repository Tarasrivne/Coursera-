# ingridiends = ['water', 'milk', 'suga', 'instant cofee']
# cap_of_cofee = ['water', 'instant cofee']
# for elem in ingridiends:
#     if elem in cap_of_cofee:
#         print('You order is complete')
#     else:
#         print('We dont have this ingredient')
#######################################################
# new_data = [2,3,4,5]
# fourx = [x for x in range(100) if x%4 == 0 ]
# print("Divisible by four", fourx)

# for x in range(len(new_data)):
#     new_data[x] = new_data[x] + 2
#     print(new_data, + 1)
#
# for x in new_data:
#     x += 2
#     print(x, end= '-')
# nums = [12,14,16]
# set_a = [x for x in range(10,20) if x not in nums]
# print(set_a)

# ########################################
# employee_list = [
#    {"id": 12345, "name": "John", "department": "Kitchen"},
#    {"id": 12456, "name": "Paul", "department": "House Floor"},
#    {"id": 12478, "name": "Sarah", "department": "Management"},
#    {"id": 12434, "name": "Lisa", "department": "Cold Storage"},
#    {"id": 12483, "name": "Ryan", "department": "Inventory Mgmt"},
#    {"id": 12419, "name": "Gill", "department": "Cashier"}
# ]
#
# # Function to be passed to the map() function. Do not change this.
# def mod(employee_list):
#    temp = employee_list['name'] + "_" + employee_list["department"]
#    return temp


# map_list = map(mod,employee_list)
# for elem in map_list:
#    print(elem)
###########################################
# def to_mod_list(employee_list):
#    map_list = list(map(mod,employee_list))
#    return list(map_list)
#
# print(to_mod_list(employee_list))
#
# def generate_usernames(mod_list):
#    username = [x.replace(' ', '_') for x in mod_list]
#    return username
#
#
# def map_id_to_initial(employee_list):
#    id_name = {employer['name'][0]: employer['id'] for employer in employee_list}
#    return id_name
#
# print(map_id_to_initial(employee_list))

#
# class A:
#    def a(self):
#       return 'funct insd a'
#
#
# class B:
#    def a(self):
#       return 'funct insd b'
#
# class C:
#    pass
#
# class D(C,B,A):
#    pass
# d = D()
# print(d.a())


sample_dict = {1: 'Cofee', 2:'Tea', 3:'Mleko'}
for x in sample_dict:
   print(x)