===============
Il campo lampade (BLF)
===============

Il campo lampade consente di controllare lo stato di un insieme di telefoni. 
Per abilitare la gestione Campo lampade BLF occorre settare il seguente parametro in *tabparam.ini*:

.. code-block:: ini
    
    [BLF]
    Active=YES

L’insieme di telefoni è specificato nel file devices presente nella cartella config.

Esempio di file devices:

.. code-block:: ini

    line 17.0.0.4=4404,4414,
    CISCO LINE: [SEP00112F557BFD] (3024)=3024,
    int_8002 (.)=8002,
    sip:2200@192.168.0.59=2200,
    arossi=2213,

.. important:: La sintassi è: device=dn,  

Descrizione degli interni (DN)
===============
E' possibile che il campo lampade associ al numero di interno (DN) la descrizione associata sulla rubrica interna/esterna eseguendo all'avvio una ricerca su database. Per attivare questa funzionalità è necessario che sia attivo il modulo database e che il parametro QueryDescription della sezione BLF sia impostato a YES.

.. code-block:: ini

    [BLF]
    Active=YES
    QueryDescription=YES



BLF  in Ambiente Tapi Cisco / Avaya-IPOffice / Innovaphone 
===============
Il parametro da configurare in *tabparam.ini* è Type=TAPI nella sessione [BLF].

.. note ::  Per Avaya IPOffice occorre acquistare la licenza PBX di” link cti pro”.


BLF  in Ambiente SIP
===============
Il parametro da configurare in *tabparam.ini* è Type=SIP nella sessione [BLF].

In ambiente SIP il servizio TConsoleServer  si ausiglia dell’applicativo TsipBLFServer.exe.


I parametri di fondamentale configurazione nel file *tabparam.ini* sono i seguenti:

.. code-block:: ini

    [SIPBLFSERVER] 
    OUTBOUND_PROXY=192.168.0.59
    REGISTRAR=192.168.0.59

    ;	USER e PASSWORD per registrarsi (come telefono) al fine di ottenere dalla centrale lo stato delle lampade  (configurare un interno affinchè si possano ricevere le subscription)
    USER=2350
    PASSWORD=2350

    ;	Indirizzo IP della macchina che ospita il servizio TConsoleServer. Verrà associato allo User Agent specificato dai parametri -su e -sp. Se omesso il processo cercherÓ automaticamente l'interfaccia di rete che raggiunge il PBX-SIP, in questo caso verificare l'opzione -int.
    SIPBLFSERVER_IP=192.168.0.12

    ;	Se omessa l'opzione SIPBLFSERVER_IP il processo cerca automaticamente l'interfaccia di rete che raggiunge il PBX-SIP. Il valore in ms e' il timeout scaduto il quale un'interfaccia di rete viene giudicata non idonea a
    ;	raggiungere il PBX-SIP
    IP_NETWORKINTERFACE_TIMEOUT=3000

    ;	TCS (TConsole Server) host (default: 127.0.0.1)
    TCS_HOST = 127.0.0.1
    ;	TCS (Telenia Console Server) port (default: 6598)
    TCS_PORT = 6598

    ;	Modalità di esecuzione (parametro case-insensitive, default: tcs-client)
    ;	tcs-client:  Processo client del TCS. E' obbligatorio che si instauri la connessione socket.
    ;            I parametri di connessione al server sono: TCS_HOST, TCS_PORT
    ;	tcs-windows: Processo client del TCS. E' obbligatorio che si instauri la connessione socket.
    ;              I parametri di connessione al server sono: TCS_HOST, TCS_PORT
    ;              Viene visualizzata all'avvio una finestra non chiudibile.
    ;	windows: Viene visualizzata all'avvio una finestra e NON viene instaurata alcuna
    ;              connessione socket  verso il TCS.
    ;	si setta tcs-client per s.o. windows server 2003, 2008 e seven i quali hanno difficoltà 
    ;             nella visualizzazione delle form per i servizi
    MODALITY=tcs-windows


