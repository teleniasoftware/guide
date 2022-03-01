==============================
Creazione Utenti e Dispositivi
==============================

.. toctree::
    :maxdepth: 5

    ./CreazioneUtentiDispositivi/Provisioning
    ./CreazioneUtentiDispositivi/Creazione_utenti_OCC
    ./CreazioneUtentiDispositivi/Creazione_utenti_Import


Creazione Utenti tramite configurazione diretta su OCC
======================================================

Tramite OCC è possibile configurare direttamente una utenza PBX andando a specificare le seguenti informazioni: username,
password, interni da associare, email, cellulare, abilitazioni all'utilizzo del client, redirezione su numeri esterni, deviazione di chiamata, gruppi di risposta / skill, Classe di servizio
(es: Abilitazione, Filtro, Registrazione conversazioni) gruppi di Pick-up, abilitazioni di Voicemail, Conferenza e definizione di caselle FAX ove disponibili.

Da OCC andare nella sezione *Gestione=>Utenti*.

In fase di creazione è necessario configurare la parte relativa all'*anagrafica*, dove oltre alle credenziali di accesso (username e password), 
è possibile andare a definire email, numero di cellulare e sito utente.


.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/CreazioneUtentiDispositivi/03-Anagrafica.JPG

.. note:: Nel caso si abbia la necessità di aggiungere ulteriori campi identificativi dell'utenza (esempio: Azienda, Settore, Competenza), è possibile aggiungere fino a 10 ulteriori campi custom. Per configurare tali campi andare da OCC nella sezione *Gestione=>Rubriche=>Campi rubrica interna*.



Assegnare poi il *Profilo Principale* selezionando la voce *Utente*

.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/CreazioneUtentiDispositivi/04-ProfiloPrincipale.JPG


A seguire dovranno essere associati i dispositivi telefonici (esempio: APP, Client, WEB, dispositivi fisici)**

.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/CreazioneUtentiDispositivi/05-Dispositivi.JPG

.. warning:: **ATTENZIONE:** Per l'utenza con Profilo *Utente* è necessario associare almeno un dispositivo SIP.
    

Per fare in modo che l'utenza possa eseguire chiamate Outbound esterne al TVOX è necessario configurare opportunamente *Abilitazione* e *Filtro*

.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/CreazioneUtentiDispositivi/06-Abilitazioni.JPG

**Opzionale**: Nel caso l'utente debba far parte di uno o più gruppi di risposta è possibile associarli nella sezione *Gruppi di Risposta*

.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/CreazioneUtentiDispositivi/07-GruppoDiRisposta.JPG

.. important:: **BEST PRACTICE:** Se l'utenza creata non si autentica tramite LDAP in fase di configurazione della stessa è importante inserire una password complessa che rispetti i criteri di sicurezza riportati nell'immagine seguente.

    .. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/CreazioneUtentiDispositivi/08-Criteri-di-Sicurezza.JPG


Per configurare la **casella vocale** dell'utente, andare nella sezione *PBX* 

    .. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/CreazioneUtentiDispositivi/CasellaVocale.JPG

Per configurare la **stanza di conferenza** dell'utente, andare nella sezione *PBX* 

    .. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/CreazioneUtentiDispositivi/Conferenza.JPG

.. note:: Sezione PBX

        Nella sezione PBX di ogni singola utenza si possono definire:

        - PIN per accesso telefonico
        - Lista di accesso
        - Abilitazione per Authorization code
        - Redirezione su numeri esterni


        .. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/CreazioneUtentiDispositivi/ImpostazioniTelefono.JPG
        
        **Pin per accesso telefonico**:  Numero di identificazione personale dell'utente TVox Omnichannel Contact Center.
        Necessario per utilizzare correttamente le seguenti funzionalità telefoniche:
   
        - Blocca / Sblocca il telefono 
   
        - Chiamate in uscita nel contesto di Authorization code (fare riferimento a Avanzate ⇒ Canale Telefonico ⇒ Codici di servizio) 
   
        - Intrusione valida solo per i supervisori opportunamente configurati (fare riferimento al menu Avanzate ⇒ Canale Telefonico ⇒ Codici di servizio). 
        
        **Lista di accesso**: L'utente può essere dotato di una lista di accesso di tipo BLACK List o WHITE List tra quelle già definite. Le liste di accesso sono quelle definite dal menù Telefono ⇒ Liste di accesso

        **Abilitazione per 'Authorization Code'**: Abilitazione telefonica per le chiamate uscenti effettuate in contesto Authorization Code. Per accedere alla prestazione è necessario sia definito il PIN nella sezione PBX che deve essere fornito al TVox Communication in fase di accesso alla funzionalità.

        **Redirezione su numeri esterni**: Abilita/Disabilita la possibilità per l'utente di redirigere chiamate (call-forward) verso numeri esterni al TVox Communication sia via telefono sia via element manager. 
        
        
        
