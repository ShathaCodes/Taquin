import math

class Jeu_Taquin:
    def __init__(self, etat,parent = None, depth = 0,n = 3,fval=0):
        self.etat = etat
        self.depth = depth
        self.parent = parent
        self.n = n
        self.fval = fval
        
def sous_noeuds(noeud):

    sous_noeuds_possibles = []
    sous_noeuds_possibles.append(Jeu_Taquin(etat=permuter(noeud.etat, 0, 1,noeud.n),parent=noeud, depth=noeud.depth + 1,n=noeud.n)) #haut
    sous_noeuds_possibles.append(Jeu_Taquin(etat=permuter(noeud.etat, 0, -1,noeud.n),parent=noeud, depth=noeud.depth + 1,n=noeud.n)) #bas
    sous_noeuds_possibles.append(Jeu_Taquin(etat=permuter(noeud.etat, -1, 0,noeud.n),parent=noeud, depth=noeud.depth + 1,n=noeud.n)) #gauche
    sous_noeuds_possibles.append(Jeu_Taquin(etat=permuter(noeud.etat, 1, 0,noeud.n),parent=noeud, depth=noeud.depth + 1,n=noeud.n)) #droite
    sous_noeuds = []
    for noeud in sous_noeuds_possibles:
        if (noeud.etat != None):
            sous_noeuds.append(noeud)
    return sous_noeuds

def permuter(etat, ei, ej, n): 
    nov_etat = etat.copy()

    index = nov_etat.index(0)
    index_a_permuter = index + ei*1 + ej*(-n)
    
    if index_a_permuter in range(0,n**2):
       temp = nov_etat[index] 
       nov_etat[index] = nov_etat[index_a_permuter] 
       nov_etat[index_a_permuter] = temp      
       return nov_etat
   
    return None

def afficher(noeud):  
    
    n = noeud.n
    for i in range(0,n**2,n):
        print('\t'.join(str(e) for e in noeud.etat[i:i+n]))
    print("            ")

def afficher_performance(etat_initial,noeud_final,nbre_noeuds_visités, start_time, end_time):     

    noeud = noeud_final
    chemin_solution = [noeud_final]
    while noeud.etat != etat_initial:
        noeud = noeud.parent
        chemin_solution.append(noeud)
        
    print("Le chemin de la solution est :")
    for noeud in reversed(chemin_solution):
        afficher(noeud)
    print("Nombre totale des noeuds visités: ", nbre_noeuds_visités)
    print("La profondeur de recherche ou on a trouvé la solution: ", noeud_final.depth)
    print("Time elapsed: " , (end_time - start_time)*(10**6), " ns")
    print("            ")