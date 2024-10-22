PI = 3.14
E = 2.718

def carre(x):
  return x ** 2

def cube(x):
  return x ** 3

def factorielle(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorielle(n-1)

def valeur_absolue(x):
   return abs(x)

def maximum(liste):
   return max(liste)

def minimum(liste):
   return min(liste)

def moyenne(liste):
   long = len(liste)
   somme = sum(liste)
   return(somme / long)

def ecart_type(liste):
   moy = moyenne(liste)
   variance = sum((x - moy) ** 2 for x in liste) / len(liste)
   return variance ** 0.5

def mediane(liste):
   liste = sorted(liste)
   long = len(liste)
   if long % 2 == 0:
      return (liste[long // 2 - 1] + liste[(long // 2)]) / 2
   else:
      long = long - 1
      return list[(long // 2) + 1]

