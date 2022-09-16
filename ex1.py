

def f1(x):
    resultat=0
    resultat=x+9
    return resultat 

         
         
c=0
e=0.000000001
a=0
b=0
a = int(input("Entrer la valeur de a: "))
b = int(input("Entrer la valeur de b: "))

while f1(a)*f1(b)>0 :
    print("Pas de solution dans cet interval")
    print("saisir a nouveau l'interval [a,b] a etudier : ")
    a = int(input("Entrer la valeur de a: "))
    b = int(input("Entrer la valeur de b: "))

c=(b-a)/2

while ((b-a)/2)>e :
    c=(b+a)/2
    if (f1(a)*f1(c)<0) :
        b=c
        
    else :
        a=c
    
    


print("c = ", c)

 


