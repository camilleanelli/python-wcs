def somme_cumulee(liste):
  i = 0
  for x in liste:
    while i < len(liste) - 1:
      liste[i + 1] = liste[i + 1] + liste[i]
      i += 1
  return liste

print(somme_cumulee([3, 3, 2, 5]))

def compter_occurrences(liste):
  dict_occ = {}
  for i in liste:
    value = liste.count(i)
    dict_occ[i] = value
  return dict_occ

print(compter_occurrences([3, 3, 3, 4]))

def inverser_dict(dictionnaire):
  new_dict = {}
  for key, value in dictionnaire.items():
    new_value = key
    new_key = value
    new_dict[new_key] = new_value
  return new_dict

print(inverser_dict({'a': 1, 'b': 2}))

def filtrer_pairs(liste):
  new_liste = []
  for i in liste:
    if i%2 == 0:
      new_liste.append(i)
  return new_liste

print(filtrer_pairs([1, 2, 3, 4]))

def celsius_to_fahrenheit(celsius):
  nbr = ''
  for x in celsius:
    if x.isdigit():
      nbr = nbr + x
  return str(round(int(nbr) * 9/5 + 32)) + "°F"

print(celsius_to_fahrenheit("0°C"))

def trouver_doublons(liste):
  new_list = []
  for i in liste:
    if liste.count(i) == 2 and i not in new_list:
      new_list.append(i)
  return new_list

print(trouver_doublons([1, 2, 2, 3, 3]))

def calculer_moyenne_ponderee(valeurs, poids):
  index_poids = 0
  prod_valeur_poids = 0
  for i in valeurs:
    prod_valeur_poids += i * poids[index_poids]
    index_poids += 1
  return round(prod_valeur_poids / sum(poids), 2)

print(calculer_moyenne_ponderee([3,5], [1,2]))
