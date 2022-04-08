.. _Tabparam:

========
Tabparam
========

Il file *tabparam* (si tratta di un file di testo senza estensione) contiene ulteriori parametri di configurazione, tra i quali i più significativi sono di seguito descritti.

.. code-block:: ini

    *              ABILITA_POPUP        SI
    *              ATTIVA_SKIN          SI
    rubrica        ACOD_RUB_EXT         0

    [...]

    *              PICKUP_SOUND_1       Ring.wav
    *              PICKUP_SOUND_2       -
    *              PICKUP_SOUND_2_NUM   -1
    *              PICKUP_SOUND_3       -
    *              PICKUP_SOUND_3_NUM   -1

    [...]

    *              TCONSOLE_SERVER      127.0.0.1

    [...]

    *              TQM_TYPE             -
    
    [...]

ABILITA_POPUP
-------------

Se configurato a *SI*, attiva il lookup in rubrica del numero chiamante: all'arrivo della chiamata viene presentato, al posto del numero chiamante, il nominativo del contatto, se presente in rubrica. Analogamente, il nominativo viene sintetizzato dalla Sintesi Vocale e/o riprodotto dalla Barra Braille, se la rispettiva funzionalità è attivata a livello di :ref:`Profilo Utente`. Il valore di default è *NO*.

.. warning :: Il lookup in rubrica, se abilitato, avviene **solo** per le chiamate entranti. NON viene effettuato per le chiamate uscenti (ad es. digitando col tastierino numerico il numero da chiamare).

ATTIVA_SKIN
-----------

**Solo nella vista Normale**, se configurato a *SI* (valore di default), imposta i colori dell'interfaccia con tonalità prevalentemente di grigi, come nella seguente immagine:

.. image:: /images/TCONSOLE/INSTALLAZIONE/CONFIGURAZIONE/ATTIVA_SKIN_SI.png

.. important :: Questa configurazione va a sovrascrivere le personalizzazioni dei colori eventualmente effettuate in alcune sezioni dell'interfaccia (ad es. per i :ref:`Tasti FLEX`) o tramite modifica dei files di configurazione.

.. warning :: Nelle viste IPO e IPO PLUS questo parametro viene ignorato e la sua modifica non ha alcun effetto.

La seguente immagine illustra la stessa interfaccia TConsole precedente ma con il parametro *ATTIVA_SKIN=NO* e la combinazione di colori predefinita al termine dell'installazione:

.. image:: /images/TCONSOLE/INSTALLAZIONE/CONFIGURAZIONE/ATTIVA_SKIN_NO.png

.. _ACOD_RUB_EXT:

ACOD_RUB_EXT
------------

Definisce il codice di impegno linea da anteporre, in deteriminati contesti (vedi :ref:`Codice Impegno Linea`), al numero da chiamare. Il valore di default è *0*.

PICKUP_SOUND_1, PICKUP_SOUND_2, PICKUP_SOUND_3
----------------------------------------------

Questi parametri, congiuntamente a *PICKUP_SOUND_2_NUM* e *PICKUP_SOUND_3_NUM*, permettono di personalizzare la notifica sonora (emessa da TConsole tramite l'audio del PC) che indica la presenza di chiamate in coda, e sono utilizzati **solo nelle seguenti modalità**:

- TAPI CISCO con TQM (vedi :ref:`TConsole.ini CISCO TQM`)
- TVOX (vedi :ref:`Parametri TVox`)

.. code-block:: ini

    [...]

    *              PICKUP_SOUND_1       Ring.wav
    *              PICKUP_SOUND_2       start.wav
    *              PICKUP_SOUND_2_NUM   3
    *              PICKUP_SOUND_3       notify.wav
    *              PICKUP_SOUND_3_NUM   7
    
    [...]

In riferimento all'esempio riportato:

- con 1 o 2 chiamate in coda (numero inferiore a *PICKUP_SOUND_2_NUM=3*) verrà eseguito il file *PICKUP_SOUND_1=Ring.wav*
- con 3, 4, 5 o 6 chiamate in coda (raggiungimento di *PICKUP_SOUND_2_NUM=3* ma numero inferiore a *PICKUP_SOUND_3_NUM=7*) verrà eseguito il file *PICKUP_SOUND_2=start.wav*
- con 7 o più chiamate in coda (raggiungimento di *PICKUP_SOUND_3_NUM=7*) verrà eseguito il file *PICKUP_SOUND_3=notify.wav*

I files audio indicati **devono trovarsi** in *\[INSTALLDIR\]\\sounds\\* ([1]_): al termine dell'installazione standard di TConsole alcuni files audio sono già presenti in questo percorso ma, se necessario, è possibile aggiungerne altri nello stesso formato.

Sempre al termine dell'installazione standard i valori di default per le notifiche sonore sono i seguenti:

.. code-block:: ini

    [...]

    *              PICKUP_SOUND_1       Ring.wav
    *              PICKUP_SOUND_2       -
    *              PICKUP_SOUND_2_NUM   -1
    *              PICKUP_SOUND_3       -
    *              PICKUP_SOUND_3_NUM   -1

    [...]

..
    - *PICKUP_SOUND_1=Ring.wav*
    - *PICKUP_SOUND_2=-* (trattino)
    - *PICKUP_SOUND_2_NUM=-1*
    - *PICKUP_SOUND_3=-* (trattino)
    - *PICKUP_SOUND_3_NUM=-1*

Con il risultato che per qualsiasi numero di chiamate in coda verrà eseguito sempre e solo il file *PICKUP_SOUND_1=Ring.wav*.

.. warning :: Se per *PICKUP_SOUND_1*, *PICKUP_SOUND_2* o *PICKUP_SOUND_3* viene specificato un parametro o un nome file non valido (o inesistente) allora verrà utilizzato il suono di notifica predefinito di Windows.

.. tip :: Per NON emettere alcuna notifica sonora per le chiamate in coda è possibile impostare come *PICKUP_SOUND_1* un file audio contenente silenzio, lasciando i valori di default per gli altri parametri.

TCONSOLE_SERVER
---------------

Vedi anche :ref:`Campo Lampade`.

Il valore di default è *-* (trattino). Se è presente il TConsoleServer, il parametro deve essere valorizzato con l'IP della macchina su cui il TConsoleServer è installato: se si tratta dello stesso PC su cui è installato TConsole allora inserire il valore *127.0.0.1* (in questo caso NON inserire *localhost*).

Per i dettagli della configurazione fare riferimento al manuale di installazione del :ref:`TConsoleServer`.

TQM_TYPE
--------

Il valore di default è *-* (trattino). Deve essere valorizzato diversamente **solo nelle seguenti modalità**:

- TAPI CISCO con TQM (vedi :ref:`TConsole.ini CISCO TQM`)
- TVOX (vedi :ref:`Parametri TVox`)

**In tutti gli altri casi il parametro va lasciato valorizzato a** *-* (trattino).

.. rubric:: Note

.. [1] valore di default di *\[INSTALLDIR\]*: |tconsole_default_installdir|