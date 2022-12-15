# %%
import csv

# %%
f = open("../Data/raw/Crime_Data_from_2020_to_Present_column_modified.csv", "r")
f_csv = csv.reader(f)
new_Info = []

for row in f_csv:
    Mocodes = row[10].split(" ")
    for i in range(0, len(Mocodes)):
        new_Info.append(row[0:10] + [Mocodes[i]] + row[11:])


f.close()
f = open("../Data/clean/Crime_Data_from_2020_to_Present_column_modified_zys1.csv", "w")
f_csv = csv.writer(f)
f_csv.writerows(new_Info)
f.close()





