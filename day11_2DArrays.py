arr = [
      [1, 1, 1, 0, 0, 0], 
      [0, 1, 0, 0, 0, 0], 
      [1, 1, 1, 0, 0, 0], 
      [0, 0, 2, 4, 4, 0], 
      [0, 0, 0, 2, 0, 0], 
      [0, 0, 1, 2, 4, 0]
      ]

count = 0
i = 0
j = 0


hourGlass_1 = arr[0][0] + arr[0][1] + arr[0][2] + arr[1][1] + arr[2][0] + arr[2][1] + arr[2][2]

print(hourGlass_1)

hourGlass_2 = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][j + 1] + arr[i +2][ j + 2]

print(hourGlass_2)

for i 