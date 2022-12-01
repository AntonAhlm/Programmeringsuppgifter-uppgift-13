print("\n a*x + b = c \n")

TalA=int(input("Tal A= "))
TalB=int(input("Tal B= "))
TalC=int(input("Tal C= "))

if TalA !=0 : 
    TalX=(TalC-TalB)/TalA
else:
    TalX=0

vl=TalA*TalX+TalB

print("\n",TalA,"*",TalX,"+",TalB,"=",TalC,"\n")

if vl!=TalC: 
    print("Ekvationen ",vl,"=",TalC,"Saknar Losning ")

if TalA*TalX==0 and TalB==TalC and TalX!=0:
    print("Ekvationen ",vl,"=",TalC,"Har Oandligt Manga Losnignar  ")

if TalA*TalX==0 and TalB==TalC:
    print("Ekvationen ",vl,"=",TalC,"Har 1 Losning ")

if TalA*TalX!=0 and vl==TalC:
    print("Ekvationen ",vl,"=",TalC,"Har 1 Losning ")

print("\n\n")

