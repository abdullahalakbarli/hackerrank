name = input()
name_lst = name.split(' ')
rename = ''
for word in name_lst:
    word = word.capitalize()
    rename += word + ' '
print(name_lst)
print(rename)
