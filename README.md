# Comparaison méthodes numériques
## Objectif 
Représenter graphiquement le nombre d'itérations nécessaire à chaque méthode numérique (Dichotomie, sécante et Newton) pour faire une approximation de la racine d'une fonction dans un intervalle précis en fonction d'une précision donné afin de comparer la vitesse de convergence des trois méthodes. 
## Langage de programmation
Python
## Interface de programmation 
Spyder
## Bibliothèques utilisées 
#### Matplotlib
Pour illustrer graphiquement les fonctions 
#### Numpy 
Pour générer et manipuler les vecteurs et les fonctions mathématiques
## Hypothèses utilisées
Tout au long du projet, les fonctions utilisées respectent toutes les hypothèses citées ci-dessous. 
Considérons f la fonction utilisée.
### Méthode de dichotomie
f est continue sur un intervalle [a,b] de R et f(a)*f(b) < 0 donc par le théorème des valeurs intermédiaires, il existe x0 dans [a,b] tel que f(x0) = 0
### Méthode de newton
f est dérivable sur un intervalle [a,b] de R et la dérivée ne s'annule pas sur cet intervalle, c'est-à-dire que f est monotone sur cet intervalle. Aussi il existe un x0 dans [a,b] tel que f(x0) = 0
### Méthode de la sécante
c'est une variante de la méthode de newton ne nécessitant pas la connaissance de la dérivée. Donc f est continue sur [a,b] et (f(b) - f(a)) différent de zéro.

