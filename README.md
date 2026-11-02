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
f est continue sur un intervalle [a,b] de R et **f(a) * f(b) < 0** donc par le théorème des valeurs intermédiaires, il existe x* dans [a,b] tel que f(x*) = 0
### Méthode de newton
f est dérivable sur un intervalle [a,b] de R et la dérivée ne s'annule pas sur cet intervalle, c'est-à-dire que f est monotone sur cet intervalle. Aussi il existe un x* dans [a,b] tel que f(x*) = 0
### Méthode de la sécante
c'est une variante de la méthode de newton ne nécessitant pas la connaissance de la dérivée. Donc f est continue sur [a,b] et **(f(b) - f(a))** différent de zéro.

## Fonctions utilisées 
Pour ce projet, j'ai utilisé 04 fonctions donc certaines ont été proposées dans l'exercice de groupe. Parmi ces fonctions, nous avons f1(x) = 3cos(x) - 2log(x+1) -1 avec x > -1; f2(x) = 9x - 3/2; f3(x) = (5x - 2)^3; f4(x) = (2x - 1)^5  pour tout x dans R, et toutes ces fonctions vérifient toutes les hypothèses énumérées ci-dessus avec pour dérivées respectives df1(x) = -3sin(x) - 2/(1+x); df2(x) = 9; df3(x) = 15(5x-2)^2; df4(x) = 10(2x-1)^4
### Illustration graphique
<img width="1710" height="880" alt="Figure 2026-10-31 230925 (0)" src="https://github.com/user-attachments/assets/bc250c73-d62c-47a3-ac83-f6b0307a66e9" />

## Méthodes numériques
### Méthode de dichotomie
#### Principe
soit f une fonction vérifiant les hypothèses ci-dessus. la méthode de dichotomie consiste à diviser l'intervalle [a,b] en deux sous-intervalles de longueur égale et on sélectionne parmi eux celui où se trouve de manière certaine une racine de f, puis on répète de manière itérative cet opération jusqu'à obtenir un intervalle jugé suffisamment petit.  
#### Dichoto(f, a:float, b:float, k:int, nbetap = 10000)
la fonction dichoto() prend en argument une fonction f vérifiant les hypothèses ci-dessus, deux réels a, b, un entier k pour la précision et un nombre d'itérations maximales ici fixé à 10000. Elle renvoie une erreur si les conditions **a < b ou f(a) * f(b) < 0** ne sont pas vérifiées ou si la méthode ne converge pas après 10000 itérations et dans le cas contraire, renvoie un couple constitué d'un réel x* qui est l'approximation d'une racine de la fonction f tel que **|f(x *)| < 10^(-k)**; et d'un entier i représentant le nombre d'itérations nécessaire pour atteindre cette précision (10^(-k)).

### Méthode de newton
#### Principe
soit f une fonction vérifiant les hypothèses ci-dessus. Partant d’un point initial x(0) connu dans un voisinage suffisamment petit de la racine x* de la fonction f, on construit itérativement une suite de points x(k) qui convergera vers le point x* recherché. On approche à chaque itération k la courbe de la fonction par sa tangente en x(k). Le point x(k+1) est alors l’intersection de la tangente au point x(k) avec l’axe des abscisses. on a donc **x(k+1) = x(k) - f(x(k)) / df(x(k))** pour tout k >= 0 et c'est bien définie sur [a,b]  car df ne s'annule pas par hypothèse. 
#### Newton(f, df, b:float, k:int, nbetap = 10000)
Elle prend en argument une fonction f vérifiant les hypothèses ci-dessus avec sa dérivée df, un réel b qui représente x(0), un entier k pour la précision et le nombre d'itérations maximales fixé à 10000. Elle renvoie une erreur si pour tout x, df(x) = 0 ou si la méthode ne converge pas après 10000 et dans le cas contraire renvoie un couple constitué d'un réel x* qui est l'approximation d'une racine de la fonction f tel que **|f(x *)| < 10^(-k)**; et d'un entier i représentant le nombre d'itérations nécessaire pour atteindre cette précision (10^(-k)).

