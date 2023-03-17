#Pricopel Daria-Elena
#132
#AFD

with open("date.txt") as f:
    stari=int(f.readline().strip())
    starifin=[int(x) for x in f.readline().strip().split()]

    tranz={}
    for line in f:
        l=line.strip().split()
        initial=int(l[0])
        destinatie=int(l[1])
        cale=l[2]
        tranz[(initial,cale)]=destinatie

cuvant=input("Cuvantul: ")
drum=[0]
starecurenta=0
acc=True
for litera in cuvant:
    if (starecurenta, litera) in tranz:
        starecurenta=tranz[(starecurenta,litera)]
        drum.append(starecurenta)
    else:
        print("Neacceptat!")
        acc=False
        break;

if acc:
    if starecurenta in starifin:
        print("Acceptat!")
        print(drum)
    else:
        print("Neacceptat!")
