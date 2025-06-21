def groupAnagrams(strs):
  hashmap={}
  for letter in strs:
    sortedstr="".join(sorted(letter))
    if sortedstr in hashmap:
      hashmap[sortedstr].append(letter)
    else:
      hashmap[sortedstr]=[letter]
  return list(hashmap.values())