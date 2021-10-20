=======================
RubInt.ini e RubEst.ini
=======================

I files *Rubint.ini* e *RubEst.ini* contengono rispettivamente le configurazioni relative alla rubrica Interna (*RubInt.ini*) e alla rubrica Esterna (*RubEst.ini*).

**La loro struttura e i parametri in essi contenuti sono del tutto analoghi**, pertanto le seguenti configurazioni sono applicabili sia a *Rubint.ini* che a *RubEst.ini*.

Sezione COMMON
==============

..
    F12
    ---

    .. code-block:: ini

        ;	Invio: F12, Shift+F12, Ctrl+F12, Alt+F12
        F12=TEL_EST,LIBERO_1,LIBERO_2,LIBERO_3

RIC_ALT
-------
Questo parametro è utilizzato per la ricerca alternativa all’interno della rubrica Interna/Esterna e va settato con il nome del campo (campo database, non label) su cui verrà effettuata la ricerca alternativa.

**Se lasciato vuoto**, la ricerca alternativa verrà effettuata nel campo del dettaglio contatto che si trova selezionato al momento della pressione del tasto funzione associato (default F11).

Es. per eseguire la ricerca alternativa **sempre** nel campo *SETTORE*:

.. code-block:: ini

    RIC_ALT=SETTORE

Es. per eseguire la ricerca alternativa nel campo dettaglio che è stato **di volta in volta** selezionato:

.. code-block:: ini

    RIC_ALT=

.. _Rubint.ini RubEst.ini Sezione LABELS:

Sezione LABELS
==============

Questa sezione contiene:

- l'associazione tra il nome campo del database di rubrica e l'etichetta presentata su TConsole
- eventuali vincoli sul tipo di dato (numero o stringa) che il campo può contenere
- eventuali vincoli sul valore che può essere inserito nel campo

.. important ::
    I vincoli sul tipo di dato e sul valore che esso può contenere sono verificati al momento della modifica o inserimento di un contatto effettuati **tramite interfaccia di TConsole**. Se si prova a inserire un dato che non rispetta tali vincoli, al momento del salvataggio del contatto verrà restituito un messaggio di errore con la descrizione del vincolo non rispettato.

    Se la rubrica viene importata direttamente nel database TConsole (tramite file CSV, SQL, ...) gli unici vincoli che vengono controllati al momento dell'importazione sono i vincoli di struttura della tabella del database.

.. warning :: Se in questa sezione viene eliminata o commentata una delle righe di associazione campo - etichetta, su TConsole verrà presentato come etichetta il nome stesso del campo, e dalla rubrica TConsole **non** sarà possibile inserire né modificarne il contenuto.

**Esempio di RubEst.ini** (file di configurazione della rubrica **Esterna**)\ **:**

.. code-block:: ini

    ;	Etichette dei campi di tabella, Tipo di dato (NUM=numerico, STR=stringa)
    ;	NOME_CAMPO=Label[,Type][,Maschera]
    ;	Se per un campo non è specificata l'etichetta, viene assunta come etichetta il nome del campo. 
    ;	Se non è specificato il Type viene assunto il type STR=Stringa
    ;	Se non è specificata la maschera, nessuna maschera impostata Es. maschera 3**********|3*********|0*********
    CAT=Ufficio
    UFF=Ruolo
    RAG_SOC=Descrizione
    TEL_EST=Numero,NUM
    LIBERO_1=Cellulare,NUM,3**********|3*********
    LIBERO_2=Altern 1,NUM
    LIBERO_3=Altern 2,NUM
    LIBERO_4=Email
    ;	LIBERO_5=Azienda
    NOTES=Note

Nell'esempio riportato, la dicitura:

.. code-block:: ini

    LIBERO_1=Cellulare,NUM,3********|3*********

indica rispettivamente:

- campo (*NOME_CAMPO*) del database di rubrica Esterna: *LIBERO_1*
- etichetta (*Label*) visualizzata su TConsole: *Cellulare*
- vincolo sul tipo (*Type*) di dato accettato: *NUM* (numero)
- vincolo (Maschera) sul contenuto accettato: *3\*\*\*\*\*\*\*\*|3\*\*\*\*\*\*\*\*\** (solo numeri di 9 o 10 cifre che iniziano con 3)

Sempre relativamente allo stesso esempio:

