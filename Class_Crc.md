Tout nos CRC serons contenu ici sous le format décris en classe:
<a href='Hidden comment: 

voici le format a suivre pour les CRC, ne vous occupé pas du HTML si sa vous mélange, vous n"Avez qu"a remplacé ce qui est entre [[ ]] (en effaçant les crochet)
<table border=1>
<tr>
<td width=60% width=70%>[[nom de la classe]]

Unknown end tag for &lt;/td&gt;


<td rowspan=3> [[
* classe avec laquel elle interagit
* autre classe]]


Unknown end tag for &lt;/td&gt;




Unknown end tag for &lt;/tr&gt;


<tr>
<td align="right">[[proprio]]

Unknown end tag for &lt;/td&gt;




Unknown end tag for &lt;/tr&gt;


<tr>
<td>[[
* action fais par la classe
* autre action]]


Unknown end tag for &lt;/td&gt;




Unknown end tag for &lt;/tr&gt;




Unknown end tag for &lt;/table&gt;



'></a>

# Modèle Client (Jonatan C) #

<table width='70%' border='1'>
<blockquote><tr>
<blockquote><td width='60%'> Projet </td>
<td>
<ul><li>ModelClient<br>
</li><li>ModelServeur<br>
</li><li>ControleurClient<br>
</li><li>ControleurServeur<br>
</li></ul></td>
</blockquote></tr>
<tr>
<blockquote><td align='right'>Jonatan C.</td>
</blockquote></tr>
<tr>
<blockquote><td>
<ul><li>init(self)<br>
</li><li>projetSerialized serialize(self)<br>
</li><li>deserialize(self, serializedProject)<br>
</li><li>unicodize(self)<br>
</li></ul></td>
</blockquote></tr>
</table></blockquote>

<table width='70%' border='1'>
<blockquote><tr>
<blockquote><td width='60%'> Analyse </td>
<td>
<ul><li>ModelClient<br>
</li><li>ModelServeur<br>
</li><li>Projet<br>
</li></ul></td>
</blockquote></tr>
<tr>
<blockquote><td align='right'>Jonatan C.</td>
</blockquote></tr>
<tr>
<blockquote><td>
<ul><li>init(self,parent)<br>
</li><li>listeAnaliseTuple getForDB()<br>
</li><li>addItem(self, nom, verbe, adjectif,handled=0)<br>
</li><li>unicodize(self)<br>
</li></ul></td>
</blockquote></tr>
</table></blockquote>

<table width='70%' border='1'>
<blockquote><tr>
<blockquote><td width='60%'> CasUsage </td>
<td>
<ul><li>ModelServeur<br>
</li><li>Projet<br>
</li><li>CasUsageItem<br>
</li></ul></td>
</blockquote></tr>
<tr>
<blockquote><td align='right'>Jonatan C.</td>
</blockquote></tr>
<tr>
<blockquote><td>
<ul><li>init(self)<br>
</li><li>CasUsage addCasUsage(nom,priorite=0)<br>
</li><li>serializedCasUsage serialize()<br>
</li><li>void deserialize(serializedCasUsage)<br>
</li><li>unicodize(self)<br>
</li></ul></td>
</blockquote></tr>
</table></blockquote>

<table width='70%' border='1'>
<blockquote><tr>
<blockquote><td width='60%'> CasUsageItem </td>
<td>
<ul><li>CasUsage<br>
</li><li>ScenarioUtilisation<br>
</li><li>ModelServeur<br>
</li></ul></td>
</blockquote></tr>
<tr>
<blockquote><td align='right'>Jonatan C.</td>
</blockquote></tr>
<tr>
<blockquote><td>
<ul><li>init(self,nom="",priorite=0)<br>
</li><li>unicodize(self)<br>
</li><li>serializedCasUsageItem serialize()<br>
</li><li>void deserialize(serializedCasUsageItem)<br>
</li></ul></td>
</blockquote></tr>
</table></blockquote>

