==========================================
Policy di gestione per ambienti Hypervisor
==========================================


Questa sezione serve ad indicare delle linee guida per evitare problemi nella gestione, in ambienti basati su Hypervisor, di componenti software di proprietà di Telenia Software srl.

Nel documento verranno evidenziate le principali problematiche di funzionamento riscontrare in caso di mancato rispetto delle basilari best practices, in merito alla gestione di software fortemente basti su protocollo di tipo ‘real-time’ (es. RTP).

In riferimento agli ambienti basati su Hypervisor è bene precisare che gli applicativi Telenia NON risentono di perdite di performance e/o malfunzionamenti di sorta se e solo se la gestione delle VM ospitate seguono le best practices di settore.

-------------------------

Problematiche Riscontrate
=========================

I problemi di funzionamento del software Telenia possono essere riassunti nelle queste categorie:

- Problemi legati al network (es: problemi di eccessiva latenza nell’utilizzo di uplink ba-sati su fibre channel o iscsi)
- Problemi legati alla mancanza di risorse hardware
- Problemi legati al tipo di hardware in uso nel bare-metal usato dall’Hypervisor
- Problemi legati al tipo di Hypervisor utilizzato (es: VMware/Citrix vs Hyper-V) e/o all’utilizzo di una versione obsoleta di questo
- Problemi legati al Timekeeping (es: de-sync del timing tra vm e bios del bare-metal causato da snapshot e/o politiche di backup)
  
Nei seguenti paragrafi breve descrizioni delle problematiche sopra evidenziate.