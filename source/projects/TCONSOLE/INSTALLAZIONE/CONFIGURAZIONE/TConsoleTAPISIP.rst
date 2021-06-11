===============================
TConsole.ini Sezione [TAPI-SIP]
===============================

SIP_ENABLE_BLIND_TRANSFER
-------------------------
La trasferta di chiamata da TConsole per tutti i tipi di centrale si può fare come:

- trasferta con consultazione
- trasferta su ring

**Per il TConsole di tipo SIP SNOM** è possibile effettuare anche la trasferta "blind" (cieca) settando il parametro *SIP_ENABLE_BLIND_TRANSFER=SI* (il valore di default è *NO*).

.. code-block:: ini

    SIP_ENABLE_BLIND_TRANSFER=SI

Per effettuare questo tipo di trasferta:

- si digita l’interno a cui trasferire la chiamata;
- si preme il tasto *TN\[Invio\]* (NON si preme il tasto *TN\[.\]* come si fa normalmente su TConsole SIP SNOM per concludere la digitazione del numero).

SIP_DISPLAY_INTERNAL_STR
------------------------
**Per il TConsole di Tipo SIP SNOM** è possibile riconoscere le chiamate interne attraverso il riconoscimento di una particolare “stringa” che identifica una chiamata proveniente da un interno.
La stringa da riconoscere deve essere impostata nel parametro *SIP_DISPLAY_INTERNAL_STR*.

Al riconoscimento della stringa si ottiene l’illuminazione del tasto ICI “INTERNA”.

.. code-block:: ini

    SIP_DISPLAY_INTERNAL_STR=Internal

Per **non** riconoscere le chiamate interne occorre settare il parametro con il carattere *-* (trattino).

SIP_DISPLAY_RIT_STR
-------------------
**Per il TConsole di Tipo SIP SNOM** è possibile riconoscere i ritorni sul PO attraverso il riconoscimento di una particolare “stringa”.
La stringa da riconoscere deve essere impostata nel parametro *SIP_DISPLAY_RIT_STR*.

Al riconoscimento della stringa si ottiene l’illuminazione del tasto ICI “RITORNO”.

.. code-block:: ini

    SIP_DISPLAY_RIT_STR=-

Per **non** riconoscere i ritorni occorre settare il parametro con il carattere *-* (trattino).

SIP_DTMF_BUTTON
---------------
**Per il TConsole di Tipo SIP SNOM** si può abilitare la possibilità di digitare i caratteri DTMF settando il parametro *SIP_DTMF_BUTTON*.
Il parametro deve assumere il valore del numero della linea **meno** utilizzata del telefono, per cui se un telefono ha 6 linee disponibili occorre settare il parametro con il valore *6*.

.. code-block:: ini

    SIP_DTMF_BUTTON=6

TEST_DEVICE_TIMEOUT
-------------------
Espresso in millisecondi, **se valorizzato** viene eseguito periodicamente:

- un test di connessione verso il TVox/TQM se in *\[INSTALLDIR\]\\config\\tabparam* il parametro *TQM_TYPE* è valorizzato a *TVOX_R1* oppure *TVOX_R2* oppure *TVOX_R2_PICKUP* oppure *TAPITVOX*
- un test delle TAPI (vedi :ref:`Requisiti TAPI`) nel caso in cui in *\[INSTALLDIR\]\\config\\tabparam* il parametro *TQM_TYPE* assuma altri valori

.. code-block:: ini

    TEST_DEVICE_TIMEOUT=500

Per **non** eseguire il test di connessione lasciare il parametro vuoto (valore di default).

TAPI_AVAYA_OUTBOUND_CONNECTED_ON_RING
------------------------------------------
Parametro valido (il valore di default è *NO*) **solo per centrale Avaya che utilizza Softphone Avaya**.
Tale parametro si rende necessario solo nel caso di mancanza di informazioni provenienti dal carrier.

Se impostato a *SI* la chiamata in uscita viene riconosciuta come risposta anche se di fatto è ancora in ring.
Se impostato a *NO* nel caso di alcune chiamate in uscita esterne potrebbe non essere riconosciuto il connect e quindi non sarà possibile mettere in hold o trasferire.

.. code-block:: ini

    TAPI_AVAYA_OUTBOUND_CONNECTED_ON_RING=NO