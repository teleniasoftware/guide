.. _Rimozione TConsole:

=====================
Rimozione di TConsole
=====================

Durante il processo di installazione di TConsole vengono installate, oltre al programma TConsole, anche altre componenti necessarie al funzionamento dell’applicazione.

Si possono distinguere due processi di rimozione dell’applicazione TConsole:

- la rimozione del solo programma TConsole (**rimozione parziale**);
- la rimozione di tutte le componenti dell’applicazione (**rimozione completa**).

Rimozione parziale
==================

Seguire la seguente procedura:

- se attivo, uscire dal programma TConsole;
- da *Pannello di controllo* \| *Installazione applicazioni* rimuovere *Telenia – TConsole*;
- nella cartella TConsole del disco usato per l’installazione (tipicamente |tconsole_default_installdir|) rimangono le sottocartelle contenenti i files di log creati durante l’utilizzo ed eventuali altri files di configurazione o di aggiornamento aggiunti dopo l’installazione: è possibile tenere questi files anche in caso di una re-installazione dell’applicazione. In caso contrario si può procedere ad una loro cancellazione manuale;
- verificare se esiste la cartella (nell’utente Windows di utilizzo TConsole) e obbligatoriamente occorre cancellarla: *C:\\Users\\<UTENTE>\\AppData\\Local\\VirtualStore\\Program Files\\Telenia\\TConsole\\*

Al termine, riavviare il PC.

Rimozione completa
==================

**Eseguire per prime le istruzioni per la rimozione parziale.**

Solo nel caso in cui TConsole sia stato installato in modalità Server/Standalone (vedi :ref:`Installazione Server Standalone`) si potranno rimuovere anche tutte le altre componenti installate: **MySQL**, **Borland Database Engine 5.5**, **Borland Runtime Environment 5.0**, **IBM ViaVoice TTS Runtime**.

Rimozione MySQL 5 (per release TConsole da 5.x)
-----------------------------------------------

Seguire la seguente procedura per la rimozione del servizio *MySQL Server 5.1*:

- dai Servizi Windows (tipicamente *Pannello di controllo* \| *Strumenti di amministrazione* \| *Servizi*) arrestare *MySQL*;
- da *Pannello di controllo* \| *Installazione applicazioni* rimuovere *MySQL Server 5.1*;
- importante: Eliminare le cartelle di *MySQL* relative agli eseguibili e ai dati: vedi path *basedir* e *datadir* (cartella *data*) definito all’interno di *my.ini*, tipicamente in *C:\\Program Files (x86)\\MySQL\\MySQL Server 5.1\\*: tipicamente *datadir=C:\\ProgramData\\MySQL\\MySQL Server 5.1\\Data\\* oppure *datadir=C:\\Documents and Settings\\All Users\\Application Data\\MySQL\\MySQL Server 5.1\\Data\\*. Per S.O. a 32 bit il percorso di *my.ini* e *basedir* è in *C:\\Program Files\\* anziché in *C:\\Program Files (x86)\\*.
- accedere al Registro di sistema ed eliminare, se ancora presente, la seguente chiave: 

  .. code-block:: ini

        Computer\HKEY_LOCAL_MACHINE\SOFTWARE\MySQL AB

  Per S.O. a 64 bit la chiave è:

  .. code-block:: ini

      Computer\HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\MySQL AB

Rimozione MySQL 4 (per release TConsole fino a 4.x)
---------------------------------------------------

Seguire la seguente procedura per la rimozione del servizio *MySQL 4*:

- dai Servizi Windows (tipicamente *Pannello di controllo* \| *Strumenti di amministrazione* \| *Servizi*) arrestare MySQL;
- dalla cartella *C:\\mysql\\bin* eseguire il programma *winmysqladmin.exe*; compare l’icona di un semaforo verde nel Systray;
- clic col tasto destro sul semaforo e selezionare *WinNT* \| *Stop the Service* dando conferma alla successiva finestra di dialogo: il semaforo diventa rosso;
- clic col tasto destro sul semaforo e selezionare *WinNT* \| *Remove the Service* dando conferma alla successiva finestra di dialogo;
- clic col tasto destro sul semaforo e selezionare *WinNT* \| *Shutdown this Tool* dando conferma alla successiva finestra di dialogo;
- Da *Pannello di controllo* \| *Installazione applicazioni* rimuovere *MySQL Servers and Clients*.

Se con *winmysqladmin.exe* non si riesce a eseguire lo Stop/Remove di *MySQL* si ottiene lo stesso risultato aprendo una finestra di **CMD come amministratore** e digitando il comando:

.. code-block:: ini
    
    sc delete MySQL

A questo punto verificare nei servizi che *MySQL* non sia più elencato.

Rimozione altre componenti TConsole
-----------------------------------

Da Pannello di controllo \| Installazione applicazioni rimuovere le seguenti applicazioni:

- Borland Database Engine 5.5;
- Borland Runtime Environment 5.0;
- IBM Via Voice TTS Runtime (se presente).

Al termine, riavviare il PC.

Aggiornamento versioni TConsole precedenti alla 5.2
===================================================

Quando si aggiornano versioni precedenti alla 5.2, verificare che in *C:\\Users\\<UTENTE>\\AppData\\Local\\VirtualStore\\Program Files\\* non sia presente la cartella *Telenia*, in caso contrario rimuoverla.

Procedere poi all’aggiornamento della versione ricordandosi di settare i premessi cartella come indicato in :ref:`Installazione TConsole`.