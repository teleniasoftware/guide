=========
AURA R.8
=========

Per la realizzazione dell'ambiente test è stata utilizzata una piattaforma Avaya in versione 8.x..

In Figura  Vengono illustrate le componenti Avaya utilizzate per la realizzazione dell'ambiente di test. 

.. image:: /images/TCONSOLE/INSTALLAZIONE/REQUISITI/Schema_Blocchi_AURA.PNG


Licenze AES
============

La comunicazione tragli applicativi Telenia (Tconsole e Tconsoleserver) e Avaya è garantita dalle funzionalità del server Avaya AES (Application Enablement Services), attivabile attraverso licenza TSAPI Simultaneous Users.

La licenza utente di base TSAPI viene spesso definita *licenza basata su agente* o *licenza basata su stazione*. È destinata ad applicazioni che desiderano monitorare o controllare una stazione o monitorare uno split ACD. Nel file di licenza è indicata come licenza "Utente simultaneo". 

Le licenze devono essere dimensionate in termini di numero di agenti, stazioni o divisioni ACD che si desidera monitorare e controllare contemporaneamente.

NOTE: Per la funzionalità “campo lampade” (BLF) è necessario avere una licenza AES *Utente simultaneo* aggiuntiva. 


Prerequisito terminale telefonico
=================================
L’utilizzo di TConsole è certificato con terminali telefonici SIP di tipo J1xx che potranno essere utilizzati con cuffia e in base alle esigenze del cliente possono essere configurati con più call-appearence per la gestione di più chiamate contemporanee

Per ogni terminale telefonico deve essere prevista una licenza TSAPI necessaria per  consentire al TConsole l’accesso a tutte le funzionalità telefoniche necessarie al P.O. Attraverso il server AES si stabilisce un link TSAPI tra il TConsole e il terminale telefonico del P.O. consentendo l’accesso alle funzioni telefoniche attraverso tastiera, mouse e Display Braille e la traduzione degli eventi telefonici in Sintesi Vocale.

E’ possibile abilitare sulla station il parametro IP SoftPhone mettendolo a Y per utilizzare un SoftPhone (Avaya Workplace) al posto del telefono fisico 


.. image:: /images/TCONSOLE/INSTALLAZIONE/REQUISITI/Aura_dispositivo.PNG

    Avaya AES TSAPI client si installa sul PC che ospita Tconsole come descritto nelle pagine seguenti.

La cartella compressa contiene i TSAPI Tools tra cui l'applicazione TSAPI Test.

.. image:: /images/TCONSOLE/INSTALLAZIONE/REQUISITI/InstallazioneAvayaTSAPI01.PNG

.. image:: /images/TCONSOLE/INSTALLAZIONE/REQUISITI/InstallazioneAvayaTSAPI02.PNG

.. image:: /images/TCONSOLE/INSTALLAZIONE/REQUISITI/InstallazioneAvayaTSAPI03.PNG

.. Esempio:
AES: <ip-address del server AES> 
port number 450

Premere il tasto  Add to list


.. image:: /images/TCONSOLE/INSTALLAZIONE/REQUISITI/InstallazioneAvayaTSAPI04.PNG

    Premere il tasto Install

.. image:: /images/TCONSOLE/INSTALLAZIONE/REQUISITI/InstallazioneAvayaTSAPI05.PNG

Utilizzare un web browser per accedere al server AES Avaya per creare le utenze dei Posti Operatori, che verranno utilizzate da TConsole si Telenia.

Tramite l’interfaccia di un web browser, inserire https://<ip-addr> nel campo indirizzi del web browser, dove <ip-addr> è l’indirizzo IP di management del server AES.

Dal menu dell’AES, seleziona User Management  User Admin  Add User. Verrà proposta una nuova finestra dove andranno compilati i campi come indicato nell’immagine sotto riportata (Figura 2).
Nel nostro test è stato creato un utente con queste caratteristiche:
- User Id = PO1
- User Password = xxxxxxxxx

..NOTE: inserire a YES il campo CT User confermando con il tasto Apply in fondo alla pagina.

.. image:: /images/TCONSOLE/INSTALLAZIONE/REQUISITI/Aura_conf01.PNG

