.. _Chiamate VIP:

===============
Le chiamate VIP
===============

Il modulo VIP si occupa della gestione delle chiamate prioritarie cosidette "VIP". Il modulo si attiva da parametro **Active** della sezione *[VIP]* nel file *tabparam.ini*.

Di seguito si riportano le sezioni da configurare per la gestione VIP del file *tabparam.ini* :

.. code-block:: ini

    [VIP]
    Active=SI

.. note:: Per attivare la sezione VIP è necessario attivare la sezione DATABASE.

.. code-block:: ini
    
    [DATABASE]
    Active=YES
    DSNPrimary=teleniadb
    DSNSecondary=teleniabackup
    FaultTolerance=NO

.. warning:: Nel caso sia attivo il modulo VIP non attivare il fault tolerance del db (parametro **FaultTolerance**\ =\ *NO*).