<table width='70%' border='1'>
<blockquote><tr>
<blockquote><td width='60%'> EtapeScenarioUtilisation </td>
<td>
<ul><li>CasUsage<br>
</li><li>ScenarioUtilisation<br>
</li><li>ModelServeur<br>
</li></ul></td>
</blockquote></tr>
<tr>
<blockquote><td align='right'>Jonatan C.</td>
</blockquote></tr>
<tr>
<blockquote><td>
<ul><li>init(self,nom="",ordre=0)<br>
</li><li>unicodize(self)<br>
</li><li>serializedEtapeScenario serialize()<br>
</li><li>void deserialize(serializedEtapeScenario)<br>
</li></ul></td>
</blockquote></tr>
</table></blockquote>

<table width='70%' border='1'>
<blockquote><tr>
<blockquote><td width='60%'> ScenarioUtilisation </td>
<td>
<ul><li>ModelServeur<br>
</li><li>CasUsageItem<br>
</li><li>EtapeScenarioUtilisation<br>
</li></ul></td>
</blockquote></tr>
<tr>
<blockquote><td align='right'>Jonatan C.</td>
</blockquote></tr>
<tr>
<blockquote><td>
<ul><li>ScenarioUtilisation addEtapeScenario(nom,ordre=0)<br>
</li><li>serializedScenarioUtilisation serialize()<br>
</li><li>refaireOrdreNumerique(self)<br>
</li><li>unicodize(self)<br>
</li><li>void deserialize(serializedScenarioUtilisation)<br>
</li></ul></td>
</blockquote></tr>
</table></blockquote>

<table width='70%' border='1'>
<blockquote><tr>
<blockquote><td width='60%'> DictDonne </td>
<td>
<ul><li>ModelClient<br>
</li><li>ModelServeur<br>
</li><li>Projet<br>
</li></ul></td>
</blockquote></tr>
<tr>
<blockquote><td align='right'>Jonatan C.</td>
</blockquote></tr>
<tr>
<blockquote><td>
<ul><li>init(self)<br>
</li><li>updateDictionnaire(self,variables,fonctions)<br>
</li><li>unicodize(self)<br>
</li><li>serializedDictDonne serialize()<br>
</li><li>void deserialize(serializedDictDonne)<br>
</li></ul></td>
</blockquote></tr>
</table></blockquote>

<table width='70%' border='1'>
<blockquote><tr>
<blockquote><td width='60%'> Crc </td>
<td>
<ul><li>ModelClient<br>
</li><li>ModelServeur<br>
</li><li>Projet<br>
</li></ul></td>
</blockquote></tr>
<tr>
<blockquote><td align='right'>Jonatan C.</td>
</blockquote></tr>
<tr>
<blockquote><td>
<ul><li>init(self)<br>
</li><li>unicodize(self)<br>
</li><li>serializedCrc serialize()<br>
</li><li>void deserialize(serializedCrc)<br>
</li></ul></td>
</blockquote></tr>
</table></blockquote>

<table width='70%' border='1'>
<blockquote><tr>
<blockquote><td width='60%'> LstCrc </td>
<td>
<ul><li>Crc<br>
</li></ul></td>
</blockquote></tr>
<tr>
<blockquote><td align='right'>Jonatan C.</td>
</blockquote></tr>
<tr>
<blockquote><td>
<ul><li>init(self)<br>
</li><li>unicodize(self)<br>
</li><li>serializedCrc serialize()<br>
</li><li>void deserialize(serializedCrc)<br>
</li><li>addCrc(self,nom)<br>
</li><li>updateCrc(self,crc)<br>
</li><li>getClassName(self)<br>
</li><li>getClass(self,className)<br>
</li></ul></td>
</blockquote></tr>
</table></blockquote>

