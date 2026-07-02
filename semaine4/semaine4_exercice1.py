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
    nb_confirmes = int(input('Nombre de cas confirmés :'))
    nb_deces = int(input('Nombre de décès :'))
    cas_actifs = nb_confirmes - nb_deces
    print('Nombre de cas actifs :', cas_actifs)
    taux_letalite = (nb_deces/nb_confirmes)*100
    print('Taux de létalité :', taux_letalite,'%')
    if nb_confirmes ==1:
        alerte = 'VERT'
        action = 'Surveillance standard'
        print(f"""Alerte : {alerte}
Action recommandée : {action}""")
    elif nb_confirmes >= 2 and nb_confirmes <=4:
        alerte = 'JAUNE'
        action = 'Renforcer la surveillance'
        print(f"""Alerte : {alerte}
Action recommandée : {action}""")
    elif nb_confirmes >= 5 and nb_confirmes <= 9:
        alerte = 'ORANGE'
        action = "Envoyer une équipe d'intervention"
        print(f"""Alerte : {alerte}
Action recommandée : {action}""")
    else:
        alerte = 'ROUGE'
        action = 'URGENCE - intervention immédiate'
        print(f"""Alerte : {alerte}
Action recommandée : {action}""")

print('='*70)
print('Rapport de surveillance épidémiologique nationale - Mpox Congo')
total_suspects = sum(nb_suspects[i])
total_confirme = sum(nb_confirmes[i])
total_deces = sum(nb_deces[i])
total_actif = sum(cas_actifs[i])
total_letalite = (total_deces/total_actif)*100
total_vert = sum(alerte=='VERT')
total_jaune = sum(alerte=='JAUNE')
total_orange = sum(alerte=='ORANGE')
total_rouge = sum(alerte=='ROUGE')
print(f""" Nombre de cas suspect : {total_suspects}
    Nombre de cas confirmés : {total_confirme}
    Nombre de décès : {total_deces}
    Nombre de cas actif : {total_actif}
    Taux de létalité national : {total_letalite}%
    Nombre d'alerte verte : {total_vert}
    Nombre d'alerte jaune : {total_jaune}
    Nombre d'alerte orange : {total_orange}
    Nombre d'alerte rouge : {total_rouge}""")
print('='*70)