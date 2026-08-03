# Vos règles de choix de mot de passe servent-elles à quelque chose ?

Autre projet tutoré de L3, sur l'entropie de Shannon appliquée aux mots de
passe. Rapport détaillé : `rapport_entropie.pdf`.

Point de départ : on nous impose partout des majuscules, chiffres, symboles
dans les mots de passe. Est-ce que ça sert vraiment à grand chose ? J'ai
voulu vérifier avec des calculs d'entropie plutôt qu'à l'instinct.

Il y a deux entropies à distinguer. La théorique, qui suppose un mot de
passe totalement aléatoire. Et la réelle, calculée à partir des caractères
effectivement utilisés. L'écart entre les deux est le truc intéressant :
`Bonjour!2025?` a l'air complexe mais son entropie réelle reste basse, parce
que la structure (mot + année + symbole classique) est prévisible pour un
logiciel de cassage. Un mot de passe complètement random comme
`fK9#pL2@xQ7!mT4$` colle presque au modèle théorique, lui.

Bilan un peu contre-intuitif : la longueur compte souvent plus que la
complexité visuelle.

```
python3 entropy_checker.py
```

Le script demande un mot de passe, affiche l'entropie théorique et réelle,
un temps de cassage estimé, et un niveau de robustesse.

Limite actuelle : le calcul se base seulement sur la distribution des
caractères du mot de passe testé, pas sur les fréquences réelles du
français ni sur des dictionnaires d'attaque. Un vrai outil comme zxcvbn
(Dropbox) va plus loin là-dessus.