<table width='70%' border='1'>
<blockquote><tr>
<blockquote><td width='60%'> Sprint </td>
<td>
<ul><li>ModelClient<br>
</li><li>ModelServeur<br>
</li><li>Projet<br>
</li></ul></td>
</blockquote></tr>
<tr>
<blockquote><td align='right'>Jonatan C.</td>
</blockquote></tr>
<tr>
<blockquote><td>
<ul><li>init(self)<br>
</li><li>unicodize(self)<br>
</li><li>serializedSprint serialize()<br>
</li><li>void deserialize(serializedSprint)<br>
</li></ul></td>
</blockquote></tr>
</table></blockquote>

<table width='70%' border='1'>
<blockquote><tr>
<blockquote><td width='60%'> LstSprint </td>
<td>
<ul><li>Sprint<br>
</li></ul></td>
</blockquote></tr>
<tr>
<blockquote><td align='right'>Jonatan C.</td>
</blockquote></tr>
<tr>
<blockquote><td>
<ul><li>init(self)<br>
</li><li>unicodize(self)<br>
</li><li>serializedSprint serialize()<br>
</li><li>void deserialize(serializedSprint)<br>
</li></ul></td>
</blockquote></tr>
</table></blockquote>

<table width='70%' border='1'>
<blockquote><tr>
<blockquote><td width='60%'> Scrum </td>
<td>
<ul><li>ModelClient<br>
</li><li>ModelServeur<br>
</li><li>Projet<br>
</li><li>ScrumList<br>
</li></ul></td>
</blockquote></tr>
<tr>
<blockquote><td align='right'>Jonatan C.</td>
</blockquote></tr>
<tr>
<blockquote><td>
<ul><li>init(self)<br>
</li><li>unicodize(self)<br>
</li><li>serializedScrum serialize()<br>
</li><li>void deserialize(serializedTask)<br>
</li></ul></td>
</blockquote></tr>
</table></blockquote>

<table width='70%' border='1'>
<blockquote><tr>
<blockquote><td width='60%'> ScrumList </td>
<td>
<ul><li>Scrum<br>
</li></ul></td>
</blockquote></tr>
<tr>
<blockquote><td align='right'>Jonatan C.</td>
</blockquote></tr>
<tr>
<blockquote><td>
<ul><li>init(self)<br>
</li><li>unicodize(self)<br>
</li><li>serializedScrum serialize()<br>
</li><li>void deserialize(serializedScrum)<br>
</li></ul></td>
</blockquote></tr>
</table></blockquote>

<table width='70%' border='1'>
<blockquote><tr>
<blockquote><td width='60%'> Task </td>
<td>
<ul><li>ModelClient<br>
</li><li>ModelServeur<br>
</li><li>Projet<br>
</li><li>TaskList<br>
</li></ul></td>
</blockquote></tr>
<tr>
<blockquote><td align='right'>Jonatan C.</td>
</blockquote></tr>
<tr>
<blockquote><td>
<ul><li>init(self)<br>
</li><li>unicodize(self)<br>
</li><li>serialize(self)<br>
</li><li>deserialize(self, serializedTask)<br>
</li></ul></td>
</blockquote></tr>
</table></blockquote>

<table width='70%' border='1'>
<blockquote><tr>
<blockquote><td width='60%'> TaskList </td>
<td>
<ul><li>Task<br>
</li></ul></td>
</blockquote></tr>
<tr>
<blockquote><td align='right'>Jonatan C.</td>
</blockquote></tr>
<tr>
<blockquote><td>
<ul><li>init(self)<br>
</li><li>unicodize(self)<br>
</li><li>serialize(self)<br>
</li><li>deserialize(self, sertasklist)<br>
</li></ul></td>
</blockquote></tr>
</table></blockquote>

<table width='70%' border='1'>
<blockquote><tr>
<blockquote><td width='60%'> User </td>
<td>
<ul><li>ModelClient<br>
</li><li>ModelServeur<br>
</li><li>Projet<br>
</li></ul></td>
</blockquote></tr>
<tr>
<blockquote><td align='right'>Jonatan C.</td>
</blockquote></tr>
<tr>
<blockquote><td>
<ul><li>init(self)<br>
</li><li>unicodize(self)<br>
</li><li>serialize(self)<br>
</li><li>deserialize(self, serializedUser)<br>
</li></ul></td>
</blockquote></tr>
</table></blockquote>