### Méthode de la sécante
#### Principe 
soit f une fonction vérifiant les hypothèses ci-dessus. La méthode de la sécante est une variante géométrique de la méthode de newton et ne nécessite pas de calcul de la dérivée. Elle utilise les deux derniers points calculés pour déterminer le point suivant. À l’itération k, la droite sécante passe par les points **M(k−1) = (x(k−1),f(x(k−1))) et M(k) = (x(k),f(x(k)))**. Le nouveau point x(k+1) est l’intersection de cette droite avec l’axe des abscisses. on a donc **x(k + 1) = x(k) - f(x(k)) * ((x(k) - x(k-1)) / (f(x(k))-f(x(k-1))))** pour tout k >= 1 et x(0) et x(1) connus. 
#### Secante(f, a:float, b:float, k:int, nbetap = 10000)
Elle prend en argument une fonction f vérifiant les hypothèses ci-dessus, deux réels a, b tels que a = x(0) et b = x(1), un entier k pour la ^précision et un nombre d'itérations maximales fixé à 10000. Elle renvoie une erreur si **f(a) - f(b) = 0** ou si la méthode ne converge pas après 10000 itérations. Sinon elle renvoie un couple constitué d'un réel x* qui est l'approximation d'une racine de la fonction f tel que **|f(x *)| < 10^(-k)**; et d'un entier i représentant le nombre d'itérations nécessaire pour atteindre cette précision (10^(-k)).

## Principe de comparaison 
Toutes les fonctions dichoto(), newton() ou secante(), ont comme argument une précision k et retournent une approximation de la racine de la fonction tel que **|f(x * )| < 10^(-k)** et le nombre d'itérations nécessaires pour atteindre cet précision. Ici, pour chacune des quatre fonctions f1, f2, f3 et f4 citées ci-dessus, nous allons tracer des graphes représentant le nombre d'itérations nécessaire pour atteindre la précision de 10^(-k) en fonction de k avec k = {1,2,3,4,5,6}
### Données 
J'ai exécuté les fonctions dichoto(), newton() ou secante() avec chacune des quatre fonctions f1, f2, f3 et f4 citées ci-dessus et avec la précision k allant de 1 à 6. j'ai récupéré le nombre d'itérations pour chaque méthode et avant de présenter le graphe je vais présenter ces données numériques sous formes de tableau
#### Méthode de dichotomie 
| Fonction | k = 1 | k = 2 | k = 3 | k = 4 | k = 5 | k = 6 |                 
|:--------:|------:|------:|------:|------:|------:|------:|
| f1       | 1     | 1     | 10    | 10    | 14    | 19    |
| f2       | 3     | 7     | 11    | 14    | 16    | 21    |
| f3       | 1     | 2     | 3     | 5     | 6     | 7     |
| f4       | 0     | 0     | 0     | 0     | 3     | 3     |
#### Méthode de newton
| Fonction | k = 1 | k = 2 | k = 3 | k = 4 | k = 5 | k = 6 |
|:--------:|------:|------:|------:|------:|------:|------:|
| f1       | 1     | 2     | 2     | 2     | 3     | 3     |
| f2       | 1     | 1     | 1     | 1     | 1     | 1     |
| f3       | 5     | 7     | 9     | 11    | 13    | 15    |
| f4       | 3     | 5     | 7     | 9     | 11    | 13    |
#### Méthode de  la sécante
| Fonction | k = 1 | k = 2 | k = 3 | k = 4 | k = 5 | k = 6 |
|:--------:|------:|------:|------:|------:|------:|------:|
| f1       | 2     | 2     | 3     | 3     | 4     | 4     |
| f2       | 1     | 1     | 1     | 1     | 1     | 1     |
| f3       | 5     | 7     | 10    | 13    | 15    | 18    |
| f4       | 1     | 1     | 4     | 7     | 10    | 13    |

### Illustration graphique
<p align = "center"> <img width="435" height="282" alt="Figure 2026-11-02 200822 (1)" src="https://github.com/user-attachments/assets/fdbd3dad-46be-4a42-8e26-6559b96035fe" />
<img width="345" height="282" alt="Figure 2026-11-02 200822 (2)" src="https://github.com/user-attachments/assets/2fb3431b-166c-4877-9b53-a33870e7a9a4" /> </p> 

<p align = "center"><img width="352" height="285" alt="Figure 2026-11-02 200822 (3)" src="https://github.com/user-attachments/assets/71f81fe7-769f-4648-9783-3867d3fc1e19" />
<img width="352" height="285" alt="Figure 2026-11-02 200822 (4)" src="https://github.com/user-attachments/assets/b660ffd5-bb4e-4ab4-a947-b7ad79955e25" /> </p> 

## Analyse et interprétation
### Méthode de dichotomie
#### Observation
- Pour f1, le nombre d'itérations augmente de 1 à 19 lorsque la précision augmente de 10^(-1) à 10^(-6).
- Pour f2, il passe de 3 à 21 itérations.
- Pour f3, il augmente progressivement de 1 à 7 itérations.
- Pour f4, aucune itération n'est effectuée pour les premières précisions, puis le nombre d'itérations atteint 3.
#### Interprétation :
La dichotomie présente une convergence régulière : plus la précision demandée est élevée, plus le nombre d'itérations nécessaires augmente. Cette méthode possède l'avantage d'être robuste, à condition que la fonction respecte les hypothèses énumérées ci-dessus. En revanche, sa convergence est relativement lente comparée aux méthodes utilisant davantage d'informations sur la fonction, notamment sa dérivée.

