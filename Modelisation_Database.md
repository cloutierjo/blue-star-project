
```
# Base de donnée des Projets
# Les Étoiles Scintillantes
# 11 MAI 2009
#############################


Tables :

|===========================================================|
| Projets                                                   |
|===========================================================|
| ID NUMBER(6) PRIMARY KEY | Nom VARCHAR2(50) | MANDAT LONG |
|===========================================================|
| La table Projet contient un nom de projet et un mandat.
| Elle est identifier par une clé artificiel (Séquence) pour permettre à 2 projet d'avoir le meme nom.


|========================================================================================================================|
| AnalysesExp                                                                                                            |
|========================================================================================================================|
| IDPROJ NUMBER(6) REFERENCES Projets | Nom VARCHAR2(30) | Verbe VARCHAR2(30) | Adjectif VARCHAR2(30) | Handled NUMER(1) |
|========================================================================================================================|
| La Table AnalysesExp contient l'Analyse explicite de tous les projets.
| Un nom, un verbve, un adjectif et une Référence à un projet.


|========================================================================================================================|
| AnalysesImp                                                                                                            |
|========================================================================================================================|
| IDPROJ NUMBER(6) REFERENCES Projets | Nom VARCHAR2(30) | Verbe VARCHAR2(30) | Adjectif VARCHAR2(30) | Handle NUMBER(1) |
|========================================================================================================================|
| La Table AnalysesImp contient l'Analyse implicite de tous les projets.
| Un nom, un verbve, un adjectif et une Référence à un projet. 


|===================================================================================================|
| CasUsages                                                                                         |
|===================================================================================================|
| IDCAS NUMBER(6) PRIMARY KEY | IDPROJ NUMBER(6) REFERENCES Projets | PRIORITE NUMBER(6) | CAS LONG |
|===================================================================================================|
| La table CasUsages contient les cas d'usages d'un projet et son ordre de priorité.
| Elle est identifier par une clé artificiel (Séquence)


|==================================================================================|
| Senarii                                                                          |
|==================================================================================|
| IDCASUSAGES NUMBER(9) REFERENCES CasUsages | ORDREDEXEC NUMBER(6) | SENARII LONG |
|==================================================================================|
| La table Senarii contient le Senarii et son ordre d'exécution dans le code.
| Elle contient une référence au cas d'usage.


|===========================================================================|
| Variables                                                                 |
|===========================================================================|
| IDPROJ NUMBER(6) REFERENCES Projets | Var VARCHAR2(30) | Handle NUMBER(1) |
|===========================================================================|
| La table Variables contient les variables du dictionnaire de données de chaque projet


|===========================================================================|
| Fonctions                                                                 |
|===========================================================================|
| IDPROJ NUMBER(6) REFERENCES Projets | Var VARCHAR2(30) | Handle NUMBER(1) |
|===========================================================================|
| La table Fonctions contient les Fonctions du dictionnaire de données de chaque projet

|=========================================================================================|
| Usagers                                                                                 |
|=========================================================================================|
| IDUsager NUMBER(6) PRIMARY KEY | IDPROJ NUMBER(6) REFERENCES Projets | Nom VARCHAR2(30) |
|=========================================================================================|
| La table Usagers contient tous les Usagers existent et leurs références aux projets


|===============================================================================================================================|
| CRC                                                                                                                           |
|===============================================================================================================================|
| IDPROJ NUMBER(6) REFERENCES Projets | IDCRC NUMBER(6) PRIMARY KEY | Nom VARCHAR2(50) | Usager varchar2(30) | Handle NUMBER(1) |
|===============================================================================================================================|
| La table CRC contient les Fonctions et Variables du dictionnaire de données de chaque projet.
| Elle contient une référence au projet et à l'usager propriétaire du CRC.


|======================================================================|
| Responsabilite                                                       |
|======================================================================|
| IDCRC NUMBER(6) REFERENCES CRC | Nom VARCHAR(50) |  Handle NUMBER(1) |
|======================================================================|
| La table responsabilite contient les méthodes des CRCs
| Elle contient une référence à l'IDCRC


|==================================================|
| Collaboration                                    |
|==================================================|
| IDCRC NUMBER(6) REFERENCES CRC | Nom VARCHAR(50) |
|==================================================|
| La table Collaboration contient les CRCs qui collaborent avec elle
| Elle contient une référence à l'IDCRC

// Générateur d'ID de Projets
|===============|
| SeqProj       |
|===============|
| Val NUMBER(6) |
|===============|

// Générateur d'ID de CasUsages
|===============|
| SeqCasUsages  |
|===============|
| Val NUMBER(6) |
|===============|

// Générateur d'ID de Usagers
|===============|
| SeqUsagers    |
|===============|
| Val NUMBER(9) |
|===============|

// Générateur d'ID de CRC
|===============|
| SeqCRC        |
|===============|
| Val NUMBER(9) |
|===============|

############################################################## TO BE CONTINUED ##################################################
```