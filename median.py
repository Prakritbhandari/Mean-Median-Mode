import csv

with open("heightweight.csv",newline = "") as f:
    reader = csv.reader(f) 
    file_data = list(reader)

file_data.pop(0)

new_data = []

for i in range(len(file_data)):
    n_num = file_data[i][2]
    new_data.append(float(n_num))

n = len(new_data)
new_data.sort()


if n%2 == 0:
    n1 = float(new_data[n//2])
    n2 = float(new_data[n//2-1])
    median = (n1+n2)/2
else:
    median = new_data[n//2]

print("mean/average is : "+str(median))