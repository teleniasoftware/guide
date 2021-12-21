.. _Tabparam:

========
Tabparam
========

Il file *tabparam* (si tratta di un file di testo senza estensione) contiene ulteriori parametri di configurazione, tra i quali i più significativi sono di seguito descritti.

.. **ABILITA_POPUP**, **ATTIVA_SKIN**, **ACOD_RUB_EXT**, **PICKUP_SOUND_1**, **TQM_TYPE**.

.. code-block:: ini

    *              ABILITA_POPUP        SI
    *              ATTIVA_SKIN          SI
    rubrica        ACOD_RUB_EXT         0

    [...]

    *              PICKUP_SOUND_1       Ring.wav

    [...]

    *              TCONSOLE_SERVER      127.0.0.1

    [...]

    *              TQM_TYPE             -

ABILITA_POPUP
-------------

Se configurato a *SI*, attiva il lookup in rubrica del numero chiamante: all'arrivo della chiamata viene presentato, al posto del numero chiamante, il nominativo del contatto, se presente in rubrica. Analogamente, il nominativo viene sintetizzato dalla Sintesi Vocale e/o riprodotto dalla Barra Braille, se la rispettiva funzionalità è attivata a livello di :ref:`Profilo Utente`. Il valore di default è *NO*.

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

PICKUP_SOUND_1
--------------

TCONSOLE_SERVER
---------------

Il valore di default è *-* (trattino). Se è presente il TConsoleServer, deve essere valorizzato con l'IP della macchina su cui il TConsoleServer è installato: se si tratta dello stesso PC su cui è installato TConsole allora inserire il valore *127.0.0.1* (in questo caso NON inserire *localhost*).

Per ulteriori dettagli fare riferimento alla Guida di Installazione del TConsoleServer

TQM_TYPE
--------

Il valore di default è *-* (trattino). Deve essere valorizzato diversamente **solo nelle seguenti modalità**:

- TAPI CISCO con TQM (vedi :ref:`TConsole.ini CISCO TQM`)
- TVOX (vedi :ref:`Parametri TVox`)

**In tutti gli altri casi il parametro va lasciato valorizzato a** *-* (trattino).