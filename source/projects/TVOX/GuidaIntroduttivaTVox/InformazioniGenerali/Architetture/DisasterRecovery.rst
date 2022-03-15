======================
TVox Disaster Recovery
======================

Con il termine **Disaster Recovery** (brevemente DR, in italiano: *Recupero dal Disastro*), in informatica ed in particolare nell'ambito della sicurezza informatica, si intende l'insieme delle misure tecnologiche e logistico/organizzative atte a ripristinare sistemi, dati e infrastrutture necessarie all'erogazione di servizi di business per imprese, associazioni o enti, a fronte di gravi emergenze che ne intacchino la regolare attività.

Il **Disaster Recovery Plan** (DRP, in italiano: *Piano di Disaster Recovery*) è il documento che esplicita tali misure. Esso fa parte del più ampio **Business Continuity Plan** (BCP).

Architettura
============

Un sistema TVox Disaster Recovery consiste nell'affiancare alla macchina TVox principale (|tvox_dr_master|) una seconda macchina TVox (|tvox_dr_client|). La sincronizzazione tra le due macchine garantisce che le configurazioni presenti nel |tvox_dr_master| vengano replicate in tempo reale sul |tvox_dr_client|.

In caso di indisponibilità del |tvox_dr_master| sarà possibile attivare la macchina |tvox_dr_client| in modo da garantire la continuità di servizio telefonico per il tempo necessario al ripristino della macchina |tvox_dr_master|.

.. warning:: A differenza dell'architettura di Fault Tolerance (vedi :ref:`CM&R`), all'indisponibilità del |tvox_dr_master| **NON** corrisponde l'automatica attivazione della macchina |tvox_dr_client|, ma quest'ultima va attivata e disattivata **manualmente** agendo sulla sua interfaccia OCC.


|br| 


Requisiti
=========

- Tra le macchine |tvox_dr_master| e |tvox_dr_client| dev'essere garantita l'apertura delle seguenti porte:
  
  +-----------+----------------+-----------------+
  | **Porta** | **Protocollo** | **Note**        |
  +-----------+----------------+-----------------+
  | 22        | TCP            | SSH             |
  +-----------+----------------+-----------------+
  | 873       | TCP            | FileSystem Sync |
  +-----------+----------------+-----------------+
  | 3306      | TCP            | MySQL           |
  +-----------+----------------+-----------------+
  | 27017     | TCP            | MongoDB         |
  +-----------+----------------+-----------------+

.. TODO 5460? 5461?

- L'istanza |tvox_dr_master| deve disporre della licenza Disaster Recovery. In caso di sistema ridondato questa licenza deve essere presente su entrambe le macchine che compongono il Cluster TVox
- L'istanza |tvox_dr_client| deve disporre della licenza Client Disaster Recovery
- Il |tvox_dr_client| deve essere raggiunto da tutti i dispositivi SIP/WebRTC (SoftPhone, terminali SIP e ATA Gateway) puntando **al reale indirizzo IP, non deve essere quindi nattato**
- Per un corretto controllo telefonico del TVoxClient sui dispositivi supportati è necessario che tutti i terminali si presentino al |tvox_dr_client| **con il loro reale indirizzo IP, non devono essere quindi nattati**. **Il TVox deve a sua volta essere in grado di raggiungere gli indirizzi IP reali dei terminali**
- In caso di sistema ridondato il |tvox_dr_client| deve avere piena visibilità anche dell’IP di nodo del Cluster TVox
- Nella configurazione di Disaster Recovery, è necessaria la presenza di un trunk direttamente attestato sul |tvox_dr_client|
.. - tra le macchine |tvox_dr_master| e |tvox_dr_client| dev'essere garantita l'apertura delle seguenti porte TCP: 22, 873, 3306, 27017
.. - tra le macchine |tvox_dr_master| e |tvox_dr_client| dev'essere garantita l'apertura delle seguenti porte TCP: 22, 873, 3306, 5460, 5461, 27017


|br| 


Requisiti relativi ai dispositivi SIP per l'attivazione di un TVox-DR
=====================================================================

Per poter attivare un |tvox_dr_client| i terminali telefonici ed eventualmente i voice gateway relativi alla sede principale devono soddisfare le seguenti caratteristiche:

- Possibilità di configurare una seconda identità di fallback associata al |tvox_dr_client| o eventualmente sull'identità principale poter configurare un server SIP secondario
- Poter configurare la tempistica di attivazione/disattivazione dell'identità di fallback o del server SIP secondario


|br|


Configurazione del sistema TVox Disaster Recovery
=================================================

|tvox_dr_master|
----------------

Nella sezione *Sistema=>Configurazione di sistema=>Disaster Recovery* del TVox Master impostare l'IP del |tvox_dr_client|.

.. image:: /images/DR/01_dr_ip_configuration_master.png

|tvox_dr_client|
----------------

Nella sezione *Sistema=>Configurazione di sistema=>Rete=>Disaster Recovery* del |tvox_dr_client| impostare l'IP del |tvox_dr_master|. È possibile configurare anche i destinatari email e/o SMS degli allarmi emessi dal |tvox_dr_client| in condizioni di mancanza di visibilità con il |tvox_dr_master| (vedi Nota [1]_).

.. image:: /images/DR/02_dr_ip_configuration_client.png