<table width='70%' border='1'>
<blockquote><tr>
<blockquote><td width='60%'> ModelClient </td>
<td>
<ul><li>Projet<br>
</li><li>ControleurClient<br>
</li></ul></td>
</blockquote></tr>
<tr>
<blockquote><td align='right'>Jonatan C</td>
</blockquote></tr>
<tr>
<blockquote><td>
<ul><li>void creerProjet(String nom)<br>
</li></ul></td>
</blockquote></tr>
</table></blockquote>

# Interface Graphique (Pascal L & Jean-Philippe C) #

<table width='70%' border='1'>
<blockquote><tr>
<blockquote><td width='60%'> Dictionnaire de donnée </td>
<td>
<ul><li>Vue<br>
</li><li>ControleurClient<br>
</li></ul></td>
</blockquote></tr>
<tr>
<blockquote><td align='right'> Jonathan H </td>
</blockquote></tr>
<tr>
<blockquote><td>
<ul><li>Intialise mes deux frames secondaires de données et actions<br>
</li><li>updateListes(self) // va chercher l'info de mes tableaux<br>
</li></ul></td>
</blockquote></tr>
</table></blockquote>

<table width='70%' border='1'>
<blockquote><tr>
<blockquote><td width='60%'> Données </td>
<td>
<ul><li>Dictionnaire de donnée<br>
</li></ul></td>
</blockquote></tr>
<tr>
<blockquote><td align='right'> Jonathan H </td>
</blockquote></tr>
<tr>
<blockquote><td>
<ul><li>initDonnee(self)<br>
</li><li>addRow(self)<br>
</li><li>gestion(self)<br>
</li><li>addEntry(self)<br>
</li><li>deleteRow(self)<br>
</li></ul></td>
</blockquote></tr>
</table></blockquote>

<table width='70%' border='1'>
<blockquote><tr>
<blockquote><td width='60%'> Actions </td>
<td>
<ul><li>Dictionnaire de donnée<br>
</li></ul></td>
</blockquote></tr>
<tr>
<blockquote><td align='right'> Jonathan H </td>
</blockquote></tr>
<tr>
<blockquote><td>
<ul><li>initActions(self)<br>
</li><li>addRow(self)<br>
</li><li>gestion(self)<br>
</li><li>addEntry(self)<br>
</li><li>deleteRow(self)<br>
</li></ul></td>
</blockquote></tr>
</table></blockquote>

<table width='70%' border='1'>
<blockquote><tr>
<blockquote><td width='60%'> AnalyseTextuelle </td>
<td>
<ul><li>Vue<br>
</li><li>Analyse<br>
</li><li>ControleurClient<br>
</li></ul></td>
</blockquote></tr>
<tr>
<blockquote><td align='right'>Pascal L.</td>
</blockquote></tr>
<tr>
<blockquote><td>
<ul><li>init(self,vueParent,analyse,implicite=False,explicite=False)<br>
</li><li>updateAnalyse(self)<br>
</li><li>addRow(self)<br>
</li><li>gestion(self)<br>
</li><li>deleteRow(self)<br>
</li></ul></td>
</blockquote></tr>
</table></blockquote>

<table width='70%' border='1'>
<blockquote><tr>
<blockquote><td width='60%'> CasUsageVue </td>
<td>
<ul><li>Vue<br>
</li><li>CasUsage<br>
</li><li>ControleurClient<br>
</li></ul></td>
</blockquote></tr>
<tr>
<blockquote><td align='right'>Mathieu L.</td>
</blockquote></tr>
<tr>
<blockquote><td>
<ul><li>monter(self)<br>
</li><li>descendre(self)<br>
</li><li>renommer(self)<br>
</li><li>ajouter(self)<br>
</li><li>supprimer(self)<br>
</li><li>remplirListe(self)<br>
</li><li>updateScenarioAssocie(self,evt=None)<br>
</li><li>updateCasUsage(self)<br>
</li></ul></td>
</blockquote></tr>
</table></blockquote>

