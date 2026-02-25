s = "          luffy       is still joyboy   "
length = 0
result = 0
for char in s:
    if char != " ":
        length += 1
        if char == s[-1]:
            result = length
    elif (char == " ") :
        if length != 0:
            result = length
        length = 0
print(result)

print("*********************")

s=len(s.strip().split(" ")[-1])
print(s)

