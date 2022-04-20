.. _Vista Normale:

=============
Vista Normale
=============

È la vista standard di TConsole ed è sempre referenziabile.

Per la sua caratteristica è la vista che può contenere tutte le prestazioni dell’applicazione. Dopo il menu dell'applicazione vengono di seguito descritte le due parti principali che la compongono: la console e la Rubrica.

Menu
====

Sotto il titolo è presente il menu orizzontale dell’applicazione, per mezzo del quale è possibile accedere ad alcune funzioni supplementari ed alla configurazione del Posto Operatore.

.. note :: Alcune di queste opzioni possono essere temporaneamente o permanentemente disabilitate in base alla configurazione corrente dell’applicazione o delle prestazioni abilitate all'utenza TConsole che ha effettuato l'accesso.

Le voci del menu sono accessibili cliccandoci sopra con il mouse oppure premendo la lettera sottolineata in combinazione con il tasto *Alt* (es. *Alt+S*, *Alt+C*, *Alt+O*, *Alt+V*). Nel menu sono anche indicate le combinazioni di tasti con le quali è possibile attivare la funzionalità direttamente dalla tastiera del PC (particolarmente utili per operatori ipovedenti o non vedenti, ad es. *Ctrl+D*, *Ctrl+Alt+X*).

Strumenti
---------

.. image:: /images/TCONSOLE/UTENTE/CONSOLE/Strumenti.png

Il menu *Strumenti* è composto dalle seguenti voci:

- **Data e Ora** (*Ctrl+D*): se abilitata la Sintesi Vocale (vedi :ref:`Profilo Utente`), riproduce la data e ora corrente del PC. Utile ad operatori diversamente abili
- **Blocca Urbane** (*Ctrl+B*): **solo per console Nortel di tipo CIU/M2250** emula il tasto *TGB 0*, il quale deve essere programmato sul PBX per svolgere questa funzione
- **Inizia Reg.** (*Ctrl+I*): solo se abilitata l’opzione SmartRec, inizia la registrazione della conversazione in corso
- **Fine Reg.** (*Ctrl+F*): come per **Inizia Reg.** arresta la registrazione della conversazione in corso
- **Dump**: **solo per console Nortel di tipo CIU/M2250**, abilita/disabilita la scrittura di un file in formato binario contenente tutte le attività della console
- **Marca file di Log** (*Shift+Ctrl+Alt+M*): scrive una riga di *marklog* nel file log di TConsole (utile a fini di debug)
- **Uscita** (*Ctrl+Alt+X*): chiude l’applicazione TConsole

Chiamate
--------

.. image:: /images/TCONSOLE/UTENTE/CONSOLE/Chiamate.png

