days = int(input("Enter the number of days : ")) * 3600 * 24
hours = int (input("Enter the number of hours : ")) * 3600
minutes = int(input("Enter the number of minutes : ")) * 60
seconds = int(input("Enter the number of seconds : "))

total = days + hours + minutes + seconds

print(f"Total number of seconds : {total}")