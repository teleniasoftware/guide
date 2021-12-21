===============
Installazione
===============

L'installazione si effettua eseguendo il setup che provvede ad installare i programmi necessari. 

Il percorso di installazione di default è C:\\Programmi\\Telenia\\TConsoleServer.

.. note:: Se si sta installando il TConsoleServer su una macchina in cui è già installato il TSAM o il TConsole, è necessario deselezionare tutti gli applicativi di supporto (BDE, Runtime, ...), lasciando flaggati i soli moduli TConsoleServer (obbligatorio) e JVM (aggiuntivo).

Dopo l'installazione occorre configurare i parametri presenti nel file *tabparam.ini* all'interno della cartella config.

.. code-block:: ini
    
    [DATABASE]  
    Active=NO

    [BARRATELSERVER]
    Ip=192.168.0.4 
    Port=5450

    [BLF]
    Active=NO 
    QueryDescription=NO

    [VIP]
    Active=YES

    [LOG] 
    Level=0xFFFFFFF6

I parametri presenti nel file *tabparam.ini* saranno illustrati nei capitoli di ciascun modulo.

Una volta configurati i parametri si può procedere all'avvio del servizio di Windows *TConsoleServerStdSvc*.

.. note:: Nel caso di utilizzo del database MYSQL, prima di avviare il servizio, creare la dipendenza del servizio *TConsoleServerStdSvc* dal servizio MySql. Lo si può fare manualmente o mediante file batch presente nella cartella \bin del *TConsoleServerStd*.

