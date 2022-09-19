.. _collegamentocustomer:

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


|br| 

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
    #. Enable Let's Encrypt = spunta la casella se vuoi che MCS fornisca autonomamente a TVox il certificato SSL e ne gestisca il rinnovo


DA COMPLETARE