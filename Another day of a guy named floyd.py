print("==== Let's create a star pyramid ====")

rows = int(input("Enter num of rows."))

for i in range(rows):
    for j in range(i + 1):
        print("* ", end="")
    print()
    
print("=== THAT GUY'S TRIANGLE ===")

rows = int(input("Enter num of rows."))
number = 1

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(number, end="")
        
        number += 1
    print()
    
print("RHOMBUS")
row_size = int(input("Enter number of rows."))
if row_size % 2 == 0:
    half_rows =  row_size // 2
else:
    half_rows = row_size // 2 + 1
    
space = half_rows - 1

for i in range(1, half_rows+1):
    for j in range(1, space + 1):
        print(" ", end = "")
        
    space -= 1
    number = 1
    
    for j in range(2 * i - 1):
        print(number, end = "")
        number += 1
        
    print()
    
space = 1

for i in range(1, half_rows):
    for j in range(1, space+1):
        print(" ", end = "")
        
    space += 1
    number = 1
    
    for j in range(1, 2 * (half_rows - i)):
        print(number, end="")
        number += 1
    print()
    
print("Loop design")
print("You created a star, triangle, and diamond with nested loops.")