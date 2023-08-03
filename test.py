import csv

possible_values = [-5, -4.5, -4, -3.5, -3, -2.5, -2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
running_totals = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

with open('OPA445_offset_voltage_dataset.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    # total = 0
    for row in csv_reader:
        for index, value in enumerate(possible_values):
            if float(row[0]) == value:
                running_totals[index-1] = running_totals[index-1] + 1
        # print(row[0])
        # print(type(row[0]))
        # total += float(row[0])
        # break
        
# print(total/1000000)
print(running_totals)