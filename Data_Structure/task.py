# Task : store application log messages in a file

def write_log(message):
    with open(r"C:\Main\Python\app.log", "a") as file:
        r= file.write(message + "\n")
        return r

w=write_log("App Started")
print(w)