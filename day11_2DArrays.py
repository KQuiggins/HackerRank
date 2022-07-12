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

def get_hourglass_sum(matrix, row, col):
      sum = 0
      sum += matrix[row - 1][col - 1] # get value top-left
      sum += matrix[row - 1][col]     # get value directly above
      sum += matrix[row - 1][col + 1] # get value top-right
      sum += matrix[row][col]         # element itself
      sum += matrix[row + 1][col -1]  # get value below to left
      sum += matrix[row + 1][col]     # get value directly below
      sum += matrix[row + 1][col + 1] # get value below to the right

      return sum

max_hourglass_sum = -63

for i in range(1,5):
      for j in range(1,5):
            current_hourglass_sum = get_hourglass_sum(arr, i, j)
            if current_hourglass_sum > max_hourglass_sum:
                  max_hourglass_sum = current_hourglass_sum

print(max_hourglass_sum)

