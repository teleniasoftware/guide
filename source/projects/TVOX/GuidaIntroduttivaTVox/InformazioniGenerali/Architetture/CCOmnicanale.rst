==============================
TVox Contact Center Omnicanale
==============================

**TVox OmniChannel Contact Center** è il modulo della piattaforma TVox per la gestione dei servizi di **Contact Center** in contesti multicanale (voce, mail, chat, video, etc...), multi servizio e multi customer.

.. Per ciascun cliente è possibile definire IVR e servizi di Contact center personalizzabili.


Quando parliamo di |tvox| possiamo avere un sistema in architettura di tipo **Stand Alone** (vedi :ref:`StandAlone`) o **ridondata** (vedi :ref:`CM&R`) e, in base ai canali o alle funzionalità che si decide di attivare, può essere necessario disporre di uno o due server aggiuntivi.

In quest'ultimo caso, si parlerà dei seguenti moduli che si aggiungono al modulo TVox:

* **Support**: Modulo aggiuntivo a TVox necessario per erogare il servizio Support Mail e per erogare la funzionalità di Knowledge Base

* **Insight**: Modulo aggiuntivo a TVox in grado di aggregare in dashboard e statistiche le interazioni Omnicanale e i dati di operatività degli Agenti (NPS, affidabilità della rubrica, activity code, callback ecc)

* **Customer Journey Server**: Accentratore di tutte le interazioni (voce, mail/ticket, video, webchat, sms, callback) stabilite dai contatti con l’azienda, le interazioni sono storicizzate e disponibili in primo piano all’operatore di Contact Center per assicurare al contatto sempre una risposta appropriata evitando di chiedere informazioni che sono già presenti nel contact cente. Il Customer Journey è un elemento indispensabile per inquadrare velocemente l’esperienza che il contatto ha maturato nei confronti dell’azienda

* **Knowledge Base**: Funzionalità che permette di memorizzare un repository documenti sotto forma di articoli o contenuti descritttivi (utili per la consultazione da parte degli utenti TVox)

.. .. note:: Il modulo TVox **Contact Center** per il solo canale telefonico può essere erogato anche su un solo server (sia esso fisico, virtuale che in Cloud).


.. .. important:: Nel caso **TVox Contact Center Omnicanale mail** oppure nel caso si abbia necessità di avere prestazioni evolute (*Knoledge base, Dashboard, Customer Journey*) è necessario avere un ulteriore server (*Stand Alone o Ridondato*) per l'erogazione di tali servizi. **A prescindere dall'esigenza o meno di avere il server aggiuntivo, le configurazioni vengono eseguite tutte su server principale**.
    


