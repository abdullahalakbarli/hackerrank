def decimaltohexadecimal(n): 
    table = {'0': 0, '1': 1, '2': 2, '3': 3,  
         '4': 4, '5': 5, '6': 6, '7': 7, 
         '8': 8, '9': 9, 'A': 10, 'B': 11,  
         'C': 12, 'D': 13, 'E': 14, 'F': 15} 
  
    hexadecimal = str(n)
    res = 0
    size = len(hexadecimal) - 1
    for num in hexadecimal: 
        res = res + table[num]*16**size 
        size = size - 1
    return res 
n=input()
print(decimaltohexadecimal(n))