Creato l’utente PO (o gli utenti), selezionare nel menù di sinistra la voce Security  Security Database  CTI Users  List All Users

Nella tabella che comparirà selezionare l’utente appena creato e premere il tasto Edit

.. image:: /images/TCONSOLE/INSTALLAZIONE/REQUISITI/Aura_conf02.PNG

Spuntare il campo Unrestricted Access come da immagine e premere Apply Changes.
L’utente PO è pronto per interfacciarsi correttamente con la T.Console Telenia

.. image:: /images/TCONSOLE/INSTALLAZIONE/REQUISITI/Aura_conf03.PNG



Verifica funzionamento TSAPI
=============================

Ad installazione terminata lancia re l'applicazione TSAPI test

Esempio:
USR: Telenia
PWD: !Telenia01
Eseguire una chiamata (Es. da 5000 a 5009) per verificare il buon  funzionamento della  comunicazione TSAPI..


.. image:: /images/TCONSOLE/INSTALLAZIONE/REQUISITI/TestTsapiDevice.png


Configurazione TConsole e AVAYA AURA R. 8
=========================================

Lato Tconsole, configurare opportunamente il file TConsole.ini. Di seguito un esempio:

[PO]
;	TYPE: Tipo di centrale
TYPE=AVAYA_CSTA
;	IADN: Interno del PO da controllare
IADN=3005
;	DEVICE:  device da controllare (es. Cisco Line: [SEP00221904C2A7] (3028)) o com a cui collegare il dispositivo (es. COM1) 
DEVICE=3005

[TAPI-SIP]
AVAYA_CSTA_LINK=AVAYA#CM#CSTA#AES
AVAYA_CSTA_LINK_VERSION=ECS2-6
AVAYA_CSTA_LINK_USR=PO1
AVAYA_CSTA_LINK_PWD=Console@01


Lato Avaya sono necessarie alcune configurazioni base per il corretto funzionamento del PO con la T-Console Telenia.
Le postazioni PO non possono essere configurate come Attendant Console ma devono essere configurate come station modello J1xx utilizzando quindi un telefono hardware SIP.
Se si preferisce utilizzare un SoftPhone è necessario abilitare l’opzione all’interno della configurazione della station.

.. image:: /images/TCONSOLE/INSTALLAZIONE/REQUISITI/Aura_conf04.PNG

Creare un VDN, legato alla numerazione pubblica in ingresso, con il parametro Attendant Vectoring? a Y (yes). Al VDN appena creato assegnare un vector dove andremo a configurare il servizio PO.


.. image:: /images/TCONSOLE/INSTALLAZIONE/REQUISITI/Aura_conf05.PNG

Se il cliente identifica un orario di servizio e vuole che il sistema dia un messaggio di dissuasione anche se i PO non sono in servizio notte, è necessario configurare il check orario all’interno del vettore. Se in orario di servizio o se non è presente il check, andare a fare un route-to-number verso il Group Extension dell’Hunt-Group creato per i PO.
Di seguito l’Hunt-Group creato

.. image:: /images/TCONSOLE/INSTALLAZIONE/REQUISITI/Aura_conf06.PNG

E’ il vettore per l’accodamento al Gruppo PO. In questo di esempio non è presente nessun controllo orario.

.. image:: /images/TCONSOLE/INSTALLAZIONE/REQUISITI/Aura_conf07.PNG

Il parametro cov in questo caso impostato a y (yes) indica al sistema che se l’Hunt-Group ha una copertura, allora deve essere presa in considerazione. Questo deve avvenire nel caso in cui sia necessaria una configurazione Ring-All, una copertura verso tutti gli interni PO per farli squillare assieme, oppure nel caso in cui si voglia configurare il servizio Notte con la copertura su un DN diverso o su un annuncio di dissuasione.
All’interno dell’Hunt-Group devono essere inseriti gli interni o l’interno in caso di PO unico, creati precedentemente come indicato in figura che segue

.. image:: /images/TCONSOLE/INSTALLAZIONE/REQUISITI/Aura_conf08.PNG


