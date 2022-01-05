.. _Parametri SIP SNOM:

==============================================
Parametri SIP SNOM (nel caso di telefono SNOM)
==============================================

Parametri richiesti in fase di installazione (sezioni "SIP")
=============================================================

- **PO DN**: impostare il parametro con il DN del dispositivo da pilotare
- **Device Tapi o COM (per Nortel)**: *-* (trattino **obbligatorio**)
- **DN deviazione a Notte**: (opzionale) inserire l’interno per la “deviazione a notte”, se non utilizzato lasciare il parametro vuoto
- **IP Telefono/TVox**: indirizzo IP del telefono
- **User Telefono/TVox**: username di accesso all’interfaccia web del telefono ([1]_), se non impostato lasciarlo vuoto
- **Password Telefono/TVox**: password di accesso all’interfaccia web del telefono ([1]_), se non impostato lasciarlo vuoto
- **IP PC TConsole (SIP only)**: indirizzo IP del PC

.. important ::
    Si ricorda che, per questa configurazione, **PC e telefono devono avere IP statico e devono poter comunicare:**

    - sulla porta 80 (HTTP) del telefono
    - sulla porta 5452 TCP del PC TConsole (valore di default, vedi parametro SIP_PO_PORT)

    (vedi :ref:`Requisiti SIP SNOM`): una modifica effettuata successivamente dei parametri IP, senza l’opportuno aggiornamento del file *Tconsole.ini*, determina tipicamente uno (o più) di questi comportamenti:

    - da TConsole si riesce a fare partire una chiamata, ma poi non si riesce a controllarla (occorre utilizzare il telefono) e non viene visualizzata nel loop (Linea 0, Linea 1, ...)
    - una chiamata in ingresso arriva sul telefono, ma su TConsole non compare nulla
    - all’avvio di TConsole viene visualizzato il messaggio *Problemi durante l’apertura di <DN>. Funzionalità telefoniche non disponibili*, con relativo pallino rosso nella Status Bar in basso

Parametri configurabili in TConsole.ini
=======================================

- impostare il parametro **TYPE**\ =\ *SIP_SNOM*
- impostare il parametro **IADN** con il DN del dispositivo da pilotare
- impostare il parametro **DEVICE**\ =\ *-* (trattino obbligatorio)
- impostare il parametro **LINENUM**\ =\ *6* oppure *12* (linee disponibili sul telefono)
- inserire nel parametro **QUEUE** l’interno per la “deviazione a notte” (opzionale), se non utilizzato lasciarlo vuoto
- impostare il parametro **HOST** con l’indirizzo IP del telefono
- impostare il parametro **PORT**\ =\ *80* (valore di default): porta HTTP di comunicazione sul telefono
- impostare il parametro **SIP_PO_HOST** con l’indirizzo IP del PC
- impostare il parametro **SIP_PO_PORT**\ =\ *5452* (valore di default): porta TCP di comunicazione sul PC TConsole
- impostare il parametro **SIP_PO_SLEEP**\ =\ *250* (valore di default)
- impostare il parametro **SIP_PO_USR** con lo username di accesso all’interfaccia web del telefono ([1]_), se non impostato lasciare vuoto
- impostare il parametro **SIP_PO_PWD** con la password di accesso all’interfaccia web del telefono ([1]_), se non impostato lasciare vuoto
- Impostare il parametro **SIP_ENABLE_SIMULATED_BUSY**\ =\ *SI* per attivare la segnalazione di BUSY simulato (eventualmente impostarlo a *NO* nel caso il TConsole non dovesse riconoscere alcuni eventi di disconnessione/rilascio da parte del telefono)
- verificare la presenza del parametro **redirect_allways**\ =\ *"off"*, necessario per poter mettere a Notte/Giorno il TConsole (per TConsole release ≥ 5.2 o 4.5)

Nel file *\[INSTALLDIR\]\\config\\tabparam* ([2]_) configurare il parametro **TQM_TYPE**\ =\ *-*

Esempio TConsole.ini SIP SNOM
-----------------------------

.. code-block:: ini

    TYPE=SIP_SNOM
    IADN=2337
    DEVICE=-
    HOST=192.168.0.222
    PORT=80
    SIP_PO_HOST=192.168.0.12
    SIP_PO_PORT=5452
    SIP_PO_SLEEP=250
    SIP_PO_USR=
    SIP_PO_PWD=

Esempio tabparam SIP SNOM
-------------------------

.. code-block:: ini
        
        *              TQM_TYPE             -

.. TODO: descrivere le porte da aprire lato FW sul PC TConsole: 5450, parametro SIP_PO_PORT) ed eventualmente descrivere come modificare se necessario il parametro PORT=80 nel menu dello SNOM (https://service.snom.com/display/wiki/http_port)

.. rubric:: Note

.. [1] username e password di accesso all'interfaccia web del telefono si impostano nella scheda **Advanced | QoS/Security** nella sezione *HTTP Server*: in questo caso verificare che il parametro **Authentication Scheme** sia settato a: *Basic* (vedi :ref:`Requisiti SIP SNOM`).

.. [2] valore di default di *\[INSTALLDIR\]*: |tconsole_default_installdir|