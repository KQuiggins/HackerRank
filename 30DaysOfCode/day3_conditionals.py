""" If is odd, print Weird
If is even and in the inclusive range of 2 to 5, print 'Not Weird'
If is even and in the inclusive range of 6 to 20, print 'Weird'
If is even and greater than 20, print 'Not Weird' """

# N = 3
N = 24

if N % 2 != 0:
    print('Weird')
elif N % 2 == 0 and N in range(2, 6):
        print("Not Weird")
elif N % 2 == 0 and N in range(6, 21):
        print("Weird")
elif N % 2 == 0 and N > 20:
        print("Not Weird")
