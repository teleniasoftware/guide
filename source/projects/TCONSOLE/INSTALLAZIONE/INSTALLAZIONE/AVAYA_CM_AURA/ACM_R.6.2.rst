==============
Avaya CM R.6.2
==============

Licenze AES
===========

Con l'introduzione della release 6.2 di ACM non è più possibile utilizzare AVAYA IP Softphone come service provider TAPI lato PC.

L'utilizzo del TConsole in ambito AVAYA 6.2 deve prevedere una licenza *AES 6.X BSC TSAPI (X>=2)*; 

l'opzione Campo Lampade necessita anch'essa di una licenza *AES 6.X BSC TSAPI (X>=2)* per singolo Posto Operatore.

Quindi se ad esempio servono tre Posto Operatori di cui due con il Campo Lampade le licenze *AES 6.X BSC TSAPI (X>=2)*necessarie sono 5.

In questo modo possiamo garantire la massima efficienza a ciascun P.O. dotato di campo lampade avendo un connettore dedicato TSAPI per l'accesso su richiesta allo 
stato telefonico degli utenti di centrale. 


Installazione di Avaya AES TSAPI client
=======================================

Avaya AES TSAPI client si installa sul PC che ospita Tconsole come descritto nelle pagine seguenti.

La cartella compressa contiene i TSAPI Tools tra cui l'applicazione TSAPI Test.

.. image:: /images/TCONSOLE/INSTALLAZIONE/REQUISITI/InstallazioneAvayaTSAPI01.PNG

.. image:: /images/TCONSOLE/INSTALLAZIONE/REQUISITI/InstallazioneAvayaTSAPI02.PNG

.. image:: /images/TCONSOLE/INSTALLAZIONE/REQUISITI/InstallazioneAvayaTSAPI03.PNG


.. code-block:: ini
    
    AES: <ip-address del server AES> 
    port number 450


Premere il tasto  **Add to list**


.. image:: /images/TCONSOLE/INSTALLAZIONE/REQUISITI/InstallazioneAvayaTSAPI04.PNG

    Premere il tasto Install


.. image:: /images/TCONSOLE/INSTALLAZIONE/REQUISITI/InstallazioneAvayaTSAPI05.PNG


Verifica funzionamento TSAPI
=============================

Ad installazione terminata lanciare l'applicazione TSAPI test

.. code-block:: ini

    USR: Telenia
    PWD: xxxxxxxxxxx

Eseguire una chiamata (Es. da 5000 a 5009) per verificare il buon  funzionamento della  comunicazione TSAPI..


.. image:: /images/TCONSOLE/INSTALLAZIONE/REQUISITI/TestTsapiDevice.png

Configurazione SoftPhone
========================

Lanciando per la prima volta il softphone vengono chieste delle configurazioni. Indipendentemente dalle configurazioni impostate si arriva poi a una pagina riassuntiva in cui si devono impostare i parametri come segue:

.. image:: /images/TCONSOLE/INSTALLAZIONE/REQUISITI/ConfigurazioneAvayaIPSoftPhone01.PNG

.. image:: /images/TCONSOLE/INSTALLAZIONE/REQUISITI/ConfigurazioneAvayaIPSoftPhone02.PNG

Impostare Configuration: *Control of Avaya Telephone (via the server)*. Nel caso invece si voglia usere il softphone impostare Configuration: *Road Warrior* e inserire la password.

Di seguito gli altri screenshot di configurazione dell’interno 641 usato come PO. Ricordiamo che il 641 è un telefono IP fisico.

.. image:: /images/TCONSOLE/INSTALLAZIONE/REQUISITI/ConfigurazioneAvayaIPSoftPhone03.PNG

.. image:: /images/TCONSOLE/INSTALLAZIONE/REQUISITI/ConfigurazioneAvayaIPSoftPhone04.PNG

.. image:: /images/TCONSOLE/INSTALLAZIONE/REQUISITI/ConfigurazioneAvayaIPSoftPhone05.PNG

.. image:: /images/TCONSOLE/INSTALLAZIONE/REQUISITI/ConfigurazioneAvayaIPSoftPhone06.PNG


Configurazione TConsole e AVAYA CM 6.2
=======================================

C:\\Programmi\\Telenia\\TConsole\\TConsole.ini settare i seguenti parametri come segue:

.. code-block:: ini

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



Gestione clid di chiamate provenienti dagli interni
---------------------------------------------------

