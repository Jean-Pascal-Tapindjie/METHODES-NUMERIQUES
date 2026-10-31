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

## Fonctions utilisées 
Pour ce projet, j'ai utilisé 04 fonctions donc certaines ont été proposées dans l'exercice de groupe. Parmi ces fonctions, nous avons f1(x) = 3cos(x) - 2log(x+1) -1 avec x > -1; f2(x) = 9x - 3/2; f3(x) = (5x - 2)^3; f4(x) = (2x - 1)^5  pour tout x dans R, et toutes ces fonctions vérifient toutes les hypothèses énumérées ci-dessus avec pour dérivées respectives df1(x) = -3sin(x) - 2/(1+x); df2(x) = 9; df3(x) = 15(5x-2)^2; df4(x) = 10(2x-1)^4
### Illustration graphique
<img width="2710" height="1680" alt="Figure 2026-10-30 175124 (0)" src="https://github.com/user-attachments/assets/2c376113-c9b6-423e-8f62-b6bd26cba390" />

## Méthodes numériques

