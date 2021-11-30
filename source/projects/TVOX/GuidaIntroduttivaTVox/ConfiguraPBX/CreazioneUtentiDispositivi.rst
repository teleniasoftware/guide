.. _creazione_interni&dispositivi:

Creazione Utenti e Dispositivi
==============================



Creazione Utenti tramite import
===============================







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




Creazione Utenti tramite configurazione diretta su occ
======================================================

Per la configurare le utenze PBX direttamente su OCC andare nella sezione *Gestione=>Utenti*.

In fase di creazione è necessario configurare la parte relativa all'*anagrafica*

.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/CreazioneUtentiDispositivi/03-Anagrafica.JPG

Assegnare poi il *Prfilo Principale* selezionando la voce *Utente*

.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/CreazioneUtentiDispositivi/04-ProfiloPrincipale.JPG


Associare poi i dispositivi telefonici (esempio: APP, Client, WEB, dispositivi fisici)

.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/CreazioneUtentiDispositivi/05-Dispositivi.JPG

.. warning:: **ATTENZIONE:** Per l'utenza con Profilo *Utente* è necessario associare almeno un dispositivo fisico.
    
Per fare in modo che l'utenza possa eseguire chiamate Outbound esterne al TVOX è necessario configurare opportunamente *Abilitazione* e *Filtro*

.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/CreazioneUtentiDispositivi/06-Abilitazioni.JPG

Opzionale: Nel caso l'utente debba far parte di uno o più gruppi di risposta è possibile  associarli nella sezione *Gruppi di Risposta*

.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/CreazioneUtentiDispositivi/07-GruppoDiRisposta.JPG

.. warning:: **BEST PRACTICE:** Se l'utenza creata non si autentica tramite LDAP in fase di configurazione della stessa è importante inserire una password complessa che rispetti i criteri di sicurezza riportati nell'immagine seguente.

    .. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/CreazioneUtentiDispositivi/08-Criteri-di-Sicurezza.JPG