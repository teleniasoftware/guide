.. _Requisiti generali:

==================
Requisiti generali
==================

I requisiti minimi per installare ed utilizzare TConsole sono:

Sistema Operativo
-----------------
- Sistema Operativo a 32 o 64 bit: Windows Vista PRO, Windows Seven PRO, Windows 8/8.1 PRO, Windows 10 PRO o superiore
- Accesso al PC con l'utente *Administrator* locale (chiamato anche Super Amministratore, Built-in Administrator o Amministratore nascosto): è l'account che dispone di tutte le autorizzazioni, può effettuare qualsiasi tipo di modifica sul sistema e non richiede nessun tipo di conferma (ad es. tramite la finestra d'avviso UAC). **Se disabilitato, è necessario farlo attivare** (potrebbe non essere sufficiente accedere con un utente generico a cui sono stati dati i diritti di amministratore).
- Creare una cartella dedicata (ad es. *C:\\Telenia_Setup*) in cui copiare ed estrarre i files di installazione e utility forniti da Telenia (tramite CD oppure dai links per il download).

.. warning:: Per versioni TAPI/TSAPI verificare che il Sistema Operativo sia supportato dal TAPI/TSAPI driver del PBX prima di procedere con l'installazione TConsole (vedi :ref:`Requisiti TAPI`).

Hardware
--------
- CPU processore Intel Dual Core ≥ 2.0 GHz
- RAM ≥ 2GB
- HD ≥ 250 GB di spazio disponibile
- Unità DVD-ROM (16x) (se prevista installazione da CD/DVD)
- Scheda di rete C-LAN
- Scheda audio per Sintesi Vocale e segnalazioni acustiche
- 5 porte USB libere (per dongle, tastiera QWERTY, mouse, barra Braille, alimentazione mixer)
- Monitor 4/3 o 16/9 con risoluzione minima 1280*1024
- Tastiera QWERTY **con tastierino numerico** (*Keypad*)
- Mouse

Opzionali
---------
- Monitor multimediale (o casse separate) per riproduzione Sintesi Vocale e segnalazioni acustiche
- Porta parallela (solo se si utilizza barra Braille Sistel)
- Per la barra Braille Sistel è necessario installare i driver separatamente utilizzando l'apposito setup ed è necessario disporre di una chiave SISTEL del tipo 87/6

Firewall di Windows o di terze parti
------------------------------------
.. important:: Deve essere mantenuto attivo durante le fasi di installazione di MySQL, di TConsole e anche al primo avvio di TConsole, affinché (ad es. nel caso di Windows Firewall) vengano richieste e fornite tutte le conferme per la creazione delle eccezioni o l'apertura di determinate porte (vedi :ref:`Installazione MySQL` e :ref:`Installazione TConsole`).

Antivirus di sistema
--------------------
.. important:: Deve essere prevista la possibilità, una volta terminata l'installazione di TConsole, di creare un'eccezione per la cartella e gli eseguibili del programma (*TConsole.exe*).

.. spostato in Requisiti
  **In base al tipo di centrale sono inoltre richiesti ulteriori requisiti, illustrati nella relativa sezione.**