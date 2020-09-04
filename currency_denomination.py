till_amount = int(input("Amount required in till(In INR): "))

d={}
count=1

currency=[1,2,5,10,20,50,100,200,500,2000]

while count>0:
    tot=0
    n= int(input("\nHow many types of denomination do you want:"))
    m=n
    print("\nEnter the no. of notes with their denominations\n[FORMAT: 4 50 ...(4 notes of Rs.50)]")

    while n>0:
        try:
            a,b=input("-").split(" ")
            tot+=int(a)*int(b)
            if int(b) not in currency:
                print("Enter amount according to Indian currency:")
            else:
                d[int(b)]=int(a) 
                n-=1
                if n==0:
                    if tot!=till_amount:
                        print("The notes don't match up with the till amount")
                    else:
                        count=-1

        except:
            print("Please enter correct amount in the given format")

total_bill = int(input("\nBill amount:"))
amount_paid = int(input("\nAmount paid:"))

change = amount_paid - total_bill
denoms = sorted(list(d.keys()),reverse=True)

l=[]
n=1

for x in range(len(denoms)):
    n=1
    while n!=0:
        if d[denoms[x]]>0:
            if change>=denoms[x]:
                change-=denoms[x]
                l.append(denoms[x])
                d[denoms[x]]-=1
            else:
                n=0
        else:
            n=0
        if change==0:
            break

print("\nChange to be given: {}".format(amount_paid-total_bill))
s=sorted(set(l))
for x in s:
    if x<10:
        print(l.count(x),"coin(s) of",x,"i.e", l.count(x)*x)
    else:
        print(l.count(x),"note(s) of",x,"i.e", l.count(x)*x)

if change!=0:
    print("\nSorry, change {} is not present".format(change))




