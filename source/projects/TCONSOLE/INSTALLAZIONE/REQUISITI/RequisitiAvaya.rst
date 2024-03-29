.. _Requisiti Avaya:

==========================================================
Prerequisiti configurazione per gestione tramite Avaya
==========================================================

Nel seguito vengono riportati i prerequisiti lato centrale telefonica e TConsole distinti per i sistemi:

- ACM R. 5.1

- ACM R. 6.2

- AURA R.8


Avaya Communication Manager R.5.1
=================================

L\'accodamento simultaneo delle chiamate sui terminali dei P.O. è realizzato attraverso un sistema a doppia copertura, occorre quindi definire un Coverage Path relativo ad un Coverage Answer Group a cui appartengono tutti i terminali dedicati ai P.O. 

Il Coverage Answer Group deve essere inserito in un apposito Hunt Group indirizzato da un VDN configurato come attendant Vectoring 
e gestito tramite un vettore. 
Attraverso questa architettura tutte le chiamate indirizzate al servizio di ATTENDANT vengono presentate a tutti i telefoni dei P.O. 
e il primo che risponde svincola la chiamata consentendo agli altri P.O. di gestire le altre. 
Ogni P.O. è in grado di gestire fino a 5 chiamate contemporanee quindi un singolo servizio di ATTENDANT basato su un coverage Answer Group consente un massimo di 8 P.O. e una gestione di 40 chiamate contemporanee. 

Nel caso in cui i servizi Attendant siano regolati da un calendario/orario occorre prevedere tale prestazione sull’AVAYA Communication Manager in modo da inoltrare le chiamate ai  P.O. solo nei giorni e negli orari desiderati.

L\'Overflow viene gestito in tre modi:

- Attraverso l\'emissione di un tono di occupato
- Il trasferimento su un numero alternativo
- Un annuncio di dissuasione se disponibile sull’AVAYA Communication Manager l’apposita scheda annunci.

La gestione Notte può essere attivata in due modalità 

- **AUTOMATICA** configurando sul Coverage Path un numero massimo di squilli trascorsi i quali la chiamata viene inoltrata ad un altro numero o gestita tramite un annuncio di dissuasione 
- **MANUALE** attraverso un tasto del TConsole preconfigurato per trasferire in modalità BLIND le chiamate in arrivo sul P.O. verso un numero alternativo. Tale modalità attiva lo stato NOTTE per tutti i P.O. 

.. image:: /images/TCONSOLE/INSTALLAZIONE/REQUISITI/Avaya_CM5_IMG00.png

**Prerequisito terminale telefonico**

L\'utilizzo di TConsole è certificato con terminali telefonici di tipo 14xx o 16xx che potranno essere utilizzati con cuffia e dovranno essere configurati con almeno 6 tasti linea di cui 5 configurati in modalità bidirezionale e dedicati all’accodamento delle chiamate mentre il 6° monodirezionale per svincolare le chiamate.

Per ogni terminale telefonico deve essere prevista una licenza Avaya IP Softphone necessaria per  consentire al TConsole l’accesso a tutte le funzionalità telefoniche necessarie al P.O. L’Avaya IP Softphone stabilisce un link TAPI tra il TConsole e il terminale telefonico del P.O. consentendo l’accesso alle funzioni telefoniche attraverso tastiera, mouse e Display Braille e la traduzione degli eventi telefonici in Sintesi Vocale.

A tal proposito è necessario configurare la centrale con tipi di terminali correttamente
supportati dall’Avaya Soft Phone, infatti quest’ultimo permette il controllo solo di terminali digitali di tipo 24xx oppure di terminali IP della serie 46xx o 96xx. Quindi, anche se i terminali che si utilizzano sono di tipo 14xx o 16xx, dovranno essere configurati sulla centrale rispettivamente come 24xx e 46xx o 96xx.

.. rubrica:: Note

.. [1] 

In  C:\\Programmi\\Telenia\\TConsole\\TConsole.ini settare i seguenti parametri come segue:

Nel caso di AVAYA CM 5.1 
[PO]
ID=1
TYPE=AVAYA_CM
IADN=<DN del telefono da pilotare> Es. IADN=2211
DEVICE=Avaya IP/Line

