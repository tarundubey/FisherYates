import random
class Shuffle:

    def __init__(self, inp_list,num_items):
        self.input_list = inp_list
        self.total_to_select =num_items

    def random_num_generator(self, limit):
            x = random.randint(0, limit-1)
            return x

    def fisher_yates(self):
        output_list = []
        len_of_input = len(self.input_list)
        range_to_select=self.total_to_select
        if range_to_select>len_of_input:
            range_to_select=len_of_input
        for i in range(range_to_select):
            index_to_select = self.random_num_generator(len_of_input-i)
            if self.input_list[index_to_select] not in output_list:
                 output_list.append(self.input_list[index_to_select])
            self.input_list[index_to_select],self.input_list[len_of_input-i-1] = self.input_list[len_of_input-i-1], self.input_list[index_to_select]
        print(output_list)

inp_arr = [int(x) for x in input().split()]
num_elements = int(input())
shuffle_obj = Shuffle(inp_arr, num_elements)
shuffle_obj.fisher_yates()

