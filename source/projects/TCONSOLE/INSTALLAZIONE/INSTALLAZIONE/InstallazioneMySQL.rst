.. _Installazione MySQL:

=================================================
Installazione e configurazione del servizio MySQL
=================================================

Seguire i seguenti passaggi:

- spostarsi nella cartella (ipotizzando di aver estratto i files di setup in *C:\\Telenia_Setup*):

  .. code-block:: shell

     C:\Telenia_Setup\TConsole V5.7.27\MySql_5.1.34\

  ed eseguire (clic con il tasto destro del mouse, **Installa**) il file:

  .. code-block:: shell

     mysql-essential-5.1.34-win32.msi

.. Important :: Inserire i seguenti parametri **esattamente** come vengono descritti, **senza apporre variazioni** rispetto a quanto specificato: valori diversi di questi parametri potrebbero determinare l'interruzione dell'installazione TConsole o anomalie di funzionamento.

- alla finestra del wizard di MySQL Server 5.1 premere **Next**;
- scegliere **Typical** e premere **Next**;
- premere **Install**;
- alla finestra di **MySQL Enterprise** premere **Next** (2 volte);
- lasciare selezionata la voce **Configure the MySQL Server now**, premere **Finish** ed alla successiva schermata premere **Next**;
- selezionare **Detailed Configuration** e premere **Next**;
- selezionare **Developer Machine** e premere **Next**;
- selezionare **Non-Transactional Database Only** e premere **Next**;
- selezionare **Manual Setting**, impostare **Concurrent connections** a **100** e premere **Next**;
- lasciare selezionate entrambe le opzioni: **Enable TCP/IP Networking** ed **Enable Strict Mode**; modificare il parametro **Port Number** inserendo il valore **3366** e selezionare **Add firewall exception for this port** (solo se il servizio Windows Firewall è attivo, altrimenti comparirà un messaggio d’errore nella successiva applicazione delle configurazioni: i dettagli dell’errore e su come procedere in tal caso sono descritti nella Nota [1]_) e premere **Next**;
- selezionare **Manual Selected Default Character Set / Collation**, impostare **Character Set** ad **utf8** e premere **Next**;
- lasciare la selezione su **Install As Windows Service** e lasciare **Service Name=MySQL**; selezionare anche **Include Bin Directory in Windows PATH** e premere **Next**;
- lasciare la selezione su **Modify Security Settings** e nei campi **New root password** e **Confirm** inserire **root**; selezionare la voce **Enable root access from remote machines** e premere **Next**;

.. warning :: Nel passaggio appena descritto la password **deve** essere impostata al valore *root*: in caso contrario, le query per la creazione delle tabelle TConsole, eseguite durante la successiva installazione dell'applicativo, falliranno!

- applicare le configurazioni premendo **Execute** (se a questo punto la finestra dovesse bloccarsi o dare un errore, procedere come indicato nella Nota [2]_);
- al termine verificare che sia presente la spunta su **tutte** le voci ([1]_) e premere **Finish**;

**Terminata l’installazione e la configurazione di MySQL Server si continua con l’installazione di TConsole e delle altre componenti.**

.. toctree::
    :maxdepth: 1

    .. TipologieInstallazione
    InstallazioneTConsole
    InstallazioneServerStandalone

.. rubric:: Note

.. [1] se il servizio Windows Firewall non è attivo, e in precedenza si è messo il flag su **Add firewall exception for this port**, potrebbe comparire un messaggio di errore di questo tipo:

    .. code-block:: shell

        There are no more endpoints available from the endpoint mapper Error code $00800706D9

    In tal caso premere **Back** fino a tornare alla finestra in cui si imposta l’opzione, deselezionarla e procedere con la configurazione.

.. [2] nel caso la finestra di configurazione di MySQL dovesse interrompersi, non rispondere più o restituire un errore per cui fosse impossibile chiuderla allora sarà necessario forzarne la chiusura e ripeterla interamente: nel Task Manager cercare *MySQLInstanceConfig (32 Bit)* e terminarlo, a questo punto nel menu Avvio cercare **MySQL Server Instance Configuration Wizard**, o in alternativa eseguire come amministratore (tasto destro del mouse, clic su **Esegui come Amministratore**):

    .. code-block:: shell

        C:\Program Files (x86)\MySQL\MySQL Server 5.1\bin\MySQLInstanceConfig.exe
    
    selezionare la voce **Reconfigure Instance** e ripetere i passi precedenti (da “selezionare **Detailed Configuration**...” in poi).
