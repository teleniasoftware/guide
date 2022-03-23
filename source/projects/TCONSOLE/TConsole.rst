==========
TConsole 5
==========

.. image:: /images/TCONSOLE/TConsole_logo.png

TConsole è la soluzione basata su PC Windows per il posto operatore e può essere utilizzato su diverse tipologie di centrale tra cui Nortel, Cisco, Avaya, |tvox| e qualsiasi altro centralino SIP che consenta l’utilizzo di telefoni SNOM (vedi :ref:`centrali compatibili`).

**TConsole è adatto per centralinisti vedenti, ipo vedenti e non vedenti.**

TConsole è il posto operatore che gestisce in modo rapido ed efficiente le chiamate in ingresso ed in uscita, fornendo utili informazioni come il numero chiamante e chiamato, il tipo di chiamata (interna, entrante, uscente), lo stato delle chiamate in coda ([1]_). Ogni chiamata è facilmente controllabile attraverso appositi tasti funzione richiamabili da tastiera del PC oppure, se richiesto, da :ref:`Barra Braille`.

TConsole è caratterizzato da una semplice ed intuitiva interfaccia grafica, progettata per essere utilizzabile anche da operatori inesperti o diversamente abili, che migliora l’immagine aziendale e le performance di servizio ai clienti-utenti.

È fornito di una rubrica **locale** ([2]_) che permette di gestire e di ricercare in modo semplice e rapido i numeri interni o esterni e di inoltrare la chiamata automaticamente senza la necessità di comporre il numero telefonico.

.. important ::
    La conoscenza delle funzioni di base del posto operatore (dispositivo telefonico oppure dispositivo M2250 o PC-CIU nel caso Nortel) è un pre-requisito per l’utilizzo del posto operatore Telenia TConsole.

    **L’installazione e la configurazione di TConsole deve essere effettuata a cura di un tecnico qualificato.**

.. Questa sezione illustra la procedura di installazione e configurazione di TConsole 5, **applicabile a partire dalla versione 5.7.27**.

Questa documentazione si suddivide in due macrosezioni:

- :ref:`Manuale Installazione`, destinato principalmente a personale tecnico affinché possa eseguire correttamente l'installazione e la configurazione dell'applicazione
- :ref:`Guida Utente`, necessaria all'operatore centralinista per lavorare correttamente sfruttando l'interfaccia del programma e le funzionalità messe a disposizione

.. toctree::
    :maxdepth: 5
 
    ./INSTALLAZIONE/ManualeInstallazione
    ./UTENTE/GuidaUtente

.. rubric:: Note

.. [1] per disporre su TConsole dell'informazione relativa al numero di chiamate in coda, ed eseguire funzioni quali pickup della chiamata e parcheggi **è necessaria la presenza di un TVOX** che svolga la funzione di TQM
.. [2] in presenza di più postazioni TConsole è possibile utilizzare un'unica rubrica centralizzata, condivisa da tutte le postazioni (vedi :ref:`Installazione Client`). È anche possibile, previa verifica di fattibilità, predisporre una procedura di import dei dati di rubrica da una fonte esterna.