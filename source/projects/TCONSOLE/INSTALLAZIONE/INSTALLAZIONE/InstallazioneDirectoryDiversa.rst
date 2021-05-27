=============================================================
Installazione su directory diversa dalla directory di default
=============================================================

Dalla release TConsole 5.7.13, se in fase di installazione si è selezionata una directory di installazione *\[INSTALLDIR\]* diversa dalla directory di default (*C:\\Telenia\\TConsole*), al termine dell’installazione sarà necessario configurare opportunamente i seguenti files:

- *\[INSTALLDIR\]\\THotKeys\\THotKeys.ini* impostando il corretto percorso di TConsole.exe nel parametro *Key1*
- *\[INSTALLDIR\]\\bin\\AvvioTConsole.bat* modificando la selezione della cartella con la corretta cartella di installazione

.. toctree::
    :maxdepth: 1
    
    .. InstallazioneServerStandalone
    .. InstallazioneClient
    InstallazionePersonalizzata
    TipologieInstallazione