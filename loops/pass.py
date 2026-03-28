'''
we are using pass statement for now we are skipping this , later on can do something here , but now please pass , if i come later then i can here /
we are going to do here something

'''

names = ['john', 'rohan', 'mohan', ' ', 'kumar']
for name in names:
    if name == ' ':
        pass # handle empty value
    print(f'{name}')


'''
after a week i come here , and meet my team and ask them hey , here we have to do something i can see empty value in data and love to know how to handle it
'''

'now after 3 years'


names = ['john', 'rohan', 'mohan', ' ', 'kumar']
for name in names:
    if name == ' ':
        name = name.replace(' ', 'unknown value')
    print(f'{name}')
