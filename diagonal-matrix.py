matrix = []
m = int(input("Enter the number of rows or colums - "))
n = m
for i in range(m):
    temp = []
    for j in range(n):
        x = int(input(f"Enter the element [{i+1}][{j+1}] - "))
        temp.append(x)
    matrix.append(temp)
    
sum=0
for i in range(m):
    for j in range(n):
        if(i==j):
            sum+=matrix[i][j]
        if(i+j==len(matrix)-1):
            if(i!=j):
                sum+=matrix[i][j]
                
for i in matrix:
    print(i)                

# Repetation sum of middle element is restricted
print("sum is ",sum)
