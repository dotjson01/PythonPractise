def chai_flavor(flavor="Masala"):
    """
    This function prepares chai of given flavor
    If no flavor is given, it prepares Masala chai
    """
    return f"Preparing {flavor} chai"

print(chai_flavor())
print(chai_flavor("Ginger"))
print(chai_flavor.__doc__)
print(chai_flavor.__name__)


name = "Hello"
number = 1
num

print(type(name))
print(type(number))

print(len(name))
# print(len(number)) it will generate error
print(name.upper())
print(number.bit_length())
