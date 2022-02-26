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

.. note:: **Esclusione utenti da autenticazione**. Nel caso sia attivi l'autenticazione tramite LDAP, è possibile escludere dal controllo utenze specifiche.
    Affinchè tali utenze possano accedere a OCC o al client è necessario che inseriscano la password impostata direttamente su OCC.

    Per configurare tali utenze è necessario andare da OCC nella sezione *SISTEMA=>LDAP esterno=>Autenticazione utente su LDAP*

     .. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/LDAP/Esclusione.JPG 

.. note:: **Test Login**. Nella sezione *SISTEMA=>LDAP esterno=>Autenticazione utente su LDAP* è presente un form permette di testare una reale login di utente sul client TVox utilizzando l'autenticazone LDAP (nel caso in cui sia abilitata) oppure l'autenticazione TVox (nel caso in cui l'utente sia escluso oppure non ci sia l'autenticazione LDAP).

    .. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/LDAP/TestLogin.JPG

Importazione utenti da server LDAP
==================================

Configurazione
--------------


Nel caso di connessione TVOX tramite Active Directory, oltre alla gestioen dell'autenticazione, è possibile importare e sincronizzare utenti da server LDAP.

L'importazione di utenti da una fonte LDAP richiede che venga fornita una precisa mappatura tra gli attributi specificati sul server LDAP ed i valori tipici per l'utente delle applicazioni Telenia.

Tale associazione avviene andando da OCC nella sezione *SISTEMA => Configurazione di sistema => LDAP Esterno* ed editare il nome di donimio creato. 
Andare poi nel TAB *Configurazione importazione*.
 
.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/LDAP/IMPORT01.JPG

Per ogni mappatura è anche possibile impostare la modalità di aggiornamento dati com eindicato nella figura sottostante

.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/LDAP/IMPORT02.JPG


.. important:: **Configurazioni default TVox per gli utenti importati**. Quando si importano utenti da una fonte LDAP possono essere necessarie manipolazioni del contenuto di attributi indispensabili come Numerazione interna e la definizione di variabili tipiche del sistema telefonico TVox Communication 
    
    .. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/LDAP/IMPORT03.JPG
Per i dettagli della manipolazione della numerazione interna si rimanda all'Help On Line presente in OCC


Import
--------------

Una volta configurata la sezione relativa alla configurazione *Import utenti da LDAP* e possibile sia importare manualmente che eseguire schdualzioni di import.

Per importare manualmente andare nel TAB *Importazione utenti*.

- Premendo il pulsante **Recupera utenti**, verranno recuperati tutti gli utenti disponibili

- Premendo il pulsante **Importa**, gli utenti selezionati verranno importati


.. note:: E\' anche possibile selezionare i singoli utenti ed escluderli dall'import in modo che ai successivi recuperi o schedulazioni di import, gli stessi non vengano importati
    
    .. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/LDAP/IMPORT04.JPG

Per programmare la schedulazione andare da OCC nella sezione *SISTEMA => Configurazione di sistema => LDAP Esterno => Lista di server LDAP* e nel TAB *Importazione utenti* ed impostare la frequenza di schedulazione

.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/LDAP/IMPORT05.JPG