===================================
Impostazione Parametri Fondamentali
===================================

In fase di :ref:`Installazione TConsole`, dopo aver selezionato il tipo di Centrale, nella finestra successiva è possibile impostare, compilando le sezioni opportune (ad es. "TVOX/TAPI/SIP/NORTEL", "SIP/TVOX" etc.), i parametri del dispositivo telefonico da pilotare.

.. important :: In base al tipo di Centrale è necessario compilare **solo i parametri indicati nelle sezioni corripondenti al tipo di Centrale scelta**, lasciando vuoti o inalterati i parametri delle altre sezioni.

Ad es. per versioni SIP vanno compilate tutte e sole le sezioni che presentano la dicitura "**SIP**", quindi "TVOX/TAPI/**SIP**/NORTEL", "TAPI/**SIP**/NORTEL", "**SIP**/TVOX", "**SIP ONLY**", e ignorata l’ultima sezione "TVOX ONLY"; per versioni TAPI vanno compilate tutte e sole le sezioni che presentano la dicitura "**TAPI**", quindi "TVOX/**TAPI**/SIP/NORTEL", "**TAPI**/SIP/NORTEL" e ignorate le altre sezioni.

**I dettagli sulla configurazione dei singoli parametri in base al tipo di Centrale sono descritti nelle apposite sezioni.**

.. image:: /images/TCONSOLE/INSTALLAZIONE/configurazione-parametri.png

I parametri inseriti in questa fase vengono memorizzati nel file di configurazione:

*\[INSTALLDIR\]\\TConsole.ini* ([#]_)

.. important ::
 Se necessario, questo file potrà essere modificato successivamente, ad es. per aggiornamenti di configurazione o per l’impostazione di parametri avanzati, senza dover eseguire una reinstallazione completa di TConsole.
 **Si consiglia il supporto del Service Desk Telenia per modifiche di questo tipo ai files di configurazione**.

.. warning ::
 La modifica del file *TConsole.ini* e degli altri files di configurazione va effettuata **a TConsole chiuso**, pena la possibile perdita delle modifiche applicate.

Di seguito si riportano i parametri del dispositivo da impostare in base al tipo di Centrale selezionata: **per la configurazione effettuata nel corso dell’installazione TConsole fare riferimento solo alla sezione “Parametri richiesti in fase di installazione”**.

**Per l’eventuale modifica dei parametri effettuata successivamente all’installazione** (tramite modifica manuale del file *TConsole.ini* e di eventuali altri files di configurazione) **fare invece riferimento alla sezione “Parametri configurabili in TConsole.ini”**.

.. toctree::
    :maxdepth: 1
 
    ParametriNortel
    ParametriTAPI
    ParametriSIPSNOM
    ParametriTVOX
    .. InstallazioneTConsole
    
.. rubric:: Note

.. [#] valore di default di *\[INSTALLDIR\]*: *C:\\Telenia\\TConsole*