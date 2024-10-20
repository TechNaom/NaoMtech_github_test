number = int(input())
strings = []
for i in range(number):
    strings.append(input())

for word in strings:
    is_digit = 0
    is_special = 0
    is_upper = 0

    uid = list(''.join(word))
    uid2 = set(uid)

    for ch in uid:
        if ch.isupper():
            is_upper += 1
        if ch.isdigit():
            is_digit += 1
        if not ch.isalnum():
            is_special += 1
    if len(uid) == 10 and len(uid) == len(uid2) and  is_upper >= 2 and   is_digit >= 3 and  is_special == 0:
        print("valid")
    else:
        print("invalid")