.. _TConsole.ini Sezione BRAILLE:

==============================
TConsole.ini Sezione [BRAILLE]
==============================

In questa sezione è possibile associare ai tasti funzione della Barra Braille determinate funzioni di TConsole.

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

Sempre per la Barra Braille Lilli è possibile impostare il tipo di alfabeto utilizzato (a 6 o ad 8 punti):

.. code-block:: ini

    ;	TABLE=8 o TABLE=6 (alfabeto braille a 6 o 8 pti)
    TABLE=8

Per l’associazione dei tasti funzione della Barra Braille **alle rispettive combinazioni di tasti della tastiera del PC** è presente una configurazione predefinita che è possibile modificare a seconda delle esigenze dell’operatore:

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