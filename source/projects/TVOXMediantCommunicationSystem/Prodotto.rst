.. _mcs:
=========
Prodotto
=========

TVox **Mediant Communication System (MCS)** è la piattaforma che consente l'esposizione su internet dei servizi di comunicazione erogati da TVox Omnichannel Contact Center.

.. image:: ../../images/MCS/mcs_product.png
   :scale: 60%
   :align: center

Come rappresentato in figura, MCS è necessario nel momento in cui si ha la necessità di:

* far lavorare in smartworking gli utenti TVox attraverso l'utilizzo di TVox Web Client e/o dell'applicazione mobile TVox Team
* fornire i certificati SSL necessari all'utilizzo di TVox Web Client e TVox Team
* integrare al TVox applicazioni aziendiali residenti in cloud
* utilizzare la widget del TVox integrata sul web

.. important:: Ad una istanza  **MCS di release 22**  è possibile collegare TVox di release 10.26, 21, 22 |br| |br| Nel caso invece di una istanza MCS di release precedente, NON è possibile collegare TVox di release 22 ma solamente TVox di release inferiori. Per qualsiasi dubbio è possibile contattare il supporto tecnico di Telenia Software

TVox MCS è multitenant, consentendo quindi di esporre su internet servizi erogati da più piattaforme TVox **fino ad un massimo di 250**. A TVox MCS deve essere associato un dominio pubblico e può essere installato su piattaforme server standard  o virtualizzate **Almalinux 8.5 Arctic Sphynx**, come ad esempio:

- **VMWare** (ESXi / vSphere) Richiesti Workstation v.7 e setup VMWare Tools 
- **Citrix System XEN Center** Installazione in modalità Hardware-assited Virtual Machine (no ParaVirtualization) 
- **Oracle VM Virtual Box** Richiesto setup extension pack

L’installazione di TVox MCS necessita di risorse che dipendono dalla consistenza degli utenti come indicato nella seguente tabella:

+-----------------+--------------------------------------------------------------+
| MCS Partner (a) |                            Risorse                           |
+-----------------+----------+------+-----------+--------+-----------------------+
|      Utenti     | CPU/Core |  RAM |   Disco   |   Eth  | Bandwith Internet (b) |
+-----------------+----------+------+-----------+--------+-----------------------+
|   Fino a 1000   |     4    | 8 Gb | 150GB SSD | 1 Gbit |       >=100Mb/s       |
+-----------------+----------+------+-----------+--------+-----------------------+
|   Fino a 10000  |     8    | 8 Gb | 150GB SSD |  1Gbit |       >=1000Mb/s      |
+-----------------+----------+------+-----------+--------+-----------------------+

Il sistema TVox MCS dovrà essere connesso a Internet con disponibilità di banda (massima) di circa 60 KB/s per ogni connessione attiva dei dispositivi (APP, UCC Web RTC e Widget).

.. warning:: Il servizio MCS non è ridondabile! Su richiesta, è possibile definire una procedura di backup concordata con il Customer Service di Telenia.
