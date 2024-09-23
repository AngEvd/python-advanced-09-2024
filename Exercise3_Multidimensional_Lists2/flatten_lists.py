user_input = input().split("|")

sub_list = []

for sub_string in user_input[::-1]:
    sub_list.extend(sub_string.split())

print(*sub_list)
