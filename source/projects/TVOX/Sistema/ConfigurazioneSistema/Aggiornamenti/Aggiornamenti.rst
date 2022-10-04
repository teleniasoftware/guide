.. _aggiornamentisistema:

========================
Aggiornamenti di Sistema
========================


.. |Tipo_upgrade| image:: /images/TVOX/Sistema/ConfigurazioneSistema/Aggiornamenti/Tipo_upgrade.PNG
.. |Personalizzazioni01| image:: /images/TVOX/Sistema/ConfigurazioneSistema/Aggiornamenti/Personalizzazioni01.PNG
.. |Personalizzazioni02| image:: /images/TVOX/Sistema/ConfigurazioneSistema/Aggiornamenti/Personalizzazioni02.PNG
.. |DispAgg| image:: /images/TVOX/Sistema/ConfigurazioneSistema/Aggiornamenti/Aggiornamento01.PNG
.. |CodiceAttivazione| image:: /images/TVOX/Sistema/ConfigurazioneSistema/Aggiornamenti/Aggiornamento02.PNG
.. |VerificaCodice| image:: /images/TVOX/Sistema/ConfigurazioneSistema/Aggiornamenti/Aggiornamento03.PNG
.. |DownloadPatch| image:: /images/TVOX/Sistema/ConfigurazioneSistema/Aggiornamenti/Aggiornamento04.PNG
.. |ContAggiornamento| image:: /images/TVOX/Sistema/ConfigurazioneSistema/Aggiornamenti/Aggiornamento05.PNG
.. |EsempioEmail| image:: /images/TVOX/Sistema/ConfigurazioneSistema/Aggiornamenti/EsempioEmail.PNG 
.. |StartUpdate| image:: /images/TVOX/Sistema/ConfigurazioneSistema/Aggiornamenti/Aggiornamento06.PNG
.. |Update01| image:: /images/TVOX/Sistema/ConfigurazioneSistema/Aggiornamenti/Aggiornamento07.PNG
.. |Update02| image:: /images/TVOX/Sistema/ConfigurazioneSistema/Aggiornamenti/Aggiornamento08.PNG
.. |Update03| image:: /images/TVOX/Sistema/ConfigurazioneSistema/Aggiornamenti/Aggiornamento09.PNG   
.. |UpdateCompleted| image:: /images/TVOX/Sistema/ConfigurazioneSistema/Aggiornamenti/Aggiornamento10.PNG         
.. |UPG_KO| image:: /images/TVOX/Sistema/ConfigurazioneSistema/Aggiornamenti/UPG_KO.PNG   


L'aggiornamento TVOX è fruibile tramite OCC.
 
Prima di procedere con l'aggiornamento verifica le seguenti informazioni:

- per quale tipo di aggiornamento è abilitata la licenza
- che tipo di architettura stai aggiornando (*Stand Alone, Ridondato, Branch office*, etc...)
- se sono presenti personalizzazioni (custom/fix puntuali)
- quale mail è associata alla licenza


--------------------------
Prerequisiti aggiornamento
--------------------------

Come prima cosa vai da *OCC* nel tab *Security Update* del menu *SISTEMA -> Licenza*.

Nella voce *Upgrade* troverai a quali tipi di aggiornamenti è abilitata la licenza in cui dovrai intervenire.


|Tipo_upgrade|


-------------------------
Tipologia di architettura
-------------------------

Se stai aggiornando un sistema **Stand Alone** ricordati che le funzionalità TVOX non saranno fruibili per tutto il tempo di aggiornamento del sistema, mentre nel caso di aggiornamento di un sistema **ridondato** il disservizio sarà limitato solo all'indisponibilità provvisoria dei dati di reportistica (analitica e riepilogativa).

Se invece stai aggiornando un **Branch Office** e/o un **Disaster**, non causerai alcun disservizio se le machcine non sono in stato **active**.  

Se devi aggiornare un **MCS** ricordati che per tutti i TVOX collegati ad esso, fino a quando non si terminerà l'aggiornamento, l'accesso in smartworking e/o la fruzione di widget non saranno disponibili.



