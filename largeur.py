from collections import deque
from taquin import Jeu_Taquin,sous_noeuds,afficher


def largeur_dabord(etat_debut,n):
    etat_final = []
    for i in range(0,n*n):
        etat_final.append(i)
        
    etats_explores = []

    noeuds_à_explorer = deque([Jeu_Taquin(etat=etat_debut,n=n)]) 

    while noeuds_à_explorer:
        noeud = noeuds_à_explorer.popleft()

        etats_explores.append(noeud.etat)
        
        if noeud.etat == etat_final: 
            noeud_final = noeud
            return [etats_explores, noeud_final,noeuds_à_explorer]

        possibles = sous_noeuds(noeud)
        for pos in possibles:
            if (pos.etat not in etats_explores) and (pos not in noeuds_à_explorer):
                noeuds_à_explorer.append(pos)