r = 3
c = 3
matrix = [[1, 2, 3], 
          [4, 5, 6],
          [7, 8, 9]]
prefix = [[0]*(r+1) for _ in range(c+1)]
for j in range(1,c+1):
   for k in range(1,r+1):
      prefix[k][j] = prefix[k-1][j] + prefix[k][j-1] - prefix[k-1][j-1] + matrix[k-1][j-1]

print(prefix)

[[0, 0, 0, 0], 
 [0, 1, 3, 6], 
 [0, 5, 12, 21], 
 [0, 12, 27, 45]]
row1 = 0
col1 = 1

row2 = 0
col2 = 2

total = prefix[row2+1][col2+1] - prefix[row1][col2+1] - prefix[row2+1][col1] + prefix[row1][col1]
print(total)

print(matrix[1][1],matrix[1][2],matrix[2][1],matrix[2][2])
print(prefix[row2+1][col2+1] , prefix[row1][col2+1] , prefix[row2+1][col1] , prefix[row1][col1])
# tamamı - üst - sol + kesişim


# k artarsa aşağı iniyom. k azalırsa yukarı çıkıyom. 
# j artarsa sağa gidiyom. j azalırsa sola gidiyom.