Se si vuole demandare al centralino Avaya la gestione delle chiamate in coda sarà sufficiente configurare le station dei PO con 2 call-appearence. 

NOTA: I tasti call-appearence sono tasti configurati sui dispositivi telefonici associati alle notifiche di chiamate in arrivo dirette ad un interno /utente o ad un Hunt-Group al quale l’utente appartiene. Ogni call-appearence consente anche l’impegno linea per programmare una chiamata in uscita.

Se il cliente necessita della possibilità di destinare fino a 5 chiamate per ogni PO, dove ogni operatore gestisce le chiamate in coda in modalità manuale, allora si renderà necessario configurare 6 call-appearence per ogni PO di cui:
- 5 per le chiamate in ingresso 
- 1 per i trasferimenti
Riportiamo di seguito un esempio.


.. image:: /images/TCONSOLE/INSTALLAZIONE/REQUISITI/Aura_conf09.PNG


Gestione di clid di chiamate provenienti dagli interni
------------------------------------------------------
Per poter visualizzare correttamente il clid di chiamate provenienti da interni In C:\Programmi\Telenia\TConsole\TConsole.ini valorizzare a SI il parametro 
- TAPI_CALLERNAME_ON_CLID_UNK.
- TAPI_CALLERNAME_ON_CLID_UNK=SI


Trattamento Notte AUTOMATICA
----------------------------
Configurare una  Coverage Path con un numero massimo di squilli trascorsi i quali la chiamata viene inoltrata ad  un altro numero o gestita tramite un annuncio di dissuasione. La Coverage Path creata deve essere associata all’Hunt-Group dedicato alla gestione del PO.

- Lato ACM: 
Per la creazione della coverage eseguire il comando sul CM Avaya add coverage path xx (nel nostro esempio la coverage utilizzata è la numero 1)

.. image:: /images/TCONSOLE/INSTALLAZIONE/REQUISITI/Aura_conf10.PNG

Impostare a yes (Y) solamente la voce Don’t Answer per la gestione delle chiamate che, dopo 4 squilli senza risposta, viene inoltrata automaticamente all’interno desiderato. 2002 nel nostro laboratorio è un annuncio di dissuasione.

Associare la coverage path creata all’Hunt-Group di accodamento ai PO.

.. image:: /images/TCONSOLE/INSTALLAZIONE/REQUISITI/Aura_conf11.PNG


Trattamento Notte MANUALE (singola postazione)
----------------------------------------------
Si possono configurare 2 metodi per gestire la notte in maniera manuale che sono:
-	Tramite un trasferimento verso un nuovo numero, che può essere una destinazione alternativa oppure un annuncio di dissuasione;
-	Configurare sia sull’extension Avaya dei PO sia sulla T-Console il tasto Notte.

Metodo 1 -Trasferimento
Trasferire in modalità BLIND le chiamate in arrivo sul P.O. verso un numero alternativo (CTRL-N).
Tale modalità attiva lo stato NOTTE per un P.O. alla volta
- Lato ACM: disponibilità di un DN a cui deviare le chiamate
- Lato TCONSOLE: In C:\Programmi\Telenia\TConsole\TConsole.ini valorizzare il parametro QUEUE_ID con il numero di interno a cui rediriggere. Es. QUEUE_ID=205


Metodo 2 – Configurazione tasto notte
E’ necessario configurare sul CM Avaya, il feauture-access-code “Hunt Group Busy Activation”, come riportato in figura 3, inserendo il codice funzione che attiverà la feature (nel nostro lab. *65 per l’attivazione *66 per la disattivazione)
 
.. image:: /images/TCONSOLE/INSTALLAZIONE/REQUISITI/Aura_conf12.PNG


Configurare su tutte le extension delle postazioni PO attive, il tasto “hntpos-bsy  Grp: n°” specificando il numero dell’Hunt-Group (nel nostra caso l’HG 1) che si vuole utilizzare. In esempio la configurazione di una station:


.. image:: /images/TCONSOLE/INSTALLAZIONE/REQUISITI/Aura_conf13.PNG

