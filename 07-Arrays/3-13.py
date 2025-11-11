def occurs(number, array):
   x=0
   x= array.count(number)
   if x != 0:
      return (print('Its in the array'))
   else:
      return (print('Its not in the array'))
      



list= [15,38,7,23,14]
inx = int(input('Insert number'))
occurs(inx,list)