<table width='70%' border='1'>
<blockquote><tr>
<blockquote><td width='60%'> CRCVue </td>
<td>
<ul><li>Vue<br>
</li><li>Crc<br>
</li><li>ControleurClient<br>
</li></ul></td>
</blockquote></tr>
<tr>
<blockquote><td align='right'>Pascal L. && Jean-Philippe C.</td>
</blockquote></tr>
<tr>
<blockquote><td>
<ul><li>init(self,vueParent,listeDeCRC)<br>
</li><li>nouveauCrc(self)<br>
</li><li>getCrc(self,evt)<br>
</li><li>afficherRoles(self)<br>
</li><li>afficherCollabo(self)<br>
</li><li>updateCRC(self)<br>
</li><li>addRow(self)<br>
</li><li>gestion(self)<br>
</li><li>deleteRow(self)<br>
</li></ul></td>
</blockquote></tr>
</table></blockquote>

<table width='70%' border='1'>
<blockquote><tr>
<blockquote><td width='60%'> ListeProjets </td>
<td>
<ul><li>Vue<br>
</li><li>ControleurClient<br>
</li></ul></td>
</blockquote></tr>
<tr>
<blockquote><td align='right'>Pascal L.</td>
</blockquote></tr>
<tr>
<blockquote><td>
<ul><li>init(self,data,parent)<br>
</li><li>choisirProjet(self)<br>
</li></ul></td>
</blockquote></tr>
</table></blockquote>

<table width='70%' border='1'>
<blockquote><tr>
<blockquote><td width='60%'> Liste </td>
<td>
<ul><li>Vue<br>
</li><li>ControleurClient<br>
</li></ul></td>
</blockquote></tr>
<tr>
<blockquote><td align='right'>Pascal L.</td>
</blockquote></tr>
<tr>
<blockquote><td>
<ul><li>init(self,parent,data=<a href='.md'>.md</a>,width=20,height=1)<br>
</li><li>fillListe(self,data)<br>
</li><li>getData(self,evt=0)<br>
</li></ul></td>
</blockquote></tr>
</table></blockquote>

<table width='70%' border='1'>
<blockquote><tr>
<blockquote><td width='60%'> Mandat </td>
<td>
<ul><li>Vue<br>
</li><li>ControleurClient<br>
</li></ul></td>
</blockquote></tr>
<tr>
<blockquote><td align='right'>Pascal L.</td>
</blockquote></tr>
<tr>
<blockquote><td>
<ul><li>init(self,vueParent,mandat)<br>
</li><li>updateMandat(self)<br>
</li></ul></td>
</blockquote></tr>
</table></blockquote>

<table width='70%' border='1'>
<blockquote><tr>
<blockquote><td width='60%'> ScenarioVue </td>
<td>
<ul><li>Vue<br>
</li><li>ControleurClient<br>
</li></ul></td>
</blockquote></tr>
<tr>
<blockquote><td align='right'>Mathieu L.</td>
</blockquote></tr>
<tr>
<blockquote><td>
<ul><li>init(self,vueParent)<br>
</li><li>monter(self)<br>
</li><li>descendre(self)<br>
</li><li>renommer(self)<br>
</li><li>ajouter(self)<br>
</li><li>supprimer(self)<br>
</li><li>remplirListe(self, evt = None)<br>
</li><li>updateCasUsage(self)<br>
</li></ul></td>
</blockquote></tr>
</table></blockquote>

