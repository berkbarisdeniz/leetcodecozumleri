class MyHashSet:

    def __init__(self):
        self.myHashSet = [False]*((10**6)+1)
        

    def add(self, key: int) -> None:
        if self.myHashSet[key] == False :
            self.myHashSet[key] = True
        

    def remove(self, key: int) -> None:
        if self.myHashSet[key] == True:
            self.myHashSet[key] = False

        

    def contains(self, key: int) -> bool:
        if self.myHashSet[key]: return True
        else:return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)