###
# Prints employees employed in a specified position.
#

# Employee List
file_name = 'it_company.txt'

# Position
job_title = 'Software Engineer'

with open('it_company.csv','r') as file:
   for line in file:
      if job_title in line:
         line_split = line.split(',')
         print(line_split[0], line_split[1])