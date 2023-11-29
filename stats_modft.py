import random

# Création d'une liste d'entiers aléatoires entre [a, b] et dont le nombre est aléatoire et appartient à [min, max]
def list_intRndCreate(a, b, min, max) :
  numbers=[]
  maxLen=random.randint(min, max)
  for i in range(0, maxLen) :
    numbers.append(random.randint(a, b))
  return numbers

# Fonction carré
def math_squarre(x) :
  return x**2

# Fonction cube
def math_cube(x) :
  return x**3

# Fonction valeur absolue
def math_abs(x) :
  if x < 0 :
    return -x
  return x

# Fonction factoriel
def math_factorial(x) :
  x=int(x)
  f = 1
  for i in range(2, x + 1) :
    f *= i
  return f

#### Mode d'une liste de nombres ####
# Classe value_count
class value_count :
    def __init__(self, value, count) :
      self.value = value
      self.count = count

    def increment(self) :
      self.count += 1

#  Fonction de tri
def value_count_sort(e) :
  return e.count

# Fonction list_mstOftValue
def list_mstOftValue(listA) :
  # Vérifie si la liste est vide
  if len(listA) == 0 :
    # Pas de valeur mode
    raise ValueError("Empty list.")

  ## Cherche la valeur mode
  # Trie la liste par ordre croissant
  listA.sort()
  values_counts = []
  currentValue = value_count(listA[0], 1)
  for i in range(1, len(listA)) :
    if currentValue.value != listA[i] :
      values_counts.append(currentValue)
      currentValue = value_count(listA[i], 1)
    else :
      currentValue.increment()
  values_counts.sort(reverse=True, key=value_count_sort)
  return values_counts[0]

# Fonction moyenne
def math_average(listA) :
  # Vérifie si la liste est vide
  if len(listA) == 0 :
    raise ValueError("Empty list.")

  # Calcule la moyenne
  sum=0
  n=len(listA)
  for i in range(0, n) :
    sum += listA[i]
  return sum/n

# Fonction minimum
def math_min(listA) :
  # Vérifie si la liste est vide
  if len(listA) == 0 :
    raise ValueError("Empty list.")

  # Cherche la valeur minimale
  listA.sort()
  return listA[0]

# Fonction maximum
def math_max(listA) :
  # Vérifie si la liste est vide
  if len(listA) == 0 :
    raise ValueError("Empty list.")

  # Cherche la valeur maximale
  listA.sort(reverse=True)
  return listA[0]
