.. _AWS: https://aws.amazon.com/it/

====================
Installazione in AWS
====================

Per poter procedere all'attivazione di un'istanza TVox in ambiente `AWS`_ è necessario disporre di un account per l'accesso ai servizi Amazon EC2.

Dato tale acceso, la procedura di attivazione è la seguente:

* Navigare nella sezione Istanze e premere il pulsante  **Avvia Istanze** 

.. image:: /images/TVOX/GuidaIntroduttivaTVox/InstallazioneAttivazione/InstallazioneAWS/avvia_istanze.png

* Selezionare la voce  **AMI della community** nel menu sulla sinistra, successivamente inserire nel campo di ricerca la parola  *tvox* e premere il tasto  *Invio*. Selezionare tra i risultati proposti la versione desiderata.

.. image:: /images/TVOX/GuidaIntroduttivaTVox/InstallazioneAttivazione/InstallazioneAWS/scelta_ami.PNG

* Selezionare il tipo di istanza desiderato e successivamente premere sul pulsante *Successivo: Configura i dettagli dell'istanza*

.. image:: /images/TVOX/GuidaIntroduttivaTVox/InstallazioneAttivazione/InstallazioneAWS/scelta_istanza.png

* Configurare i dettagli dell'istanza quali:
  
   1.  *Numero di istanze* : se si ha la necessità di avviare più istanze a partire dalla stessa ami è possibile indicare il numero di istanze che AWS inizializzerà
   2.  *Rete* : selezionare la vpc desiderata tra le proprie disponibili
   3.  *Sottorete* : selezionare la sottorete desiderata tra le disponibili
   4.  *Assegna automaticamente IP pubblico* : si raccomanda di selezionare il valore "Attiva"
   
Successivamente premere sul pulsante *Successivo: Aggiungi Storage*

.. image:: /images/TVOX/GuidaIntroduttivaTVox/InstallazioneAttivazione/InstallazioneAWS/configura_istanza.png

* Configurare la dimensione del disco, espressa in GB, e scegliere il tipo di Volume (si consiglia la tipologia  *General Purpose SSD (gp3)*  ) e successivamente premere sul pulsante  *Successivo: Aggiungi Tag* 

.. image:: /images/TVOX/GuidaIntroduttivaTVox/InstallazioneAttivazione/InstallazioneAWS/aggiunta_storage.PNG

* Configurare gli eventuali tag se previsti dalla propria policy di gestione dell'ambiente, successivamente cliccare sul pulsante  *Successivo: Configura il gruppo di sicurezza* 
|br| 

* Aggiungere un nuovo gruppo di sicurezza opportunamente configurato. Se nel proprio ambiente AWS esistono già opportuni gruppi di sicurezza, scegliere quello ottimale per l'installazione che si sta eseguendo. Successivamente cliccare sul pulsante  *Analizza e avvia* 
|br| 

* Verificare le informazioni riepilogate e quindi cliccare sul pulsante  *Lancio* . Il wizard di AWS proporrà quindi, come ultima scelta, di selezionare la coppia di chiavi di sicurezza per l'accesso all'istanza.

.. image:: /images/TVOX/GuidaIntroduttivaTVox/InstallazioneAttivazione/InstallazioneAWS/coppia_chiavi.PNG


Dopo aver cliccato sul pulsante Avvia le istanze, si esce dal wizard e AWS provvederà all'inizializzazione delle istanze stesse. Da quel momento, sarà possibile accedere alla loro amministrazione attraverso la sezione EC2 - Istanze.


.. tip:: In ambiente AWS, la password di accesso web ad OCC per l'utente admin corrisponde al'ID istanza 

