===========
TCLoops.txt
===========

Questo file viene utilizzato per le diciture visualizzate nei campi "Linea" (Loop) a fronte di un cambiamento di stato della linea (“Libero”, “Risposta” etc.).

Nella configurazione di default quando una linea è libera viene visualizzata la scritta "Libero": se si desidera che il campo linea non riporti alcuna scritta occorre sostituire la dicitura "Libero" con una stringa vuota, modificando la riga:

.. code-block:: ini

    0,0,0,Libero,N,

Nella dicitura:

.. code-block:: ini

    0,0,0,,N,