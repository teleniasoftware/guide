==================================
Collega TVox al tuo LDAP Aziendale
==================================

Configurazione server LDAP
==========================

Nel caso sia presente un sistema di autenticazione tramite *Active Directory*, è possibile integrarlo con il TVOX

La connessione ad un server LDAP esterno è utilizzata per le seguenti ragioni:

- **Importare utenti da server LDAP** (Importare e sincronizzare utenti da server LDAP semplifica la loro gestione)

- **Autenticare gli utenti utilizzando le credenziali del server LDAP** (Queste credenziali sono utilizzate dagli utenti per accedere alle applicazioni Telenia)

.. note:: E\' possibile avere anche più domini LDAP 

    .. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/LDAP/Domini.JPG


Per configurare i parametri di connessione ad un server LDAP esterno è necessario andare in OCC nella sezione *SISTEMA=> Configurazione di Sistema => LDAP Esterno.*


.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/LDAP/LDAP_configurazione.JPG

In tale sezione si dovranno impostare:

- **Nome dominio** unico senza caratteri di underscore (_), utilizzato per identificare il server LDAP esterno

- **Hostname o Indirizzo IP** del server LDAP esterno

- **Porta** Gateway per il server LDAP (il predefinito per plain / starttls è389, per ssl è 636)

- **Modalità di connessione al server LDAP esterno**

    - plain: la connessione non è sicura(la porta di accesso predefinita è la 389)

    - ssl: connessione sicura utilizzando SSL (Secure Socket Layer) (gateway predefinito 636)

- **DN o Username** con privilegi sul ramo LDAP contenente i dati utente

- **Password**

- **DN base per ricerca utenti** ovvero LDAP DN del ramo sul quale condurre la ricerca degli utenti

- **Filtro utenti** Filtro da applicare agli utenti forniti dal server LDAP (Parametro opzionale richiesto se nel Base DN sono anche memorizzati oggetti che non sono utenti)

- **DN Base per ricerca gruppi** ovvero LDAP DN del ramo sul quale condurre la ricerca dei gruppi

- **Filtro gruppi** Filtro da applicare ai gruppi forniti dal server LDAP (parametro opzionale)

- **Filtro lista gruppi** Filtro da applicare per mostrare tutti i gruppi forniti dal server LDAP (Default: "(objectClass=groupOfNames)")



Autenticazione tramite server LDAP
==================================
Per abilitare l'autenticazione utente sul server LDAP andare in OCC nella sezione *SISTEMA=> Configurazione di Sistema => LDAP Esterno* ed impostare il flag *Autenticazione tramite server LDAP*

.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/LDAP/LDAP_autenticazione.JPG

.. note:: **Esclusione utenti da autentizazione**. Nel caso sia attiva l'autenticazione tramite LDAP, è possibile escludere dal controllo utenze specifiche.
    Affinchè tali utenze possano accedere a OCC o al client è necessario che inseriscano la password impostata direttamente su OCC.

    Per configurare tali utenze è necessario andare da OCC nella sezione *SISTEMA=>LDAP esterno=>Autenticazione utente su LDAP*

     .. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/LDAP/Esclusione.JPG 

.. note:: **Test Login**. Nella sezione *SISTEMA=>LDAP esterno=>Autenticazione utente su LDAP* è presente un form permette di testare una reale login di utente sul client TVox utilizzando l'autenticazone LDAP (nel caso in cui sia abilitata) oppure l'autenticazione TVox (nel caso in cui l'utente sia escluso oppure non ci sia l'autenticazione LDAP).

    .. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/LDAP/TestLogin.JPG

Importazione utenti
===================