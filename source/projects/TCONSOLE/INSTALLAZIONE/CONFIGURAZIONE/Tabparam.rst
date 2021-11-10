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

    *              TQM_TYPE             -

ABILITA_POPUP
-------------

Se configurato a *SI*, attiva il lookup in rubrica del numero chiamante: all'arrivo della chiamata viene presentato, al posto del numero chiamante, il nominativo del contatto, se presente in rubrica. Analogamente, il nominativo viene sintetizzato dalla Sintesi Vocale e/o riprodotto dalla Barra Braille, se la rispettiva funzionalità è attivata a livello di :ref:`Profilo Utente`. Il valore di default è *NO*.

ATTIVA_SKIN
-----------

**Solo nella vista Normale**, se configurato a *SI* (valore di default), imposta l'interfaccia in una tonalità di grigio come nella seguente immagine:

.. image:: /images/TCONSOLE/INSTALLAZIONE/CONFIGURAZIONE/ATTIVA_SKIN_SI.png

.. important :: Questa configurazione va a sovrascrivere le personalizzazioni dei colori eventualmente effettuate in alcune sezioni dall'interfaccia (ad es. per i :ref:`Tasti FLEX`) o tramite modifica dei files di configurazione.

La seguente immagine illustra la stessa interfaccia TConsole precedente ma con il parametro *ATTIVA_SKIN=NO*:

.. image:: /images/TCONSOLE/INSTALLAZIONE/CONFIGURAZIONE/ATTIVA_SKIN_NO.png

ACOD_RUB_EXT
------------

Vedi :ref:`Codice Impegno Linea`. Il valore di default è *0*.

PICKUP_SOUND_1
--------------

TQM_TYPE
--------

.. vedi :ref:`Parametri TVox` e :ref:`Parametri TAPI`.