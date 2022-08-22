def freqQuery(queries):
    newdict={}
    freqdict={}
    result=[]
    for item in queries:
        if item[0] == 1:
            if item[1] in newdict:
                old_freq=newdict[item[1]]
                current_freq=old_freq+1
                newdict[item[1]]=current_freq
                freqdict=find_freq(freqdict,current_freq,old_freq)
            else:
                old_freq=0
                current_freq=old_freq+1
                newdict[item[1]]=current_freq
                freqdict=find_freq(freqdict,current_freq,old_freq)
        if item[0] == 2:
            if item[1] in newdict:
                old_freq=newdict[item[1]]
                if old_freq>0:
                    current_freq=old_freq-1
                    newdict[item[1]]=current_freq
                    freqdict=find_freq(freqdict,current_freq,old_freq)
            else:
                pass
        if item[0] == 3:
            if item[1] in freqdict:
                result.append(1)
            else:
                result.append(0)
    return result

def find_freq(freqdict, current_freq,old_freq):
    if current_freq in freqdict:
        freqdict[current_freq]=freqdict[current_freq]+1
    else:
        freqdict[current_freq]=1
    if old_freq in freqdict:
        if freqdict[old_freq]>0:
            freqdict[old_freq]=freqdict[old_freq]-1
        else:
            freqdict[old_freq]=0
    return freqdict
queries=[[1,1],[2,2],[3,2],[1,1],[1,1],[2,1],[3,2]]
#queries=[[1, 5], [1, 6], [3, 2], [1, 10], [1, 10], [1, 6], [2, 5], [3, 2]]
print(freqQuery(queries))