# sorting in ascending order
letters = ['a', 'v', 'b', 'f', 'l', 'r']
letters.sort()
print(letters)


# sorting in descending order
letters = ['a', 'c', 'w', 'x', 'z']
letters.sort(reverse=True)
print(letters)

# matrix update

matrix = [
    [
        'a', 'b', 'c'
    ],
    [

        'f', 'g', 'h'
    ],
    [
        'd', 'e', 'f'
    ]
]

matrix.sort()
print(matrix)

matrix[1].sort()