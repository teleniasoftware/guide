.. _collegamentocustomer:
.. _paragrafo: http://guide.teleniasoftware.com/it/22/projects/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/PrimiPassi/CertificatoSSL.html?highlight=certificat#integrazione-let-s-encrypt

====================
Collegare TVox a MCS
====================

Dopo aver :ref:`attivato il tuo MCS <attivazionemcs>` puoi procedere con il collegamento di un TVox a MCS stesso.

Requisiti:

- TVox deve essere già installato e licenziato
- su TVox devi aver già definito un dominio opportuno tramite OCC nella sezione *Sistema - Configurazione di sistema - Rete - Dominio*
- sul DNS pubblico di riferimento, il dominio assegnato a TVox deve essere risolto com CNAME con il dominio del tuo MCS

.. important:: 
    Nel caso che TVox sia installato in una rete locale, per distinguere la tipologia di accesso, locale o smartworking, è necessario che il dominio assegnato a TVox, configurato come CNAME del dominio di MCS sul DNS pubblico, sia risolto dal DNS interno sull'ip locale di TVox stesso.
    
    |br|    
    Per questo e tutti gli altri dettagli architetturali, vedi :ref:`qui <architetturaMCS>`.



Nel seguente video sono illustrati gli step per procedere con il collegamento di TVox a MCS:

.. raw:: html

        <iframe width="908" height="515" src="https://www.youtube.com/embed/AEyT_n0UML4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>    


|br|


Aggiungi il customer su MCS
---------------------------

- Accedi a *https://<dominio MCS>/mcs* con utente **mcsadmin**
- Spostati nella sezione *Customer-Add Customer* e configura i campi proposti nel seguente modo:

  #. Domain = dominio di TVox
  #. Name = inserisci un nome identificativo per il customer che stai inserendo (ad esempio il nome del cliente che ha acquistato TVox)
  #. VPN Ip = è precompilato e non modificabile
  #. Enable Let's Encrypt = spunta la casella se vuoi che MCS fornisca autonomamente a TVox un certificato SSL tramite il servizio Let's Encrypt e ne gestisca il rinnovo


.. note:: 
    Il certificato SSL fornito da Let's Encrypt può essere gestito anche direttamente su TVox, come descritto in questo `paragrafo`_ . In questo caso, al punto 4 del precedente elenco lascia la casella vuota.


.. important:: 
    Quando configuri la sezione *Add Customer* assicurati che la configurazione del CNAME sul DNS pubblico sia già attiva!


.. image:: /images/MCS/mcs_add_customer.PNG


Avvia la connessione MCS - TVox
-------------------------------

La connessione MCS - TVox è una connessione sicura realizzata tramite un tunnel OpenVpn punto-punto. Per instaurare questa connessione, scarica il certificato vpn disponibile dalla pagina del customer appena creato, e caricalo su TVox.

- Accedi a *https://<dominio MCS>/mcs* con utente **mcsadmin** 
- Spostati nella sezione *Customer - Customers*
- Clicca sul dominio del customer che hai appena aggiunto per aprire la sezione di dettaglio del customer stesso
- Dalla sezione *VPN* esegui il download del certificato VPN

.. image:: /images/MCS/mcs_download_vpncert.PNG

|br|

- Accedi a *https://<dominio tvox>/occ* con utente **admin**
- Spostati nella sezione *Sistema - Configurazione di sistema - Accesso servizi - Client MCS* 

|br|

.. image:: /images/MCS/mcs_tvox_loadvpncert.PNG

|br|

- Clicca su *Seleziona certificato* e carica il certificato che hai precedentemente scaricato da MCS
- Esegui il riavvio del sistema dalla sezione *Sistema - Configurazione di sistema - Riavvio/Arresto*


.. image:: /images/MCS/mcs_tvox_reboot.PNG


|br|

Dopo il riavvio, viene instaurata la connessione VPN tra MCS e TVox. Su Tvox, nella sezione *Sistema - Configurazione di sistema - Accesso servizi - Client MCS*  troverai compilate le informazioni sullo stato della connessione stessa

|br|

.. image:: /images/MCS/mcs_tvox_vpn_on.PNG

|br|

Il pulsante FERMA/AVVIA presente in questa sezione permette di stoppare e riavviare il servizio MCS in caso di necessità. Fermando il servizio, le funzionalità MCS, come ad esempio l'accesso a client ed OCC in modalità smartworking, non sono attive.

|br|
