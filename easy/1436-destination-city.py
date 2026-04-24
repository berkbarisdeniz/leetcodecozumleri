class Solution:
   def destCity(self, paths: list[list[str]]) -> str:
        hashmap =  {}
        for path in paths:
            hashmap[path[0]] = path[1]
        start = next(iter(hashmap))
        for i in range(len(hashmap)):
            stop = hashmap[start]
            if stop in hashmap:
                 start = stop
            else:
                 return stop