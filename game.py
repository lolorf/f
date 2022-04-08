import numpy as np

predict_number = np.random.randint(1, 101)
findnumber = 50
min_numb = 0
max_numb = 100
count = 1
i = 0
while findnumber != predict_number:
    if predict_number > findnumber:
        min_numb = findnumber
    else:
        max_numb = findnumber
    if i == 0:
        findnumber = (max_numb + min_numb) // 2 + 1
        i = 1
    else:
        findnumber = (max_numb + min_numb) // 2
        i = 0
    count += 1

print(count)