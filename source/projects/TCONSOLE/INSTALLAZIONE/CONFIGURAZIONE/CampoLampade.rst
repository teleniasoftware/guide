.. _CampoLampade:

=============
Campo Lampade
=============

Per gestire il campo lampade è necessario configurare nel :ref:`Profilo Utente` il valore *CAMPO LAMPADE = SI*.

Per le centrali Nortel il TConsoleServer NON viene utilizzato per la gestione del campo lampade per cui occorre assicurarsi che il parametro contenuto in *\[TCS_INSTALLDIR\]\\config\\tabparam.ini* ([1]_) sia disabilitato:

.. code-block:: ini

    [BLF]
    Active=NO

e che il file *\[TCS_INSTALLDIR\]\\config\\devices* ([1]_) sia vuoto.

Per le altre tipologie di centrale il campo lampade viene gestito con l’ausilio del TConsoleServer per cui occorre inserire, in *\[INSTALLDIR\]\\config\\tabparam* ([2]_) nel parametro *TCONSOLESERVER*, l’IP della macchina su cui è installato il TConsoleServer.

**Per i dettagli della configurazione si rimanda al manuale di installazione del TConsoleServer.**

.. rubric:: Note

.. [1] valore di default di *\[TCS_INSTALLDIR\]* per macchine a 64 bit: |tconsoleserver_default_installdir|

.. [2] valore di default di *\[INSTALLDIR\]*: |tconsole_default_installdir|