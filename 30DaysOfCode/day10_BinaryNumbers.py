""" Given a base-10 integer,n , convert it to binary (base-2). Then find and print the base-10 integer denoting the maximum number of consecutive 1's in n's binary representation. When working with different bases, it is common to show the base as a subscript.  """

n = 125
# temp = []

binary = format(n, 'b')
con_ones = binary.split('0')
print(con_ones)
print(len(max(con_ones)))


    