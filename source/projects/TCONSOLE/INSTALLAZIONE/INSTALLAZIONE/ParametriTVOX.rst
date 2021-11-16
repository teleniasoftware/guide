.. _Parametri TVox:

==============
Parametri TVOX
==============

Parametri richiesti in fase di installazione (sezioni "TVOX")
=============================================================

- **PO DN**: impostare il parametro con il DN del dispositivo da pilotare
- **IP Telefono/TVox**: indirizzo IP del TVox
- **User Telefono/TVox**: username dell’utente TVox con profilo di tipo Operatore
- **Password Telefono/TVox**: password dell’utente TVox con profilo di tipo Operatore
- **PIN**: inserire il codice numerico (“PIN profilo per TConsole 5.0”) ([1]_) dell’utente TVOX con profilo di tipo Operatore
- **Codice Servizio**: inserire il Codice Servizio del servizio di tipo Posto Operatore ([2]_) su cui l'operatore è skillato
- **Codice Parcheggio**: inserire il codice di servizio "Prefisso per parcheggio pubblico/privato" ([3]_), seguito dal DN del dispositivo da pilotare

.. tip :: La configurazione di default al termine dell'installazione TConsole è la modalità **READY (senza PICKUP)**: in base alle esigenze dell'operatore è possibile modificare questo comportamento attivando la modalità **NOTREADY con PICKUP e parcheggi** (vedi `Modalità PICKUP`_).

.. warning :: Per utilizzare la funzionalità del parcheggio chiamata, il codice di servizio "Prefisso per parcheggio pubblico/privato" ([3]_) deve essere **abilitato** nel dialplan generale di |tvox_pbx|. Inoltre, nel caso che il codice venga successivamente modificato, andrà di conseguenza aggiornato il file *TConsole.ini* (parametro **TQM_PARK_DN**) con il nuovo valore. In caso contrario non sarà possibile da TConsole parcheggiare le chiamate o riprenderle dopo averle parcheggiate.

Parametri configurabili in TConsole.ini
=======================================

- impostare il parametro **TYPE**\ =\ *SNOM*
- impostare il parametro **IADN** con il DN del dispositivo da pilotare
- impostare il parametro **DEVICE** con il DN del dispositivo da pilotare
- impostare il parametro **HOST** con l’indirizzo IP del TVox
- impostare il parametro **PORT**\ =\ *5450* (valore di default)
- impostare il parametro **SIP_PO_HOST**\ =\ *-* (trattino obbligatorio)
- impostare il parametro **SIP_PO_PORT**\ =\ *-* (trattino obbligatorio)
- impostare il parametro **TQM_SERVICE** con il Codice Servizio([2]_) su cui l'operatore è skillato, seguito da *\*pointernal*
- impostare il parametro **TQM_USER** con lo username dell’utente TVox con profilo di tipo Operatore
- impostare il parametro **TQM_PASSWORD** con la password dell’utente TVox con profilo di tipo Operatore
- impostare il parametro **TQM_PIN** con il codice numerico (“PIN profilo per TConsole 5.0”) ([1]_) dell’utente TVOX con profilo di tipo Operatore
- impostare il parametro **TQM_HOST** con l’indirizzo IP del TVox
- impostare il parametro **TQM_PORT**\ =\ *5450* (valore di default)
- impostare il parametro **TQM_LICENSE_HOST** con l’indirizzo IP del TVox
- impostare il parametro **TQM_LICENSE_PORT**\ =\ *5451* (valore di default)
- impostare il parametro **TQM_DEVICE** con il DN del dispositivo da pilotare
- impostare il parametro **TQM_PARK_DN** con il codice di servizio "Prefisso per parcheggio pubblico/privato" ([3]_), seguito dal DN del dispositivo da pilotare
- impostare il parametro **TQM_CONF_DN**\ = (lasciare vuoto)
- impostare il parametro **TQM_SKILLSET**\ =\ *ESTERNE,INTERNE,RITORNO,PARK* (valore di default)

Nel file *\[INSTALLDIR\]\\config\\tabparam* ([4]_) configurare il parametro **TQM_TYPE**\ =\ *TVOX_R2*

.. important ::
    In questa modalità il pulsante “Notte/Giorno” (Sole Luna) è disabilitato: lo "stato a Giorno/Notte" della postazione, e la conseguente disponibilità/indisponibilità dell'operatore a gestire chiamate, avviene rispettivamente tramite le manovre di Login e di Logout, effettuabili in due modi:

    - da TConsole, con gli appositi tasti FLEX "Login" e "Logout"
    - automaticamente al momento dell'apertura e chiusura di TConsole il quale provvede, senza la necessità di ulteriori azioni, ad eseguire rispettivamente il Login e il Logout dell'operatore
    
    Per commutare invece il servizio in “stato a Notte/Giorno” è necessario definire un tasto FLEX (vedi :ref:`Tasti FLEX`) contenente il codice del servizio TVox “Imposta Servizio in stato Notte” seguito dal numero associato al servizio.

    Con il servizio in stato "Notte" le chiamate destinate al contesto "Attivo", cioè che in presenza di un calendario entrano nell'orario di apertura del servizio, oppure **tutte** le chiamate se **non** è presente alcun calendario, seguiranno invece il trattamento definito nel contesto “Fuori Servizio”, indipendentemente dallo stato di login/logout degli operatori.

