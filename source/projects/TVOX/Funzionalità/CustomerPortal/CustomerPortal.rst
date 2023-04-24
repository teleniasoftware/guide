.. _customerportal:

===============
Customer Portal
===============

.. |CustomerPortal_AreaRiservata_Registrazione| image:: /images/TVOX/CustomerPortal/CP_AreaRiservata_reg.PNG
.. |CustomerPortal_AreaRiservata_Login| image:: /images/TVOX/CustomerPortal/CP_AreaRiservata_login.PNG
.. |CustomerPortal_Riepilogativo| image:: /images/TVOX/CustomerPortal/CP_Riepilogativo.PNG
.. |CustomerPortal_Griglia01| image:: /images/TVOX/CustomerPortal/CP_Griglia01.png
.. |CustomerPortal_Nota| image:: /images/TVOX/CustomerPortal/CP_Inserimento_Nota.png
.. |CustomerPortal_Configurazione01| image:: /images/TVOX/CustomerPortal/CP_Abil01.png
.. |CustomerPortal_Configurazione02| image:: /images/TVOX/CustomerPortal/CP_Abil02.png
.. |CustomerPortal_Configurazione03| image:: /images/TVOX/CustomerPortal/CP_Abil03.png
.. |CustomerPortal_Configurazione04| image:: /images/TVOX/CustomerPortal/CP_Abil04.png
.. |CustomerPortal_Configurazione05| image:: /images/TVOX/CustomerPortal/CP_Abil05.png


Qui troverai le informazioni necessarie per consultare il **Customer Portal** di Telenia Software. 
Si tratta della nuova funzionalità erogata da TVox Support, che può essere anche integrata al sito aziendale e che consente il monitoraggio, 
la consultazione e la gestione dei ticket aperti nei confronti di Telenia, come ad esempio ticket con il nostro servizio di supporto tecnico.


Registrazione Utenza
====================

Per poter accedere al portale, è necessario registrarsi preventivamente nella pagina **Area Riservata** sul nostro sito internet.

.. important:: A seguito della recente introduzione di politiche di sicurezza sugli accessi all'area riservata del nostro sito, per chi fosse già in possesso delle credenziali di acceso è richiesto il cambio della password cliccando sul link **Dimenticato Password?** prima di effettuare il primo accesso.

|CustomerPortal_AreaRiservata_Registrazione|


Accesso al Customer Portal
==========================

Dopo la fase iniziale di registrazione, ed una volta effettuato l'accesso in area riservata, sarà disponibile un 
link per l'accesso diretto al **Customer Portal**

|CustomerPortal_AreaRiservata_Login| 

All'interno del **Customer Portal** è disponibile una dashboard che presenta in due grafici lo stato dei 
ticket in gestione suddivisi per stato **NUOVO** (giallo), **APERTO** (rosso), **PENDING** (azzurro).

- Quello a sinistra è relativo ai ticket in gestione aperti da tutti i contatti della propria azienda (Tutti i ticket)
- Quello a destra  è relativo ai soli ticket aperti dall'utente che ha eseguito l'accesso al portale (I miei ticket)

|CustomerPortal_Riepilogativo| 

    
**Legenda stato ticket**
 .. code-block:: ini

    Giallo - Nuovo: Ticket che non è ancora in gestione da parte di alcun operatore
    Rosso - Aperto: Ticket in gestione per il quale Telenia deve fornire un feedback
    Azzurro - Pending: Ticket in gestione per il quale Telenia sta attendendo una risposta dal cliente
    Grigio - Chiuso: Ticket gestito e completato


Oltre alla dashboard, sono disponibili due tab analitiche *Tutti i tickets* e *I miei tickets* che presentano l'elenco dei ticket. Da tali sezioni è possibile leggere i singoli ticket, ed apportare modifiche con l'inserimento di comunicazioni per i soli ticket in carico a sè stessi.

Ogni ticket in gestione al nostro supporto tecnico è assegnato ad un determinato servizio (colonna *Servizio* nelle tab di *elenco ticket*): il nome di tale servizio può cambiare in ragione del contratto di assistenza associato al cliente finale.


|CustomerPortal_Griglia01|


E\' possibile inserire una nota interna che vedrà l'agente che ha in gestione il ticket

|CustomerPortal_Nota|


.. important:: Esistono due tipologie di utente per l'accesso al **Customer Portal**:

 - **Utente**: può visualizzare sulla dashboard solamente il riepilogo dei propri ticket, e potrà leggere e inserire comunicazioni solamente per i propri ticket tramite la tab "I miei ticket"
 - **Utenze aziendale**: può visualizzare in dashboard il riepilogo di tutti i ticket dell'azienda, anche quelli aperti dai propri colleghi, può consultare tutti i ticket disponibili nella tab "Tutti i ticket", può inserire comunicazioni solamente sui ticket a sè assegnati (tab "I miei ticket)"



.. note:: L'apertura di nuovi ticket dovrà avvenire ancora come di consueto inviando un'email ai nostri contatti.

.. note:: I nuovi ticket, una volta creati sul sistema, diventeranno disponibili anche tramite **Customer Portal**.


Come configurare l'accesso al Customer Portal
===========================================

Ora troverai le istruzioni per abilitare l'accesso al **Customer Portal**

Per erogare il servizio è nel seguente modo:

- il tuo TVOX deve essere provvisto della licenza "Customer Portal"
- l'utente che dovrà accedere al Customer Portal dovrà essere censito in rubrica con la propria email
- l'agente dovrà abilitare tale utente andando da client nel dettaglio dell'utente, nella tab **Customer Portal** (vedi esempio)

|CustomerPortal_Configurazione01| 

- si potrà decidere di assegnare il ruolo Utente o Utente aziendale

|CustomerPortal_Configurazione02| 

|CustomerPortal_Configurazione03| 

- una volta che l'utente verrà abilitato, riceverà una mail con le credenziali di accesso (username= email, password generata in maniera randomica)

- a questo punto l'utente che riceverà la mail potrà accedere al portale https://fqdn_tvox/apps/customerportal ed inserire le credenziali ricevute tramite email

    |CustomerPortal_Configurazione04|

- una volta che si avrà accesso al portale, l'utente potrà anche decidere di cambiare password andando nel suo profilo

|CustomerPortal_Configurazione05|


.. note:: Per abilitare gli utenti ad accedere al Customer Portal, l'agente dovrà avere un ruolo che contenga il permesso "Customer Portal"