### Méthode de Newton
#### Observation
- Pour f1, le nombre d'itérations reste relativement faible, entre 1 et 3.
- Pour f2, une seule itération suffit quelle que soit la précision demandée.
- Pour f3, le nombre d'itérations augmente de 5 à 15.
- Pour f4, il passe de 3 à 13.
#### Interprétation :
Les résultats montrent que la méthode de Newton peut être particulièrement rapide pour certaines fonctions, notamment f1 et f2. Cependant, son comportement dépend fortement de la nature de la racine. En particulier, f3 et f4 possèdent des racines multiples (respectivement d'ordre 3 et 5). Dans ce cas, la convergence quadratique habituelle de Newton n'est plus obtenue : la convergence devient généralement linéaire. Cela explique pourquoi le nombre d'itérations augmente davantage pour ces deux fonctions lorsque la précision demandée devient plus élevée. La méthode nécessite également le calcul de la dérivée et un choix judicieux du point initial.

### Méthode de la sécante
#### Observation
- Pour f1, le nombre d'itérations reste relativement faible et passe de 2 à 4.
- Pour f2, une seule itération suffit pour toutes les précisions.
- Pour f3, le nombre d'itérations augmente de 5 à 18.
- Pour f4, il passe de 1 à 13.
#### Interprétation :
La méthode de la sécante présente de bonnes performances pour certaines fonctions, notamment f1 et f2. Pour f3 et f4, on observe une augmentation plus importante du nombre d'itérations. Cela peut notamment s'expliquer par la présence de racines multiples, qui dégrade le comportement de convergence habituel de cette méthode. La méthode de la sécante présente l'avantage de ne pas nécessiter le calcul de la dérivée. Cependant, elle nécessite deux approximations initiales et peut être sensible à leur choix.

## Analyse comparative des trois méthodes 
Pour cette partie j'ai décidé de représenter cela sous forme de tableau.
| Critères | Dichotomie | Newton | Sécante |
|:---|:---:|:---:|:---:|
| Utilise la dérivée | Non | Oui | Non |
| Approximations initiales | Un intervalle | Un point | Deux points |
| Convergence habituelle | Linéaire | Quadratique | Superlinéaire |
| Robustesse | Élevée sous conditions | Dépend du point initial | Dépend des points initiaux |
| Coût par itération | Faible | Calcul de la dérivée | Calcul de deux fonctions |
#### Interprétation générale
Les résultats numériques mettent en évidence des différences de comportement entre les trois méthodes. 

La méthode de dichotomie présente une convergence linéaire et relativement régulière. Elle constitue une méthode fiable lorsque les conditions d'encadrement sont satisfaites. 

La méthode de Newton peut atteindre rapidement la précision souhaitée, notamment lorsque la racine est simple et que le point initial est suffisamment proche de celle-ci. Elle présente généralement une convergence quadratique dans ces conditions.

La méthode de la sécante constitue une alternative intéressante à Newton puisqu'elle ne nécessite pas le calcul de la dérivée. Pour une racine simple, elle possède généralement une convergence superlinéaire, mais reste sensible au choix des approximations initiales.

Enfin, les fonctions f3 et f4 mettent en évidence l'influence de la multiplicité des racines sur la convergence des méthodes numériques.

## Conclusion
Ce travail a permis d'étudier et de comparer trois méthodes numériques de recherche des zéros d'une fonction : la dichotomie, la méthode de Newton et la méthode de la sécante. L'étude des résultats numériques et des représentations graphiques montre que les performances de ces méthodes dépendent à la fois de la fonction étudiée, de la précision recherchée et des conditions initiales. La dichotomie se distingue par sa robustesse et la régularité de sa convergence, mais nécessite généralement davantage d'itérations. La méthode de Newton peut être particulièrement rapide grâce à sa convergence quadratique dans le cas d'une racine simple, mais son efficacité dépend du choix du point initial et de la dérivée de la fonction. La méthode de la sécante constitue un compromis intéressant puisqu'elle ne nécessite pas le calcul de la dérivée, tout en présentant une convergence généralement plus rapide que celle de la dichotomie pour une racine simple. L'étude des fonctions possédant des racines multiples a également permis de mettre en évidence une dégradation de la vitesse de convergence, notamment pour les méthodes de Newton et de la sécante. Ainsi, aucune méthode ne présente un avantage absolu dans toutes les situations. Le choix d'une méthode numérique doit dépendre des propriétés de la fonction étudiée, de la précision souhaitée et des informations disponibles.
