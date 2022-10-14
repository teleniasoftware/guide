.. _CM&R:

==================================================
TVox Ridondato - Continuous Monitoring & Reporting
==================================================

TVox può essere ridondato attraverso la predisposizione di due server dislocati in LAN o in WAN che sono tra loro sincronizzati realtime a livello di Database e di File System (per la
componente file system è possibile configurare il limite di consumo di banda).

L'architettura che si va a costruire prevede che una delle due istanze assuma il ruolo di Master mentre l'altra il ruolo di Slave, realizzando un cluster di **Fault Tolerance**.

La ridondanza è garantita da un sistema di monitor tra i due TVox e da processi di sincronizzazione di configurazioni (**DataBase replication**) e dati (**synch file
system**) in real time tra TVox Master e TVox Slave. 

.. image:: /images/TVOX/CM_R/FaultTolerance.PNG
   :scale: 60%
   :align: center



L'architettura ridondata permette la completa accessibilità ai dati storici dell'impianto, che sono resi disponibili in tempo reale sul server con ruolo Slave, permettendo in tal modo di effettuare richieste di elaborazione e presentazione dati senza pesare sulle risorse del server che eroga servizi applicativi.

.. warning:: La procedura di configurazione di macchine ridondate prevede che entrambi le macchine siano licenziate e poi andare a configurare la parte di fault tolerance su tutte e due con successivo riavvio.
 
.. important:: E\' per tale motivo che questo tipo di architettura è denominata **Continuous Monitoring & Reporting**: un corretto stato di allineamento del cluster consente di avere la disponibilità costante di dati grezzi, analitici e statistici.


Esistono due tipi di architettura possibili a 
seconda che l'installazione sia o meno in **Pure Cloud**.

Architettura **non Pure Cloud**
===============================

Requisiti
---------

Tale architettura richiede la configurazione di almeno 3 indirizzi IP:

- un indirizzo IP fisico per ognuno dei due sistemi 
- un terzo indirizzo IP (chiamato IP TVox o IP di nodo) che verrà attivato su un'interfaccia di rete virtuale dal TVox con ruolo Master, e che sarà l'indirizzo IP sul quale verranno erogati tutti i servizi applicativi (ad esempio, telefoni SIP, ATA FXS, trunk, etc...)

.. note:: Il funzionamento in modalità ridondata prevede che, quando il sistema Master risulta inaccessibile allo Slave, quest'ultimo attivi automaticamente l'IP TVox sulla propria interfaccia di rete virtuale eleggendo sè stesso al ruolo Master e consentendo a tutti i dispositivi di proseguire nel loro normale funzionamento. Tale architettura permette di evitare politiche di failover sui dispositivi SIP che inevitabilmente introdurrebbero delle latenze ulteriori e semplificarne la configurazione.

.. important:: Un vincolo essenziale per il sistema ridondato è legato al fatto che TVox Master e Slave devono reciprocamente risultare accessibili con continuità: viene demandato quindi agli apparati hardware e software che compongono l'infrastruttura di rete dell'utente finale il compito fondamentale di mantenere costantemente accessibili le due piattaforme.


Configurazione
--------------

Per andare a configurare la parte fault tolerance è necessario andare da OCC nella sezione *SISTEMA -> Configurazione di sistema -> Rete -> Fault Tolerance* ed impostare i riferimenti ip della macchina ridondata e del nodo.

.. image:: /images/TVOX/CM_R/FaultTolerance_conf_LAN.PNG
   :scale: 60%
   :align: center



Architettura **Pure Cloud**
===============================

Requisiti
---------

In caso di Pure Cloud servono solo i due ip fisici che verranno assegnati alle due istanze in Cloud.
Lo switch di nodo può avvenire solamente andando da OCC nella sezione *Monitor* ed eseguendo delle attività manuali.

Lo switch da Master a Slave avviene nel seguente modo:


- Puntare al nome di dominio e andare da OCC nella sezione *SISTEMA -> Monitor di Sistema* e premere nella voce *STATO (master)* selezionando dal menu a tendina la voce *Servizi spenti*

   .. image:: /images/TVOX/CM_R/Monitor_PC.PNG
     :scale: 60%
     :align: center

- Da client di gestione Cloud spostare associazione ip pubblico da TVOX Master a TVOX Slave

- Puntare al nome di dominio e andare da OCC nella sezione *SISTEMA -> Monitor di Sistema* e premere nella voce *STATO (slave)* selezionando dal menu a tendina la voce *Master*

- Puntare all'ip pubblico della slave e andare da OCC nella sezione *SISTEMA -> Monitor di Sistema* e premere nella voce *STATO (off)* selezionando dal menu a tendina la voce *Slave*



Configurazione
--------------

Per andare a configurare la parte fault tolerance è necessario andare da OCC nella sezione *SISTEMA -> Configurazione di sistema-> Rete -> Fault Tolerance* ed impostare i riferimenti ip delle due macchine ridondate.


.. image:: /images/TVOX/CM_R/FaultTolerance_conf_PC01.PNG
   :scale: 60%
   :align: center


Andare poi sempre da OCC nella sezione *SISTEMA -> Configurazione di sistema -> Rete -> Dominio* ed impostare i riferimenti dominio e ip pubblico.

.. image:: /images/TVOX/CM_R/FaultTolerance_conf_PC02.PNG
   :scale: 60%
   :align: center


.. warning:: IP pubblico del sistema TVox tramite il quale è accessibile da internet.


  


