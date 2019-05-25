import difflib
from time import time
start = time()

listofmatches = []
matchesdic={}
sorted_rates=[]

#####search in sequence lists######

def seqsearch(alist,item):
    for i in range(len(alist)):
        s=difflib.SequenceMatcher(isjunk=None,a=alist[i],b=item)
        rate = s.ratio()*100
        if rate > 75:
            listofmatches.append(alist[i])
    return listofmatches

### saving dictionary as list of word ###
dictionary = open("dictionary.txt","r")
string = dictionary.read()
fulldic = list (string.split("\n"))
dictionary.close()

###splitin the dictionary########

ion=[]
ure=[]
ou=[]
gh=[]
re=[]
ing=[]
ed=[]
ent=[]
er=[]
ve=[]
ly=[]
ect=[]
ous=[]
o_r=[]
un=[]
eh=[]
ness=[]
al=[]
able=[]
tor=[]
cal=[]
qu=[]

for i in range (len(fulldic)):
    if 'ion' in fulldic[i]:
       ion.append(fulldic[i])
    if 'ure' in fulldic[i]:
        ure.append(fulldic[i])
    if 'ou' in fulldic[i]:
        ou.append(fulldic[i])
    if 'gh' in fulldic[i]:
        gh.append(fulldic[i])
    if 're' in fulldic[i]:
        re.append(fulldic[i])
    if 'ing' in fulldic[i]:
        ing.append(fulldic[i])
    if 'ed' in fulldic[i]:
        ed.append(fulldic[i])
    if 'ent' in fulldic[i]:
        ent.append(fulldic[i])
    if 'er' in fulldic[i]:
        er.append(fulldic[i])
    if 've' in fulldic[i]:
        ve.append(fulldic[i])
    if 'ly' in fulldic[i]:
        ly.append(fulldic[i])
    if 'ect' in fulldic[i]:
        ect.append(fulldic[i])
    if 'ent' in fulldic[i]:
        ent.append(fulldic[i])
    if 'ous' in fulldic[i]:
        ous.append(fulldic[i])
    if 'or' in fulldic[i]:
        o_r.append(fulldic[i])
    if 'un' in fulldic[i]:
        un.append(fulldic[i])
    if 'eh' in fulldic[i]:
       eh.append(fulldic[i])
    if 'ness' in fulldic[i]:
       ness.append(fulldic[i])
    if 'al' in fulldic[i]:
        al.append(fulldic[i])
    if 'able' in fulldic[i]:
        able.append(fulldic[i])
    if 'tor' in fulldic[i]:
        tor.append(fulldic[i])
    if 'cal' in fulldic[i]:
        cal.append(fulldic[i])
    if 'qu' in fulldic[i]:
        qu.append(fulldic[i])

##########binary Search#########
def search(L,word):
    if len(L)==0:
        return False
    else:
        mid = len(L)//2
        if L[mid] == word:
            return True
        else:
            if word > L[mid]:
                return search(L[mid+1:],word)
            else:
                return search(L[:mid],word)

#########matcher search#########
def msearch(item):
    if "ion" in item:
        return seqsearch(ion,item)
    elif "ure" in item:
        return seqsearch(ure,item)
    elif "ou" in item:
        return seqsearch(ou,item)
    elif "gh" in item:
        return seqsearch(gh,item)
    elif "re" in item:
        return seqsearch(re,item)
    elif "ing" in item:
        return seqsearch(ing,item)
    elif "ed" in item:
        return seqsearch(ed,item)
    elif "ent" in item:
        return seqsearch(ent,item)
    elif "er" in item:
        return seqsearch(er,item)
    elif "ve" in item:
        return seqsearch(ve,item)
    elif "ly" in item:
        return seqsearch(ly,item)
    elif "ect" in item:
        return seqsearch(ect,item)
    elif "ous" in item:
        return seqsearch(ous,item)
    elif "or" in item:
        return seqsearch(o_r,item)
    elif "un" in item:
        return seqsearch(un,item)
    elif "eh" in item:
        return seqsearch(eh,item)
    elif "ness" in item:
        return seqsearch(ness,item)
    elif "al" in item:
        return seqsearch(al,item)
    elif "able" in item:
        return seqsearch(able,item)
    elif "tor" in item:
        return seqsearch(tor,item)
    elif "cal" in item:
        return seqsearch(cal,item)
    elif "qu" in item:
        return seqsearch(qu,item)
    else:
        return seqsearch(fulldic,item)

##getting the text form the user#
x=input("please enter your string here : \n ")
par=x.lower()
lofpar=list(par.split( ))
### searching###
for i in range(len(lofpar)):
    if search(fulldic,lofpar[i]):
        print (lofpar[i]+" IS CORRECT")
    else:
        listofmatches = []
        print (lofpar[i]+" PREDECTION IS :".upper())
        print (msearch(lofpar[i]))
end=time()
print (end-start)
