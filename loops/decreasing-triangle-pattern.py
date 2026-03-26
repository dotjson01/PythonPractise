'''

* * * *
* * *
* *
*

'''

# code 1
n=5
for rows in range(n):
    for col in range(rows, n):
        print('*',  end=" ")
    print()


print("------------------------------------Difference--------------------------------------")



# code 2
n=6
for rows in range(n):
    for col in range(rows, n-1):
        print('*', end=" ")
    print()


print('---------------------------------Another way to understand-------------------------------')

n = 5 
for row in range(n):
    print(row)
    print(n)
    for col in range(row,n):
        print("*",end=" ")
    print()