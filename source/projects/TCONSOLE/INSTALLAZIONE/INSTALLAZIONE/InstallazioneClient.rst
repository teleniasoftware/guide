=========================
Installazione tipo Client TODO
=========================

L’installazione di tipo Server/Standalone va effettuata nei seguenti casi:

- **postazione TConsole unica e indipendente**
- **postazione master di una rete di TConsole**

.. important :: **Prima di procedere con l’installazione dell’applicativo TConsole** è necessario installare e configurare il servizio MySQL, attraverso il relativo wizard.

.. warning :: L'installazione dell'applicativo TConsole esegue una serie di *query* per creare, nel database locale della postazione, le tabelle necessarie al funzionamento del programma: **è quindi fondamentale che il servizio MySQL sia stato preventivamente installato e configurato correttamente!**

.. toctree::
    :maxdepth: 1

    .. TipologieInstallazione
    .. InstallazioneServerStandalone
    InstallazioneMySQL
    InstallazioneTConsole