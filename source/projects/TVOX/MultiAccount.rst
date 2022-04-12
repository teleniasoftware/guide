.. _sms_multiaccount:
.. _Agcom: https://www.agcom.it/alias
.. _PMF - Plus Messaging Framework: https://www.plus-srl.com/pmf/


========================
Servizi WEB di invio SMS
========================

La modalità Multi Account permette di definire uno o più account di invio SMS legato ad uno o più provider di servizio.

.. image:: /images/TVOX/sms_multiaccount1.PNG


Per aggiungere un nuovo account cliccare sul tasto *NUOVO* presente nel quadro **Account SMS**. 

Si presenterà un finestra che richiede di selezionare il provider da cui si è acquistato il servizio ed alcuni parametri di configurazione del servizio stesso.

I provider proposti sono:

* Messagenet
* KPNQwest
* PLUS
* TIM


.. important:: Prima di poter configurare un Account SMS legato ad un servizio WEB è necessario aver già acquistato dal provider prescelto il servizio stesso, in modo da disporre dei necessari parametri di configurazione dell'account su TVox

|br|


Messagenet
----------


.. image:: /images/TVOX/sms_messagenet.PNG
    
*  **Descrizione**: breve descrizione dell'account. La descrizione consente di riconoscere a prima vista l'account nell'elenco di tutti gli account configurati (vedi immagine seguente)
*  **Username**: codice che identifica lo username dell'account fornito da Messagenet. Il codice è fornito sempre da Messagenet
*  **Password**: password dell'account fornito da Messagenet
*  **Nome del mittente**: In questo campo è possibile inserire il nome che verrà presentato a chi riceve un SMS inviato tramite questo account. Prima di poter configurare il nome mittente, è necessario concordare il nome stesso con il provider per la verifica dell'attendibilità verso `Agcom`_


.. warning:: La **password** da inserire è la stessa che può essere utilizzata per accedere al portale web di Messagenet per la gestione dell'account. La gestione tramite il portale di Messagenet consente, tra le altre cose, anche di modificare la password stessa. Se ciò avvenisse, è necessario impostare la nuova password anche su OCC

.. image:: /images/TVOX/sms_account_configurato.PNG


|br|


KPNQwest
--------

.. image:: /images/TVOX/sms_kpn.PNG

*  **Descrizione**: breve descrizione dell'account. La descrizione consente di riconoscere a prima vista l'account nell'elenco di tutti gli account configurati (vedi immagine seguente)
*  **Username**: username dell'account fornito dal provider
*  **Password**: password dell'account fornito dal provider
*  **Email dell'account amministrativo**: indirizzo email associato all'account fornito dal provider


|br|


PLUS - PMF
----------

.. image:: /images/TVOX/sms_plus.PNG

*  **Descrizione**: breve descrizione dell'account. La descrizione consente di riconoscere a prima vista l'account nell'elenco di tutti gli account configurati (vedi immagine seguente)
*  **Username**: cusername dell'account fornito dal provider
*  **Password**: password dell'account fornito dal provider
*  **UUID Utente**: Il parametro userUUID è il codice di identificazione per l'autenticazione `PMF - Plus Messaging Framework`_
*  **Accedi tramite**: indica la modalità di login al servizio PMF
*  **Nome del mittente**: Nome utilizzato come mittente dell'SMS
*  **pmfUrl**: URL del servizio PMF
*  **pmfQName**: QName del servizio PMF  



|br|


TIM
---


.. image:: /images/TVOX/sms_tim.PNG

.. important:: 
    La configurazione dell'account con provider TIM prevede che sia stato sottoscritto un contratto con Telecom Italia per l'utilizzo dei servizi di messaggistica in base alla convenzione  **Consip6**. |br| 
    Il contratto è associato ad uno o più servizi identificati dai seguenti codici:
     * BAS
     * InfoMessage AVC
     * InfoCity AVD
     * Informazioni FIGLIO
     * Infosondaggi
    Questi parametri definiscono il codice del servizio acquistato che si intende utilizzare

*  **Descrizione**: breve descrizione dell'account. La descrizione consente di riconoscere a prima vista l'account nell'elenco di tutti gli account configurati (vedi immagine seguente)
*  **Username**: cusername dell'account fornito dal provider
*  **Password**: password dell'account fornito dal provider
*  **Contratto**: si veda la nota *important* precedente
*  **Codice del servizio acquistato**: si veda la nota *important* precedente

