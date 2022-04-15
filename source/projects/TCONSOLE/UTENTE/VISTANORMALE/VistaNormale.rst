.. _Vista Normale:

=============
Vista Normale
=============

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
- **Blocca Urbane** (*Ctrl+B*): solo per console Nortel di tipo M2250/CIU emula il tasto *TGB 0*, il quale deve essere programmato sul PBX per svolgere questa funzione
- **Inizia Reg.** (*Ctrl+I*): solo se abilitata l’opzione SmartRec, inizia la registrazione della conversazione in corso
- **Fine Reg.** (*Ctrl+F*): come per **Inizia Reg.** arresta la registrazione della conversazione in corso
- **Dump**: solo per console Nortel di tipo M2250/CIU, abilita/disabilita la scrittura di un file in formato binario contenente tutte le attività della console
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
- **Colori** (*Ctrl+C*): nella scheda **Form** consente di personalizzare carattere e colori di visualizzazione della maschera principale del programma in modo da adattare l’applicazione ai propri gusti e abitudini
- **Telefono** (*Ctrl+T*): disponibile solo per console Nortel di tipo M2250/CIU, consente di regolare il volume ed il tono di squillo (buzzer) della console stessa
- **Rubrica Interna**: opzione non ancora attiva
- **Rubrica Esterna**: opzione non ancora attiva
- **Sintesi Vocale** (*Ctrl+Alt+V*): se abilitata la funzionalità di Sintesi Vocale, permette di modificare, fino al successivo riavvio del programma ([1]_), i parametri della voce: tipo voce, velocità testo, velocità numeri etc.
- **Sintesi On/Off** (*Ctrl+Alt+S*): se abilitata la funzionalità di Sintesi Vocale, permette di abilitarla o disabilitarla temporaneamente, fino alla pressione della medesima combinazione di tasti oppure fino al riavvio del programma; viene riprodotto lo stato della sintesi

Vista
-----

.. image:: /images/TCONSOLE/UTENTE/CONSOLE/Vista.png

Tqm
-----

.. image:: /images/TCONSOLE/UTENTE/CONSOLE/Tqm.png

? (Informazioni)
----------------

.. image:: /images/TCONSOLE/UTENTE/CONSOLE/Informazioni.png

Come mostrato in figura, questa opzione visualizza informazioni relative all’applicazione; in particolare sono significativi i numeri di versione.

.. image:: /images/TCONSOLE/UTENTE/CONSOLE/info.png

.. .. important :: zzz

.. .. note :: ttt

Pannelli della Console
======================

Util: comandi di utilità
------------------------

ICI: identificazione chiamate entranti
--------------------------------------

Comandi
-------

Display
-------

Loop: pulsanti di impegno linea
-------------------------------

Keypad: tastiera telefonica
---------------------------

FIX: comandi di base
--------------------

Flex: comandi definiti dall’utente
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
.. [1] al riavvio di TConsole vengono ripristinati i parametri della Sintesi Vocale precedenti alle modifiche applicate tramite l'interfaccia dell'applicazione. Per rendere effettive queste modifiche i valori desiderati vanno impostati nel :ref:`Profilo Utente`, riquadro *Permessi*, funzionalità **Sintesi Vocale**