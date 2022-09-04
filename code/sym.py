
class Sym:
    
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




