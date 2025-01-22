#For Loop Basic II
#01- Biggie Size
def biggie_size(num_list):
    for i in range(len(num_list)):
        if num_list[i] > 0: 
           num_list[i] = "big" 
    return num_list

print("#1 Biggie Size")
num_list = [-1, 3, 5, -5]
print(biggie_size(num_list))

#02- Count Positives
def count_positives(num_list):
    count = 0
    length = len(num_list)
    for i in range(len(num_list)):
        if num_list[i] > 0: 
           count += 1 
      
    num_list[length - 1] = count
    return num_list

print("\n#2 Count Positives")
num_list = [-1, 1, 1, 1]
print(count_positives(num_list))

num_list2 = [1, 6, -4, -2 , -7, -2]
print(count_positives(num_list2))

#03- Sum Total
def sum_total(num_list):
    sum = 0
    for i in range(len(num_list)):
        sum += num_list[i]
    return sum

print("\n#3 Sum Total")
num_list = [1, 2, 3, 4]
print(sum_total(num_list))

num_list = [6, 3, -2]
print(sum_total(num_list))

#04- Average
def average(num_list):
    sum = 0
    average = 0
    length = len(num_list)
    for i in range(len(num_list)):
        sum += num_list[i]
    
    average = sum / length
    return average

print("\n#4 Average")
num_list = [1, 2, 3, 4]
print(average(num_list))


#05- Length
def length(num_list):
    _length = 0
    for num in num_list:
        _length += 1
    return _length

print("\n#5 Length")
num_list = [37, 2, 1, -9]
print(length(num_list))

num_list = []
print(length(num_list))

#06- Minmum
def minmum(num_list):
    if len(num_list) == 0:
        return False
    else:
        _min = num_list[0]
        for item in num_list:
            if item <  _min:
              _min = item
        return _min

print("\n#06 Minmum")
num_list = [37, 2, 1, -9]
print(minmum(num_list))

num_list = []
print(minmum(num_list))

#07- Maximum
def maximum(num_list):
    if len(num_list) == 0:
        return False
    else:
        _max = num_list[0]
        for item in num_list:
            if item > _max:
              _max = item
        return _max

print("\n#7 Maximum")
num_list = [37, 2, 1, -9]
print(maximum(num_list))

num_list = []
print(maximum(num_list))


#08- Ultimate Analysis
def ultimate_analysis(num_list):
    ultimate_dict = {"sumTotal": 0, "avarage": 0, "minimum": 0, "maximum": 0, "length": 0}
    
    if not num_list:
        return ultimate_dict

    ultimate_dict["sumTotal"] = sum_total(num_list)
    ultimate_dict["avarage"] = average(num_list)
    ultimate_dict["minimum"] = maximum(num_list)
    ultimate_dict["maximum"] = minmum(num_list)
    ultimate_dict["length"] = length(num_list)
    return ultimate_dict


print("\n#08 Ultimate Analysis")
num_list = [37, 2, 1, -9]
print(ultimate_analysis(num_list))

num_list = []
print(ultimate_analysis(num_list))


#09- Reverse
def reverse(num_list):
    if not num_list:
        return num_list
    
    reverse_list = []
    for i in range(len(num_list), 0, -1):
        reverse_list.append(num_list[i - 1])
    return reverse_list


print("\n#09 Reverse")
num_list = [37, 2, 1, -9]
print(reverse(num_list))
