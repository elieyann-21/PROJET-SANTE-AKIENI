# ============================================================
# AKIENI ACADEMY — Projet Sante Publique
# Semaine 3 — Exercice 1 : Classification Stocks Medicaments
# ============================================================
# --- DONNEES S2 : Variables medicaments --
# Médicament 1
m1_nom            = 'Artemether-Lumefantrine'
m1_stock          = 3200
m1_seuil_rupture  = 2000
m1_cout_unitaire  = 3500.0   # FCFA

# Médicament 2
m2_nom            = 'Amoxicilline 500mg'
m2_stock          = 950
m2_seuil_rupture  = 800
m2_cout_unitaire  = 850.0

# Médicament 3
m3_nom            = 'Paracetamol 500mg'
m3_stock          = 12400
m3_seuil_rupture  = 3000
m3_cout_unitaire  = 120.0

#Médicament 4
m4_nom            = 'SRO (sachets)'
m4_stock          = 4200
m4_seuil_rupture  = 5000
m4_cout_unitaire  = 125.0

# Médicament 5
m5_nom            = 'Vaccin DTP-HepB-Hib'
m5_stock          = 820
m5_seuil_rupture  = 1000
m5_cout_unitaire  = 8500.0

# Classification médicament
# Médicament 1
if m1_stock <= m1_seuil_rupture:
    m1_statut  = 'RUPTURE CRITIQUE'
    m1_couleur = '[ROUGE]'
    m1_action  = 'Alerte immediate PNA — commande express sous 24h'
elif m1_stock <= m1_seuil_rupture * 1.5:
    m1_statut  = 'ALERTE STOCK'
    m1_couleur = '[ORANGE]'
    m1_action  = 'Commande urgente a declencher sous 72h'
elif m1_stock <= m1_seuil_rupture * 2.0:
    m1_statut  = 'STOCK LIMITE'
    m1_couleur = '[Jaune]'
    m1_action  = 'Surveillance renforcee — planifier commande'
else:
    m1_statut  = 'STOCK NORMAL'
    m1_couleur = '[VERT]'
    m1_action  = 'Situation normale — suivi standard'

# Médicament 2
if m2_stock <= m2_seuil_rupture:
    m2_statut  = 'RUPTURE CRITIQUE'
    m2_couleur = '[ROUGE]'
    m2_action  = 'Alerte immediate PNA — commande express sous 24h'
elif m2_stock <= m2_seuil_rupture * 1.5:
    m2_statut  = 'ALERTE STOCK'
    m2_couleur = '[ORANGE]'
    m2_action  = 'Commande urgente a declencher sous 72h'
elif m2_stock <= m2_seuil_rupture * 2.0:
    m2_statut  = 'STOCK LIMITE'
    m2_couleur = '[Jaune]'
    m2_action  = 'Surveillance renforcee — planifier commande'
else:
    m2_statut  = 'STOCK NORMAL'
    m2_couleur = '[VERT]'
    m2_action  = 'Situation normale — suivi standard'

# Médicaments 3
if m3_stock <= m3_seuil_rupture:
    m3_statut  = 'RUPTURE CRITIQUE'
    m3_couleur = '[ROUGE]'
    m3_action  = 'Alerte immediate PNA — commande express sous 24h'
elif m3_stock <= m3_seuil_rupture * 1.5:
    m3_statut  = 'ALERTE STOCK'
    m3_couleur = '[ORANGE]'
    m3_action  = 'Commande urgente a declencher sous 72h'
elif m3_stock <= m3_seuil_rupture * 2.0:
    m3_statut  = 'STOCK LIMITE'
    m3_couleur = '[Jaune]'
    m3_action  = 'Surveillance renforcee — planifier commande'
else:
    m3_statut  = 'STOCK NORMAL'
    m3_couleur = '[VERT]'
    m3_action  = 'Situation normale — suivi standard'

# Médicament 4
if m4_stock <= m4_seuil_rupture:
    m4_statut  = 'RUPTURE CRITIQUE'
    m4_couleur = '[ROUGE]'
    m4_action  = 'Alerte immediate PNA — commande express sous 24h'
elif m4_stock <= m4_seuil_rupture * 1.5:
    m4_statut  = 'ALERTE STOCK'
    m4_couleur = '[ORANGE]'
    m4_action  = 'Commande urgente a declencher sous 72h'
elif m4_stock <= m4_seuil_rupture * 2.0:
    m4_statut  = 'STOCK LIMITE'
    m4_couleur = '[Jaune]'
    m4_action  = 'Surveillance renforcee — planifier commande'
else:
    m4_statut  = 'STOCK NORMAL'
    m4_couleur = '[VERT]'
    m4_action  = 'Situation normale — suivi standard'

# Médicament 5
if m5_stock <= m5_seuil_rupture:
    m5_statut  = 'RUPTURE CRITIQUE'
    m5_couleur = '[ROUGE]'
    m5_action  = 'Alerte immediate PNA — commande express sous 24h'
