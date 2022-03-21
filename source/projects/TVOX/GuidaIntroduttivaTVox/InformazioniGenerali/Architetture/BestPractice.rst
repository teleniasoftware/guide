.. _bparchitettura:

=============================
Quale architettura scegliere?
=============================

Vuoi essere totalmente cloud o vuoi mantenere TVox nella tua infrastruttura privata e consentire l'accesso da internet solamente per determinati servizi?

Vuoi mantenere TVox in un cloud pubblico ma vuoi anche sfruttare le linee telefoniche attestate in azienda e riutilizzare i telefoni SIP già in tuo possesso?

Qual è la scelta migliore in termini architetturali? VEDIAMOLO INSIEME!


.. image:: /images/TVOX/tabella_purecloud_mcs.PNG


Nel prospetto che trovi nell'immagine precedente, abbiamo messo a confronto le 2 principali opzioni architetturali **TVOX PURE CLOUD** e **TVOX MCS**, con l'obiettivo di evidenziare analogie e differenze in merito a:

* **SMART WORKING**: In entrambi i casi gli utenti TVox hanno la possibilità di fruire di |client| o |winweb| con semplice connessione internet.
  

  .. tip:: Nel caso di architettura Tvox+MCS l'accesso in smart working al client è possibile a fronte della presenza di licenze  *Webclient in Smart Woking*  e/o  *Utenti TVoxTeam Smartworking* che consentono l'abilitazione nominale a singolo utente della funzionalità smart working

|br| 


* **Apparati fisici interconnessi pubblicamente**: questa opzione è disponibile nel caso di TVOX PURE CLOUD per definizione, mentre non è disponibile nel caso TVOX + MCS. In quest'ultimo caso, l'interconnessione di dispositivi fisici a TVox deve necessariamente transitare per un collegamento diretto: LAN locale, VPN o MPLS.

|br| 
    
* **Ridondanza Applicativa**: 