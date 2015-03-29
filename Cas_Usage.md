# Cas d'usage et scénario d'utilisation #
## Etape 1 (base+analyse) ##

  * Ouvrir un projet
    1. Demander la liste des projets
    1. Afficher la liste des projets
    1. Sélectionner le projet
    1. Attendre une action  de utilisateur

  * Ouvrir le programme
    1. Démarrer l'interface et le modèle côté client

  * Créer un projet
    1. Demander un nom de projet
    1. Vérifier que ce nom n'existe pas
    1. Le sauvegarder

  * Sauvegarder le projet
    1. Envoyer les données au serveur puis les sauvegarder dans la BD

  * Remplir un champ
    1. Copier le mot sélectionné par l'utilisateur
    1. Ajouter le mot à la liste correspondante

## Etape 2 (cas d'usage+scénario d'utilisation) ##
  * ouvrir mode cas d'usages & scénarios d'utilisations
    1. demander les cas d'usages déjà enregistrés dans la BD
    1. demander les scénarios d'utilisations déjà enregistrés dans la BD
    1. afficher l'analyse implicite à gauche
    1. afficher les cas d'usages & scénarios d'utilisations à droite
    1. afficher les cas d'usages présents ordonné par priorité
    1. afficher les scénarios d'utilisations présents
    1. permettre a l'utilisateur d'entrer des nouveaux cas d'usages ou scénarios d'utilisations

  * entrée d'un nouveau cas d'usage
    1. entrer le cas d'usage, 1 par ligne

  * assombrir les analyse
    1. désactivé la ligne de l'analyse

  * placer la priorité des cas d'usages
    1. écrire le chiffre de priorité à côté de chacun des cas d'usages
    1. vérifier l'unicité des priorités
    1. actualiser l'affichage (réordonner les cas)

  * entrer les étapes d'un scénario d'utilisation
    1. entrer le scénario du cas d'usage
    1. indiquer l'ordre de procédure (car le scénario peut avoir plusieurs étapes bien entendu)

  * enregistrer les cas d'usages & scénarios d'utilisations
    1. envoyer a la BD
      * les cas d'usages
      * les priorités
      * les analyses désactivées
      * les scénarios d'utilisations
      * leur ordres

## Étape 3 (Dictionnaire de données + CRC) ##
  * ouvrir le mode dictionnaire de données
    1. demander les dictionnaires déjà enregistrés à la BD
    1. afficher les scénarios d'utilisations à gauche
    1. afficher le dictionnaire de données à droite
    1. permettre à l'utilisateur d'entrer des nouveaux éléments au dictionnaire

  * entrer les éléments des dictionnaires (variables et les fonctions)
    1. ntrer chaque élément des listes de variables et fonctions, 1 par ligne

  * ouvrir le mode CRC
    1. demander les CRC déjà enregistrés à la BD
    1. afficher à gauche les dictionnaires de données et les cas/scénarios dans une "tabbed pane"
    1. afficher les CRC à droite
    1. permettre à l'utilisateur d'entrer des nouveaux éléments dans les CRC

  * entrer nom de classe, propriétaire, la "signature" de méthode
    1. entrer chaque élément de CRC selon le format CRC

  * dérive du dictionnaire et des cas d'usage/scénario
    1. comment ????? (résolue directement par l'équipe d'interface)

## Étape 4 (planning + sprint) ##
  * ouvrir le mode planning
> > ![http://blue-star-project.googlecode.com/svn/wiki/planing.jpg](http://blue-star-project.googlecode.com/svn/wiki/planing.jpg)

  * permettre d'ajouter des tâches GÉNÉRALES à chaque sprint
    1. ajouté une tache générale par ligne dans la case du sprint

  * avoir une vue générale de l'ensemble du projet (tout les sprint)
    1. montrer tout les sprint un a coté de l'autre avec leurs tâches associées

  * permettre d'ajouter les tâches détaillées à chacun des sprints
    1. ajouter une tache détaillée par ligne dans la vue du sprint détaillé

  * avoir une checkbox pour montrer ce qui est fait dans la vue détaillée
    1. passer au vert les tâches faites


  * ouvrir le mode scrum
> > ![http://blue-star-project.googlecode.com/svn/wiki/scrum.jpg](http://blue-star-project.googlecode.com/svn/wiki/scrum.jpg)

  * permettre de crée un nouveau scrum en date d'aujourd'hui
    1. créer un scrum avec tout les usagers du projet
    1. mettre dans les tâches faites toutes les tâches qui étaient à faire dans le scrum précédent (précédé d'un ? pour demandé un vérification)
    1. permettre à l'utilisateur de vérifier ce qui a été réellement fait, ce qui sera fait, et les problèmes

  * permettre de voir les anciens scrum par date
    1. afficher l'ancien scrum

  * voir les scrum par usager
    1. afficher le scrum de l'utilisateur sélectionné
