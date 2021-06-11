=========================================
RubInt.ini e RubEst.ini Sezione [BRAILLE]
=========================================

In questa sezione vengono elencati tutti i parametri relativi alle informazioni inviate alla Barra Braille per un’installazione non vedente con barra.

È possibile specificare, compatibilmente con il numero di caratteri a disposizione sulla Barra Braille, quali campi e in quale ordine visualizzare sulla barra **al momento dello scorrimento dei risultati** della ricerca in rubrica.

È anche possibile specificare, tramite l'opzione *NoLabel*, se visualizzare o meno sulla barra l'etichetta di tali campi (configurata nella :ref:`Rubint.ini RubEst.ini Sezione LABELS`).
L’opzione *NoLabel* assume significato **solo per l’elenco dei nominativi restituiti dalla ricerca**: non si riferisce quindi ai campi di ricerca e di dettaglio del nominativo, che quando vengono scorsi con le freccette sono letti comprensivi di etichetta e nell'ordine configurato nelle rispettive sezioni.

.. code-block:: ini

    ;Idx=NomeCampo[,NoLabel]
    ;Dove NoLabel va messo a 1 se NON si vuole visualizzare la label per quel campo sul risultato di prima battua a braille,
    ;non mettere la nolabel corrisponde a mettere 0 che significa che si vuole visualizzare la label di quel campo.
    1=RAG_SOC
    2=TEL_EST,0
    3=UFF,1
    4=CAT,1

Nell'esempio riportato, nella riga 3 la dicitura:

.. code-block:: ini

    3=UFF,1

indica rispettivamente:

- numero ordinale (*Idx*) con cui visualizzare su barra questo campo: *3* (terzo campo da visualizzare, preceduto da *RAG_SOC* e da *TEL_EST*)
- campo (*NomeCampo*) del database di rubrica Esterna: *UFF* (visualizzato con l'etichetta descritta nella :ref:`Rubint.ini RubEst.ini Sezione LABELS`)
- ignorare (*NoLabel*) la visualizzazione su barra dell'etichetta: *1* (**non** visualizzare l'etichetta)

Sempre relativamente allo stesso esempio:

- il primo campo visualizzato sulla barra è *RAG_SOC*, del quale viene letta **anche** l'etichetta (*NoLabel* non valorizzato)
- il secondo campo visualizzato sulla barra è *TEL_EST*, del quale viene letta **anche** l'etichetta (*NoLabel*\ =\ *0*)
- il terzo campo visualizzato sulla barra è *UFF*, del quale viene letto solo il contenuto ma **non** l'etichetta (*NoLabel*\ =\ *1*)
- il quarto campo visualizzato sulla barra è *CAT*, del quale viene letto solo il contenuto ma **non** l'etichetta (*NoLabel*\ =\ *1*)