Modalità PICKUP
===============

In base alla configurazione di TConsole scelta l’operatore può lavorare in una di queste modalità:

- in stato **READY (senza PICKUP)**: le chiamate in ingresso sul servizio vengono proposte direttamente all’operatore in base all’ordine di arrivo
- in stato **NOTREADY con PICKUP e parcheggi**: l’operatore vede le chiamate in coda sul servizio e sceglie a quale chiamata rispondere. Ha inoltre la possibilità di mettere in parcheggio una chiamata e di riprenderla

**TConsole TVOX con PICKUP e parcheggi**: per utilizzare la funzionalità di parcheggio (TQM_PARK) è necessario che su TConsole sia licenziata la modalità TQM e che nel file *\[INSTALLDIR\]\\config\\tabparam* ([4]_) sia configurato il parametro **TQM_TYPE**\ =\ *TVOX_R2_PICKUP*

Con questa configurazione il Posto Operatore lavorerà in modalità **PICKUP**: agendo in **NOTREADY** avrà a disposizione il display del TQM con le chiamate in coda e, muovendosi con le freccette, potrà scegliere quale chiamata gestire. Una volta posizionato sulla chiamata desiderata potrà rispondere tramite il tasto "Invio" della tastiera (non quello del tastierino numerico sulla destra).

Per mettere in park una chiamata, eseguire la combinazione di tasti CTRL+SHIFT+P. La chiamata verrà messa in parcheggio e comparirà sul display TQM con l’etichetta “P”. Per riprenderla, l’operatore dovrà posizionarsi sulla riga della chiamata con le freccette e premere il pulsante "Invio" come per le altre chiamate in coda.

Esempio TConsole.ini TVOX senza PICKUP (operatore in stato READY)
-----------------------------------------------------------------

.. code-block:: ini

    [PO]
    TYPE=SNOM
    IADN=2611
    DEVICE=2611
    HOST=192.168.0.59
    PORT=5450
    SIP_PO_HOST=-
    SIP_PO_PORT=-
    SIP_PO_SLEEP=250
    SIP_PO_USR=
    SIP_PO_PWD=

    [TQM]
    TQM_SERVICE=db_po_dev_service*pointernal
    TQM_USER=db_po
    TQM_PIN=1111
    TQM_HOST=192.168.0.59
    TQM_PORT=5450
    TQM_LICENSE_HOST=192.168.0.59
    TQM_LICENSE_PORT=5451
    TQM_DEVICE=2611
    TQM_PARK_DN=*3332611
    TQM_CONF_DN=
    TQM_SKILLSET=ESTERNE,INTERNE,RITORNO,PARK

Esempio tabparam TVOX senza PICKUP (operatore in stato READY)
-------------------------------------------------------------

.. code-block:: ini
        
        *              TQM_TYPE             TVOX_R2

----------------------------

Esempio TConsole.ini TVOX con PICKUP (operatore in stato NOTREADY) e parcheggio
-------------------------------------------------------------------------------

.. code-block:: ini

    [PO]
    TYPE=SNOM
    IADN=2611
    DEVICE=2611
    HOST=192.168.0.59
    PORT=5450
    SIP_PO_HOST=-
    SIP_PO_PORT=-
    SIP_PO_SLEEP=250
    SIP_PO_USR=
    SIP_PO_PWD=

    [TQM]
    TQM_SERVICE=db_po_dev_service*pointernal
    TQM_USER=db_po
    TQM_PIN=1111
    TQM_HOST=192.168.0.59
    TQM_PORT=5450
    TQM_LICENSE_HOST=192.168.0.59
    TQM_LICENSE_PORT=5451
    TQM_DEVICE=2611
    TQM_PARK_DN=*3332611
    TQM_CONF_DN=
    TQM_SKILLSET=ESTERNE,INTERNE,RITORNO,PARK

Esempio tabparam TVOX con PICKUP (operatore in stato NOTREADY) e parcheggio
---------------------------------------------------------------------------

.. code-block:: ini
        
        *              TQM_TYPE             TVOX_R2_PICKUP

.. rubric:: Note

.. [1] il “PIN profilo per TConsole 5.0” è definito nella scheda *Profili* alla voce *Identificativo profilo* dell’utente TVOX con profilo di tipo Operatore

.. [2] scheda *Configurazione*, voce *Impostazioni avanzate* dei *Parametri generali* del servizio di tipo Posto Operatore

.. [3] pagina *Impostazioni | Avanzate | Canale Telefonico | Codici di servizio* (valore di default: *\*333*). Il codice di servizio deve inoltre essere **abilitato** nel dialplan generale di |tvox_pbx|

.. [4] valore di default di *\[INSTALLDIR\]*: |tconsole_default_installdir|