TConsole memorizza automaticamente il numero, lo stato del Display (con l'eventuale nome del chiamante/chiamato/linea), la data e l’ora di ogni chiamata effettuata o ricevuta. Mediante il menu *Chiamate* è possibile accedere a tali liste ed eseguire, eventualmente, la richiamata ad uno di questi numeri.

Il menu contiene le seguenti voci principali:

- **Richiama Ultima** (*Ctrl+R*): richiama il numero dell’ultima chiamata in uscita effettuata
- **Lista Chiamate Entranti** (*Ctrl+E*): visualizza la lista delle ultime 25 chiamate ricevute, con la possibilità di richiamare il numero di una di queste
- **Lista Chiamate Uscenti** (*Ctrl+U*): visualizza la lista delle ultime 25 chiamate effettuate, con la possibilità di richiamare il numero di una di queste

**Lista Chiamate Entranti/Uscenti**

Tali liste vengono visualizzate ognuna in una finestra del tipo seguente (in questo caso per le chiamate entranti: per le chiamate uscenti è presente una finestra analoga) con le logiche di seguito descritte:

.. image:: /images/TCONSOLE/UTENTE/CONSOLE/ListaChiamateEntranti.png

Nella terza colonna la lettera *I* sta per *Chiamata Interna*, mentre *E* sta per *Chiamata Esterna*. Se in rubrica è abilitato il lookup (vedi :ref:`ABILITA_POPUP`) e il numero chiamante è contenuto in rubrica, nel campo *Descrizione* viene presentato il nome del contatto di Rubrica Interna o Esterna.

In questa finestra è possibile eseguire le seguenti operazioni:

- scorrere la lista, selezionando la riga desiderata, mediante i tasti freccia della tastiera o muovendo la barra di scorrimento verticale con il mouse
- richiamare il numero relativo al record selezionato premendo il tasto *Invio* della tastiera (NON il tasto *Invio\[Tn\]* del tastierino numerico), oppure cliccando sul pulsante *Chiama* oppure facendo doppio click sul numero con il mouse
- azzerare la lista cliccando sul pulsante *Azzèra Lista*
- tornare alla finestra principale di TConsole tramite *Alt+F4* o cliccando sul pulsante *Annulla*

Configurazione
--------------

.. image:: /images/TCONSOLE/UTENTE/CONSOLE/Configurazione.png

.. TODO: Colori? in alternativa spostare in installazione

Il menu *Configurazione* è composto dalle seguenti voci:

.. - **Colori** (*Ctrl+C*): consente di personalizzare i colori di visualizzazione in modo da adattare l’applicazione ai propri gusti e abitudini
- **Colori** (*Ctrl+C*): nella scheda **Form** consente di personalizzare carattere e colori di visualizzazione della maschera principale del programma in modo da adattare l’applicazione ai propri gusti e abitudini. Per la modifica della combinazione di colori di determinate sezioni dell'applicazione o di determinati pulsanti fare riferimento a :ref:`Selezione Colori`
- **Telefono** (*Ctrl+T*): disponibile **solo per console Nortel di tipo CIU/M2250**, consente di regolare il volume ed il tono di squillo (buzzer) della console stessa
- **Rubrica Interna**: opzione non ancora attiva
- **Rubrica Esterna**: opzione non ancora attiva
- **Sintesi Vocale** (*Ctrl+Alt+V*): se abilitata la funzionalità di Sintesi Vocale, permette di modificare, fino al successivo riavvio del programma ([1]_), i parametri della voce: tipo voce, velocità testo, velocità numeri etc.
- **Sintesi On/Off** (*Ctrl+Alt+S*): se abilitata la funzionalità di Sintesi Vocale, permette di abilitarla o disabilitarla temporaneamente, fino alla pressione della medesima combinazione di tasti oppure fino al riavvio del programma; viene riprodotto lo stato della sintesi (abilitata/disabilitata)

.. _Selezione Colori:

Selezione Colori
----------------

.. image:: /images/TCONSOLE/UTENTE/CONSOLE/SelezioneColori.png

.. .. image:: /images/TCONSOLE/UTENTE/CONSOLE/SelezioneColori_old.png

La finestra *Selezione Colori* permette di impostare il carattere e i colori dei pulsanti e delle aree di testo della Rubrica e della Console facendo clic con il tasto destro del mouse sulla sezione o sul componente interessato.

I componenti sono raggruppati nel seguente modo:

..
  - pulsanti ICI
  - pulsanti FLEX
  - pulsanti Fix
  - pulsanti Keypad
  - pulsanti Linea (pannello Loop)
  - aree di testo descrizione Linee (pannello Loop)
  - aree di testo Display

- pulsanti :ref:`ICI`
- pulsanti :ref:`FLEX`
- pulsanti :ref:`FIX`
- pulsanti :ref:`Keypad`
- pulsanti :ref:`Loop`
- aree di testo (descrizione Linee) del :ref:`Loop`
- aree di testo (linea sorgente/destinazione, stato della console etc.) del :ref:`Display`
.. - pulsanti :ref:`TQM`

La modalità di selezione e di impostazione dei parametri è uguale per tutti:

- selezionare la zona di interesse
- impostare il colore di primo piano "**FG**" (*ForeGround*), cliccando sul colore preferito con il tasto **sinistro** del mouse
- impostare il colore di sfondo "**BG**" (*BackGround*), cliccando sul colore preferito con il tasto destro del mouse
- selezionare la dimensione del carattere e lo stile
- nella parte inferiore della finestra viene riprodotto un esempio delle impostazioni scelte sia per la vista Normale che per quella IPO
- salvare le scelte fatte cliccando sul pulsante "Conferma", oppure ignorarle cliccando su "Annulla"

**Le scelte confermate diventano immediatamente operative.**

.. important :: I pulsanti hanno due differenti stati: *Normale* e *Attivo*, per i quali è opportuno impostare combinazioni di colori diverse tra loro. Le aree di testo hanno solamente lo stato *Normale*.

.. warning :: Evitare di impostare per primo piano e sfondo la stessa tonalità di colore, pena l'illeggibilità del pulsante o dell'area di testo. Questo può accadere ad es. quando si clicca con il tasto destro e il sinistro del mouse sullo stesso colore: in questo caso compare "**FB**" sulla stessa casella di selezione colore.

Telefono (solo per Nortel CIU o Nortel M2250)
---------------------------------------------

.. image:: /images/TCONSOLE/UTENTE/CONSOLE/ConfigurazioneTelefonoNortelCIU.png

Per modificare volume e tono del segnale acustico emesso dalla console CIU/M2250 cliccare sulle freccette per impostare il valore desiderato.

**Solo per la console CIU** è possibile attivare/disattivare, tramite l'opportuno flag "Audio", l’audio del segnale acustico della console. Per console M2250 la finestra è identica ma il flag non è presente.

Vista
-----

.. image:: /images/TCONSOLE/UTENTE/CONSOLE/Vista.png

L’opzione *Vista* consente di commutare dalla vista Normale (*Ctrl+Alt+N*) alle altre viste disponibili, se abilitate a livello di :ref:`Profilo Utente`. Ad esempio, nella precedente immagine è abilitata anche la vista IPO (*Ctrl+Alt+I*), mentre non sono abilitate le viste IPO PLUS (*Ctrl+Alt+Z*) e la vista Batteria (*Ctrl+Alt+B*).

.. note :: Nonostante questo menu sia visivamente disponibile solo nella vista Normale, le configurazioni di tasti indicate sono utilizzabili anche dopo aver commutato ad una vista qualsiasi: ad esempio, trovandosi nella vista IPO PLUS, si potrà commutare direttamente alla vista Normale tramite *Ctrl+Alt+N* oppure alla vista IPO tramite *Ctrl+Alt+I*.

Tqm
-----

.. image:: /images/TCONSOLE/UTENTE/CONSOLE/Tqm.png

? (Informazioni)
----------------

.. image:: /images/TCONSOLE/UTENTE/CONSOLE/Informazioni.png

Come mostrato in figura, questa opzione visualizza informazioni relative all’applicazione; in particolare sono significativi i numeri di versione.

.. image:: /images/TCONSOLE/UTENTE/CONSOLE/info.png

Pannelli della Console
======================

Questa è la parte di controllo della console o telefono che l’applicazione gestisce direttamente ed è provvista dei seguenti pannelli (da sinistra a destra):

- :ref:`Util`
- :ref:`ICI`
- :ref:`Display`
- :ref:`Loop`
- :ref:`FIX`
- :ref:`Keypad`
- :ref:`Comandi`
- :ref:`FLEX`
.. - :ref:`TQM`

.. _Util:

Util: comandi di utilità
------------------------

.. _ICI:

ICI: identificazione chiamate entranti
--------------------------------------

.. _Display:

Display
-------

.. _Loop:

Loop: pulsanti di impegno linea
-------------------------------

.. _FIX:

FIX: comandi di base
--------------------

.. _Keypad:

Keypad: tastiera telefonica
---------------------------

.. _Comandi:

Comandi
-------

.. _FLEX:

FLEX: comandi definiti dall’utente
----------------------------------

..
    .. _TQM:

    TQM: comandi per la gestione TQM
    ----------------------------------

Rubrica F3
==========

Ricerca nominativi
------------------

Composizione automatica
-----------------------

Inserimento nominativi
----------------------

Modifica e cancellazione nominativi
-----------------------------------

.. xxx

.. .. image:: /images/TCONSOLE/UTENTE/CONSOLE/info.png

.. rubric:: Note

.. .. [1] Le modifiche applicate ai parametri della Sintesi Vocale rimangono effettive fino al successivo riavvio di TConsole, quando vengono ripristinati i parametri precedenti alle modifiche applicate tramite l'interfaccia dell'applicazione. Per rendere effettive queste modifiche i valori desiderati vanno impostati nel :ref:`Profilo Utente`, riquadro Permessi, funzionalità Sintesi Vocale
.. [1] al riavvio di TConsole vengono ripristinati i parametri della Sintesi Vocale precedenti alle modifiche applicate tramite interfaccia dell'applicazione. Per rendere effettive queste modifiche i valori desiderati vanno impostati nel :ref:`Profilo Utente`, riquadro *Permessi*, funzionalità **Sintesi Vocale**