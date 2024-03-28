
str_val = "GeeksForGeeks"
new_arr_str = []
stack = list(str_val)

for i in range(0, len(str_val)):
    new_arr_str.append(stack[len(stack) - 1])
    stack.pop()

new_str = "".join(new_arr_str)
print(new_str)
