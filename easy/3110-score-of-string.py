s = "hello"
score = 0
for letter in range(len(s)-1):
    print(s[letter])
    sum=abs(ord(s[letter])-ord(s[letter+1]))
    print(sum)
    score += sum


        