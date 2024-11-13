def matchword(words):
    ctr=0
    lst=[]
    for word in words:
        if len(word)>1 and word[0]==word[-1]:
            ctr +=1
            lst.append(word)
    print("list of words with first and last character same. ")
    return ctr
count=matchword(['aba','cfc','xyz','jkj','1221'])
print("number of words having first and last charecter same.: ",count)