Una volta assegnato il tasto a tutte le postazioni PO è possibile inserire nel campo Night Destination  dell’Hunt-Group di accodamento al PO, un DN (Destination Number), un  VDN o un interno. Nel nostro laboratorio è stato utilizzato un interno associato ad un annuncio:
 
.. image:: /images/TCONSOLE/INSTALLAZIONE/REQUISITI/Aura_conf14.PNG

    Sul Tconsole, deve essere creato il tasto FLEX con lo stesso codice creato precedentemente su Avaya come feauture-access-code. Nell’esempio sopra il codice *65.
[FLEX]
; 	Key=Desc,Desc_IPO+,[<tipo>numero],
0=NOTTE,NOTTE,@*65,

NOTE: Quando si ha la necessità di abilitare la funzionalità Notte, è importante che su tutte le postazioni sia attivo il tasto altrimenti la centrale Avaya considererà disponibile la/le postazione/i su cui la funzionalità non è stata abilitata.

4.8.4	Inoltro su occupato
-----------------------------

Possibilità di inoltrare chiamate veso interni già occupati ponendole in coda sul telefono.
- Lato ACM: configurare nei feauture-access- codes il “Priority Calling Access Code=”. Nell’esempio sotto è stato impostato il codice *60

.. image:: /images/TCONSOLE/INSTALLAZIONE/REQUISITI/Aura_conf15.PNG

- Lato TCONSOLE: In C:\Programmi\Telenia\TConsole\TConsole.ini nella sezione [TAPI-SIP]  Settare il parametro TAPI_CALL_ON_BUSY_CODE con il codice di Inoltro su occupato. 
Es: TAPI_CALL_ON_BUSY_CODE=*60

Il TAPI_CALL_ON_BUSY_CODE se attivato viene anteposto nei seguenti casi:

-	composizione da tastierino numerico
-	inoltro da rubrica se abilitato in base alla configurazione di rubest.ini e rubint.ini

Il TAPI_CALL_ON_BUSY_CODE non viene mai inviato nell’utilizzo con postit.

E’ possibile selezionare il campo di rubrica su cui inviare il busycode compilando opportunamente rubest.ini e rubint.ini come segue:

[COMMON]
F12_BUSYCODE=Flag_F12,Flag_Shift+F12,Flag_Ctrl+F12,Flag_Alt+F12
Per ognuno dei 4 flag, i valori ammessi sono:
- S, SI, Y, YES, 1
- N, NO, 0
in qualsiasi combinazione minuscola/maiuscola.
Esempio: F12_BUSYCODE=SI,N,si,Yes


Ritorni a P.O.
--------------
Abilitare il ritorno delle chiamate trasferite dal P.O. verso interni in caso di non risposta.
- Lato ACM: impostare nei system-parameters feauture il parametron “Station call transfer recall timer (n) sec” inserendo al posto di n il numero di secondi passati i quali la chiamata trasferita dal PO all’interno in caso di non risposta torna al PO.

NOTE: Questo è un parametro di sistema che agisce anche sui trasferimenti effettuati dagli altri interni e non solo per i PO.

Nell’esempio sotto il parametro è stato impostato ad 8 secondi.

.. image:: /images/TCONSOLE/INSTALLAZIONE/REQUISITI/Aura_conf16.PNG


- Lato TCONSOLE: In C:\Programmi\Telenia\TConsole\TConsole.ini  nella sezione [TAPI-SIP] valorizzare a SI il parametro TAPI_CALLEDNAME_ON_DNIS_UNK

TAPI_CALLEDNAME_ON_DNIS_UNK=SI


Campo Lampade
-------------

Lato TConsoleserver configurare il file tabpara.ini nel seguente modo:
[BLF]
Active=YES
QueryDescription=NO
;	Type: TAPI o SIP o TVOX o CSTA
Type=TAPI
ActiveBlfOnDB=NO
;	abilita il getstatus sui device tapi. se lo status è ko riavvio la lampada
TestDeviceTimeout=20000

[CSTAPARAMS]
AVAYA_CSTA_LINK=AVAYA#CM#CSTA#AES
AVAYA_CSTA_LINK_VERSION=ECS2-6
AVAYA_CSTA_LINK_USR=PO1
AVAYA_CSTA_LINK_PWD=Console@01
