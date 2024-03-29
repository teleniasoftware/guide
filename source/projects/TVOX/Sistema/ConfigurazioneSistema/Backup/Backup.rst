.. _systembackup:

===============================
Backup e Ripristino del sistema
===============================
In questa sezione si riportano gli step fondamentali per configurare il Backup della centrale telefonica TVox PBX e come ripristinare un Backup.

.. warning:: Quando parliamo di Backup, intendiamo il backup delle sole configurazioni e non dei dati storici

Per la sezione 'Backup/Ripristino' è necessario andare in OCC nella sezione SISTEMA => Configurazione di sistema => Backup/Rispristino.


Backup
===================================


.. image:: /images/TVOX/Sistema/ConfigurazioneSistema/Backup/backup_ripristino_occ.png


Su Occ sono a disposizione due tipologie di backup: 

-  **Istantaneo**, cliccando su \"Crea backup ora\" si darà una descrizione al backup e lo si farà partire.  Il processo di backup partirà istantaneamente e sarà salvato localmente. 
-  **Schedulato**, crea un nuova schedulazione configurabile con la possibilità di caricare su un server FTP i file che vengono generati 

.. note:: Quando si esegue un backup, viene mostrato un messaggio di alert che informa l'utente che l'operazione causerà un utilizzo delle risorse di CPU e memoria. Una volta avviato il processo, avremo una schermata simile di progresso che potrà essere chiusa una volta terminato:

.. image:: /images/TVOX/Sistema/ConfigurazioneSistema/Backup/progresso_creazione.png

**Configurazione Backup Schedulato:**

- **Nome:** Nome del backup corrente. Stringa alfanumerica, spazi non ammessi
- **Esegui ogni:** Un'operazione di backup può essere: disabilitata, se Mai è selezionato; giornaliera, se Ogni giorno è selezionato; mensile, se Primo giorno di ogni Mese è selezionato; settimanale, se selezionato un giorno specificato.
- **Alle ore:** Orario in cui schedulare l'esecuzione del backup
- **Backup remoti:** Numero massimo di file di backup mantenuti su server FTP remoto. **Superato questo valore i backup più vecchi vengono cancellati**
- **Backup locali:** Numero massimo di file di backup mantenuti localmente nel Telenia Application Manager. **Superato questo valore i backup più vecchi vengono cancellati**
- **Parametri FTP Server:** parametri di accesso al server FTP sulla quale verranno salvati i backup. 

.. warning:: L'utente FTP preposto ad accedere a questo server dovrà avere la possiblità di navigare sul percorso, di copiare i file di backup 

.. image:: /images/TVOX/Sistema/ConfigurazioneSistema/Backup/backup_schedulato.png


.. note:: Per ogni backup le operazioni che possono essere fatte sono:

    - Download
    - Ripristino
    - Elimina
    - Nel caso di backup schedulato, dove è prevista anche una configurazione FTP, si ha anche la possibilità di forzare la copia in remoto


Ripristino
===================================

Una volta creato il backup, avremo l'elenco di quelli generati e che possono essere rispristinati

.. image:: /images/TVOX/Sistema/ConfigurazioneSistema/Backup/lista_backup.png


Il ripristino si può eseguire premendo il tasto \"Ripristino\" sui backup in elenco oppure, in caso di una nuova macchina, cliccando su \"Seleziona file\" nella sezione \"Ripristina\" e selezionando il file zip recuperato dalla macchina da ripristinare.

.. warning:: In caso di restore,  la macchina su cui si intente eseguire il restore deve avere una licenza valida ed essere della stessa versione per la quale si è eseguito il backup. 

.. image:: /images/TVOX/Sistema/ConfigurazioneSistema/Backup/lista_backup_opzioni.png


In fase di restore, viene prima caricato il file e poi avviene la procedura di ristoro che consiste nel **fermare i servizi** e caricare le configurazioni. 
