import random
import pickle
#Declarattion des variables
Non_user=""
chwa_user=0
min=0
max=4
chans=0;nouvo_sko=0

def maj_verifikasyon(chaine):
    for i in chaine:
        if i.isupper():
            return True
    return False

def espas_verifikasyon(chain):
    if " " in chain:
        return True
    return False

nonb_machin=random.randint(min,max)

Non_user=input("Bienvini nan jwèt Lawoulèt la;SVP antre yon epsedo : ")

while maj_verifikasyon(Non_user) or espas_verifikasyon(Non_user):
    Non_user=input("antre yon epsedo ki san espas ni lèt minskil : ")
    
# ITILIZASYON pickle

non_fichye="database"
try:
    with open(non_fichye, "rb") as fichier:
        data=pickle.load(fichier)
except:
    data={}
with open(non_fichye, "wb") as fichier:
    pickle.dump(data, fichier)

if not Non_user in data:
    data[Non_user] =0
with open(non_fichye, "wb") as fichier:
    pickle.dump(data, fichier)
with open(non_fichye, "rb") as fichier:
        data=pickle.load(fichier)

print(data)
nouvo_sko=data[Non_user]

while True:
    chans=5
    score=0
    while chans >0:   
        try:
            chwa_user=int(input(f"{Non_user} antre yon nomb ant {min} ak {max} :"))
            if chwa_user >=min and chwa_user<=max:
                if chwa_user==nonb_machin:
                    a=chans-1
                    if a ==0:
                        score+=30
                    else:
                        score+=30*(a)
                    nouvo_sko+=score
                    print(f"Bravo {Non_user} !!! ou genyen pati a\n Ou gen  {score} pwen. Nouvo sko w se {nouvo_sko} pwen")
                    data[Non_user] += score
                    with open(non_fichye, "wb") as fichier:
                        pickle.dump(data, fichier)
                    break
                else:
                    chans-=1
                    
                    if chwa_user>nonb_machin:
                        print(f"ou pèdi !! {chwa_user} pi gro pase nomb kache a ou rete {chans} chans ou gn yon sko {score} pwen")
                    else:
                        print(f"ou pèdi !! {chwa_user} pi piti pase nomb kache a ou rete {chans} chans ou gn yon sko {score} pwen")
            
        except:
            print(f" {Non_user} sa ou antre a pa yon chif ")
    print(f"Nonb kache a se  {nonb_machin}")
    sortir=input("Peze k pou w kite jwèt la epi nenpot lot touch pou w kontinye jwet la " )
    if sortir.lower() =='k':
        break