<table width='70%' border='1'>
<blockquote><tr>
<blockquote><td width='60%'> Vue </td>
<td>
<ul><li>AnalyseTextuelle<br>
</li><li>CasUsageVue<br>
</li><li>CRCVue<br>
</li><li>DictionnaireDonnee<br>
</li><li>Liste<br>
</li><li>Mandat<br>
</li><li>ScenarioVue<br>
</li><li>ControleurClient<br>
</li></ul></td>
</blockquote></tr>
<tr>
<blockquote><td align='right'>Pascal L.</td>
</blockquote></tr>
<tr>
<blockquote><td>
<ul><li>init(self,parent)<br>
</li><li>menuPrincipal(self)<br>
</li><li>OuvrirProjet(self)<br>
</li><li>chargerEnMemoireProjet(self)<br>
</li><li>NouveauProjet(self)<br>
</li><li>effacerFenetre(self)<br>
</li><li>fermerProjet(self)<br>
</li><li>save(self)<br>
</li><li>afficherFenMandat(self)<br>
</li><li>afficherLesAnalyses(self)<br>
</li><li>afficherCasUsage(self)<br>
</li><li>afficherScenario(self)<br>
</li><li>afficherDictionnaire(self)<br>
</li><li>afficherCRC(self)<br>
</li><li>afficherUnMessage(self,Texte,erreur="ERREUR!!!")<br>
</li><li>updateListeCRC(self)<br>
</li></ul></td>
</blockquote></tr>
</table></blockquote>

<table width='70%' border='1'>
<blockquote><tr>
<blockquote><td width='60%'> Onglets </td>
<td>
<ul><li>Vue<br>
</li></ul></td>
</blockquote></tr>
<tr>
<blockquote><td align='right'>Pascal L.</td>
</blockquote></tr>
<tr>
<blockquote><td>
<ul><li>init(self,vueParent)<br>
</li></ul></td>
</blockquote></tr>
</table></blockquote>

<table width='70%' border='1'>
<blockquote><tr>
<blockquote><td width='60%'> PlanningGeneral </td>
<td>
<ul><li>Planning<br>
</li></ul></td>
</blockquote></tr>
<tr>
<blockquote><td align='right'>Mathieu L.</td>
</blockquote></tr>
<tr>
<blockquote><td>
<ul><li>init(self, frameParent, txtParent, lblText, uneListe=<a href='.md'>.md</a>)<br>
</li><li>addRow(self)<br>
</li><li>deleteRow(self)<br>
</li><li>update(self)<br>
</li></ul></td>
</blockquote></tr>
</table></blockquote>

<table width='70%' border='1'>
<blockquote><tr>
<blockquote><td width='60%'> Planning </td>
<td>
<ul><li>PlanningGeneral<br>
</li><li>PlanningDetaillee<br>
</li><li>Vue<br>
</li><li>LstSprint<br>
</li><li>TaskList<br>
</li></ul></td>
</blockquote></tr>
<tr>
<blockquote><td align='right'>Mathieu L.</td>
</blockquote></tr>
<tr>
<blockquote><td>
<ul><li>init(self, parent, CRC, listeSprint=<a href='.md'>.md</a>)<br>
</li><li>creationNouveauObjetGraphiqueSprint(self, i)<br>
</li><li>afficherDetails(self, indexSprint)<br>
</li><li>ajouterNouveauSprint(self)<br>
</li><li>update(self)<br>
</li><li>cacher(self)<br>
</li><li>afficherDetailSelectionne(self,date)<br>
</li><li>afficher(self)<br>
</li></ul></td>
</blockquote></tr>
</table></blockquote>

<table width='70%' border='1'>
<blockquote><tr>
<blockquote><td width='60%'> ButtonCallBack </td>
<td>
<ul><li>PlanningDetail<br>
</li></ul></td>
</blockquote></tr>
<tr>
<blockquote><td align='right'>Mathieu L.</td>
</blockquote></tr>
<tr>
<blockquote><td>
<ul><li>init(self, method, bouton)<br>
</li><li>invoke(self)<br>
</li></ul></td>
</blockquote></tr>
</table></blockquote>

