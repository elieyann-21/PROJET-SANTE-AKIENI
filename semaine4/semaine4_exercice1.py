# ============================================================
# AKIENI ACADEMY — Projet Sante Publique
# Semaine 4 — Exercice 1 : système de surveillance du Mpox
# ============================================================

# Données de surveillance épidémiologique
district_sanitaire = ['Mossaka-loukolela', 'Owando','Oyo-alima','Impfondo','Enyellé-bétou',
    'Gamboma', 'Lumumba','Mvou-mvou', 'Poto-poto']
Departement = ['Cuvette','Likouala', 'Plateaux', 'Pointe-Noire', 'Brazzaville']
total_rouge = 0
total_orange = 0
total_jaune = 0
total_vert = 0
total_confirme = 0
total_suspects = 0
total_deces = 0
total_actif = 0
# ==========================================================================
print('='*70)
print('Rapport de surveillance épidémiologique par district sanitaire - Mpox Congo')
for i in district_sanitaire:
    Nom_district = i
    print("-"*60)
    print('District sanitaire :',Nom_district)
    nb_suspects = int(input('Nombre de cas suspects :'))
    total_suspects = total_suspects + nb_suspects
    nb_confirmes = int(input('Nombre de cas confirmés :'))
    total_confirme = total_confirme + nb_confirmes
    nb_deces = int(input('Nombre de décès :'))
    total_deces = total_deces + nb_deces
    cas_actifs = nb_confirmes - nb_deces
    print('Nombre de cas actifs :', cas_actifs)
    taux_letalite = (nb_deces/nb_confirmes)*100
    print('Taux de létalité :', taux_letalite,'%')
    if nb_confirmes ==1:
        alerte = 'VERT'
        action = 'Surveillance standard'
        total_vert = total_vert + len(['VERT'])
        print(f"""Alerte : {alerte}
Action recommandée : {action}""")
    elif nb_confirmes >= 2 and nb_confirmes <=4:
        alerte = 'JAUNE'
        action = 'Renforcer la surveillance'
        total_jaune = total_jaune + len(['JAUNE'])
        print(f"""Alerte : {alerte}
Action recommandée : {action}""")
    elif nb_confirmes >= 5 and nb_confirmes <= 9:
        alerte = 'ORANGE'
        action = "Envoyer une équipe d'intervention"
        total_orange = total_orange + len(['ORANGE'])
        print(f"""Alerte : {alerte}
Action recommandée : {action}""")
    else:
        alerte = 'ROUGE'
        action = 'URGENCE - intervention immédiate'
        total_rouge = total_rouge + len(['ROUGE'])
        print(f"""Alerte : {alerte}
Action recommandée : {action}""")

print('='*70)
print('Rapport de surveillance épidémiologique nationale - Mpox Congo')
total_actif = total_confirme - total_deces
total_letalite = (total_deces/total_confirme)*100
print(f"""  Nombre de cas suspect : {total_suspects}
    Nombre de cas confirmés : {total_confirme}
    Nombre de décès : {total_deces}
    Nombre de cas actif : {total_actif}
    Taux de létalité national : {total_letalite}%
    Nombre d'alerte verte : {total_vert}
    Nombre d'alerte jaune : {total_jaune}
    Nombre d'alerte orange : {total_orange}
    Nombre d'alerte rouge : {total_rouge}""")
print('='*70)