elif m5_stock <= m5_seuil_rupture * 1.5:
    m5_statut  = 'ALERTE STOCK'
    m5_couleur = '[ORANGE]'
    m5_action  = 'Commande urgente a declencher sous 72h'
elif m5_stock <= m5_seuil_rupture * 2.0:
    m5_statut  = 'STOCK LIMITE'
    m5_couleur = '[Jaune]'
    m5_action  = 'Surveillance renforcee — planifier commande'
else:
    m5_statut  = 'STOCK NORMAL'
    m5_couleur = '[VERT]'
    m5_action  = 'Situation normale — suivi standard'


# Comptage des alertes
nb_ruptures_critiques = 0 
if m1_statut == 'RUPTURE CRITIQUE': nb_ruptures_critiques = nb_ruptures_critiques + 1
if m2_statut == 'RUPTURE CRITIQUE': nb_ruptures_critiques = nb_ruptures_critiques + 1
if m3_statut == 'RUPTURE CRITIQUE': nb_ruptures_critiques = nb_ruptures_critiques + 1
if m4_statut == 'RUPTURE CRITIQUE': nb_ruptures_critiques = nb_ruptures_critiques + 1
if m5_statut == 'RUPTURE CRITIQUE': nb_ruptures_critiques = nb_ruptures_critiques + 1

nb_alertes_stock = 0
if m1_statut == 'ALERTE STOCK': nb_alertes_stock = nb_alertes_stock + 1
if m2_statut == 'ALERTE STOCK': nb_alertes_stock = nb_alertes_stock + 1
if m3_statut == 'ALERTE STOCK': nb_alertes_stock = nb_alertes_stock + 1
if m4_statut == 'ALERTE STOCK': nb_alertes_stock = nb_alertes_stock + 1
if m5_statut == 'ALERTE STOCK': nb_alertes_stock = nb_alertes_stock + 1

nb_stock_limite = 0
if m1_statut == 'STOCK LIMITE': nb_stock_limite = nb_stock_limite + 1
if m2_statut == 'STOCK LIMITE': nb_stock_limite = nb_stock_limite + 1
if m3_statut == 'STOCK LIMITE': nb_stock_limite = nb_stock_limite + 1
if m4_statut == 'STOCK LIMITE': nb_stock_limite = nb_stock_limite + 1
if m5_statut == 'STOCK LIMITE': nb_stock_limite = nb_stock_limite + 1

nb_stock_normal = 0
if m1_statut == 'STOCK NORMAL': nb_stock_normal = nb_stock_normal + 1
if m2_statut == 'STOCK NORMAL': nb_stock_normal = nb_stock_normal + 1
if m3_statut == 'STOCK NORMAL': nb_stock_normal = nb_stock_normal + 1
if m4_statut == 'STOCK NORMAL': nb_stock_normal = nb_stock_normal + 1
if m5_statut == 'STOCK NORMAL': nb_stock_normal = nb_stock_normal + 1


# Méssage d'alerte
message_alerte = f""" Attention : 
- {nb_ruptures_critiques} médicaments en rupture critique !
- {nb_alertes_stock} médicaments en alerte de stock !
- {nb_stock_limite} médicaments en limite de stock !
Transmettre immédiatement le message au Dr MOUKALA """


# Rapport
print("=="*70)
print('  RAPPORT DE STOCK — PHARMACIE NATIONALE D APPROVISIONNEMENT')
print('  Date : 25 juin 2026')
print('='*70)
print("Niveau de stock de chaque médicament")
print(f""" {m1_couleur} {m1_nom}
    Stock : {m1_stock} unités | Seuil : {m1_seuil_rupture}
    Statut : {m1_statut}
    Action : {m1_action}""")
print("-"*70)
print(f""" {m2_couleur} {m2_nom}
    Stock : {m2_stock} unités | Seuil : {m2_seuil_rupture}
    Statut : {m2_statut}
    Action : {m2_action}""")
print("-"*70)
print(f""" {m3_couleur} {m3_nom}
    Stock : {m3_stock} unités | Seuil : {m3_seuil_rupture}
    Statut : {m3_statut}
    Action : {m3_action}""")
print("-"*70)
print(f""" {m4_couleur} {m4_nom}
    Stock : {m4_stock} unités | Seuil : {m4_seuil_rupture}
    Statut : {m4_statut}
    Action : {m4_action}""")
print("-"*70)
print(f""" {m5_couleur} {m1_nom}
    Stock : {m5_stock} unités | Seuil : {m5_seuil_rupture}
    Statut : {m5_statut}
    Action : {m5_action}""")
print("="*70)
print("Bilan du stock - PNA CONGO")
print(f"""
    Ruptures critiques : {nb_ruptures_critiques}
    Alertes de stocks : {nb_alertes_stock}
    Limite de stock : {nb_stock_limite}
    Stocks normaux : {nb_stock_normal}""")
print("="*70)
print(message_alerte)
print("="*70)