VISION DE L'AVENIR DU PROJET

# Jonatan C. #
## interface ##
pour évité le goulot d'étranglement qu'est le développement d'interface avec tkinter-TIX,
j'aurais tendance a privilégier l'utilisation d'une autre librairie, les choix sont large,
voici les principale que je considèrerai (c'est aussi les plus grosse librairie graphique
utilisable dans plusieurs langage,) :
  * directement en python (par contre je ne les est jamais utilisé en python)
    * wxpython
    * pyQt (déjà utilisé Qt dont est dérivé pyQt en c++)
  * en java
    * swing

si l'on doit prendre en considération les outils disponible au cégep, le plus simple reste
probablement d'utiliser java swing, sinon reste a voir de quoi on l'aire wxPython et pyQt en python
et s'il est possible de les intégré dans notre environnement du cégep par nous même (donc sans
demandé leur ajout au département)

### direction: librairie différent ###
le fais de changé de librairie demande de refaire complètement les interface déjà fais,
ceux-ci demandant déjà un refactoring assé profond et le travaille serai accéléré par la suite en
utilisant une librairie "complète". je considéré donc qu'il serai avantageux de changé de librairie
graphique.

swing
+est déjà connue et 'maitrisé' par chacun de nous
+présent au cégep
+le développement est assé rapide
+oblige a bien séparé vue/modele
-le model évènementiel n'est (a mon avis) pas des meilleur ni des plus logique qui soit
-oblige a utilisé un langage différent pour l'interface que pour le reste de l'aplication

wxpython & pyQt
+grande libraire très utilisé
+grande source d'information pour appendre a l'utilisé
+utilisable directement en python
-inconnue par nous (surtout en python) donc temps d'apprentissage plus élevé
-non présent au cégep donc on doit voir si l'inclusion est possible

### direction: tkinter-TIX ###
le projet est déjà partie sur la base de ces librairie, elle sont présente dans une installation
de base de python par contre puisque l'on a appris beaucoup sur ceux-ci durant le développement du
projet il y a beaucoup de chose a refactoré (liste non exhaustive):
  * faire UN widget qui représente nos différente liste et dictionnaire
    * sa nous permet de faire évolué le widget sans devoir refaire le code partout dans le projet
  * refaire la mainWindows avec le notebook widget (je ne suis as 100% certain du nom, mais c un
widget d'onglet) de TIX
    * sa nous permet de simplifié énormément la main windows
  * niformisation des différente vue
  * etc.

et il y a encore quelque vue a ajouté avec les modules qui le sont autant ainsi que des modification
au vue existante (surtout les denieres qui on été fais assé rapidement)

## modele serveur ##
j'hésite a le gardé coté serveur, étant donné qu'il est difficile d'héberger un serveur python autrement
que chez nous et que la plupart d'entre nous n'avons pas de serveur **stable** autant a la maison
(je croi qu'il n'y a que frank qui a une connexion permettant d'en avoir un) et un serveur dédier a un
prix exorbitant pour une utilisation de ce type. je n'est pas trouvé d'hébergeur gratuit ou a _tres_
peu de frais offrant la possibilité de faire tourné un serveur en python, quelque un par contre permette
d'avoir un fichier python qui agisse comme un fichier php et peu donc répondre a des requêtes, mais on
devrait donc changé de protocole pour utilisé le http (je crois que c'est le seul disponible dans une
installation de cette sorte, a vérifier) et revoir comment on gère les connexion puisque le serveur
ne fonctionnerai pas en permanence mais seulement lorsqu'il reçoit une requête (peut-être que sa ne change
rien dans notre cas.) encore une fois par contre il faudrait exploré la possibilité et voir si c'est
réellement faisable sans créé trop de problème.

une dernière possibilité, mais qui demanderai probablement trop en réécriture et en apprentissage serais
de refaire le serveur complètement en php, mais rendu la aussi bien faire l'interface sous forme de site web
par contre je ne crois pas que se soit vraiment envisageable pour le moment. reste a voir si l'on pouvais utilisé
le modèle serveur (surtout la bdd) en python peut-être que sa pourrais être possible étant donné que le coté client
doit pratiquement tout est refait (la partie connexion réseau n'étant plus important si l'on prend cette direction)
par contre coté désavantage, l'application ne peu pas être utilisable offline, et il faut revoir la conception visuel
d'un bout a l'autre.

## modèle client ##
un refactoring du 'Projet' est nécessaire pour utiliser le pickle unpickle plutot que le serialise unserialise
de plus j'aimerai que l'on ajoute la possibilité de :
  * sortir des rapports (histoire de pouvoir remettre directement sans devoir tout recopié)
  * d'avoir des aide a la gestion du projet
  * graphique d'évolution du projet, des objectif a atteindre (gant)
  * tout autre chose qui puisse être utile