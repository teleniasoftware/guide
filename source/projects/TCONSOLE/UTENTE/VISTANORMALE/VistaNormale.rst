.. _QBE: https://en.wikipedia.org/wiki/Query_by_Example
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

.. image:: /images/TCONSOLE/UTENTE/VISTANORMALE/Strumenti.png

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

.. image:: /images/TCONSOLE/UTENTE/VISTANORMALE/Chiamate.png

TConsole memorizza automaticamente il numero, lo stato del Display (con l'eventuale nome del chiamante/chiamato/linea), la data e l’ora di ogni chiamata effettuata o ricevuta. Mediante il menu *Chiamate* è possibile accedere a tali liste ed eseguire, eventualmente, la richiamata ad uno di questi numeri.

Il menu contiene le seguenti voci principali:

- **Richiama Ultima** (*Ctrl+R*): richiama il numero dell’ultima chiamata in uscita effettuata
- **Lista Chiamate Entranti** (*Ctrl+E*): visualizza la lista delle ultime 25 chiamate ricevute, con la possibilità di richiamare il numero di una di queste
- **Lista Chiamate Uscenti** (*Ctrl+U*): visualizza la lista delle ultime 25 chiamate effettuate, con la possibilità di richiamare il numero di una di queste

.. _Lista Chiamate Entranti/Uscenti:

**Lista Chiamate Entranti/Uscenti**

Tali liste vengono visualizzate ognuna in una finestra del tipo seguente (in questo caso per le chiamate entranti: per le chiamate uscenti è presente una finestra analoga) con le logiche di seguito descritte:

.. image:: /images/TCONSOLE/UTENTE/VISTANORMALE/ListaChiamateEntranti.png

Nella terza colonna la lettera *I* sta per *Chiamata Interna*, mentre *E* sta per *Chiamata Esterna*. Se in rubrica è abilitato il lookup (vedi :ref:`ABILITA_POPUP`) e il numero chiamante è contenuto in rubrica, nel campo *Descrizione* viene presentato il nome del contatto di Rubrica Interna o Esterna.

In questa finestra è possibile eseguire le seguenti operazioni:

- scorrere la lista, selezionando la riga desiderata, mediante i tasti freccia della tastiera o muovendo la barra di scorrimento verticale con il mouse
- richiamare il numero relativo al record selezionato premendo il tasto *Invio* della tastiera (NON il tasto *Invio\[Tn\]* del tastierino numerico), oppure cliccando sul pulsante **Chiama** oppure facendo doppio click sul numero con il mouse
- azzerare la lista cliccando sul pulsante **Azzèra Lista**
- tornare alla finestra principale di TConsole tramite *Alt+F4* o cliccando sul pulsante **Annulla**

Configurazione
--------------

.. image:: /images/TCONSOLE/UTENTE/VISTANORMALE/Configurazione.png

Il menu *Configurazione* è composto dalle seguenti voci:

- **Colori** (*Ctrl+C*): nella scheda **Form** consente di personalizzare carattere e colori di visualizzazione della maschera principale del programma in modo da adattare l’applicazione ai propri gusti e abitudini. Per la modifica della combinazione di colori di determinate sezioni dell'applicazione o di determinati pulsanti fare riferimento a :ref:`Selezione Colori`
- **Telefono** (*Ctrl+T*): disponibile **solo per console Nortel di tipo CIU/M2250**, consente di regolare il volume ed il tono di squillo (buzzer) della console stessa
- **Rubrica Interna**: opzione non ancora attiva
- **Rubrica Esterna**: opzione non ancora attiva
- **Sintesi Vocale** (*Ctrl+Alt+V*): se abilitata la funzionalità di Sintesi Vocale, permette di modificare, fino al successivo riavvio del programma ([1]_), i parametri della voce: tipo voce, velocità testo, velocità numeri etc.
- **Sintesi On/Off** (*Ctrl+Alt+S*): se abilitata la funzionalità di Sintesi Vocale, permette di abilitarla o disabilitarla temporaneamente, fino alla pressione della medesima combinazione di tasti oppure fino al riavvio del programma; viene riprodotto lo stato della sintesi (abilitata/disabilitata)

.. _Selezione Colori:

Selezione Colori
----------------

.. image:: /images/TCONSOLE/UTENTE/VISTANORMALE/SelezioneColori.png

.. .. image:: /images/TCONSOLE/UTENTE/VISTANORMALE/SelezioneColori_old.png

La finestra *Selezione Colori* permette di impostare il carattere e i colori dei pulsanti e delle aree di testo della Rubrica e della Console facendo clic con il tasto destro del mouse sulla sezione o sul componente interessato.

I componenti sono raggruppati nel seguente modo:

- pulsanti :ref:`ICI`
- pulsanti :ref:`FLEX`
- pulsanti :ref:`Fix`
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
- salvare le scelte fatte cliccando sul pulsante **Conferma**, oppure ignorarle cliccando su **Annulla**

**Le scelte confermate diventano immediatamente operative.**

.. important :: I pulsanti hanno due differenti stati: *Normale* e *Attivo*, per i quali è opportuno impostare combinazioni di colori diverse tra loro. Le aree di testo hanno solamente lo stato *Normale*.

.. warning :: Evitare di impostare per primo piano e sfondo la stessa tonalità di colore, pena l'illeggibilità del pulsante o dell'area di testo. Questo può accadere ad es. quando si clicca con il tasto destro e il sinistro del mouse sullo stesso colore: in questo caso compare "**FB**" sulla stessa casella di selezione colore.

Telefono (solo per Nortel CIU o Nortel M2250)
---------------------------------------------

.. image:: /images/TCONSOLE/UTENTE/VISTANORMALE/ConfigurazioneTelefonoNortelCIU.png

Per modificare volume e tono del segnale acustico emesso dalla console CIU/M2250 cliccare sulle freccette per impostare il valore desiderato.

**Solo per la console CIU** è possibile attivare/disattivare, tramite l'opportuno flag "Audio", l’audio del segnale acustico della console. Per console M2250 la finestra è identica ma il flag non è presente.

.. _Vista:

Vista
-----

.. image:: /images/TCONSOLE/UTENTE/VISTANORMALE/Vista.png

L’opzione *Vista* consente di commutare dalla vista Normale (*Ctrl+Alt+N*) alle altre viste disponibili, se abilitate a livello di :ref:`Profilo Utente`. Ad esempio, nella precedente immagine è abilitata anche la vista IPO (*Ctrl+Alt+I*), mentre non sono abilitate le viste IPO PLUS (*Ctrl+Alt+Z*) e la vista Batteria (*Ctrl+Alt+B*).

.. note :: Nonostante questo menu sia visivamente disponibile solo nella vista Normale, le configurazioni di tasti indicate sono utilizzabili anche dopo aver commutato ad una vista qualsiasi: ad esempio, trovandosi nella vista IPO PLUS, si potrà commutare direttamente alla vista Normale tramite *Ctrl+Alt+N* oppure alla vista IPO tramite *Ctrl+Alt+I*.

Tqm
---

.. image:: /images/TCONSOLE/UTENTE/VISTANORMALE/Tqm.png

Il menu *Tqm*, presente **solo quando TConsole è configurato in modalità TVOX** (vedi :ref:`Parametri TVox`), è composto dalle seguenti voci:

- **Login** (*Ctrl+Shift+F7*): Esegue, se non già effettuato, il Login dell'operatore ([2]_)
- **Logout** (*Ctrl+Shift+F8*): Esegue, se non già effettuato, il Logout dell'operatore ([2]_)
- **Stato** > **Ready** (*Ctrl+Shift+F11*): Imposta l'operatore in stato Ready (Pronto)
- **Stato** > **Not Ready** (*Ctrl+Shift+F12*): Imposta l'operatore in stato NotReady (Non Pronto)

? (Informazioni)
----------------

.. image:: /images/TCONSOLE/UTENTE/VISTANORMALE/Informazioni.png

Come mostrato in figura, questa opzione visualizza informazioni relative all’applicazione; in particolare sono significativi i numeri di versione.

.. image:: /images/TCONSOLE/UTENTE/VISTANORMALE/info.png

Pannelli della Console
======================

Questa è la parte di controllo della console o telefono che l’applicazione gestisce direttamente ed è provvista dei seguenti pannelli (da sinistra a destra):

- :ref:`Util`
- :ref:`ICI`
- :ref:`Display`
- :ref:`Loop`
- :ref:`Fix`
- :ref:`Keypad`
- :ref:`Comandi`
- :ref:`FLEX`
.. - :ref:`TQM`

.. important:: Questi pannelli consistono solitamente di pulsanti e aree di testo: i pulsanti sono attivabili cliccandoci sopra con il tasto sinistro del mouse oppure tramite combinazioni di tasti. Per conoscere la combinazione di tasti associata ad un determinato pulsante è sufficiente posizionarsi con il mouse sopra il pulsante per far comparire il popup indicante la relativa combinazione di tasti.

.. important:: La dicitura *[Tn]* indica di utilizzare il tasto funzione **del tastierino numerico** (*Keypad*): ad esempio *\*[Tn]* indica l'asterisco del tastierino numerico, *Invio[Tn]* indica il tasto *Invio* del tastierino numerico, e così via.

.. _Util:

Util: comandi di utilità
------------------------

.. image:: /images/TCONSOLE/UTENTE/VISTANORMALE/Util.png

- **[?] (Help)** (*F1*):  visualizza l’Help in linea
- **[Sole/Luna] (Giorno/Notte)** (*Ctrl+Alt+N*):  il pulsante Giorno/Notte pone lo stato della console in libero/occupato: per il significato e configurazione di tali stati si rimanda alla configurazione del PBX. Per TConsole in modalità TVox (vedi :ref:`Parametri TVox`) il pulsante è disattivato.
- **[Stato PO]** (*F4*): per TConsole in modalità non vedente riporta, in Sintesi Vocale e/o in Barra Braille, informazioni relative allo stato della console. Oltre a questo, in tutte le modalità la pressione del tasto toglie il focus dalla Rubrica e lo riporta alla console principale del programma
- **[Postit]** (*F9*): attiva/disattiva la finestra PostIt per consentire di digitare da tastierino numerico il numero da chiamare dettato durante durante la conversazione, senza che la digitazione metta in attesa la chiamata in corso
- **[In] (Lista Ch. Entranti)** (*Ctrl+E*): visualizza la finestra con l’elenco delle ultime chiamate entranti (vedi :ref:`Lista Chiamate Entranti/Uscenti <Lista Chiamate Entranti/Uscenti>`)
- **[Out] (Lista Ch. Uscenti)** (*Ctrl+U*): visualizza la finestra con l’elenco delle ultime chiamate uscenti (vedi :ref:`Lista Chiamate Entranti/Uscenti <Lista Chiamate Entranti/Uscenti>`)

.. _ICI:

ICI: identificazione chiamate entranti
--------------------------------------

.. image:: /images/TCONSOLE/UTENTE/VISTANORMALE/ICI.png

Questo pannello (*Incoming Call Identification*) indica all’operatore la tipologia delle chiamate che si presentano alla console: le etichette riportate (*Interna*, *Esterna* etc.) dipendono dalla configurazione del PBX e, in certi contesti, sono modificabili (vedi :ref:`Tasti ICI`).

L’arrivo di una chiamata attiva il relativo pulsante che consente, se premuto, di rispondere direttamente a quel tipo di chiamata senza utilizzare i pulsanti "Linea"; questa funzionalità permette, ad es. nel caso si presentino in ingresso più chiamate di diverso tipo, di privilegiare la risposta ad un tipo di chiamata (ad es. le chiamate con ICI *Esterna*) rispetto ad un altro.

La selezione del pulsante può avvenire anche tramite tastiera, premendo i tasti da *Ctrl+F1* a *Ctrl+F10*, dove il pulsante più basso corrisponde a *Ctrl+F1*, quello più alto a *Ctrl+F10*.

.. _Display:

Display
-------

.. image:: /images/TCONSOLE/UTENTE/VISTANORMALE/Display.png

Il pannello *Display* è composto da tre righe:

- la prima (**Linea sorgente**) fornisce informazioni relative alla chiamata in ingresso
- la seconda (**Linea destinazione**) fornisce informazioni sulla chiamata in uscita
- la terza (**Stato della console**) riporta lo stato della console o telefono (*Libero*/*Occupato*/*Notte*/*Attivo*) e, se previsto dalla configurazione TConsole, il numero delle chiamate in coda

Le informazioni relative alle linee sorgente e destinazione, tipicamente numero chiamante e numero chiamato, linea e nome associato al numero, possono variare in base alla programmazione del PBX. Ad esempio, in riferimento all'immagine precedente:

- la Linea sorgente visualizza il numero chiamante *0452224660* e il numero chiamato *42264* (in questo caso è l'interno del PO; in altri contesti si può presentare la numerazione pubblica chiamata)
- la Linea destinazione visualizza il numero *4226* che il PO sta chiamando, con la Linea sorgente messa in attesa
- lo Stato della console è *Attivo*

.. _Loop:

Loop: pulsanti di impegno linea
-------------------------------

.. image:: /images/TCONSOLE/UTENTE/VISTANORMALE/Loop.png

Per rispondere ad una chiamata in ingresso, si utilizzano i pulsanti *Linea* (loop); a fianco di ciascun pulsante viene riportato lo stato della linea.
I pulsanti possono essere cliccati con il  mouse oppure selezionati da tastiera mediante le combinazioni di tasti da *Ctrl+0[Tn]* a *Ctrl+5[Tn]* (se le linee visualizzate sono 6, altrimenti fino a *CTRL+11[Tn]* per 12 linee).

.. important:: Nel caso di più chiamate in ingresso in contemporanea, il tasto *+[Tn]* (tasto di Risposta/Impegno) risponde alla prima chiamata che sta squillando.

.. note:: Per centrali che prevedono l'impegno linea la pressione del relativo pulsante va ad impegnare la rispettiva linea. La pressione del *+[Tn]* impegna la prima linea libera.

Ad esempio, in riferimento all'immagine precedente:

- la Linea 0 è in stato *In Attesa* (può trattarsi indifferentemente di una chiamata ricevuta e risposta oppure di una chiamata effettuata, in seguito messa in attesa dal PO)
- la Linea 1 è in stato *Risposta* (è la linea attiva, con cui il PO si trova ora in conversazione)
- sulla linea 2 sta squillando una chiamata in ingresso il cui numero è associato al contatto "Scomparin" di Rubrica ([3]_)
- sulla linea 3 sta squillando un'altra chiamata in ingresso dal numero 0452224660 che non è associato ad alcun contatto di Rubrica

In queste condizioni è possibile eseguire una delle seguenti azioni:

- premere *Ctrl+2[Tn]* oppure *+[Tn]* per rispondere alla chiamata in ingresso da "Scomparin" sulla linea 2, mettendo in attesa anche la linea 1 e lasciando in ring la chiamata in ingresso dal numero 0452224660 sulla linea 3
- premere *Ctrl+3[Tn]* per rispondere alla chiamata in ingresso dal numero 0452224660 sulla linea 3, mettendo in attesa anche la linea 1 e lasciando in ring la chiamata in ingresso da "Scomparin" sulla linea 2
- premere *Ctrl+0[Tn]* per riprendere la chiamata sulla linea 0, mettendo in attesa la linea 1 e lasciando in ring le linee 2 e 3
- premere *-[Tn]* per mettere in attesa anche la chiamata sulla linea 1, lasciando in ring le linee 2 e 3
- (se previsto lato centrale) premere *Ctrl+4[Tn]* per impegnare la linea 4, mettendo in attesa anche la linea 1 e lasciando in ring le linee 2 e 3

.. _Fix:

Fix: comandi di base
--------------------

.. image:: /images/TCONSOLE/UTENTE/VISTANORMALE/Fix.png

Sono le funzioni "classiche" della console, indipendenti dalla programmazione del PBX pertanto sono sempre presenti. Sono normalmente utilizzate nel corso della procedura di trasferimento di una chiamata.

In particolare:

- **[Escl.] (Excl Src)** (*Ctrl+Shift+F5*): **Escludi chiamante** (origine), tasto della **prima** riga: pone nello stato *Attesa* il chiamante e permette di parlare con il chiamato senza che il chiamante ascolti
- **[Escl.] (Excl Dest)** (*Ctrl+Shift+F4*): **Escludi chiamato** (destinazione), tasto della **seconda** riga: pone nello stato *Attesa* il chiamato e permette di parlare con il chiamante senza che il chiamato ascolti
- **[Ril.] (Rls Src)** (*Ctrl+Shift+F3*): **Rilascia chiamante** (origine), tasto della **prima** riga: rilascia il chiamante dalla conversazione e torna in linea con il chiamato
- **[Ril.] (Rls Dest)** (*Ctrl+Shift+F2* oppure *\*[Tn]*): **Rilascia chiamato** (destinazione), tasto della **seconda** riga: rilascia il chiamato dalla conversazione e torna in linea con il chiamante

.. _Keypad:

Keypad: tastiera telefonica
---------------------------

.. image:: /images/TCONSOLE/UTENTE/VISTANORMALE/Keypad.png

Per comporre il numero manualmente si può utilizzare il tastierino numerico del PC (parte destra della tastiera) o cliccare sui pulsanti di composizione presenti sul pannello *Keypad*.

.. important:: In questo contesto, in caso di errata digitazione del numero da chiamare **non** è possibile cancellarne una parte (ad esempio l'ultima cifra tramite il tasto *backspace*): va annullata l'intera digitazione tramite la funzione **Rilascia chiamato** (*Ctrl+Shift+F2* oppure *\*[Tn]*) (decritta in :ref:`Fix`) e a questo punto bisogna ripetere interamente la digitazione del numero.

.. accenno alla funzione postit in cui è possibile usare il backspace?

.. _Comandi:

Comandi
-------

.. image:: /images/TCONSOLE/UTENTE/VISTANORMALE/Comandi.png

.. _FLEX:

FLEX: comandi definiti dall’utente
----------------------------------

.. image:: /images/TCONSOLE/UTENTE/VISTANORMALE/FLEX.png

Queste funzioni programmabili dipendono:

- dalla configurazione del PBX, nel caso di console Nortel M2250/CIU: in questo caso è opportuno configurare le etichette visualizzate in modo che corrispondano alle impostazioni del PBX (tasti funzione della console se si tratta di M2250)
- dalla configurazione di TConsole, nel caso di telefono SNOM o di telefono controllato via TAPI

La selezione del pulsante può avvenire cliccandoci sopra con il mouse oppure da tastiera, premendo le combinazioni di tasti da *Shift+F1*, *Shift+F2* etc. fino a *Shift+F11*, dove il pulsante FLEX più basso corrisponde a *Shift+F1*, quello più alto a *Shift+F11*.

.. warning:: Per il primo FLEX in alto **NON** viene utilizzata la combinazione *Shift+F10*, ma si deve utilizzare *Shift+F11*.

La configurazione dei tasti FLEX e delle loro etichette è descritta in :ref:`Tasti FLEX`.

..
    .. _TQM:

    TQM: comandi per la gestione TQM
    ----------------------------------

Rubrica F3
==========

TConsole integra una rubrica telefonica mediante la quale è possibile gestire (localmente od in maniera centralizzata) una notevole quantità di nominativi sia interni che esterni, effettuando rapide ricerche e composizioni automatiche. Questo è il contesto sempre presente.

Il contesto Rubrica si compone delle seguenti parti:

- campi di selezione per la ricerca dei nominativi
- risultato della ricerca
- dettaglio dei nominativi trovati
- quantità di nominativi ricercati
- tasto di ricerca (da tastiera tasto *[Invio]* **non del tastierino numerico**)
- tasto di ricerca alternativa (da tastiera *F11* - vedi parametro :ref:`RIC_ALT`)
- tasto per la composizione automatica dei numeri telefonici (da tastiera *F12* - vedi parametro :ref:`F12`)
- funzioni per la manutenzione della Rubrica (inserimento/modifica dei contatti o impostazione dei colori)

.. important:: Tutti i parametri per la configurazione dei campi di ricerca e di visualizzazione (etichetta visualizzata e ordine di presentazione) sono descritti in :ref:`RubInt.ini e RubEst.ini`.

.. image:: /images/TCONSOLE/UTENTE/VISTANORMALE/Rubrica.png

Ricerca nominativi
------------------

Per eseguire una nuova ricerca seguire le seguenti istruzioni:

- premere il tasto *F3* della tastiera: a questo punto il cursore si posiziona nel primo campo di ricerca (default *Descrizione*) svuotando tutti i campi dall'eventuale compilazione dovuta ad una ricerca precedente
- se desiderato, indicare le opzioni di ricerca compilando i vari campi in modo da restringere la ricerca effettuata. Il tasto *Tab* consente di spostarsi sul campo successivo
- cliccare sul pulsante *Cerca* ("lente d'ingrandimento") o premere il tasto *Invio* (NON del tastierino numerico)

I nominativi soddisfacenti le opzioni di ricerca verranno elencati nell’area di visualizzazione (sezione **MASTER**): spostando il cursore con i tasti freccia o selezionando un particolare nominativo con il mouse, il dettaglio del record viene mostrato nelle apposite finestre sottostanti (sezione **DETAIL**).

.. important:: Se nessun dato viene specificato nei campi di ricerca, verranno restituiti **tutti** i nominativi presenti in Rubrica.

.. note:: Per la ricerca in Rubrica si utilizzano le logiche `QBE`_ (*Query By Example*).

I tasti di ricerca possono anche essere spostati nel lato destro o sinistro della finestra in base al parametro utente opportunamente configurato: *Tasti Ricerca a Sx = SI/NO* (vedi :ref:`Profilo Utente`).

.. important:: Per togliere il focus dalla Rubrica, riportandolo alla console principale, premere il pulsante **[Stato PO]** (da tastiera *F4*) del pannello :ref:`Util`.

Ricerca testuale/Ricerca multicampo
-----------------------------------

La *ricerca testuale* è una diversa modalità di ricerca che avviene ricercando la parola in tutti i campi di Rubrica, anziché nel singolo campo di volta in volta selezionato.

Per attivare questa modalità cliccare con il mouse sul tasto **[-]** in alto a destra nel riquadro dei campi di ricerca (vedi **circoletto rosso** nell'immagine precedente) oppure utilizzare la combinazione di tasti *Ctrl+Shift+T*.

Ripetendo la stessa manovra (il pulsante in questo caso è diventato **[+]**) si ritorna alla modalità di *ricerca multicampo* standard.

.. note:: L'impostazione del tipo di ricerca viene mantenuta anche dopo la chiusura di TConsole.

Composizione automatica
-----------------------

È possibile comporre automaticamente il numero associato al nominativo di Rubrica selezionato cliccando sul pulsante *F12* (**Invio numero alla consolle**) presente in alto a destra del contesto di Rubrica o, da tastiera, premendo il tasto *F12*.

Un’estensione alla composizione automatica è data dalla pressione contemporanea dei tasti *Shift*, *Ctrl*, *Alt* ed il tasto *F12*: in questo caso il numero composto è prelevato da uno dei 3 campi alternativi opportunamente configurati. Ad es., facendo riferimento alla figura precedente, premendo *Shift+F12* viene composto, se popolato, il numero presente nella colonna *Cellulare*.

La configurazione dei campi da utilizzare per la composizione automatica è descritta nel parametro :ref:`F12`.

Inserimento nominativi
----------------------

La pressione del pulsante **Inser.** o della combinazione di tasti *Ctrl+Shift+I* permette l’inserimento di un nuovo nominativo in Rubrica.

L’operazione si realizza compilando opportunamente i campi delle finestre sotto riportate, agendo sui pannelli *Dati 1*, *Dati 2* e *Dati 3*.

.. image:: /images/TCONSOLE/UTENTE/VISTANORMALE/RubricaInserisciDati1.png
.. image:: /images/TCONSOLE/UTENTE/VISTANORMALE/RubricaInserisciDati2.png
.. image:: /images/TCONSOLE/UTENTE/VISTANORMALE/RubricaInserisciDati3.png

.. important :: È importante specificare la Rete (pannello *Dati 1*) in modo da specificare il tipo del numero telefonico (interno o esterno).

.. tip :: Da tastiera il tasto *Tab* consente di spostarsi sul campo successivo, rimanendo all'interno dello stesso pannello (ad es. *Dati 1*). Per spostarsi da un pannello all'altro utilizzare *Ctrl+Tab*.

La pressione del pulsante **Inserisci** crea nell’archivio un nuovo nominativo con i dati specificati.

La pressione del pulsante **Annulla** non inserisce alcun nominativo.

I pulsanti **Modifica** ed **Elimina** in questa fase sono disabilitati.

.. warning :: Nel riquadro **Visibilità** **NON** togliere il flag dalla voce *Centralino* altrimenti il record, pur rimanendo presente nel database, non sarà più visibile nella Rubrica TConsole.

.. tip :: Nelle immagini precedenti il campo *Libero_5* del pannello *Dati 2* e tutti i campi del pannello *Dati 3* sono disabilitati, e di conseguenza NON modificabili da TConsole, in quanto NON sono state definite le rispettive etichette nella :ref:`Rubint.ini RubEst.ini Sezione LABELS` del file *RubEst.ini*.

Modifica e cancellazione nominativi
-----------------------------------

Facendo clic con il tasto destro del mouse, seguito dal clic sulla voce "Modifica", su un nominativo risultato di una ricerca oppure premendo il tasto *Ctrl+Shift+M* con un nominativo selezionato, è possibile accedere alla finestra di modifica/cancellazione (diversa da quella di inserimento solamente per i pulsanti **Modifica** ed **Elimina** abilitati).

.. image:: /images/TCONSOLE/UTENTE/VISTANORMALE/RubricaModificaDati1.png
.. image:: /images/TCONSOLE/UTENTE/VISTANORMALE/RubricaModificaDati2.png

Per modificare il nominativo compilare opportunamente i campi desiderati (facendo attenzione al campo *Rete*) e terminare cliccando sul pulsante **Modifica**: il nominativo verrà immediatamente aggiornato in Rubrica.

Per cancellare il nominativo cliccare invece sul pulsante **Elimina**.

La pressione del pulsante **Annulla** lascia il nominativo inalterato.

Il pulsante **Inserisci** in questa fase è disabilitato.

.. note :: Sia la modifica che l'eliminazione di un contatto prevedono una seconda finestra di conferma per evitare di eseguire la manovra accidentalmente.

.. rubric:: Note

.. [1] al riavvio di TConsole vengono ripristinati i parametri della Sintesi Vocale precedenti alle modifiche applicate tramite interfaccia dell'applicazione. Per rendere effettive queste modifiche i valori desiderati vanno impostati nel :ref:`Profilo Utente`, riquadro *Permessi*, funzionalità **Sintesi Vocale**
.. [2] il Login e il Logout dell'operatore avvengono automaticamente rispettivamente al momento dell’apertura e della chiusura di TConsole
.. [3] per abilitare il lookup in Rubrica per le chiamate in ingresso occorre abilitare il parametro :ref:`ABILITA_POPUP`