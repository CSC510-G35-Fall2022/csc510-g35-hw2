import utilities
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


    #WORKING
    #finds mode of a column of data in the sym class
    def mid(data_):
        mode_dict= {}
        for i, key in enumerate(data_.keys()):
            data_list = data_[key]
            mode = max(set(data_list), key = data_list.count)
            mode_dict[key] = mode

        return mode_dict


utilobj=utilities.utilities()
data = utilobj.convert_data_list_to_dict(utilobj.get_sym_data())
print(Sym.mid(data))

