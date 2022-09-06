
class Sym:

    n=0
    _has={}
    def __init__(self,c,s):
        
        self.at=c
        self.name=s

    def add(v):
        if v != '?':
            self.n=self.n+1
            self._has[v]=1+(self.has[v] or 0)

    def fun(p):
        return p*math.log(p,2)
        

    def div():
        e=0
        for _,n in self._has:
            if n>0:
                e=e-fun(n/self.n)
            return e



    def findMode():
        mode = ""
        maxCount = 0
        dictionary = {"word": 1}
        for key in dictionary:
            if (dictionary[key] > maxCount): 
                maxCount = dictionary[key]
                mode = key
        
        return(dictionary[key], mode)

    print(findMode())




