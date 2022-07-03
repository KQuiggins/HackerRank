T = int(input())
temp = []


for i in range(0, T):
    S = input()
    temp.append(S)

for i in range(len(temp)):
    even = []
    odd = []
    
    for j in range(len(temp[i])):
        if j % 2 == 0:
            even.append(temp[i][j])
        else:
            odd.append(temp[i][j])
    
        
    print(even[i])



