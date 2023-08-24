# # import random
# # # # with open('pet_names.txt', 'w') as choice_name:
# # #     # choice_name.writelines(['juli ',' pitty ', ' kumar ', ' garold '])
# # #
# # # file = open('pet_names.txt', 'r')
# # # choice_name = file.read()
# # # split_name_list = choice_name.split("  ")
# # # print(random.choice(split_name_list))
# #
# # def write_first_line_to_file(file_contents, output_filename):
# #     lines = file_contents.split('\n')
# #     first_lines = lines[0]
# #     with open(output_filename, 'w') as output_file:
# #         output_file.write(first_lines)
# #
# # def read_file_into_list(file_name):
# #     with open(file_name, 'r') as list_file:
# #         data = []
# #         # data = list_file.readlines()
# #         for x in list_file:
# #             if x % 2 == 0:
# #                 data.append(x.strip())
# #
# #         return data
# #
# # print(read_file_into_list("names.txt"))

# def read_file_in_reverse(file_name):
#     with open(file_name, 'r') as file:
#         contents = file.read()
#         spl_list = contents.split('\n')
#         new_list = []
#         for index, even in enumerate(spl_list):
#             if index % 2 == 0:
#                 new_list.append(even)
#     return new_list
# print(read_file_in_reverse('pet_names.txt'))
def read_file_in_reverse(file_name):
    with open(file_name, 'r') as file:
        contents = file.readlines()
        line_by_line = []
        for x in contents:
            line_by_line.append(x)
            line_by_line.reverse()

        # spl_list = contents.split('\n')
        # reverse_list = spl_list.copy()
        # reverse_list.reverse()
        return line_by_line
print(read_file_in_reverse('sampletext.txt'))