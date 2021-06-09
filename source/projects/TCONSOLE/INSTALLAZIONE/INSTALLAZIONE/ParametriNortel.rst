==============================
Parametri Nortel (CIU o M2250)
==============================

Parametri richiesti in fase di installazione (sezioni "NORTEL")
===============================================================

- **PO DN**: impostare il parametro con il DN del dispositivo telefonico da pilotare
- **Device Tapi o COM (per Nortel)**: inserire il numero della porta “COM” del PC a cui sarà collegato il dispositivo (ad es. *COM1*, *COM2* etc.)
- **DN deviazione a Notte**: (lasciare vuoto)

.. note :: Il cavo di connessione tra PC e Nortel CIU è un cavo seriale 9-25 PIN inverito.

Parametri configurabili in TConsole.ini
=======================================

- impostare il parametro **TYPE**\ =\ *NORTEL_M1250* o *NORTEL_M2250* o *NORTEL_CIU* a seconda del dispositivo telefonico da pilotare
- impostare il parametro **IADN** con il DN del dispositivo telefonico da pilotare
- impostare il parametro **DEVICE** con il numero della porta “COM” del PC a cui sarà collegato il dispositivo (ad es. *COM1*, *COM2* etc.)
- (se presenti più postazioni) modificare il parametro **ID** con il numero progressivo della postazione (vedi :ref:`Installazione Client`)
- nel file *\[INSTALLDIR\]\\config\\tabparam* ([1]_) impostare il parametro **TQM_TYPE**\ =\ *-* (trattino), in questo modo si abilita il tasto “Notte/Giorno” (Sole Luna)

**Esempio TConsole.ini NORTEL_M2250:**

.. code-block:: ini
    
    TYPE=NORTEL_M2250
    IADN=2000
    DEVICE=COM1
    ID=1

**Esempio tabparam NORTEL_M2250:**

.. code-block:: ini
        
        *              TQM_TYPE             -

.. rubric:: Note

.. [1] valore di default di *\[INSTALLDIR\]*: |tconsole_default_installdir|