Nel caso di Avaya CM 6.2
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

4.7.1	Gestione di clid di chiamate provenienti dagli interni
Per poter visualizzare correttamente il clid di chiamate provenienti da interni In C:\Programmi\Telenia\TConsole\TConsole.ini valorizzare a SI il parametro TAPI_CALLERNAME_ON_CLID_UNK.
TAPI_CALLERNAME_ON_CLID_UNK=SI

4.7.2	Trattamento Notte AUTOMATICA
Configurare sul Coverage Path un numero massimo  di squilli trascorsi i quali la chiamata viene inoltrata ad  un altro numero o gestita tramite un annuncio di dissuasione. In caso di più postazioni lo stato notte può essere impostato per ciascun IADN
- Lato ACM: coverage path.

4.7.3	Trattamento Notte MANUALE
Trasferire in modalità BLIND le chiamate in arrivo sul P.O. verso un numero alternativo (CTRL-N).
Tale modalità attiva lo stato NOTTE per un P.O. alla volta
- Lato ACM: disponibilità di un DN a cui deviare le chiamate
- Lato TCONSOLE: In C:\\Programmi\\Telenia\TConsole\TConsole.ini valorizzare il parametro QUEUE_ID con il numero di interno a cui rediriggere. Es. QUEUE_ID=205

4.7.4	Inclusione
Possibilità da parte del P.O. di includersi in una conversazione attiva su un interno
- Lato ACM: COR-Can be a service observer=y
- Lato TCONSOLE: In C:\Programmi\Telenia\TConsole\TConsole.ini nella sezione [FLEX] configurare un tasto con il codice per l’inclusione.
Es. 2=Inclusione,Inc,@*88,

4.7.5	Inoltro su occupato
Possibilità di inoltrare chiamate veso interni già occupati ponendole in coda sul telefono.
- Lato ACM: Priority Calling acces code=*60
- Lato TCONSOLE: In C:\Programmi\Telenia\TConsole\TConsole.ini nella sezione [TAPI-SIP]  Settare il parametro TAPI_CALL_ON_BUSY_CODE con il codice di Inoltro su occupato. 
Es: TAPI_CALL_ON_BUSY_CODE=*60

Il TAPI_CALL_ON_BUSY_CODE se attivato viene anteposto nei seguenti casi:

-	composizione da tastierino numerico
-	doppio click su campolampade
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


4.7.6	Ritorni a P.O.
Abilitare il ritorno delle chiamate trasferite dal P.O. verso interni in caso di non risposta.
- Lato ACM: Station call transfer recall timer (0) sec.
- Lato TCONSOLE: In C:\Programmi\Telenia\TConsole\TConsole.ini  nella sezione [TAPI-SIP] valorizzare a SI il parametro TAPI_CALLEDNAME_ON_DNIS_UNK

TAPI_CALLEDNAME_ON_DNIS_UNK=SI

4.7.7	Gestione delle trasferte in modalità forzata
Nel caso in cui si abbiano delle particolari configurazioni dei flussi entranti per cui la trasferta nella modalità classica non dovesse funzionare, si può attivare un diverso tipo di trasferta TAPI nel seguente modo:
- Lato TCONSOLE: In C:\Programmi\Telenia\TConsole\TConsole.ini  nella sezione [TAPI-SIP] valorizzare a SI il parametro TAPI_FORCE_SETUP_T
TAPI_FORCE_SETUP_T = SI

4.7.8	DTMF
Dalla versione 4.3.3 è possibile inoltrare dei DTMF con l’utilizzo del tasto F6. Nessuna configurazione richiesta.

4.7.9	Altre impostazioni
Ulteriori impostazioni sono riportate nel manuale di installazione Tconsole.

.. rubric:: Note

.. [1] ultima release TVOX al momento della compilazione di questa guida: |latest_tvox_release|

.. [2] se rilevata una versione del firmware inferiore alla più bassa tra quelle indicate, la corretta versione viene automaticamente caricata dal TVOX tramite provisioning
