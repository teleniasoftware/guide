=================
Sistema Operativo
=================

Sono necessarie le seguenti impostazioni di Windows (dal Pannello di controllo):

- nelle opzioni di Risparmio energia impostare a “Mai” o disattivare le voci relative a:
 - *Spegni il monitor*
 - *Disattiva i dischi rigidi*
 - *Standby*
 - *Sospensione*
 - *Consenti sospensione ibrida*;
- nelle opzioni di configurazione aspetto e video impostare *nessuno screen saver* e lo stile Windows classico;
- dai Servizi Windows, se sono presenti problemi di comunicazione tra TConsole e telefono, disattivare Windows Firewall e verificare se i problemi si presentano ancora (in caso negativo è necessario ricreare le eccezioni a Windows Firewall per il tipo di rete utilizzato);
- dai Servizi Windows, se consentito, disattivare gli Aggiornamenti automatici di Windows;
- verificare la seguente chiave di registro per Hot-Key (ALT+F1), impostandola a *0*:

 .. code-block:: registry

    HKEY_CURRENT_USER\ControlPanel\Desktop: ForegroundLockTimeout=0

.. tip :: Se la postazione TConsole è condivisa da più utenti, ognuno che accede con la propria utenza Windows, la chiave di registro va impostata per ognuno di questi, eseguendo il seguente comando da una finestra di CMD dopo aver effettuatto l'accesso a Windows con ognuna delle utenze interessate:

    .. code-block:: shell

        reg add "HKEY_CURRENT_USER\Control Panel\Desktop" /v "ForegroundLockTimeout" /t REG_DWORD /d "0" /f