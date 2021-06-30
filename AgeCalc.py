#Simple program to calulate age

print ('Answer the questions to know how old you are.')
name = input('Name: ')
print ('What is your age?', (name), '?')
age = int(input('age: '))
# int means integer whole numbers -   1, 2, 3 or -1, -2, -3, etc.
days = age * 365
minutes = age * 525948
seconds = age * 31556926
print (name, 'has been alive for', (days), 'days', (minutes), 'minutes', (seconds),'seconds')
print ('Thank you for using my age calculating program',(name))