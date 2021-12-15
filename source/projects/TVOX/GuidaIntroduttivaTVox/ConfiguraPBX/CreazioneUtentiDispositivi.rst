==============================
Creazione Utenti e Dispositivi
==============================

.. toctree::
    :maxdepth: 5

    ./CreazioneUtentiDispositivi/Provisioning
    ./CreazioneUtentiDispositivi/Creazione_utenti_OCC
    ./CreazioneUtentiDispositivi/Creazione_utenti_Import



Creazione Utenti tramite import
===============================
Per effettuare la creazione utenti tramite import, bisogna accedere alla sezione OCC *Impostazioni=>Avanzate=>Import utenti da file*. 

In questa sezione è possibile importare dei nuovi utenti all'interno del TVox. Per effettuare una corretta importazione è necessario scaricare il file di template presente e popolarlo opportunamente rispetto agli utenti che si vogliono importare. All'interno del template si troveranno anche i codici da utilizzare per poter selezionare i campi multipli di un utente.

.. important:: **BEST PRACTICE:** Una volta scaricato il file di template, non bisogna effettuare modifiche su altri componenti del TVox fino all'import del file, in quanto potrebbero cambiare i codici che identificano delle particolari configurazioni.

.. warning:: **ATTENZIONE:** il file deve sempre essere scaricato dall'OCC nello stesso momento in cui si intende andare a popolarlo. Questo perchè il template includerà sempre una componente dinamica i codici e le eventuali abilitazioni che sono già presenti sul sistema, come i filtri, le abilitazioni e i dispositivi inseriti.


Provisioning dei dispositivi nel caso di TVox Pure Cloud
========================================================


In ambiente cloud non è possibile affidarsi alla prestazione di auto-provisioning basato su DHCP.
E\' raccomandata l'abilitazione del provisioning sicuro via OCC dalla sezione *Impostazioni=>Avanzate=>Sicurezza* impostando il parametro "Sicurezza provisioning telefoni" con il valore "Sicuro e RPS".

