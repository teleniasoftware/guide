.. _sito di SNOM: https://service.snom.com/display/wiki/D-Series+Settings
.. _TConsole.ini:

============
TConsole.ini
============

Il file *TConsole.ini* contiene le configurazioni base del programma quali ad es. tipologia di centrale e interno da controllare (vedi :ref:`Impostazione parametri fondamentali`), oltre che numerosi altri parametri di seguito descritti.

Sezione [PO]
============

PHONE_KEYPAD
------------
Se configurato a *SI*, imposta il tastierino numerico del PC come la tastiera del telefono, invertendo la posizione delle file di tasti 1-2-3 e 7-8-9, pertanto premendo ad es. *1* verrà inviato *7*, premendo *8* verrà inviato *2* e così via. Il valore di default è *NO*.

.. code-block:: ini

	PHONE_KEYPAD=SI

DISPLAY_ACTIVE_STATE
--------------------
**Solo per TConsole su PBX Avaya o Nortel M2250/CIU** è possibile abilitare/disabilitare la segnalazione dello stato attivo della console Avaya o Nortel M2250/CIU impostando il parametro *DISPLAY_ACTIVE_STATE=NO* (il valore di default è *SI*).

.. code-block:: ini

    DISPLAY_ACTIVE_STATE=SI

.. _ID:

ID
--

In presenza di più di una postazione TConsole, questo parametro va configurato con un numero progressivo e *univoco* per ogni postazione. Il valore di default è *1*.

.. important :: La configurazione di questo parametro è **fondamentale** in ambiente Nortel per la corretta gestione delle chiamate VIP (vedi :ref:`Prenotazioni VIP`, :ref:`Parametri Nortel` e :ref:`Installazione Client`).

TAPI_CALL_ON_BUSY_CODE
----------------------
Tale parametro va settato con il codice configurato su PBX per trasferire le chiamate **anche su occupato**.
Tale codice verrà anteposto ad ogni chiamata da rubrica, da Post-IT ed in fase di trasferta dal Keypad.

Valorizzare con *-* (valore di default) se **non** si vuole utilizzare alcun codice.

.. warning :: Se viene settato con un codice errato (non esistente su PBX) si ottiene l’anomalia di impossibilità di trasferire le chiamate.

.. code-block:: ini

    TAPI_CALL_ON_BUSY_CODE=*60 (settato con un codice)

.. code-block:: ini

    TAPI_CALL_ON_BUSY_CODE=- (non settato)

LINE_0_TOP
----------
Impostare il parametro *LINE_0_TOP=SI* per invertire la visualizzazione dell’ordine delle linee entranti (Loop): Linea "0" in alto e Linea "5" in basso. Il valore di default è *NO* (Linea "0" in basso e Linea "5" in alto).

.. code-block:: ini

	LINE_0_TOP=SI

.. _TConsole.ini Sezione IPO PLUS:

IPO_PLUS_ICI_TOP
----------------
**Solo per la vista IPO PLUS**, impostare il parametro *IPO_PLUS_ICI_TOP=SI* per:

- aumentare la dimensione (da 46 a 55) del carattere dei numeri in ingresso/uscita (linee del Display)
- allineare i 3 riquadri ICI ("EN"-"IN"-"RT") alla prima linea in alto, spostando in basso l'indicatore (pallino verde/rosso) di connessione del dispositivo

Il valore di default è *NO*.

.. code-block:: ini

	IPO_PLUS_ICI_TOP=SI

Vista IPO PLUS con *IPO_PLUS_ICI_TOP=NO* (default):

.. image:: /images/TCONSOLE/INSTALLAZIONE/CONFIGURAZIONE/IPO_PLUS_ICI_TOP_NO.png

Vista IPO PLUS con *IPO_PLUS_ICI_TOP=SI*:

.. image:: /images/TCONSOLE/INSTALLAZIONE/CONFIGURAZIONE/IPO_PLUS_ICI_TOP_SI.png

IPO_PLUS_TIME
-------------
**Solo per la vista IPO PLUS**, impostare il parametro *IPO_PLUS_TIME=SI* per abilitare l’orologio in alto a destra (vedi immagini di esempio precedenti relative al parametro *IPO_PLUS_ICI_TOP*, in cui è settato *IPO_PLUS_TIME=SI*).

.. code-block:: ini

	IPO_PLUS_TIME=SI

Sezione [TAPI-SIP]
==================

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
-------------------------------------
Parametro valido (il valore di default è *NO*) **solo per centrale Avaya che utilizza Softphone Avaya**.
Tale parametro si rende necessario solo nel caso di mancanza di informazioni provenienti dal carrier.

