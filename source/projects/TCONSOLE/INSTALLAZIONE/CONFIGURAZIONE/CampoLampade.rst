.. _Campo Lampade:

=============
Campo Lampade
=============

Per gestire il campo lampade è necessario disporre della licenza per il **Campo Lampade** e configurare nel :ref:`Profilo Utente` il valore *CAMPO LAMPADE = SI* e il flag sul ruolo **BLF**.

Per tutte le tipologie di centrale, ad eccezione di Nortel che verrà descritta successivamente, il Campo Lampade viene gestito con l’ausilio del TConsoleServer per cui occorre inserire, in *\[INSTALLDIR\]\\config\\tabparam* ([2]_) nel parametro *TCONSOLESERVER*, l’IP della macchina su cui è installato il TConsoleServer (vedi :ref:`Tabparam`).

.. image:: /images/TCONSOLE/INSTALLAZIONE/CONFIGURAZIONE/ATTIVA_SKIN_SI.png

In riferimento all'immagine riportata:

- gli interni 4200 (Alfonso), 4223 (Bellani), 4207 (Bonetti) sono liberi (pallino verde)
- gli interni 4213 (Boccolieri) e 4203 (Briani) sono occupati (pallino rosso)
- l'interno 919191 (alg) non è tra gli interni monitorati (pallino grigio)

.. important ::
    L'indicatore visivo dello stato Libero/Occupato (pallino verde/rosso) è disponibile **solo** nella sezione MASTER della vista Normale (vedi :ref:`Rubint.ini RubEst.ini Sezioni MASTER, DETAIL e DETAIL_IPO`).
    
    Nelle viste IPO e IPO PLUS, così come nella vista Normale, l'informazione sullo stato Libero/Occupato è disponibile nei **dettagli** del contatto (sezione DETAIL) rispettivamente tramite la dicitura *(L)* oppure *(O)* che viene **posposta** automaticamente al nominativo di rubrica consultato (vedi il dettaglio *Descrizione: Alfonso (L)* nell'immagine precedente).

    Tale informazione viene resa disponibile anche tramite Sintesi Vocale (in questo caso lo stato Libero/Occupato viene **anteposto** al nominativo di rubrica consultato, ad es. *"Libero Alfonso"* oppure *"Occupato Alfonso"*, vedi :ref:`Rubint.ini RubEst.ini Sezione SYNTH`) o tramite Barra Braille (vedi :ref:`Rubint.ini RubEst.ini Sezione BRAILLE`).

.. TODO: BLF SfB e pallino giallo -> stato Assente?

**Solo per le centrali Nortel** il TConsoleServer NON viene utilizzato per la gestione del Campo Lampade per cui occorre assicurarsi che il parametro contenuto in *\[TCS_INSTALLDIR\]\\config\\tabparam.ini* ([1]_) sia disabilitato:

.. code-block:: ini

    [BLF]
    Active=NO

e che il file *\[TCS_INSTALLDIR\]\\config\\devices* ([1]_) sia vuoto.

.. Per le altre tipologie di centrale il Campo Lampade viene gestito con l’ausilio del TConsoleServer per cui occorre inserire, in *\[INSTALLDIR\]\\config\\tabparam* ([2]_) nel parametro *TCONSOLESERVER*, l’IP della macchina su cui è installato il TConsoleServer (vedi :ref:`Tabparam`).

Per i dettagli della configurazione fare riferimento al manuale di installazione del :ref:`TConsoleServer`.

.. rubric:: Note

.. [1] valore di default di *\[TCS_INSTALLDIR\]* per macchine a 64 bit: |tconsoleserver_default_installdir|

.. [2] valore di default di *\[INSTALLDIR\]*: |tconsole_default_installdir|