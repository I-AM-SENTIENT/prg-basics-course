def read_from_file(name):
   with open(name) as file:
      content = file.read()
   return content



file_content = read_from_file('pets.txt')

file_lines = file_content.splitlines()
count = 0

for x in file_lines:
   words = x.split()
   for y in words:
      count +=1


print(count)