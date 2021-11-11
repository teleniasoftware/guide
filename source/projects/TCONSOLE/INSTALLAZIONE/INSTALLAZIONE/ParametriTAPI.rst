.. _Parametri TAPI:

===============================================================
Parametri TAPI / TSAPI (Avaya, Cisco, Nortel, Innovaphone etc.)
===============================================================

Parametri richiesti in fase di installazione (sezioni "TAPI")
=============================================================

- **PO DN**: impostare il parametro con il DN del dispositivo telefonico da pilotare (informazione riportata nella voce *ADDRESS* del *TestTapiDevice*) (vedi :ref:`Utilizzo TestTapiDevice`)
- **Device Tapi o COM (per Nortel)**: impostare il parametro con l’informazione riportata nella voce *DEVICE* del *TestTapiDevice*
- **DN deviazione a Notte**: (opzionale) inserire l’interno per la “deviazione a notte”, o lasciare il parametro vuoto

.. warning :: Il valore inserito nei parametri **PO DN** e **Device Tapi o COM (per Nortel)** deve corrispondere **esattamente** (inclusi gli spazi ed i caratteri non alfanumerici) a quanto visualizzato nel *TestTapiDevice*, altrimenti il TConsole potrebbe non riconoscere il dispositivo.
.. .. important :: **Solo per AVAYA CM con AES** (*TYPE=AVAYA_CSTA*) al termine dell'installazione vanno copiati i 4 files (librerie DLL) dalla cartella UPGRADE_CSTA, fornita nel pacchetto di installazione TConsole, alla cartella *\[INSTALLDIR\]\\bin\\* sovrascrivendo i files esistenti. Vanno inoltre impostati nel file *TConsole.ini* i 4 parametri relativi al CSTA link di Avaya (vedi parametro *AVAYA_CSTA_LINK* e successivi, descritti in :ref:`TConsole.ini AVAYA_CSTA`).
.. important :: **Solo per AVAYA CM con AES** (*TYPE=AVAYA_CSTA*) al termine dell'installazione e prima del riavvio del PC vanno eseguite le seguenti operazioni:

 .. - copiare i 4 files (librerie DLL) dalla cartella UPGRADE_CSTA, fornita nel pacchetto di installazione TConsole (ad es. *C:\\Telenia_Setup\\TConsole V5.7.27\\UPGRADE_CSTA\\*), alla cartella *\[INSTALLDIR\]\\bin\\* sovrascrivendo i files esistenti;
 - copiare in *\[INSTALLDIR\]\\bin\\* i 4 files (librerie DLL) presenti nella cartella UPGRADE_CSTA, fornita nel pacchetto di installazione TConsole (ad es. *C:\\Telenia_Setup\\TConsole V5.7.27\\UPGRADE_CSTA\\*), sovrascrivendo in *\[INSTALLDIR\]\\bin\\* i files già esistenti;
 - impostare nel file *TConsole.ini* i 4 parametri relativi al CSTA link di Avaya (vedi parametro *AVAYA_CSTA_LINK* e successivi, descritti in :ref:`TConsole.ini AVAYA_CSTA`).

Parametri configurabili in TConsole.ini
=======================================

- impostare il parametro **TYPE** nel modo corretto in relazione al PBX utilizzato:
- *SIEMENS_3000* se SIEMENS
- *CISCO* se PBX Cisco
- *AVAYA_CM* se PBX Avaya CM
- *AVAYA_CSTA* se PBX AVAYA CM con AES
- *AVAYA* se PBX Avaya IP Office
- *NORTEL_TAPI* (es. *TAPI CS1000* o altro dispositivo diverso da M2250, CIU e M1250)
- *BCM*
- *PANASONIC*
- *INNOVAPHONE*
- *NEC*
- impostare il parametro **IADN** con il DN del dispositivo telefonico da pilotare (informazione riportata nella voce *ADDRESS* del *TestTapiDevice*) (vedi :ref:`Utilizzo TestTapiDevice`)
- impostare il parametro **DEVICE** con l’informazione riportata nella voce *DEVICE* del *TestTapiDevice*
- inserire nel parametro **QUEUE** l’interno per la “deviazione a notte”, o lasciare il parametro vuoto

.. warning :: Il valore inserito nei parametri **IADN** e **DEVICE** deve corrispondere **esattamente** (inclusi gli spazi ed i caratteri non alfanumerici) a quanto visualizzato nel *TestTapiDevice*, altrimenti il TConsole potrebbe non riconoscere il dispositivo.

Esempio TConsole.ini SIEMENS
----------------------------

