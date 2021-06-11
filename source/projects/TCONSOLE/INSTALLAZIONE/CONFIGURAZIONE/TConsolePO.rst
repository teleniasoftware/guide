=========================
TConsole.ini Sezione [PO]
=========================

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

.. descrivere il parametro ID per il TConsoleServer e per il tratamento VIP

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