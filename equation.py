'''
Thomas Devlamminck + Dylan Mainghain
Recherche des racines d'une équation x^a + y^b = z^c
'''

solutions = 0
a = int(input("Entrez la valeur du coefficient a : "))
b = int(input("Entrez la valeur du coefficient b : "))
c = int(input("Entrez la valeur du coefficient c : "))
max = int(input("Entrez la valeur maximale pour x, y et z : "))


for x in range (1, max):
    for y in range (1, max):
        for z in range (1,max):
            if x**a + y**b == z**c:
                print("x=",x,"\t","y =",y,"\t","z =",z)
                solutions += 1


if solutions == 0:
    print("Aucune solution trouvee")
else:
    print(solutions, "solutions trouvees")
    
