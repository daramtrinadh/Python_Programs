input_tuples = eval(input())
output = []

for i in range(len(input_tuples)):
    for j in range(i + 1, len(input_tuples)):
        if input_tuples[i][0] == input_tuples[j][0]:
            output.append(tuple(input_tuples[i] + input_tuples[j][1:]))

print(output)