- il campo del database *LIBERO_2* verrà presentato con l'etichetta *Altern 1*, dovrà essere un numero (*Type NUM*) e potrà contenere una qualsiasi quantità di cifre (*Maschera* non presente)
- il campo del database *LIBERO_4* verrà presentato con l'etichetta *Email* e potrà contenere una stringa alfanumerica qualsiasi (*Type* e *Maschera* non presenti)
- il campo del database *LIBERO_5*, in quanto commentato, verrà presentato con il nome stesso del campo *LIBERO_5* come etichetta (quindi NON con l'etichetta *Azienda*) e il suo contenuto non sarà modificabile da TConsole
- gli altri campi del database che in questa sezione non vengono definiti verranno presentati con il nome stesso del campo come etichetta, e il loro contenuto non sarà modificabile da TConsole

.. _Rubint.ini RubEst.ini Sezioni MASTER, DETAIL e DETAIL_IPO:

Sezioni MASTER, DETAIL e DETAIL_IPO
===================================

In questa sezione è possibile specificare, eventualmente differenziando in base al tipo di vista utilizzata (Normale o IPO/IPO PLUS), quali informazioni (dettagli) di un contatto, e in quale ordine, visualizzare al momento della consultazione di un contatto in rubrica. È anche possibile specificare un'etichetta personalizzata da visualizzare solo in una determinata sezione o in una determinata vista.

.. important ::
    La sezione MASTER è disponibile **solo nella vista Normale** e consente di scorrere verticalmente i risultati della ricerca, con i dettagli contatto consultabili orizzontalmente riga per riga.

    Le sezioni DETAIL e DETAIL_IPO si riferiscono ai dettagli contatto rispettivamente nella vista Normale e nelle viste IPO/IPO PLUS.

Per NON visualizzare un campo del database in una determinata sezione è sufficiente eliminare o commentare la riga corrispondente assicurandosi che, ove richiesto, i campi presenti siano **univocamente numerati a partire da 1 e senza interruzioni nella numerazione**: se ad es. si vogliono visualizzare 6 campi, questi dovranno necessariamente essere numerati da 1 a 6.

.. warning :: Il campo n. 0 è riservato all'indicatore (pallino colorato) del :ref:`CampoLampade` nella sezione MASTER e **non può essere modificato**.

.. image:: /images/TCONSOLE/INSTALLAZIONE/CONFIGURAZIONE/DETAIL.png

**Esempio di RubEst.ini** (file di configurazione della rubrica **Esterna**) **:**

.. code-block:: ini

    [MASTER]
    ;	Elenco campi vis. master
    ; 	Idx=NomeCampo,Larghezza[,Etichetta]
    0=TEL_EST,34
    1=RAG_SOC,188
    2=TEL_EST,106
    3=UFF,197
    4=CAT,156,CAT_master
    5=LIBERO_1,144
    6=LIBERO_2,144
    7=LIBERO_3,148
    8=LIBERO_4,100
    9=NOTES,100

    [DETAIL]
    ; 	Elenco campi vis. dettaglio
    ; 	Idx=NomeCampo[,Etichetta]
    1=RAG_SOC
    2=TEL_EST
    3=UFF,UFF_detail
    4=CAT
    5=LIBERO_1
    6=LIBERO_2
    7=LIBERO_3
    8=LIBERO_4
    9=NOTES

    [DETAIL_IPO]
    ; 	Elenco campi vis. dettaglio
    ; 	Idx=NomeCampo[,Etichetta]
    1=RAG_SOC
    2=TEL_EST
    3=UFF
    4=CAT
    5=LIBERO_1,CELL
    6=LIBERO_2
    7=LIBERO_3
    8=LIBERO_4
    9=NOTES

Nell'esempio riportato, nella sezione [MASTER], nelle righe 0, 4 e 5 le diciture:

.. code-block:: ini

    0=TEL_EST,34

    [...]

    4=CAT,156,CAT_master
    5=LIBERO_1,144

indicano rispettivamente:

- numero ordinale (*Idx*) di posizionamento dell'indicatore per il Campo Lampade: *0* (prima colonna a sinistra) ed è largo 34 pixel
- numero ordinale (*Idx*) di posizionamento del campo del database *CAT*: *4* (quinto campo da sinistra considerando anche l'indicatore per il Campo Lampade), è largo 156 pixel e verrà presentato con l'etichetta alternativa *CAT_master* (vedi circoletto rosso nell'immagine precedente) anziché l'etichetta *Ufficio* definita nella sezione [LABELS]
- numero ordinale (*Idx*) di posizionamento del campo del database *LIBERO_1*: *5* (sesto campo da sinistra considerando anche l'indicatore per il Campo Lampade), è largo 144 pixel e verrà presentato con l'etichetta *Cellulare* definita nella sezione [LABELS]

..
    .. warning :: Per il Campo Lampade il valore *Idx* (posizione dell'indicatore) **deve** essere configurato pari a *0*.

.. hint :: Nella sezione [MASTER] è possibile modificare con il mouse la larghezza delle colonne.

Sempre relativamente allo stesso esempio, nella sezione [DETAIL] nelle righe 3 e 4 le diciture:

.. code-block:: ini
    
    3=UFF,UFF_detail
    4=CAT

indicano rispettivamente:

- numero ordinale (*Idx*) di posizionamento del campo del database *UFF*: *3* (terzo campo dall'alto a sinistra) e verrà presentato con l'etichetta alternativa *UFF_detail* (vedi circoletto verde nell'immagine precedente) anziché l'etichetta *Ruolo* definita nella sezione [LABELS]
- numero ordinale (*Idx*) di posizionamento del campo del database *CAT*: *4* (quarto campo da sinistra) e verrà presentato con l'etichetta *Ufficio* definita nella sezione [LABELS]

Nella sezione [DETAIL_IPO] nelle righe 4 e 5 le diciture:

.. code-block:: ini

    4=CAT
    5=LIBERO_1,CELL

indicano rispettivamente:

- numero ordinale (*Idx*) di posizionamento del campo del database *CAT*: *4* (quarto campo dall'alto) e verrà presentato con l'etichetta *Ufficio* definita nella sezione [LABELS]
- numero ordinale (*Idx*) di posizionamento del campo del database *LIBERO_1*: *5* (quinto campo dall'alto) e verrà presentato con l'etichetta alternativa *CELL* (vedi circoletto giallo nell'immagine seguente) anziché l'etichetta *Cellulare* definita nella sezione [LABELS]

.. image:: /images/TCONSOLE/INSTALLAZIONE/CONFIGURAZIONE/DETAIL_IPO.png

.. _Rubint.ini RubEst.ini Sezione SYNTH:

Sezione [SYNTH]
===============

In questa sezione è possibile specificare quali informazioni (dettagli) di un contatto, e in quale ordine, riprodurre con la Sintesi Vocale di TConsole a fronte di una ricerca in rubrica.

È anche possibile specificare, tramite l'opzione *NoLabel*, se riprodurre o meno l'etichetta di tali campi (configurata nella :ref:`Rubint.ini RubEst.ini Sezione LABELS`).
L’opzione *NoLabel* assume significato **solo per l’elenco dei nominativi restituiti dalla ricerca**: non si riferisce quindi ai campi di ricerca e di dettaglio del nominativo, che quando vengono scorsi con le freccette sono letti comprensivi di etichetta e nell'ordine configurato nelle rispettive sezioni.

.. code-block:: ini

    ; 	Elenco campi sintesi vocale
    ;	Idx=NomeCampo[,NoLabel]
    1=RAG_SOC,1
    2=TEL_EST,1
    3=CAT,0
    4=LIBERO_1

Nell'esempio riportato, nella riga 1 la dicitura:

.. code-block:: ini

    1=RAG_SOC,1
    
indica rispettivamente:

- numero ordinale (*Idx*) con cui riprodurre con la Sintesi Vocale questo campo: *1* (primo campo da riprodurre, seguito da *TEL_EST*, *CAT* e *LIBERO_1*)
- campo (*NomeCampo*) del database di rubrica Esterna: *RAG_SOC* (riprodotto con l'etichetta descritta nella :ref:`Rubint.ini RubEst.ini Sezione LABELS`)
- ignorare (*NoLabel*) la riproduzione dell'etichetta: *1* (**non** riprodurre l'etichetta)

Sempre relativamente allo stesso esempio:

.. - il primo campo riprodotto con Sintesi Vocale è *RAG_SOC*, del quale viene letto solo il contenuto ma non l'etichetta (*NoLabel*\ =\ *1*)
- il secondo campo riprodotto con Sintesi Vocale è *TEL_EST*, del quale viene letto solo il contenuto ma non l'etichetta (*NoLabel*\ =\ *1*)
- il terzo campo riprodotto con Sintesi Vocale è *CAT*, del quale viene letta anche l'etichetta (*NoLabel*\ =\ *0*)
- il quarto campo riprodotto con Sintesi Vocale è *LIBERO_1*, del quale viene letta anche l'etichetta (*NoLabel* non valorizzato)

.. _Rubint.ini RubEst.ini Sezione BRAILLE:

Sezione [BRAILLE]
=================

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

- il primo campo visualizzato sulla barra è *RAG_SOC*, del quale viene letta anche l'etichetta (*NoLabel* non valorizzato)
- il secondo campo visualizzato sulla barra è *TEL_EST*, del quale viene letta anche l'etichetta (*NoLabel*\ =\ *0*)
.. - il terzo campo visualizzato sulla barra è *UFF*, del quale viene letto solo il contenuto ma non l'etichetta (*NoLabel*\ =\ *1*)
- il quarto campo visualizzato sulla barra è *CAT*, del quale viene letto solo il contenuto ma non l'etichetta (*NoLabel*\ =\ *1*)