Una volta configurati i riferimenti IP tra le due macchine, nella sezione *Sistema=>Configurazione di sistema=>Replicazione* del |tvox_dr_client| avviare la sincronizzazione completa selezionando nel menu a tendina la voce *Tutto*.

.. TODO 03_dr_ip_configuration_client.png
.. .. image:: /images/DR/03_dr_ip_configuration_client.png

Il corretto completamento della sincronizzazione è espresso dai relativi indicatori, che al termine dell'operazione diventeranno tutti di colore verde.

.. TODO 04_dr_ip_configuration_client.png
.. .. image:: /images/DR/04_dr_ip_configuration_client.png



Configurazione Terminali SNOM
------------------------------
Per configurare un terminale SNOM di un sistema TVox dotato di TVox-DR eseguire i seguenti passi:

- Configurare la seconda identità duplicando i valori immessi per la prima identità tranne che per i parametri “Server” e “Outbound Proxy” che vanno settati con l'indirizzo IP del TVox-DR. Si consiglia nella seconda identità di impostare il parametro “Display text for idle screen” inserendo 2 asterischi prima del valore dell'interno in modo da fornire un feedback sul display del telefono che indica l'utilizzo dell'identità di fallback. Evitare di utilizzare il joystick del terminale telefonico al fine di rimanere sull'identità principale
- Selezionare “Identità 1” ed impostare il parametro “Failover Identity “a “Identità 2
- Settare il parametro “Identità 1 → SIP → Scadenza registrazione” a 180 secondi per attivare l'identità di fallback al massimo entro 180 secondi
- Impostare il parametro “Identità 1 → SIP → Subscription Expiry” a 240 secondi per aggiornare i tasti BLF qualora configurati sul telefono
- Impostare il parametro “Avanzate → Sip/RTP → Retry interval after failed registration (s)” a 180 (secondi) per riattivare l'identità principale al massimo entro 180 secondi

Con tali impostazioni trascorsi al massimo 180 secondi dal black-out di rete, il terminale SNOM attiva l'identità di fallback e indirizza le chiamate verso il TVox-DR.

Trascorsi al massimo 180 secondi dal ripristino della connettività di rete, il terminale si registra nuovamente sul |tvox_dr_master| ristabilendo il normale funzionamento.

.. note:: Tale configurazione è automaticamente predisposta dal modulo di Provisioning



Configurazione Terminali POLYCOM
--------------------------------
Per configurare un terminale POLYCOM di un sistema TVox dotato di TVox-DR è necessario utilizzare il modulo provisioning. Il provisioning Polycom imposta ai telefoni della sede remota i seguenti parametri:

- Il server 2 con il l'IP del TVox-DR
- Il timeout di scadenza della registrazione a 180 secondi
- Il timeout di aggiornamento della registrazione nel caso di manca registrazione a 180 secondi

Con tali impostazioni, persa la connettività di rete, il terminale prova per 4 secondi ad indirizzare le chiamate verso il |tvox_dr_master| per poi provare sul |tvox_dr_client|.

Questo ritardo di 4 secondi introdotto dal telefono per ogni chiamata dura al massimo per 180 secondi trascorsi i quali, scaduta la registrazione sul |tvox_dr_master|, il terminale indirizza direttamente le chiamate sul TVox-DR.
Trascorsi al massimo 180 secondi dal ripristino della connettività di rete il terminale si registra nuovamente sul |tvox_dr_master| ristabilendo il normale funzionamento.

|br| |br|


Azioni necessarie per la messa in produzione del |tvox_dr_client|
=================================================================

.. important :: L'attivazione e la disattivazione del |tvox_dr_client| vanno eseguite **manualmente** tramite il pulsante presente sull'OCC del |tvox_dr_client|.

.. Lato Telenia verranno fornite le seguenti informazioni da aggiungere al DRP:

- Aaccertarsi che la piattaforma |tvox_dr_master| della sede principale sia totalmente isolata e spenta (in caso di sistema ridondato questo deve valere per entrambe le macchine che compongono il Cluster TVox)
- Attivare **manualmente** il |tvox_dr_client| cliccando sul relativo pulsante sull'OCC

.. TODO aggiungere foto pulsante di attivazione DR

.. TODO 05_dr_activation_client.png
.. .. image:: /images/DR/05_dr_activation_client.png

.. important :: In base all’architettura specifica di ciascun cliente, quest’ultimo potrebbe avere la necessità di attivare altre procedure, ad es routing chiamate sul trunk di disaster (azione da intraprendere con l’operatore specifico), aggiornamento record DNS per far puntare i client attraverso il nome di dominio al |tvox_dr_client| e non più al |tvox_dr_master| o all’IP di nodo del Cluster TVox, etc.

|br| |br|


Azioni necessarie per roll back del |tvox_dr_client| e la riattivazione del |tvox_dr_master|
============================================================================================

.. - fermare l’erogazione del servizio di Disaster Recovery
- disattivare il |tvox_dr_client| cliccando sul relativo pulsante sull'OCC
- riattivare il |tvox_dr_master| della sede principale
- adoperarsi per la messa a normale attività dei servizi specifici in base all’architettura del cliente

.. rubric:: Note

.. [1] in queste condizioni gli allarmi emessi dal |tvox_dr_client|, non essendo disponibili lato |tvox_dr_master|, verranno inviati ai destinatari definiti in questa sezione.