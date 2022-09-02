.. _attivazionemcs:

=====================
Attivazione di un MCS
=====================

Attivare un'istanza MCS è molto semplice. Anzitutto prendi nota dei seguenti requisiti che devi soddisfare prima di iniziare:

- IP pubblico statico da assegnare all'istanza in modalità NAT 1:1 o direttamente attestato sulla scheda di rete
- FQDN associato all'ip pubblico sul DNS
- MCS va installato su cloud o su DMZ nel caso lo si debba installare nella stessa infrastruttura che ospita uno o più dei TVox che vuoi collegare
- Devi soddisfare i seguenti :ref:`requisiti di rete <requisitiNetMCS>`

Il dettaglio sui requisiti architetturali lo trovi a partire da :ref:`qui <architetturaMCS>` |br| |br|


Nel seguente video sono illustrati gli step per procedere all'attivazione:

.. raw:: html

        <iframe width="908" height="515" src="https://www.youtube.com/embed/q9tzV4nQul0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>    


|br|


Prepara l'istanza
-----------------

- Accedi a *https://<IP pubblico MCS>/occ* con utente **admin**

.. important:: Assicurati che la password dell'utente *admin* rispetti criteri di sicurezza massimi

- Attiva la licenza che ti è stata fornita ed attendi il successivo riavvio dei processi. Al termine, se necessario, effettua nuovamente l'accesso come al punto precedente
- Spostati nella sezione *Sistema - Configurazione di sistema - Rete - Dominio* e compila i campi *Dominio*, *Ip pubblico*, infine attiva il pulsante *Accedi tramite dominio*


.. note:: Quando effettui una configurazione su questa sezione, il salvataggio provoca il riavvio dei servizi TVox. Verrai avvisato da un banner che ti chiederà la conferma per procedere. Durante il riavvio, OCC non sarà disponibile.


.. note:: Il dominio che inserisci qui è il dominio di MCS, non dei TVox che successivamente collegherai a MCS stesso. Lo chiameremo *dominio di gestione* o \"dominio di management\"" di MCS

|br| 

- Carica il certificato SSL per il tuo MCS

.. attention:: Caricare un certificato SSL per certificare il dominio di MCS non è un'operazione obbligatoria perchè utilizzerai MCS via HTTPS solo per necessità di gestione e configurazione e mai per contattare i TVox collegati a MCS stesso


|br| 

A questo punto potrai procedere con la configurazione vera e propria della componente MCS. Per procedere, utilizzerai l'utente **mcsadmin**.

.. important:: Assicurati che la password dell'utente *mcsadmin* rispetti criteri di sicurezza massimi. Prima di procedere, dovrai collegarti con questo utente all'indirizzo *https://<IP pubblico MCS>/occ*, cliccare in alto a destra sull'icona a forma di utente, selezionare *Profilo* e successivamente il pulsante *Reimposta password*.
    
    .. image:: /images/MCS/mcsadmin_cambiopwd.PNG
    
    |br| 

    In questa fase è CORRETTO che tu non veda alcun menu sul lato sinistro di OCC





Configurazione iniziale MCS
--------------------------

- Accedi a *https://<dominio MCS>/mcs* con utente **mcsadmin**  
- Spostati nella sezione *Miscellaneous* e configura i campi proposti nel seguente modo:

    #. External Hostname = dominio di MCS
    #. External Publi IP = IP pubblico di MCS
    #. ICE Server - Public IP = IP pubblico di mcs
    #. ICE Server - LAN IP = IP privato di MCS
    #. Certificate - Let's Encrypt Account E-mail (opzionale) = indirizzo email per la creazione di un account su Let's Encrypt e sfruttare questo servizio per la fornitura di certificati SSL pubblici ai TVox che collegherai
    #. Certificate - Global Certificate Synchronization = attivo se vuoi che tutti i TVox che collegherai possano ricevere in automatico il proprio certificato SSL da MCS

- Salva e dai conferma del salvataggio sul banner che ti si viene presentato.


A questo punto sei pronto per iniziare a :ref:`collegare uno o più TVox al tuo MCS <collegamentocustomer>`!

|br| 