Per poter visualizzare correttamente il clid di chiamate provenienti da interni In C:\Programmi\Telenia\TConsole\TConsole.ini valorizzare a SI il parametro **TAPI_CALLERNAME_ON_CLID_UNK**.

.. code-block:: ini

    TAPI_CALLERNAME_ON_CLID_UNK=SI


Trattamento Notte AUTOMATICA
----------------------------
Configurare sul Coverage Path un numero massimo  di squilli trascorsi i quali la chiamata viene inoltrata ad  un altro numero o gestita tramite un annuncio di dissuasione. In caso di più postazioni lo stato notte può essere impostato per ciascun IADN

- *Lato ACM*: coverage path.

Trattamento Notte MANUALE
-------------------------
Trasferire in modalità BLIND le chiamate in arrivo sul P.O. verso un numero alternativo (*CTRL-N*).
Tale modalità attiva lo stato NOTTE per un P.O. alla volta

- *Lato ACM*: disponibilità di un DN a cui deviare le chiamate
- *Lato TConsole*: In C:\\Programmi\\Telenia\\TConsole\\TConsole.ini valorizzare il parametro QUEUE_ID con il numero di interno a cui rediriggere. Es. QUEUE_ID=205

Inclusione
----------
Possibilità da parte del P.O. di includersi in una conversazione attiva su un interno

- *Lato ACM*: COR-Can be a service observer=y
- *Lato TConsole*: In C:\\Programmi\\Telenia\\TConsole\\TConsole.ini nella sezione [FLEX] configurare un tasto con il codice per l’inclusione.

Es. 2=Inclusione,Inc,@*88,


Inoltro su occupato
-------------------
Possibilità di inoltrare chiamate veso interni già occupati ponendole in coda sul telefono.

- *Lato ACM*: Priority Calling acces code=*60
- *Lato TConsole*: In C:\\Programmi\\Telenia\\TConsole\\TConsole.ini nella sezione [TAPI-SIP]  Settare il parametro **TAPI_CALL_ON_BUSY_CODE** con il codice di Inoltro su occupato. 

Es: TAPI_CALL_ON_BUSY_CODE=*60


Il **TAPI_CALL_ON_BUSY_CODE** se attivato viene anteposto nei seguenti casi:

-	composizione da tastierino numerico
-	doppio click su campolampade
-	inoltro da rubrica se abilitato in base alla configurazione di rubest.ini e rubint.ini

.. Important:: Il **TAPI_CALL_ON_BUSY_CODE** non viene mai inviato nell’utilizzo con postit.

E’ possibile selezionare il campo di rubrica su cui inviare il busycode compilando opportunamente rubest.ini e rubint.ini come segue:

.. code-block:: ini

    [COMMON]
    F12_BUSYCODE=Flag_F12,Flag_Shift+F12,Flag_Ctrl+F12,Flag_Alt+F12
    
.. Warning::Per ognuno dei 4 flag, i valori ammessi sono:

  - S, SI, Y, YES, 1
  - N, NO, 0
  
  in qualsiasi combinazione minuscola/maiuscola.
  Esempio: F12_BUSYCODE=SI,N,si,Yes*


Ritorni a P.O.
--------------
Abilitare il ritorno delle chiamate trasferite dal P.O. verso interni in caso di non risposta.

- *Lato ACM*: Station call transfer recall timer (0) sec.
- *Lato TConsole*: In C:\\Programmi\\Telenia\\TConsole\\TConsole.ini  nella sezione [TAPI-SIP] valorizzare a SI il parametro **TAPI_CALLEDNAME_ON_DNIS_UNK**

.. code-block:: ini

    TAPI_CALLEDNAME_ON_DNIS_UNK=SI


Gestione delle trasferte in modalità forzata
---------------------------------------------
Nel caso in cui si abbiano delle particolari configurazioni dei flussi entranti per cui la trasferta nella modalità classica non dovesse funzionare, si può attivare un diverso tipo di trasferta TAPI nel seguente modo:

- *Lato TConsole*: In C:\\Programmi\\Telenia\\TConsole\\TConsole.ini  nella sezione [TAPI-SIP] valorizzare a SI il parametro **TAPI_FORCE_SETUP_T**
  
  .. code-block:: ini
      
      TAPI_FORCE_SETUP_T = SI

DTMF
-----
Dalla versione 4.3.3 è possibile inoltrare dei DTMF con l’utilizzo del tasto F6. Nessuna configurazione richiesta.


