======================
TVox Disaster Recovery
======================

Con il termine **Disaster Recovery** (brevemente DR, in italiano: *Recupero dal Disastro*), in informatica ed in particolare nell'ambito della sicurezza informatica, si intende l'insieme delle misure tecnologiche e logistico/organizzative atte a ripristinare sistemi, dati e infrastrutture necessarie all'erogazione di servizi di business per imprese, associazioni o enti, a fronte di gravi emergenze che ne intacchino la regolare attività.

Il **Disaster Recovery Plan** (DRP, in italiano: *Piano di Disaster Recovery*) è il documento che esplicita tali misure. Esso fa parte del più ampio **Business Continuity Plan** (BCP).

Requisiti
=========

- la macchina |tvox_dr_master| deve disporre della licenza Disaster Recovery. In caso di sistema ridondato questa licenza deve essere presente su entrambe le macchine che compongono il Cluster TVox
- la macchina |tvox_dr_client| deve disporre della licenza Client Disaster Recovery
- il TVox DR deve essere raggiunto da tutti i dispositivi SIP/WebRTC (SoftPhone, terminali SIP e ATA Gateway) puntando **al reale indirizzo IP, non deve essere quindi nattato**
- per un corretto controllo telefonico del TVoxClient sui dispositivi supportati è necessario che tutti i terminali si presentino al TVox DR **con il loro reale indirizzo IP, non devono essere quindi nattati**. **Il TVox deve a sua volta essere in grado di raggiungere gli indirizzi IP reali dei terminali**
- in caso di sistema ridondato il TVox DR deve avere piena visibilità anche dell’IP di nodo del Cluster TVox
- nella configurazione di Disaster Recovery, è necessaria la presenza di un trunk direttamente attestato sul TVox DR

Configurazione del sistema TVox Disaster Recovery
=================================================

|tvox_dr_master|
--------------

Nella sezione *Sistema=>Configurazione di sistema=>Disaster Recovery* del TVox Master impostare l'IP del |tvox_dr_client|.

..
    .. image:: /images/DR/01_ip_configuration.png
    :scale: 60%
    :align: center

.. image:: /images/DR/01_dr_ip_configuration_master.png

|tvox_dr_client|
----------------

Nella sezione *Sistema=>Configurazione di sistema=>Rete=>Disaster Recovery* del |tvox_dr_client| impostare l'IP del |tvox_dr_master| ed, eventualmente, i destinatari email e/o SMS degli allarmi emessi in caso di mancata comunicazione, e di conseguenza mancata sincronizzazione, con il |tvox_dr_master|.

..
    .. image:: /images/DR/02_ip_configuration.png
    :scale: 60%
    :align: center

.. image:: /images/DR/02_dr_ip_configuration_client.png

Azioni necessarie per la messa in produzione del DR
===================================================

Lato Telenia verranno fornite le seguenti informazioni da aggiungere al DRP:

- accertarsi che la piattaforma TVox della sede principale sia totalmente isolata e spenta
- attivare manualmente il TVoxDisaster Recovery attraverso l’interfaccia web preposta

.. important :: In base all’architettura specifica di ciascun cliente, quest’ultimo potrebbe avere la necessità di attivare altre procedure, ad es routing chiamate sul trunk di disaster (azione da intraprendere con l’operatore specifico), aggiornamento record DNS per far puntare i client attraverso il nome di dominio al |tvox_dr_client| e non più al |tvox_dr_master| o all’IP di nodo del Cluster TVox, etc.

Azioni necessarie per roll back del DR
======================================

- fermare l’erogazione del servizio di Disaster Recovery
- riattivare il TVox della sede principale
- adoperarsi per la messa a normale attività dei servizi specifici in base all’architettura del cliente