<table width='70%' border='1'>
<blockquote><tr>
<blockquote><td width='60%'> PlanningDetail </td>
<td>
<ul><li>Planning<br>
</li><li>PlanningGeneral<br>
</li><li>Sprint<br>
</li><li>TaskList<br>
</li></ul></td>
</blockquote></tr>
<tr>
<blockquote><td align='right'>Mathieu L.</td>
</blockquote></tr>
<tr>
<blockquote><td>
<ul><li>init(self, parent, listeSprint)<br>
</li><li>afficherDetails(self, indexSprint)<br>
</li><li>update(self)<br>
</li><li>addRow(self)<br>
</li><li>gestion(self)<br>
</li><li>deleteRow(self)<br>
</li><li>update(self)<br>
</li></ul></td>
</blockquote></tr>
</table></blockquote>

<table width='70%' border='1'>
<blockquote><tr>
<blockquote><td width='60%'> ScrumView </td>
<td>
<ul><li>Scrum<br>
</li></ul></td>
</blockquote></tr>
<tr>
<blockquote><td align='right'>Jonathan C.</td>
</blockquote></tr>
<tr>
<blockquote><td>
<ul><li>init(self, vueParent, scrumLst, objPlanning)<br>
</li><li>updateListeUser(self)<br>
</li><li>updateListeDate(self)<br>
</li><li>getScrum(self)<br>
</li><li>setDate(self,evt)<br>
</li><li>setUser(self,evt)<br>
</li><li>afficherTout(self)<br>
</li><li>newScrum(self,dte,usr)<br>
</li><li>saveData(self)<br>
</li></ul></td>
</blockquote></tr>
</table></blockquote>

<table width='70%' border='1'>
<blockquote><tr>
<blockquote><td width='60%'> GridView </td>
<td>
<ul><li>ScrumView<br>
</li></ul></td>
</blockquote></tr>
<tr>
<blockquote><td align='right'>Jonathan C.</td>
</blockquote></tr>
<tr>
<blockquote><td>
<ul><li>init(self, vueParent, title)<br>
</li><li>initDonnee(self,data)<br>
</li><li>getData(self)<br>
</li><li>deleteRow(self)<br>
</li><li>addRow(self)<br>
</li><li>gestion(self)<br>
</li></ul></td>
</blockquote></tr>
</table></blockquote>

# Controleur Client (Mathieu L) #

<table width='70%' border='1'>
<blockquote><tr>
<blockquote><td width='60%'> ControleurClient </td>
<td>
<ul><li>ModelClient<br>
</li><li>ControleurServeur<br>
</li><li>Vue<br>
</li><li>AnalyseTextuelle<br>
</li><li>CasUsageVue<br>
</li><li>CRCVue<br>
</li><li>DictionnaireDonnee<br>
</li><li>Liste<br>
</li><li>Mandat<br>
</li><li>ScenarioVue<br>
</li><li>Vue<br>
</li><li>Analyse (côté modèle)<br>
</li><li>CasUsage (côté modèle)<br>
</li><li>Crc (côté modèle)<br>
</li><li>DictDonnee (côté modèle)<br>
</li><li>Planning (côté modèle)<br>
</li><li>Projet (côté modèle)<br>
</li><li>ScenarionUtilisation (côté modèle)<br>
</li><li>Scrum (côté modèle)<br>
</li><li>Sprint (côté modèle)<br>
</li><li>User (côté modèle)<br>
</li></ul></td>
</blockquote></tr>
<tr>
<blockquote><td align='right'>Mathieu L.</td>
</blockquote></tr>
<tr>
<blockquote><td>
<ul><li>init(self)<br>
</li><li>connecter(self)<br>
</li><li>afficherInterface(self)<br>
</li><li>quitter(self)<br>
</li><li>getListeProjets(self)<br>
</li><li>ouvrirProjet(self, projetId)<br>
</li><li>creerProjet(self, nom)<br>
</li><li>sauvegarder(self)<br>
</li><li>creerMandat(self, mandat)<br>
</li><li>ouvrirMandat(self)<br>
</li><li>creerATImplicite(self, dictATImplicite)<br>
</li><li>ouvrirATImplicite(self)<br>
</li><li>creerATExplicite(self, dictATExplicite)<br>
</li><li>ouvrirATExplicite(self)<br>
</li><li>ouvrirScenario(self, strCasUsage = "")<br>
</li><li>monterEtapeScenario(self,indexAMonter)<br>
</li><li>descendreEtapeScenario(self,indexADescendre)<br>
</li><li>supprimerEtapsScenario(self,indexASupprimer)<br>
</li><li>renommerEtapsScenario(self,indexARenommer,nouveauNom)<br>
</li><li>ajouterEtapeScenario(self,nomNouveau)<br>
</li><li>getCurrentNomCasUsage(self)<br>
</li><li>getCurrentCasUsage(self)<br>
</li><li>ouvrirCasUsages(self)<br>
</li><li>monterPrioriteCas(self,nomCas)<br>
</li><li>descendrePrioriteCas(self,nomCas)<br>
</li><li>renommerCasUsage(self,ancienNom,nouveauNom)<br>
</li><li>supprimerCasUsage(self,nomSuppression)<br>
</li><li>ajouterCasUsage(self,nomNouveau)<br>
</li><li>ouvrirDicDonneeVar(self)<br>
</li><li>ouvrirDicDonneeFonc(self)<br>
</li><li>updateDictionnaireDonnee(self, variables, fonctions)<br>
</li><li>createNewCrc(self,nom)<br>
</li><li>updateCrc(self,crc)<br>
</li><li>getListeCRC(self)<br>
</li><li>getCRC(self,nom)<br>
</li><li>createNewUser(self,nom)<br>
</li></ul></td>
</blockquote></tr>
</table></blockquote>

