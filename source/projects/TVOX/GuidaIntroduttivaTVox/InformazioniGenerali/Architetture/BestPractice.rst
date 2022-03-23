.. _bparchitettura:
.. _modalità previste per il Pure Cloud: http://guide.teleniasoftware.com/it/22/projects/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/ProvisioningDispositivi.html#provisioning-dei-dispositivi-nel-caso-di-tvox-pure-cloud

=============================
Quale architettura scegliere?
=============================

Vuoi essere totalmente cloud o vuoi mantenere TVox nella tua infrastruttura privata e consentire l'accesso da internet solamente per determinati servizi?

Vuoi mantenere TVox in un cloud pubblico ma vuoi anche sfruttare le linee telefoniche attestate in azienda e riutilizzare i telefoni SIP già in tuo possesso?

Qual è la scelta migliore in termini architetturali? VEDIAMOLO INSIEME!


.. image:: /images/TVOX/tabella_purecloud_mcs.PNG


Nel prospetto che trovi nell'immagine precedente, abbiamo messo a confronto le 2 principali opzioni architetturali **TVOX PURE CLOUD** e **TVOX MCS**, con l'obiettivo di evidenziare analogie e differenze in merito a:

* **SMART WORKING**: In entrambi i casi gli utenti TVox hanno la possibilità di fruire di |client| o |winweb| con semplice connessione internet.
  

  .. tip:: Nel caso di architettura Tvox+MCS l'accesso in smart working al client è possibile a fronte della presenza di licenze  *Webclient in Smart Working*  e/o  *Utenti TVoxTeam Smartworking* che consentono l'abilitazione nominale a singolo utente della funzionalità smart working

|br| 


* **Apparati fisici interconnessi pubblicamente**: questa opzione è disponibile nel caso di TVOX PURE CLOUD per definizione, mentre non è disponibile nel caso TVOX + MCS. In quest'ultimo caso, l'interconnessione di dispositivi fisici a TVox deve necessariamente transitare per un collegamento diretto: LAN locale, VPN o MPLS.

|br| 
    
* **Ridondanza Applicativa**: Anche in caso di architettura TVox ridondata, formata da due istanze Master e Slave, è possibile abilitare la licenza PURE_CLOUD sulle istanze ed usufruire quindi di un sistema completamente cloud con processi di sincronizzazione delle configurazioni (**DataBase replication**) e dei dati (**synch file system**). Nel caso TVox + MCS invcece, è da considerare che la componente MCS non è ridondabile. La continuità di servizio per tale componente è pertanto demandata all’infrastruttura che ospita l'istanza MCS. Laddove necessario, si consiglia di definire una procedura di backup concordata con il Customer Service di Telenia

|br| 

* **Cyber Security**: I requisiti di rete necessari per implementare un'architettura PURE CLOUD o un'architettura che prevede MCS sono diversi. Nel caso PURE CLOUD, TVox risulta esposto pubblicamente per i medesimi servizi offerti da MCS con l’aggiunta di quanto necessario per l’interconnessione dei dispositivi telefonici in cloud. MCS invece risiede in una DMZ isolata e si occupa di esporre solamente alcuni servizi offerti dai TVox ad esso interconnessi

|br| 

* **Architettura Hybrid cloud**: L'architettura cloud ibrida è da intendersi come la possibilità di disporre di un TVox PURE CLOUD che abbia attiva anche una connessione diretta (VPN o MPLS o LAN locale) con la sede aziendale, per poter interconnettere terminali SIP sia tramite linea internet sia tramite linea privata. In questo scenario, va considerato che il provisioning dei dispositivi avviene in modo uniforme indipendentemente se collegati a TVox via internet o via linea diretta, e viene gestito secondo le `modalità previste per il Pure Cloud`_. Ciò significa che non sarà comunque possibile provisionare eventuali dispositivi collegati con linea privata tramite l'opzione DHCP.


