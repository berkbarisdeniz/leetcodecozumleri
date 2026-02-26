words = ["mass","as","hero","superhero","baris","bar","ba","deniz","niz","k"]

words = sorted(words, key=len)
print(words)

results = []


for i,word in enumerate(words):
    for m in range(i+1,len(words)):
        if word in words[m]:
            results.append(word)
            break
print(results)