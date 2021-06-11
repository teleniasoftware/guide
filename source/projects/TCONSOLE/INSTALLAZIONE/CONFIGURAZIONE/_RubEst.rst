==========
RubEst.ini
==========

Sezione COMMON
==============

RIC_ALT
-------
Questo parametro è utilizzato per la ricerca alternativa all’interno della rubrica Esterna. Si rimanda a §6.5.5 per la descrizione dell’analogo parametro per la rubrica Interna.

Se lasciato vuoto, la ricerca alternativa verrà effettuata nel campo del dettaglio contatto che si trova selezionato al momento della pressione del tasto funzione associato (default F11).

Es. per eseguire la ricerca alternativa **sempre** nel campo SETTORE:

.. code-block:: ini

    RIC_ALT=SETTORE

Es. per eseguire la ricerca alternativa nel campo dettaglio che è stato **di volta in volta** selezionato:

.. code-block:: ini

    RIC_ALT=