def freqQuery(queries):
    newdict={}
    freqdict={}
    for item in queries:
        if item[0] == 1:
            if item[1] in newdict:
                freq=newdict[item[1]]+1
                newdict[item[1]]=freq
                print("check freq in dict", freq,freqdict)
                if freq in freqdict:
                    freqdict[freq]=freqdict[freq]+1
                else:
                    freqdict[freq]=1
                #print(newdict, freqdict)
            else:
                newdict[item[1]]=1
                freqdict[1]=1
                print(newdict,freqdict)
        if item[0] == 2:
            pass
        print("print items",item,newdict, freqdict)
            # if item[1] in newdict:
            #     freq=newdict[item[1]]-1
            #     newdict[item[1]]=freq
            # value=newdict[item[1]]-1
            # newdict[item[1]]=value
            # if value in freqdict:
            #     freqdict[value]=freqdict[value]-1
            # else:
            #     freqdict[value]=0
        if item[0] == 3:
            pass

queries=[[1, 5], [1, 6], [3, 2], [1, 10], [1, 10], [1, 6], [2, 5], [3, 2]]
freqQuery(queries)