.. code-block:: ini

    TYPE=SIEMENS_3000
    IADN=610
    DEVICE="risorsa visualizzata dal TestTapiDevice e pilotabile via TAPI"
    TAPI_SLEEP_TRANSFER=400

Esempio TConsole.ini CISCO senza TQM
------------------------------------

.. code-block:: ini

    TYPE=CISCO
    IADN=3028
    DEVICE=Cisco Line: [SEP00221904C2A7] (3028)
    HOST=-

Nel file *\[INSTALLDIR\]\\config\\tabparam* ([1]_) configurare il parametro **TQM_TYPE**\ =\ *-*

Esempio tabparam CISCO senza TQM
--------------------------------

.. code-block:: ini

        *              TQM_TYPE             -

Per PBX Cisco è permesso l’utilizzo:

- del sistema di accodamento TQM
- Parcheggi

.. important :: Per queste opzioni fare riferimento al manuale di installazione dettagliato per TConsole in ambiente Cisco con TQM.

.. _TConsole.ini CISCO TQM:

Esempio TConsole.ini CISCO con TQM
----------------------------------

.. code-block:: ini

    [PO]
    TYPE=CISCO
    IADN=3602
    DEVICE=Cisco Line: [SEP00221904C2A7] (3602)

    [TQM]
    TQM_SERVICE=TQM_svc*pointernal
    TQM_USER=potqm01
    TQM_PASSWORD=potqm01
    TQM_HOST=192.168.0.234
    TQM_PORT=5450
    TQM_LICENSE_HOST=192.168.0.234
    TQM_LICENSE_PORT=5451
    TQM_DEVICE=3602
    TQM_PARK_DN=22293602
    TQM_CONF_DN=
    TQM_SKILLSET=ESTERNE,INTERNE,RITORNO,PARK

Nel file *\[INSTALLDIR\]\\config\\tabparam* ([1]_) configurare il parametro **TQM_TYPE**\ =\ *TAPI_TVOX_PICKUP*

Esempio tabparam CISCO con TQM
------------------------------

.. code-block:: ini

        *              TQM_TYPE             TAPI_TVOX_PICKUP

Esempio TConsole.ini TAPI AVAYA CM (Softphone)
----------------------------------------------

.. code-block:: ini

    TYPE=AVAYA_CM
    IADN=7503
    DEVICE=Avaya IP/Line
    HOST=-

    // Tale parametro si rende necessario solo nel caso di mancanza di informazioni provenienti dal carrier.
    // Se impostato a SI la chiamata in uscita viene riconosciuta come risposta anche se di fatto è ancora
    // in ring.
    // Se impostato a NO nel caso di alcune chiamate in uscita esterne potrebbe non essere riconosciuto
    // il connect e quindi non sarà possibile mettere in hold o trasferire.
    TAPI_AVAYA_OUTBOUND_CONNECTED_ON_RING=SI

Nel file *\[INSTALLDIR\]\\config\\tabparam* ([1]_) configurare il parametro **TQM_TYPE**\ =\ *-*

Esempio tabparam TAPI AVAYA CM (Softphone)
------------------------------------------

.. code-block:: ini

        *              TQM_TYPE             -

.. _TConsole.ini AVAYA_CSTA:

Esempio TConsole.ini TAPI AVAYA CM + AES (TSAPI)
------------------------------------------------

.. code-block:: ini

    TYPE=AVAYA_CSTA
    IADN=5009
    DEVICE=5009
    HOST=-
    AVAYA_CSTA_LINK=AVAYA#CM#CSTA#TELENIA1-AES1
    AVAYA_CSTA_LINK_VERSION=ECS2-6
    AVAYA_CSTA_LINK_USR=“Username CSTA” (es. Telenia)
    AVAYA_CSTA_LINK_PWD=“Password CSTA” (es. !Telenia01)

    TAPI_CALL_ON_BUSY_CODE=- (questo parametro è fondamentale settarlo ad un codice, es: *60 solo se realmente esistente su PBX, altrimenti è necessario lasciarlo a “-”: in caso contrario si genera l’anomalia di impossibilità di trasferire le chiamate)

Nel file *\[INSTALLDIR\]\\config\\tabparam* ([1]_) configurare il parametro **TQM_TYPE**\ =\ *-*

Esempio tabparam TAPI AVAYA CM + AES (TSAPI)
--------------------------------------------

.. code-block:: ini

        *              TQM_TYPE             -

.. important :: Per TConsole in ambiente Avaya fare riferimento al manuale di installazione dettagliato per installazione in ambiente Avaya.

.. rubric:: Note

.. [1] valore di default di *\[INSTALLDIR\]*: |tconsole_default_installdir|