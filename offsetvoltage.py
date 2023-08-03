import numpy as np

n = 100000 # specify number of elements
filename = "OPA445_offset_voltage_dataset.csv"

with open(filename, 'w') as csvfile:
    for i in range(n):
        random_number = np.random.normal(0, 1*(5/3))
        rounded_random_number = round(random_number * 2) / 2
        csvfile.write(str(rounded_random_number))
        csvfile.write(",\n")
        # print(random_number)
    