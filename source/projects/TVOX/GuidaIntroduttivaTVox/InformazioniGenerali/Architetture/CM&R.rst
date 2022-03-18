.. _CM&R:

==================================================
TVox Ridondato - Continuous Monitoring & Reporting
==================================================

TVox può essere ridondato attraverso la predisposizione di due server dislocati in LAN o in WAN che sono tra loro sincronizzati realtime a livello di Database e di File System (per la
componente file system è possibile configurare il limite di consumo di banda).

L'architettura che si va a costruire prevede che uno dei due server assuma il ruolo di Master mentre l'altro il ruolo di Slave, realizzando un cluster di **Fault Tolerance**.

Tale architettura richiede la configurazione di almeno 3 indirizzi IP:
- un indirizzo IP fisico per ognuno dei due sistemi 
- un cosiddetto IP TVox (o IP di nodo) che verrà attivato su un'interfaccia di rete virtuale dal TVox con ruolo Master, e che sarà l'indirizzo IP sul quale verranno erogati tutti i servizi applicativi (ad esempio, sarà l'indirizzo sul quale verranno registrati i dispositivi SIP)

La ridondanza è garantita da un sistema di monitor tra i due TVox e da processi di sincronizzazione di configurazioni (**DataBase replication**) e dati (**synch file
system**) in real time tra TVox Master e TVox Slave. 

.. image:: /images/TVOX/CM_R/FaultTolerance.PNG
   :scale: 60%
   :align: center


.. note:: Il funzionamento in modalità ridondata prevede che, quando il sistema Master risulta inaccessibile allo Slave, quest'ultimo attivi automaticamente l'IP TVox sulla propria interfaccia di rete virtuale eleggendo sè stesso al ruolo Master e consentendo a tutti i dispositivi di proseguire nel loro normale funzionamento. Tale architettura permette di evitare politiche di failover sui dispositivi SIP che inevitabilmente introdurrebbero delle latenze ulteriori e semplificarne la configurazione.

L'architettura ridondata permette la completa accessibilità ai dati storici dell'impianto, che sono resi disponibili in tempo reale sul server con ruolo Slave, permettendo in tal modo di effettuare richieste di elaborazione e presentazione dati senza pesare sulle risorse del server che eroga servizi applicativi.

.. important:: E\' per tale motivo che questo tipo di architettura è denominata **Continuous Monitoring & Reporting**: un corretto stato di allineamento del cluster consente di avere la disponibilità costante di dati grezzi, analitici e statistici.



Requisiti
=========

Tale architettura richiede la configurazione di almeno 3 indirizzi IP, un indirizzo IP fisico per ognuno dei due sistemi e il terzo virtuale da utilizzare come IP TVox su cui verranno
registrati tutti i telefoni SIP ed eventuali ATA FXS.



.. important :: Un vincolo essenziale per il sistema ridondato è legato al fatto che TVox Master e Slave devono reciprocamente risultare accessibili con continuità: viene demandato quindi agli apparati hardware e software che compongono l'infrastruttura di rete dell'utente finale il compito fondamentale di mantenere costantemente accessibili le due piattaforme.


Configurazione
==============

Per andare a configurare la parte faul tolerance è necessario andare da OCC nella sezione *Configurazione di Sistema -> Rete - Fault tolerance* ed impostare i rifeirmenti ip della machcina ridondata e del nodo.

.. important :: La procedura di configurazione di macchine ridondate prevede che entrambi le macchine siano licenziate e poi andare a configurare la parte di fault tilerance su tutte e due con successivo riavvio.
    


