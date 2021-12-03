
file_in = open('input.txt')
data = file_in.read().splitlines()
file_in.close


def line_scan(x, x_dict):
    for i in range(len(x)):
        x_dict[i] = x_dict[i] + int(x[i])
    return x_dict

bin_dict = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0}
    
gamma = ''
epsilon = ''

for i in range(len(data)):
    line_scan(data[i], bin_dict)

for key in bin_dict:
    if bin_dict[key] >= len(data) / 2:
        gamma += str(1)
        epsilon += str(0)
    else:
        gamma += str(0)
        epsilon += str(1)

    
print(int(gamma,2) * int(epsilon, 2))
oxy_data = data
co2_data = data


def find_most_common(index, data_list):
    zero = one = 0
    for i in data_list:
        if int(i[index]) == 0:
            zero += 1
        else:
            one += 1
    # print(zero)
    if one >= zero:
        return 1
    else:
        return 0


def find_least_common(index, data_list):
    zero = one = 0
    for i in data_list:
        if int(i[index]) == 0:
            zero += 1
        else:
            one += 1
    if one >= zero:
        return 0
    else:
        return 1


def remove_mismatch(reference, index, data_list):
    # print(len(data_list))
    if len(data_list) > 1:
        new_data_list = [i for i in data_list if int(i[index]) == reference]
        return new_data_list
    else:
        return data_list


for x in range(12):
    oxy_data = remove_mismatch(find_most_common(x, oxy_data), x, oxy_data)
    co2_data = remove_mismatch(find_least_common(x, co2_data), x, co2_data)
    # print("common : ")
    # print(find_most_common(x, oxy_data), find_least_common(x, co2_data))
    # print("new length")
    # print(len(oxy_data), len(co2_data))


print(int(co2_data[0], 2) * int(oxy_data[0], 2))