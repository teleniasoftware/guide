.. _datamanagement:

==========================================
Privacy - Crittografia - Gestione dei dati
==========================================

I dati presenti su TVox riguardano tutte le comunicazioni, indipendentemente dal canale su cui si sono svolte, avvenute tra personale interno dell'azienda e utenti esterni censiti su rubrica anagrafica. Si tratta quindi di dati storici e anagrafici.

TVox implementa la gestione della retention per tutti i dati immagazzinati su database, e consente di gestire il cosiddetto diritto all'oblio nei confronti di un utente esterno che lo richiede, nel rispetto dei diritti sanciti dal GDPR.


--------------------------------

**Data retention** 

E\' possibile configurare i limiti temporali di mantenimento dei dati all'interno di TVox tramite OCC, potendo scegliere di fissare sia un valore globale (valido per gli storici di tutti i canali), sia un valore specifico per canale o per singolo servizio.

La gestione della retention si applica anche ai file di registrazione delle chiamate prodotti nel caso la funzionalità sia stata attivata. In questo caso, oltre al mantenimento su base temporale, è possibile indicare anche la percentuale giornaliera delle conversazioni da mantenere: tale quota è configurabile da 0 a 100% del totale delle registrazioni effettuate in ogni singola giornata.


.. image:: /images/TVOX/Privacy&Security/dataretention.PNG

|br|

---------------------------------


**Diritto all'oblio** 

Il diritto all'oblio, come sancito dal GDPR, si traduce nella possibilità di eliminare dal sistema tutte le informazioni relative all'utente che ne ha fatto richiesta, ivi comprese informazioni anagrafiche ed informazioni relative ai contatti che questa persona ha avuto con l'azienda e che sono ancora presenti su TVox.

L'esecuzione del diritto all'oblio di un contatto è un'abilitazione che può essere assegnata a specifici utenti TVox opportunamente formati.

|br|

----------------------------------


**Crittografia delle comunicazioni** 


Le comunicazioni vocali scambiate tra utenti possono essere crittografate in modo diverso a seconda del protocollo di comunicazione utilizzato:


- comunicazioni basate su protocollo WebRTC: WebRTC cripta le informazioni utilizzando Datagram Transport Layer Security (DTLS)
- comunicazioni basate su protocollo SIP: è possibile attivare su TVox la segnalazione SIP tramite TLS e la trasmissione della voce tramite SRTP


TVox consente anche di registrare le comunicazioni telefoniche per il successivo riascolto. I file di registrazione delle chiamate, prodotti in formato mp3, possono essere crittografati e traferiti su storage esterni.

TVox applica su questi file una crittografia basata su protocollo asimmetrico ECDH, con utilizzo di una coppia di chiavi pubblica e privata.

|br|