BLF in ambiente Telenia TVOX
===============
In ambiente Telenia TVox il campo lampade può essere gestito come “BLF in ambiente SIP” per un numero limitato di interni.
Sempre per un numero limitato di interni il campo lampade può essere configurato anche nel seguente modo: 
*tabparam.ini*:

Type=TVOX nella sessione [BLF].

.. code-block:: ini

    [TVOXPARAMS]
    ; IP del TVOX
    TVOX_IP=159.213.33.10
    ; Utente per connessione al TVOX da parte del TConsoleServerStd
    TVOX_USER=polampade
    ; Password per connessione al TVOX da parte del TConsoleServerStd
    TVOX_PASSWORD=polampade
    ; Time sleep tra la richiesta dello stato di un device e la richista dello stato del device sucessivo
    TVOX_SLEEP_OPEN_DEVICE=100

.. note :: CAMPO LAMPADE CON UN NUMERO DI INTERNI MAGGIORE.
    Per una quantità maggiore di interni da controllare è preferibile utilizzare il servizio TBLFServer in sostituzione del servizio TConsoleServer (in questo caso il TConsoleServer non deve essere in funzione).
    Per installare il TBlfServer è sufficiente copiare bin e config in c:\Programmi\Telenia\ TBlfServer e lanciare il batch Add_TBlfServer_svc.bat che si trova in bin (per installare il servizio).
    Il servizio TBLFServer non ha bisogno ne di BDE ne di Runtime. Ha bisogno di tutti i file di ambiente (\setup\...\ambiente\BDS2006) da copiare in \windows\system32 per macchine a 32 bit o   C:\Windows\SysWOW64 per macchine a 64.


BLF in ambiente TAPI Telenia Barratel Server
===============
Affinchè il campo lampade sia aggiornato è necessario che riceva informazioni (TAPI) dal modulo Telenia BarratelServer. Impostare quindi correttamente i parametri della sezione
BARRATELSERVER nel file *tabparam.ini*.

.. code-block:: ini

    [BARRATELSERVER]
    Ip=192.168.0.4
    Port=5450

BLF in ambiente TSAPI AVAYA CM 6.2 
===============
Da TConsole 7.2 è possibile gestire il campo BLF per Avaya CM 6.2 via TSAPI.

Per ottenere il funzionamento del BLF, sulla stessa macchina il a macchina su cui risiede il TConsoleServer da rel 3.1 deve essere  installato il tsapi-client-win32-6_2-257 ( a cura del tecnico di centrale).

Impostare quindi correttamente i parametri della sezione BLF e CSTAPARAMS  nel file *tabparam.ini*.

.. code-block:: ini

    [BLF]
    Type=CSTA
    [CSTAPARAMS]
    LOGICAL_LINK=AVAYA#CM#CSTA#TELENIA1-AES1
    LINK_VERSION=ECS2-6
    LINK_USER=Telenia
    LINK_PASSWORD=!Telenia01

I parametri definiti nella zona CSTAPARAMS vengono comunicati dal tecnico di centrale, i quali si riferiscono alla connessione su Avaya AC server AES.


Di seguito i parametri per alzare il livello di log, presenti in *tabparam.ini*

.. code-block:: ini

    [GLOBAL]
    ENABLE_DB_CONN=NO
    ;	Valori LOG_LEVEL ammessi:
    ;		0: Solo segnalazioni di Start e Stop.
    ;		1: Livello precedente + segnalazioni di mafunzionamenti/errori
    ;		2: Livello precedente + segnalazioni di operazioni che vanno a buon fine
    ;		3: Livello precedente + messaggi di comunicazione client server
    LOG_LEVEL=2

Il TConsoleServerStd come tutti gli altri exe che usano le dll necessita delle DLL ATTPRV32.dll e Csta32.dll aggiornate.