Se impostato a *SI* la chiamata in uscita viene riconosciuta come risposta anche se di fatto è ancora in ring.
Se impostato a *NO* nel caso di alcune chiamate in uscita esterne potrebbe non essere riconosciuto il connect e quindi non sarà possibile mettere in attesa o trasferire.

.. code-block:: ini

    TAPI_AVAYA_OUTBOUND_CONNECTED_ON_RING=NO

Sezione [PHONE_SETTINGS]
========================

**Per il TConsole di tipo SIP SNOM**, per risolvere il problema che, nel caso di una chiamata trasferita da un Telefono SNOM verso un numero esterno, venga abbattuta la prima chiamata e rigenerata una seconda, settare il seguente parametro a *on* (valore di default):

.. code-block:: ini

    attended_transfer_on_ringing=on

.. tip :: In questa sezione, oltre ai parametri già presenti di default per il corretto funzionamento di TConsole, è possibile configurare altri parametri (vedi `sito di SNOM`_) che verranno impostati sul telefono ([1]_) al momento dell'avvio di TConsole.

.. _TConsole.ini Sezione BRAILLE:

Sezione [BRAILLE]
=================

In questa sezione è possibile associare ai tasti funzione della Barra Braille determinate funzioni di TConsole.

TYPE
----

Impostare il parametro TYPE in base al tipo di Barra Braille utilizzata:

.. code-block:: ini

    ;	TYPE: tipo di barra braille. Tipi disponibili: LILLI; SISTEL; ALVA544; LILLI_80
    TYPE=LILLI
    ;	SERIALPORT: Porta seriale da utilizzare con barra ALVA544 valori possibili: COM1, COM2, ... 
    SERIALPORT=-
    ;	LINELEN: lunghezza in caratteri della barra braille
    LINELEN=40

Per la Barra Braille Lilli a 80 caratteri occorre configurare i seguenti parametri:

.. code-block:: ini

    TYPE=LILLI_80
    LINELEN=80

TABLE
-----

Sempre per la Barra Braille Lilli è possibile impostare il tipo di alfabeto utilizzato (a 6 o ad 8 punti):

.. code-block:: ini

    ;	TABLE=8 o TABLE=6 (alfabeto braille a 6 o 8 pti)
    TABLE=8

.. _BRAILLE_STRING_ON_STATUS_BAR:

BRAILLE_STRING_ON_STATUS_BAR
----------------------------

Se impostato a *SI*, permette di visualizzare anche nella :ref:`Barra di Stato` di TConsole il testo inviato alla Barra Braille. Il valore di default è *NO*.

.. code-block:: ini

    BRAILLE_STRING_ON_STATUS_BAR=NO

Configurazione dei tasti funzione per Barra Braille Lilli
---------------------------------------------------------

Per l’associazione dei tasti funzione della Barra Braille Lilli **alle rispettive combinazioni di tasti della tastiera del PC** (e di conseguenza alle funzionalità di TConsole) è presente una configurazione predefinita che è possibile modificare a seconda delle esigenze dell’operatore:

.. code-block:: ini

    ;	ASSOCIAZIONE TRA TASTI LILLI E TASTI PC
    SHIFT=Esc
    ; 	tasti di controllo: Simple, Shift, Long, ShiftLong
    LEFT=,,,,
    UP=Up,PgUp,,Home,
    DOWN=Down,PgDn,,End,
    RIGHT=,,,,
    ;	tasti funzione: Simple, Shift, Long, ShiftLong
    F1=F3,Ctrl+D,,,
    F2=F12,,,,
    F3=,,,,
    F4=,,,,
    F5=F4,,,,
    F6=,,,Ctrl+Alt+X,
    F7=*[Tn],,,,
    F8=-[Tn],,,,
    F9=+[Tn],Ctrl+0[Tn],,,
    F10=Enter[Kp],,,,

Nell'esempio riportato, nella penultima riga la dicitura:

.. code-block:: ini

    F9=+[Tn],Ctrl+0[Tn],,,

indica rispettivamente:

- tasto funzione della Barra Braille: *F9* (secondo tasto funzione da destra)
- combinazione di tasti corrispondente alla pressione breve (semplice) del tasto funzione: *+* (del tastierino numerico)
- combinazione di tasti corrispondente alla pressione breve del tasto funzione + tasto Shift della Barra: *Ctrl+0* (del tastierino numerico)
- combinazione di tasti corrispondente alla pressione lunga del tasto funzione: non configurato
- combinazione di tasti corrispondente alla pressione lunga del tasto funzione + tasto Shift della Barra: non configurato

.. rubric:: Note

.. [1] per mantenerli anche alla chiusura di TConsole, questi parametri vanno memorizzati agendo sull'interfaccia web del telefono: https://service.snom.com/display/wiki/How+do+snom+phones+handle+setting+changes