In tal modo, nel caso si utilizzino dispositivi Yealink, sarò possibile sfruttare il provisioning via RPS (Redirect & Provisioning Service), servizio offerto da Yealink che consente il provisioning automatico del telefono al primo avvio (a seguito di un reset alle condizioni di fabbrica.

.. important:: ** BEST PRACTICE** Contestualmente si raccomanda di impostare anche il livello di sicurezza per password SIP e utente. L'OCC impedirà di salvare utenti e interni con password che non rispettano adeguati standard di sicurezza.

.. warning:: **ATTENZIONE:** La modifica del parametro "Sicurezza e password utente" porta al riavvio del servizio di autenticazione. Per il tempo necessario al riavvio, non sarà possibile eseguire login.

.. image:: /images/TVOX/PureCloud/02-sicurezza-password-provisioning.png


Con la configurazione del provisioning sicuro, per ogni telefono è presente un URL di provisioning univoco che può essere impostato manualmente sul dispositivo.

.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/CreazioneUtentiDispositivi/01-url-provisioning-purecloud.png

.. Nel caso di telefoni Yealink, 

.. :ref:`Sistemi Pure Cloud <infrastruttura>`


Nel caso di telefoni Yealink, è attivo il provisioning via `RPS <https://support.yealink.com/forward2download?path=ZIjHOJbWuW/DFrGTLnGyploAOxsQD/Xz/UplusSymbolq2lU036653TDiwrBfxz/BElK2gRiufplusSymbolXfMogMSzUeDNTfeK4uKrmJcySPdH5L6ZCVAIWLplusSymbollC7wlpLKz2kk42E24Q/8gRHNqUuQjL5uO4PYwC7Imh4ImwA/4cqC85uucVf7CWTgMYFEei8fLjhNLml5splusSymbolGQxnXU11oQ3XOigo=>`_. Si tratta di un servizio di Yealink che permette ad un telefono, alla prima accensione, di effettuare automaticamente una richiesta web per individuare il server TVox dal quale scaricare la sua configurazione, eliminando quindi la necessità di una pre-configurazione manuale.
Ricevuta tale informazione, il telefono invierà direttamente la richiesta di provisioning a tale url.

Per questioni di sicurezza, TVox permette una sola configurazione via RPS. Per provisionare nuovamente il telefono è necessario sbloccare manualmente il provisioning RPS tramite un apposito pulsante disponibile in OCC.

**Eseguire il provisioning di un telefono Yealink**

#. Creare l'interno su OCC - In questo modo viene creato l'url univoco di provisioning associato al MAC Address del telefono. Tale url viene comunicato da TVox al server RPS di Yealink
#. Togliere dalla scatola il telefono ed accenderlo
#. Attendere che la configurazione del telefono si completi (il telefono si riavvierà automaticamente alcune volte)
#. Il telefono risulta registrato su TVox e disponibile all'utilizzo

.. tip:: Il provisioning via RPS è disponibile alla prima accensione o dopo un reset alle condizioni di fabbrica. Per ripetere questo tipo di configurazione, prima di procedere al reset devi sbloccare il provisioning RPS come indicato nella prossima immagine

.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/CreazioneUtentiDispositivi/02-provisioning-rps.png




Creazione Utenti tramite configurazione diretta su OCC
======================================================

Tramite OCC è possibile configurare direttamente una utenza PBX andando a specificare le seguenti informazioni: username,
password, interni da associare, email, cellulare, abilitazioni all'utilizzo del client, redirezione su numeri esterni, deviazione di chiamata, gruppi di risposta / skill, Classe di servizio
(es: Abilitazione, Filtro, Registrazione conversazioni) gruppi di Pick-up, abilitazioni di Voicemail, Conferenza e definizione di caselle FAX ove disponibili.

**Da OCC andare nella sezione "Gestione=>Utenti".**

In fase di creazione è necessario configurare la parte relativa all'*anagrafica*, dove oltre alle credenziali di accesso (username e password), 
è possibile andare a definire email, numero di cellulare e sito utente.


.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/CreazioneUtentiDispositivi/03-Anagrafica.JPG

.. note:: Nel caso si abbia la necessità di aggiungere ulteriori campi identificativi dell'utenza (esempio: Azienda, Settore, Competenza), è possibile aggiungere fino a 10 ulteriori campi custom. Per configurare tali campi andare da OCC nella sezione *Gestione=>Rubriche=>Campi rubrica interna*.



**Assegnare poi il "Profilo Principale" selezionando la voce "Utente"**

.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/CreazioneUtentiDispositivi/04-ProfiloPrincipale.JPG


**A seguire dovranno essere associati i dispositivi telefonici (esempio: APP, Client, WEB, dispositivi fisici)**

.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/CreazioneUtentiDispositivi/05-Dispositivi.JPG

.. warning:: **ATTENZIONE:** Per l'utenza con Profilo *Utente* è necessario associare almeno un dispositivo SIP.
    

Per fare in modo che l'utenza possa eseguire chiamate Outbound esterne al TVOX è necessario configurare opportunamente *Abilitazione* e *Filtro*

.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/CreazioneUtentiDispositivi/06-Abilitazioni.JPG

**Opzionale**: Nel caso l'utente debba far parte di uno o più gruppi di risposta è possibile associarli nella sezione *Gruppi di Risposta*

.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/CreazioneUtentiDispositivi/07-GruppoDiRisposta.JPG

.. important:: **BEST PRACTICE:** Se l'utenza creata non si autentica tramite LDAP in fase di configurazione della stessa è importante inserire una password complessa che rispetti i criteri di sicurezza riportati nell'immagine seguente.

    .. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/CreazioneUtentiDispositivi/08-Criteri-di-Sicurezza.JPG


Per configurare la **casella vocale** dell'utente andare nella sezione *PBX* 

    .. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/CreazioneUtentiDispositivi/CasellaVocale.JPG

Per configurare la **stanza di conferenza** dell'utente andare nella sezione *PBX* 

    .. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/CreazioneUtentiDispositivi/Conferenza.JPG

.. note:: Impostazioni Telefono
        .. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/CreazioneUtentiDispositivi/ImpostazioniTelefono.JPG
        *Pin per accesso telefonico*: Numero di identificazione personale dell'utente TVox Omnichannel Contact Center.
        Necessario per utilizzare correttamente le seguenti funzionalità telefoniche:
        - Blocca / Sblocca il telefono 
        - Chiamate in uscita nel contesto di Authorization code (fare riferimento a Avanzate ⇒ Canale Telefonico ⇒ Codici di servizio) 
        - Intrusione valida solo per i supervisori opportunamente configurati (fare riferimento al menu Avanzate ⇒ Canale Telefonico ⇒ Codici di servizio). 
        
E' anche possibile configurare eventuali **Passante, Gruppi di pickup e Liste di numeri Brevi** 

.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/CreazioneUtentiDispositivi/UtentePBX.JPG