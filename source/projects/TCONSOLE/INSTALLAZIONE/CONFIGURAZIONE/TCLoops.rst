.. _TCLoops.txt:

=================================
TODO TCLoops.txt
=================================

La trasferta di chiamata da TConsole per tutti i tipi di centrale si può fare come:

- trasferta con consultazione
- trasferta su ring

**Per il TConsole di tipo SIP SNOM** è possibile effettuare anche la trasferta "blind" (cieca) settando il parametro *SIP_ENABLE_BLIND_TRANSFER=SI* (il valore di default è *NO*).

.. code-block:: ini

    SIP_ENABLE_BLIND_TRANSFER=SI

Per effettuare questo tipo di trasferta:

- si digita l’interno a cui trasferire la chiamata;
- si preme il tasto *TN\[Invio\]* (NON si preme il tasto *TN\[.\]* come si fa normalmente su TConsole SIP SNOM per concludere la digitazione del numero).




.. TODO serve la nota????????

.. rubric:: Note

.. [1] valore di default di *\[INSTALLDIR\]*: |tconsole_default_installdir|