# using return that means you are returning some value


def re():
    # return "I am returning some values and this is what i want"
    print("This is print")
    # noting implicity returns None


print(re())


def chai_status():
    return 200, 10

sold, remaining = chai_status()
print(f"Sold: {sold}")
print(f"Remaining: {remaining}")