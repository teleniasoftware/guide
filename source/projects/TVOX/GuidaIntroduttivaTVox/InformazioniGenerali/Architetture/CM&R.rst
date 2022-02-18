.. _CM&R:

==================================================
TVox Ridondato - Continuous Monitoring & Reporting
==================================================

Un TVox può essere ridondato attraverso la predisposizione di due piattaforme dislocate in LAN o in WAN realizzando un cluster di **Fault Tolerance**

La ridondanza permette quindi la continuità del servizio anche nel caso in cui una delle due piattaforme non sia più disponibile.

La ridondanza è garantita da un sistema di monitor tra le due piattaforme TAM e da
processi di sincronizzazione di configurazioni (**DataBase replication**) e dati (**synch file
system**) in real time tra Master e TVox Slave. 

.. image:: /images/TVOX/CM_R/FaultTolerance.PNG
   :scale: 60%
   :align: center


.. note:: Il funzionamento in modalità ridondata prevede che quando il sistema Master risulta inaccessibile allo Slave quest'ultimo si elegge automaticamente Master attivando sulla propria interfaccia di rete l'IP TVox e consentendo a tutti i dispositivi SIP di proseguire nel loro normale funzionamento. Tale architettura permette di evitare politiche di Failover sui dispositivi SIP che inevitabilmente introdurrebbero delle latenze ulteriori e semplificarne la configurazione

.. important :: 
    **Per mantenere l'erogazione dei dati di reportistica esposti tratmite OCC, è necessario che le due piattaforme siano allineate**

Requisiti
=========

Tale architettura richiede la configurazione di almeno 3 indirizzi IP, un indirizzo IP fisico per ognuno dei due sistemi e il terzo virtuale da utilizzare come IP TVox su cui verranno
registrati tutti i telefoni SIP ed eventuali ATA FXS.



.. important :: Un vincolo essenziale per il sistema ridondato è legato al fatto che TVox Master e Slave devono reciprocamente risultare accessibili con continuità: viene demandato quindi agli apparati hardware e software che compongono l'infrastruttura di rete dell'utente finale il compito fondamentale di mantenere costantemente accessibili le due piattaforme.

Configurazione
==============

Per andare a configurare la parte faul tolerance è necessario andare da OCC nella sezione *Configurazione di Sistema -> Rete - Fault tolerance* ed impostare i rifeirmenti ip della machcina ridondata e del nodo.

.. important :: La procedura di configurazione di machcine ridondate prevede che entrambi le machcine siano licenziate e poi andare a configurare la parte di fault tilerance su tutte e due con successivo riavvio.
    
