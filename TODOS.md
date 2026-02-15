# ConvexHulls

## TODOs

Nadine : 
- [ ] datasets : dans le rapport, expliquer comment on a généré le dataset C, en particulier pourquoi le rayon est la racine carrée d'une uniforme sur [0, 1]
- [x] visualisation des résultats : pour l'algo de sweeping, générer une vidéo qui montre toutes les étapes de la construction  de l'algorithme (à chaque étape, générer un plot avec les points déjà choisis)
- [ ] complexité du sweeping algorithm, à mieux formaliser mais l'idée est là
- [x] modifier les datasets pour que ce soit [0, 1] et pas [-1, 1]
- [ ] autre algo

Elsa : 
- [x] fixer le pivot dans la fonction médiane
- [x] partie 4
- [x] graphiques de comparaison des performances (ajouter optionnellemnt gift_wraping et quick_hull)
- [x] rajouter la complexité théorique
- [x] graphique évolution appels récursifs en fonction du nombre de points
- [x] graphique du nombre de tour de boucles de find pour calculer la médiane (permet de justifier la complexité linéaire en moyenne)
Tu peux utiliser la fonction `visualize_hull` dans `utils.py` pour représenter le polygone et le dataset

- [ ] README

**Brainstorming d'idées en plus**
- changer le nom de output sensitive -> done
- gif pour kirkpatrick ?



## Rajout de ce qu'on avait discuté : 
- rapport : 
  - applications
  - d'autres algorithmes
  - complexités
  - généralisation 3D


## Complexité du sweeping : 
- sorting : $O(n \log(n))$
- maximum time that adding one point can take : 
  - assume that adding a point leads to removing all previous points, the worst time it could take is $O(n)$
- for the upper hull, a point can be removed only once
  - so the sweeping is linear, since a point can either be kept or removed
- the same reasoning says that computing the lower hull is done in linear time.
- So overall, the sweeping is linear. The most time-consuming part is the sorting.