.. important:: Se il sistema è virtualizzato assicurati che prima di iniziare venga eseguita una snapshot dell'impianto.
    Se invece stiamo parlando di macchina fisica **Stand Alone** a titolo precauzionale è necessario fare prima 
    un backup del TVOX e avere pronta la iso nel caso nascesse la necessità di reinstallare ex-novo.

    Tali manovre sono necessarie nell'eventualità che la macchina si corrompa in maniera irreversibile nel mentre dell'upgrade (ad esempio nel caso la macchina venisse accidentalmente spenta mentre è in corso l'aggiornamento)

    **N.B. Si ricorda che il backup è dello sole configurazioni.** Se ti serve avere un backup anche dei dati storici, contatta il supporto tecnico di Telenia per concordare la procedura.



--------------------------
Verifica personalizzazioni
--------------------------

Accedi al manager e verifica se sono presenti delle personalizzazioni. Per verificare ciò puoi andare da *OCC* nel menu 
*SISTEMA -> Configurazioni di sistema -> Personalizzazioni*

|Personalizzazioni01|


|Personalizzazioni02|


Nel caso siano presenti delle personalizzazioni contatta il supporto tencico di Telenia affinchè ti dia una mano per ripristinare gli eseguibili originali prima dell'upgrade.

.. important:: E\' importante non eseguire alcun aggiornamento fino a quando Telenia non ti avrà supportato nel ripristino



---------------------------
Verifica destinatario email
---------------------------

Per verificare la mail associata alla licenza, da *OCC* vai nel tab *Gestione licenza* che si trova nel menu *SISTEMA -> Licenza*.

Se devi cambiare la mail associata, contatta il supporto tecnico di Telenia affinchè vada ad impostare l'indirizzo email corretto.

.. warning:: L'indirizzo email è fondamentale in quanto sarà il destinatario che riceverà il codice di autorizzazione per procedere con l'upgrade


-------------
Aggiornamento
-------------

Se hai verificato i punti precedenti puoi ora procedere con l'aggiornamento.

Da *OCC* con utenza con i privilegi di superuser vai in *SISTEMA -> Configurazione di sistema -> Aggiornamento di Sistema*. 

Se presenti, troverai un menu con l'elenco delle patch disponibili.

|DispAgg| 

Premendo il tasto **Scarica aggiornamento** si aprirà un pop-up con richiesta codice di attivazione.

Premi il pulsante **Richiedi codice** e riceverai una mail con il codice di autorizzazione per l'esecuzione del downgrade della patch, che dovrai inserire nell'apposito edit.

|CodiceAttivazione|

|VerificaCodice| 

Esempio di email con codice di attivazione

|EsempioEmail|

A questo punto partirà il download della patch. 

|DownloadPatch|


.. note:: In fase di download della patch ti verrà indicata una stima approssimativa del tempo residuo per il termine del download.

.. warning:: La chiusura del browser o il logout dell'utente non blocca il download.

Una volta terminato il download puoi procedere con l'aggiornamento andando nella medesima sezione e premendo il pulsante **Continua procedura di aggiornamento**

|ContAggiornamento| 

.. important:: Se in fase di download della patch avessi chiuso il browser, quando premerai il pulsante  **Continua procedura di aggiornamento** ti verrà richiesto nuovamente il codice di verifica


Ora premi il pulsante **Start update**

.. |StartUpdate| 

L'applicazione patch è composta da vari step, in fase di applicazione verranno indicate le attività in esecuzione riportando anche gli eventuali step per i quali si prevede un tempo di esecuzione cospicuo

|Update01|

|Update02|

|Update03|

Se l'aggiornamento andrà a buon fine, al termine premi il pulsante **Reboot**

|UpdateCompleted|

.. important:: Nel caso la procedura di aggiornamento non andasse a buon fine, al posto del pulsante di **Reboot** avrai il pulsante **Download update log**. In questo caso non riavviare la machcina. Esegui il download dei log e contatta il supporto tecnico di Telenia.
    
    |UPG_KO|