# Serveur (Jonathan H) #

<table width='70%' border='1'>
<blockquote><tr>
<blockquote><td width='60%'> ControleurServeur </td>
<td>
<ul><li>ControleurClient<br>
</li><li>ModeleServeur<br>
</li></ul></td>
</blockquote></tr>
<tr>
<blockquote><td align='right'> Jonathan H </td>
</blockquote></tr>
<tr>
<blockquote><td>
<ul><li>Initialisation du serveur<br>
</li></ul></td>
</blockquote></tr>
</table></blockquote>

<table width='70%' border='1'>
<blockquote><tr>
<blockquote><td width='60%'> ServerMethods </td>
<td>
<ul><li>ControleurServeur<br>
</li></ul></td>
</blockquote></tr>
<tr>
<blockquote><td align='right'> Jonathan H </td>
</blockquote></tr>
<tr>
<blockquote><td>
<ul><li>getListeProjets() // retourne une liste de string<br>
</li><li>sauvegarderProjet(self, serializedProjet)) // save le projet dans la db<br>
</li><li>getProjet(self, idProjet) // retourne un projet<br>
</li><li>deleteProjet(self, idProjet) // supprime un projet<br>
</li></ul></td>
</blockquote></tr>
</table></blockquote>

# Modèle Serveur (François L) #
<table width='70%' border='1'>
<blockquote><tr>
<blockquote><td width='60%'> ModeleServeur </td>
<td>
<ul><li>Projet<br>
</li><li>ControleurServeur<br>
</li></ul></td>
</blockquote></tr>
<tr>
<blockquote><td align='right'>François L.</td>
</blockquote></tr>
<tr>
<blockquote><td>
<ul><li>init(self)<br>
</li><li>initDB(self)<br>
</li><li>getProject(self, projectID)<br>
</li><li>getListeProjet(self)<br>
</li><li>saveProject(self, projet)<br>
</li><li>saveNewProject(self, projet)<br>
</li><li>updateProject(self, projet)<br>
</li><li>deleteProject(self, projetID)<br>
</li><li>getNewIDProj(self)<br>
</li><li>getNewIDCasUsages(self)<br>
</li><li>getNewIDUsager(self)<br>
</li><li>getNewIDCRC(self)<br>
</li><li>test(self) //méthodes de tests interne a la classe<br>
</li><li>getNewIdScrum(self)<br>
</li></ul></td>
</blockquote></tr>
</table>