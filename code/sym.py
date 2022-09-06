import utilities
class Sym:
    
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

