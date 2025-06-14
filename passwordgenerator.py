print("1st project")
input_list = []
for i in range(1, 4):
    input_list.append(int(input()))
max=0
for i in range(len(input_list)-1):
    if input_list[i] > max:
        max = input_list[i]

print("The maximum number is:", max)