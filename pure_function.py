my_list = [1,2,3,4,5]

def add_to_list(lst,item):
    nl = lst.copy()
    nl.append(item)
    return nl

new_list = add_to_list(my_list,9)
print(new_list)
print(my_list)