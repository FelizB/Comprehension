# square numbers
# numbers= [1,1,2,5,8,13,21,34,35]
# squared_numbers=[item**2 for item in numbers]
# print(squared_numbers)

# even numbers
# numbers= [1,1,2,5,8,13,21,34,35]
# squared_numbers=[item for item in numbers if item % 2 == 0]
# print(squared_numbers)
import pandas
file1 = []
file2 = []
with open("file1.txt") as file:
    for items in file:
        new= items.strip("\n")
        file1.append(new)
with open("file2.txt") as file:
    for items in file:
        new= items.strip("\n")
        file2.append(new)

result = [int(items) for items in file1 if items in file2]
print(result)
