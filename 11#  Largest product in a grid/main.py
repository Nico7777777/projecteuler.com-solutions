
f = open("/home/nico/Programare/priority_queue/largest product in a grid/fis.in", 'r')
g = open("/home/nico/Programare/priority_queue/largest product in a grid/fis.out", 'w')
solution = 0

if __name__ == "__main__":
    mat = [[int(x) for x in line.split()] for line in f]
    # e ok

    #on calcule les produits de quatre numeros dans les lignes:
    # les elements dans le premier ligne:     
    # mat[0, 0] * mat[0, 1] * mat[0, 2] * mat[0, 3] = 08 * 02 * 22 * 97 = 34.144;      mat[0, 1] * mat[0, 2] * mat[0, 3] * mat[0, 4] = 02 * 22 * 97 * 38 = 162.184; ..... ;  mat[0, 16] * mat[0, 17] * mat[0, 18] * mat[0, 19] = 50 * 77 * 91 * 08 = 2.802.800   
    # 
    # les elements dans le deuxieme ligne:  
    # mat[1, 0] * mat[1, 1] * mat[1, 2] * mat[1, 3] = 49 * 49 * 31 * 73 = 5.433.463;    mat[1, 1] * mat[1, 2] * mat[1, 3] * mat[1, 4] = 04 * 56 * 62 * 00 = 0; ....... ;   mat[1, 16] * mat[1, 17] * mat[1, 18] * mat[1, 19] = 04 * 56 * 62 * 00 = 0
    # ....
    # ....
    #les elements dans le dernier ligne:
    # mat[19, 0] * mat[19, 1] * mat[19, 2] * mat[19, 3] = 01 * 70 * 54 * 71 = 268.380;  ........; mat[19, 16] * mat[19, 17] * mat[19, 18] * mat[19, 19] = 89 * 19 * 67 * 48 = 5.438.256;
    for ligne in range(20):
        for colonne in range(17):
            produit_actuel = mat[ligne][colonne]*mat[ligne][colonne+1]*mat[ligne][colonne+2]*mat[ligne][colonne+3]
            g.write(  str(mat[ligne][colonne]) + " * " + str(mat[ligne][colonne+1]) + " * " + str(mat[ligne][colonne+2]) + " * " + str(mat[ligne][colonne+3]) + " = " + str(produit_actuel) + "   -->solution=" + str(solution) + "\n"  )          
            if produit_actuel > solution:
                solution = produit_actuel
        g.write('\n')
    g.write("\n--------------------------------------------------------------------------------------------\n\n")
    
    
    #on calcule les produits de quatre numeros dans les colonnes:
    #les elements dans le premier colonne:
    # mat[0, 0] * mat[1, 0] * mat[2, 0] * mat[3, 0] = 08 * 49 * 81 * 52 = 1.651.104;  mat[1, 0] * mat[2, 0] * mat[3, 0] * mat[4, 0] = 49 * 81 * 52 * 22 = 4.540.536;  .........  ; mat[16, 0] * mat[17, 0] * mat[18, 0] * mat[19, 0] = 1.600;
    #
    #les elements dans le deuxieme colonne:
    # mat[0, 1] * mat[1, 1] * mat[2, 1] * mat[3, 1] = 02 * 49 * 49 * 70 = 336.140;  mat[1, 1] * mat[2, 1] * mat[3, 1] * mat[4, 1] = 5.210.170;  ..........  ; mat[16, 1] * mat[17, 1] * mat[18, 1] * mat[19, 1] = 14.808.780
    # ....
    # ....
    #les elements dans le dernier colonne:
    #mat[0, 19] * mat[1, 19] * mat[2, 19] * mat[3, 19] = 08 * 00 * 65 * 91 = 0;     mat[1, 19] * mat[2, 19] * mat[3, 19] * mat[4, 19] = 00 * 65 * 91 * 80 = 0; ....... ; mat[16, 19] * mat[17, 19] * mat[18, 19] * mat[19, 19] = 36 * 16 * 54 * 48 = 1.492.992
    for colonne in range(20):
        for ligne in range(17):
            produit_actuel = mat[ligne][colonne]*mat[ligne+1][colonne]*mat[ligne+2][colonne]*mat[ligne+3][colonne]
            g.write(  str(mat[ligne][colonne]) + " * " + str(mat[ligne+1][colonne]) + " * " + str(mat[ligne+2][colonne]) + " * " + str(mat[ligne+3][colonne]) + "=" + str(produit_actuel) + "  -->solution=" + str(solution) + "\n"  )
            if produit_actuel > solution:
                solution = produit_actuel
        g.write('\n')
    g.write("\n--------------------------------------------------------------------------------------------\n\n")
    
    
    #on calcule les diagonales principale(de haut a gauche en bas a droite):
    #
    for premier_ligne in range(17):
        for premier_colonne in range(16, -1, -1):
            produit_actuel = mat[premier_ligne][premier_colonne]*mat[premier_ligne+1][premier_colonne+1]*mat[premier_ligne+2][premier_colonne+2]*mat[premier_ligne+3][premier_colonne+3]
            g.write(  str(mat[premier_ligne][premier_colonne]) + " * " + str(mat[premier_ligne+1][premier_colonne+1]) + " * " + str(mat[premier_ligne+2][premier_colonne+2]) + " * " + str(mat[premier_ligne+3][premier_colonne+3]) + " = " + str(produit_actuel) + "  -->solution=" + str(solution) + '\n'  )     
            if produit_actuel > solution:
                solution = produit_actuel
        g.write('\n')
    g.write("\n---------------------------------------------------------------------------------------------\n\n")
    
    
    #on calcule les diagonales secundaires(de haut a droite en bas a gauche):
    for premier_ligne in range(17):
        for premier_colonne in range(17):
            produit_actuel = mat[premier_ligne][premier_colonne+3]*mat[premier_ligne+1][premier_colonne+2]*mat[premier_ligne+2][premier_colonne+1]*mat[premier_ligne+3][premier_colonne]
            g.write(  str(mat[premier_ligne][premier_colonne]) + " * " + str(mat[premier_ligne+1][premier_colonne+1]) + " * " + str(mat[premier_ligne+2][premier_colonne+2]) + " * " + str(mat[premier_ligne+3][premier_colonne+3]) + " = " + str(produit_actuel) + "  -->solution=" + str(solution) + '\n'  )
            if produit_actuel > solution:
                solution = produit_actuel
        g.write('\n')
    g.write( str(solution) )
