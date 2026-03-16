#  removing spaces 
name = " Max ".strip()
# print(len(name))
name.lstrip()
print(len(name))
# print(removing)
# print(name.lstrip())
# print((len(name)))

txt = " Engineering".lstrip()
print(txt)

text = "Engineering ".rstrip()
print(text)

text2 = " Engineering ".strip()
print(text2)

text3 = "Data Engineering".strip()
print(text3)
# doesn't remove space from the middle


text = "Enginnering"
print(len(text))
print(len(text.strip()))

nr_of_spaces = len(text) -  len(text.strip())
is_clean = len(text) == len(text.strip())
print(f"No of Spaces: {nr_of_spaces}")
print(f"Is Clean {is_clean}")

