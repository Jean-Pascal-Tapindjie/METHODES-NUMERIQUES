# Comparaison méthodes numériques (en cours d'édition)

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
f est continue sur un intervalle [a,b] de R et f(a) * f(b) < 0 donc par le théorème des valeurs intermédiaires, il existe x* dans [a,b] tel que f(x*) = 0
### Méthode de newton
f est dérivable sur un intervalle [a,b] de R et la dérivée ne s'annule pas sur cet intervalle, c'est-à-dire que f est monotone sur cet intervalle. Aussi il existe un x* dans [a,b] tel que f(x*) = 0
### Méthode de la sécante
c'est une variante de la méthode de newton ne nécessitant pas la connaissance de la dérivée. Donc f est continue sur [a,b] et (f(b) - f(a)) différent de zéro.

## Fonctions utilisées 
Pour ce projet, j'ai utilisé 04 fonctions donc certaines ont été proposées dans l'exercice de groupe. Parmi ces fonctions, nous avons f1(x) = 3cos(x) - 2log(x+1) -1 avec x > -1; f2(x) = 9x - 3/2; f3(x) = (5x - 2)^3; f4(x) = (2x - 1)^5  pour tout x dans R, et toutes ces fonctions vérifient toutes les hypothèses énumérées ci-dessus avec pour dérivées respectives df1(x) = -3sin(x) - 2/(1+x); df2(x) = 9; df3(x) = 15(5x-2)^2; df4(x) = 10(2x-1)^4
### Illustration graphique
<img width="1710" height="880" alt="Figure 2026-10-31 230925 (0)" src="https://github.com/user-attachments/assets/bc250c73-d62c-47a3-ac83-f6b0307a66e9" />

## Méthodes numériques
### Méthode de dichotomie
#### Principe
soit f une fonction vérifiant les hypothèses ci-dessus. la méthode de dichotomie consiste à diviser l'intervalle [a,b] en deux sous-intervalles de longueur égale et on sélectionne parmi eux celui où se trouve de manière certaine une racine de f, puis on répète de manière itérative cet opération jusqu'à obtenir un intervalle jugé suffisamment petit.  
#### dichoto(f, a:float, b:float, k:int, nbetap = 10000)
la fonction dichoto() prend en argument une fonction f vérifiant les hypothèses ci-dessus, deux réels a, b, un entier k pour la précision et un nombre d'itérations maximales ici fixé à 10000. Elle renvoie une erreur si les conditions **a < b ou f(a) * f(b) < 0** ne sont pas vérifiées ou si la méthode ne converge pas après 10000 itérations et dans le cas contraire, renvoie un couple constitué d'un réel x* qui est l'approximation d'une racine de la fonction f tel que **|f(x *)| < 10^(-k)**; et d'un entier i représentant le nombre d'itérations nécessaire pour atteindre cette précision (10^(-k)).

### Méthode de newton
#### Principe
soit f une fonction vérifiant les hypothèses ci-dessus. Partant d’un point initial x(0) connu dans un voisinage suffisamment petit de la racine x* de la fonction f, on construit itérativement une suite de points x(k) qui convergera vers le point x* recherché. On approche à chaque itération k la courbe de la fonction par sa tangente en x(k). Le point x(k+1) est alors l’intersection de la tangente au point x(k) avec l’axe des abscisses. on a donc **x(k+1) = x(k) - f(x(k))/df(x(k))** pour tout k >= 0 et c'est bien définie sur [a,b]  car df ne s'annule pas par hypothèse. 
#### newton(f, df, b:float, k:int, nbetap = 10000)
Elle prend en argument une fonction f vérifiant les hypothèses ci-dessus avec sa dérivée df, un réel b qui représente x(0), un entier k pour la précision et le nombre d'itérations maximales fixé à 10000. Elle renvoie une erreur si pour tout x, df(x) = 0 ou si la méthode ne converge pas après 10000 et dans le cas contraire renvoie un couple constitué d'un réel x* qui est l'approximation d'une racine de la fonction f tel que **|f(x *)| < 10^(-k)**; et d'un entier i représentant le nombre d'itérations nécessaire pour atteindre cette précision (10^(-k)).

### Méthode de la sécante
#### Principe 
soit f une fonction vérifiant les hypothèses ci-dessus. La méthode de la sécante est une variante géométrique de la méthode de newton et ne nécessite pas de calcul de la dérivée. Elle utilise les deux derniers points calculés pour déterminer le point suivant. À l’itération k, la droite sécante passe par les points **M(k−1) = (x(k−1),f(x(k−1))) et M(k) = (x(k),f(x(k)))**. Le nouveau point x(k+1) est l’intersection de cette droite avec l’axe des abscisses. on a donc **x(k + 1) = x(k) - f(x(k)) * ((x(k) - x(k-1)) / (f(x(k))-f(x(k-1))))** pour tout k >= 1 et x(0) et x(1) connus. 
#### secante(f, a:float, b:float, k:int, nbetap = 10000)
Elle prend en argument une fonction f vérifiant les hypothèses ci-dessus, deux réels a, b tels que a = x(0) et b = x(1), un entier k pour la ^précision et un nombre d'itérations maximales fixé à 10000. Elle renvoie une erreur si f(a) - f(b) = 0 ou si la méthode ne converge pas après 10000 itérations. Sinon elle renvoie un couple constitué d'un réel x* qui est l'approximation d'une racine de la fonction f tel que **|f(x *)| < 10^(-k)**; et d'un entier i représentant le nombre d'itérations nécessaire pour atteindre cette précision (10^(-k)).

## Principe de comparaison 


