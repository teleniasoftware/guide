.. _Backup TConsole:

===============
Backup TConsole
===============

Per salvare applicativi, configurazioni e database occorre salvare le seguenti cartelle:

- **applicativi e configurazioni**: *\[INSTALLDIR\]* ([1]_), solitamente |tconsole_default_installdir| oppure *C:\\Program Files (x86)\\Telenia\\* oppure *C:\\Program Files\\Telenia\\* (se diverso dal percorso di default);
 .. tip :: Le cartelle *\[INSTALLDIR\]\\log* e *\[INSTALLDIR\]\\dbg* contengono files di log e possono essere tralasciate.

 .. tip :: I colori e la dimensione dei caratteri (preconfigurati o impostati dall'utente) sono memorizzati nel file *[INSTALLDIR\]\\TConsole.ini* e nei files *RubInt.ini*, *RubEst.ini* e *tabparam* nella cartella *\[INSTALLDIR\]\\config*.
     
- **database**: vedi path *datadir* (cartella *data*) definito all’interno di *my.ini*, tipicamente in *C:\\Program Files (x86)\\MySQL\\MySQL Server 5.1\\*: tipicamente *datadir=C:\\ProgramData\\MySQL\\MySQL Server 5.1\\Data\\* oppure *datadir=C:\\Documents and Settings\\All Users\\Application Data\\MySQL\\MySQL Server 5.1\\Data\\*. Per S.O. a 32 bit il percorso di *my.ini* è in *C:\\Program Files\\* anziché in *C:\\Program Files (x86)\\*.

 .. tip :: In alternativa, il backup del database si può effettuare eseguendo, tramite un client MySQL, un dump dei database *tconfig* e *tgest*.

.. important :: Per il ripristino di una postazione TConsole a partire da un backup completo contattare il Service Desk Telenia.

.. rubric:: Note

.. [1] valore di default di *\[INSTALLDIR\]*: |tconsole_default_installdir|