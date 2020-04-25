string_to_count = {}
text = input("pls enter the text:")
strings = text.split()
for string in strings:
    f = string_to_count.get(string, 0)
    string_to_count[string] = f + 1
strings = list(string_to_count.keys())
for string in strings:
    print("{} : {}".format(string, string_to_count[string]))
