# train info system for railway station 
# input : "sl" "ac" "first class"
# sl -> 1000,  ac -> 2000, first class -> 3000
# match using match case
# invalid -> "unknown class"

train_class = input("Enter the train class -> Sleeper, AC, First Class" "\n").lower()
match train_class:
    case "sl" | "sleeper" : print(f"Cost for sl is 1000")
    case "ac" | "acclass" : print(f"Cost for ac is 2000")
    case "first class" | "firstclass" : print(f"Cost for first class is 3000")
    case _ : print(f"Invalid train class")
