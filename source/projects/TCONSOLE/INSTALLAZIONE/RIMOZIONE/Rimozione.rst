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
- da *Pannello di controllo* \| *Installazione applicazioni* rimuovere “Telenia – TConsole”;
- nella cartella TConsole del disco usato per l’installazione (tipicamente *C:\\Telenia*) rimangono le sottocartelle contenenti i files di log creati durante l’utilizzo ed eventuali altri files di configurazione o di aggiornamento aggiunti dopo l’installazione: è possibile tenere questi files anche in caso di una re-installazione dell’applicazione. In caso contrario si può procedere ad una loro manuale cancellazione;
- verificare se esiste la cartella (nell’utente di utilizzo TConsole) e obbligatoriamente occorre cancellarla: **C:\\Users\\<UTENTE>\\AppData\\Local\\VirtualStore\\Program Files\\Telenia\\TConsole\\**

Al termine, riavviare il PC.

Rimozione completa
==================

**Eseguire per prime le istruzioni per la rimozione parziale.**

Solo nel caso in cui TConsole sia stato installato in modalità Server/Standalone si potranno rimuovere anche tutte le altre componenti installate: **MySQL**, **Borland Database Engine 5.5**, **Borland Runtime Environment 5.0**, **IBM ViaVoice TTS Runtime**.

Rimozione MySQL 4 (per release TConsole fino a 4.x)
---------------------------------------------------

Seguire la seguente procedura per la rimozione del servizio MySQL 4:

- dai Servizi Windows (tipicamente Pannello di controllo \| Strumenti di amministrazione \| Servizi) arrestare MySQL;
- dalla cartella mysql\bin (tipicamente nel disco C:\) eseguire il programma winmysqladmin.exe; compare l’icona di un semaforo verde vicino all’orologio;
- clic col tasto destro sul semaforo e selezionare “WinNT” \| “Stop the Service” dando conferma alla successiva finestra di dialogo: il semaforo diventa rosso;
- clic col tasto destro sul semaforo e selezionare “WinNT” \| “Remove the Service” dando conferma alla successiva finestra di dialogo;
- clic col tasto destro sul semaforo e selezionare “WinNT” \| “Shutdown this Tool” dando conferma alla successiva finestra di dialogo;
- Da Pannello di controllo \| Installazione applicazioni rimuovere “MySQL Servers and Clients”.

Se con winmysqladmin.exe non si riesce a eseguire lo Stop/Remove di MySQL si ottiene lo stesso risultato aprendo un CMD di Windows come amministratore e digitando sc delete MySQL (a questo punto verificare nei servizi che MySQL non sia più elencato).

Rimozione MySQL 5 (per release TConsole 5.x)
--------------------------------------------

Seguire la seguente procedura per la rimozione del servizio MySQL Server 5.1:

- dai Servizi Windows (tipicamente Pannello di controllo \| Strumenti di amministrazione \| Servizi) arrestare MySQL;
- da Pannello di controllo \| Installazione applicazioni rimuovere “MySQL Server 5.1”;
- importante: Eliminare le cartelle di MySQL relativi agli eseguibili e ai dati (vedi path basedir e datadir definiti all’interno di my.ini, tipicamente in C:\Program Files\MySQL\MySQL Server 5.1\: tipicamente basedir=C:\Program Files\MySQL\MySQL Server 5.1\ e datadir=C:\ProgramData\MySQL\MySQL Server 5.1\Data\ oppure datadir=C:\Documents and Settings\All Users\Application Data\MySQL\MySQL Server 5.1\Data\). Per S.O. a 64 bit il percorso di my.ini e basedir è in C:\Program Files (x86)\ anziché in C:\Program Files\;
- accedere al Registro di sistema ed eliminare, se ancora presente, la seguente chiave: Computer\HKEY_LOCAL_MACHINE\SOFTWARE\MySQL AB – per O.S. a 64 bit la chiave è  Computer\HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\MySQL AB

Rimozione altre componenti TConsole
-----------------------------------

Da Pannello di controllo \| Installazione applicazioni rimuovere le seguenti applicazioni:

- Borland Database Engine 5.5;
- Borland Runtime Environment 5.0;
- IBM Via Voice TTS Runtime (se presente).

Al termine, riavviare il PC.

Aggiornamento versioni TConsole precedenti alla 5.2
===================================================

Quando si aggiornano versioni precedenti alla 5.2, verificare che in *C:\\Users\\<UTENTE>\\AppData\\Local\\VirtualStore\\Program Files* non sia presente la cartella Telenia, in caso contrario rimuoverla.

Procedere poi all’aggiornamento della versione ricordandosi di settare i premessi cartella come indicato in :ref:`Installazione TConsole`.