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


    def mid(data_):

        tmp_dict = {}
        for x in range(0, len(data_[0])):
            print(data_[0][x])
            tmp_dict[data_[0][x]] = []
        print(tmp_dict)
        
        data_list = []
        mode_list = []
        mode_list.append(data_[0])
        for i in range(1, len(data_)):
            for j in range (0, len(data_[i])):
                data_list.append(data_[i][j])

        mode = [(max(set(data_list), key = data_list.count))]
        mode_list.append(mode)
        return mode_list


utilobj=utilities.utilities()
data = utilobj.get_sym_data()
print(Sym.mid(data))