.. warning:: **ATTENZIONE:**  La prestazione *Redirezione su numeri esterni* non va confusa con la possibilità di contattare e quindi trasferire chiamate verso numerazioni esterne che è invece resa possibile dall'abilitazione telefonica (più eventuale filtro) che l'amministratore ha assegnato all'utente.

.. warning:: **ATTENZIONE:** In fase di deviazione è possibile presentare il clid del chiamante nella deviazione proveniente dallo stesso sito utente. Permette di presentare il CLID del chiamante se la deviazione della chiamata a numeri esterni per chiamate interne proviene dallo stesso sito. 
        **ES**: Se utente A chiama utente B che sono all'interno dello stesso sito, la chiamata verrà presentata con il CLID del chiamante, se invece utente A e utente B fossero su due siti diversi, la chiamata si presenterebbe con il CLID del deviante



E\' anche possibile configurare eventuali **Passante, Gruppi di pickup e Liste di numeri Brevi** 

.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/CreazioneUtentiDispositivi/UtentePBX.JPG


Creazione Utenti tramite import
===============================

Per effettuare la creazione utenti tramite import, bisogna accedere alla sezione OCC *Impostazioni=>Avanzate=>Import utenti da file*. 

In questa sezione è possibile importare dei nuovi utenti all'interno del TVox. Per effettuare una corretta importazione è necessario scaricare il file xls di template presente e popolarlo opportunamente rispetto agli utenti che si vogliono importare. All'interno del template si troveranno anche i codici da utilizzare per poter selezionare i campi multipli di un utente.

.. important:: **BEST PRACTICE:** Una volta scaricato il file di template, non bisogna effettuare modifiche su altri componenti del TVox fino all'import del file, in quanto potrebbero cambiare i codici che identificano delle particolari configurazioni.

.. warning:: **ATTENZIONE:** il file deve sempre essere scaricato dall'OCC nello stesso momento in cui si intende andare a popolarlo. Questo perchè il template includerà sempre una componente dinamica i codici e le eventuali abilitazioni che sono già presenti sul sistema, come i filtri, le abilitazioni e i dispositivi inseriti.

**Come importare solo dispositivi**: Per importare solo i dispositivi è necessario compliare il foglio nominato "dispositivi sip" non inserendo alcun dato sulla colonna username. In questo modo verrà creato un dispositivo per ogni riga compilata e non verrà associato a nessun utente.

**Come importare solo utenti**: Per importare solo utenti è necessario compliare il foglio "anagrafica" inserendo le informazioni base dell'utente (username, password, pin, nome, cognome, ecc...) e poi compilare il foglio "profili utente" con le specifiche del profilo utente linkando, tramite la colonna username, le informazioni di anagrafica con quelle dell'utente che si sta creando. È possibile inserire un solo profilo di tipo utente.

**Come importare solo agenti**: Per importare solo agenti è necessario compliare il foglio "anagrafica" inserendo le informazioni base dell'agente (username, password, pin, nome, cognome, ecc...) e poi compilare il foglio "profili agente" con le specifiche del profilo agente linkando, tramite la colonna username, le informazioni di anagrafica con quelle dell'agente che si sta creando. È possibile inserire più profili agente su un utente.

**Come abilitare una feature di tipo "Flag"**: Per abilitare una casella di tipo "Flag" (ES: flag-webclient, flag-webclient-webphone, flag-app, flag-mcs ) è sufficente inserire qualsiasi carattere all'interno della cella perchè il sistema capisca che è abilitato

.. warning:: **ATTENZIONE:** L'import di Dispositivi e/o Utenti può essere utilizzato solo per la creazione degli stessi, e non per la modifica. 

Le pagine "entity-filtro", "entity-abilitazione", "entity-registrazione", "entity-lingua", "entity-device" indicano gli ID che devono essere inseriti nelle colonne delle altre pagine:

**"entity-filtro":** usato nella pagina "profili utente" nella colonna "filtro" e nella pagina "profili agente" nella colonna "filtro".

**"entity-abilitazione":** usato nella pagina "profili utente" nella colonna "abilitazione" e nella pagina "profili agente" nella colonna "abilitazione".

**"entity-registrazione":** usato nella pagina "profili utente" nella colonna "Registrazione conversazioni" e nella pagina "profili agente" nella colonna "Registrazione conversazioni".

**"entity-lingua":** usato nella pagina "anagrafica" nella colonna "lingua".

**"entity-device":** usato nella pagina "dispositivi sip" nelle colonne "Vendor" e "Model".

La procedura di caricamento va a validare il file xls prima ancora di caricare i dati, permettendo di non caricare la macchina e di avere l'output degli errori con riferimento della riga.

Passato il controllo formale, il parsing del file indicherà il contenuto da importare e quindi il totale di Dispositi e/o Utenti. 