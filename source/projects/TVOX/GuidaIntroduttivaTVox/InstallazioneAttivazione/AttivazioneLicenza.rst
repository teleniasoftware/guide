.. _AttivazioneLicenza:

===================
Attivazione Licenza
===================

Il primo step da affrontare dopo l'installazione di una qualsiasi istanza TVox è l'attivazione della licenza.

.. attention:: Se si sta avviando un'installazione cosiddetta  **Pure Cloud**, prima di procedere all'attivazione istanza è necessario aver configurato sull'istanza stessa un ip pubblico statico risolto pubblicamente con un determinato dominio. Per questo dettaglio, si rimanda alla sezione :ref:`Infrastruttura`

Per procedere all'attivazione di un'istanza TVox è necessario conoscere :

*  **Seriale** : il numero della licenza rilasciato dal Delivery
*  **Indirizzo email associato** : è importante avere accesso alla casella di posta associata alla licenza. In sede di ordine, infatti, è richiesto di comunicare un indirizzo email sul quale verranno ricevuti i codici temporanei di attivazione


Le licenze per istanze TVox rilasciate da Telenia vengono detenute da un apposito server di gestione, detto License Server, residente su cloud AWS. Questo ha il compito di rilasciare la licenza ad un TVox che ne fa richiesta.

Queste richieste sono gestite da un processo denominato :ref:`SecurityUpdate`, presente su tutte le installazioni: Security Update ha il compito di comunicare via HTTPS con il License Server per ricevere le informazioni inerenti la licenza da caricare a bordo.

Per tale motivo, risulta necessario che TVox possa liberamente generare richieste sulla porta 443 in generale verso internet.


Al primo accesso su OCC, la pagina di login presenta l'indicazione che il processo Security Update è in attivazione:


.. image:: /images/TVOX/GuidaIntroduttivaTVox/InstallazioneAttivazione/AttivazioneLicenza/securityupdate_in_attivazione.PNG


Dopo aver eseguito il login con utente admin, l'interfaccia presenta la sezione Licenza con focus sulla tab **Security Update**. Lo stato di TVox è OFF, indicato dal simbolo accanto alla scritta Omnichannel Contact Center.

.. image:: /images/TVOX/GuidaIntroduttivaTVox/InstallazioneAttivazione/AttivazioneLicenza/primo_accesso.PNG


Per attivare la licenza, spostarsi nella tab **Gestione licenza**, inserire il seriale nell'apposito campo e cliccare sul pulsante **Carica Licenza**.

.. image:: /images/TVOX/GuidaIntroduttivaTVox/InstallazioneAttivazione/AttivazioneLicenza/carica_licenza.PNG

Dopo questa operazione, verrà inviato un codice di verifica all'indirizzo email associato alla licenza in fase di ordine. Inserendo il codice e cliccando sul pulsante **Inoltra codice al server** si procederà alla verifica della licenza.

.. image:: /images/TVOX/GuidaIntroduttivaTVox/InstallazioneAttivazione/AttivazioneLicenza/codice_verifica.PNG


Quest'ultima operazione permette a TVox di ricevere dal License Server le informazioni relative ai moduli di licenza da attivare ed all'eventuale periodo di validità della licenza stessa. Vengono riepilogate le informazioni relative a:

* Scadenza
* Numero seriale
* Nome azienda intestataria della licenza
* Email associata

Successivamente, si rende necessario procedere alla notifica interna dei processi ed al riavvio di sistema.
Per fare questo, è necessario cliccare sul pulsante **Notifica i processi e riavvia il sistema**. Un prompt chiederà all'amministratore di confermare la scelta.
Data la conferma, il sistema procederà in autonomia a notificare i processi e ed al riavvio, rendendo indisponibile OCC fino al termine di questa operazione.

.. image:: /images/TVOX/GuidaIntroduttivaTVox/InstallazioneAttivazione/AttivazioneLicenza/notifica_processi.PNG


Al termine di questa fase, che può durare alcuni minuti a second della tipologia di licenza caricata e dell'istanza hardware ospite, TVox sarà disponibile e pronto per la prima configurazione 


.. :ref:`configuraTvox`