def find(data: str, finding: str):
    data = str(data)
    lenght = 0
    findlen = 0
    
    while True:
        notfound = [False, lenght + 1]

        if lenght >= len(data):

            notfound[0] = True
        
        if notfound[0] != True:
            
            if data[lenght] == finding[findlen]:

                if len(finding) == (findlen + 1):

                    return [True, ((lenght - findlen) + 1)]
                else:

                    findlen += 1
                    lenght += 1

                #if notfound[0] == False:
                #
                #    notfound[0] = None
                #else:
                #
                #    notfound[0] = True
                notfound[0] = True
            
            else:

                lenght += 1
        
        else:

            return [False, None]

def findsym(data: str, symbol: str, *method: str):
    data = str(data)

    if method != ("before",) and method != ("after",) and method != ("hide",) and method != ("lenght",):

        method = "before"
    
    else:
        method = method[-1]
    
    lenght = 0

    while True:

        if len(data) <= lenght:
            return data
        
        if data[lenght] == symbol:

            if method == "before":

                return data[:lenght]
            
            elif method == "after":

                return data[(lenght + 1):]
            
            elif method == "hide":

                return data[:lenght] + data[(lenght + 1):]
            
            elif method == "lenght":

                return lenght + 1
            
            else:

                return f"Unknown method: {method}."
            
        else:

            lenght += 1

def doublefy(data: str, counts: int):
    
    if len(data) < 1:
        return ""
    
    ln = 0
    result = ""

    while True:
        if len(data) >= (ln + 1):
            result = result + (data[ln] * counts)
        
        else:
            return result
        
        ln += 1