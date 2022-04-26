.. _Profilo Utente:

==============
Profilo Utente
==============

Il programma di configurazione consente di definire gli utenti che possono utilizzare il modulo TConsole.
Si accede a questo strumento nei Programmi della barra delle applicazioni, nel percorso *TConsole* | *Configurazione*:

.. image:: /images/TCONSOLE/INSTALLAZIONE/CONFIGURAZIONE/profilo_utente_menu_Avvio.png

Il modulo *Gestione Utenti* permette di gestire gli utenti che possono accedere a TConsole. Tramite questa applicazione è possibile:

- definire i nomi utente e le password;
- assegnare a ciascun utente dei permessi in base ai quali potrà accedere o no a determinate funzioni di TConsole (es.: permesso di modificare la Rubrica Esterna, Campo Lampade, l'accesso stesso a questo strumento di configurazione);
- configurare alcuni parametri in funzione dell’utente (modalità Ipovedente, Sintesi Vocale, Barra Braille).

.. image:: /images/TCONSOLE/INSTALLAZIONE/CONFIGURAZIONE/profilo_utente1.png

Il form di avvio elenca tutti gli utenti autorizzati ad accedere al sistema TSAM e TConsole e presenta le seguenti informazioni riepilogative:

- utente
- cognome
- nome
- descrizione

.. image:: /images/TCONSOLE/INSTALLAZIONE/CONFIGURAZIONE/profilo_utente2.png

Per visualizzare nel dettaglio il profilo di un utente, fare doppio clic col mouse sulla riga corrispondente oppure selezionarlo e premere il pulsante *Proprietà*:

.. image:: /images/TCONSOLE/INSTALLAZIONE/CONFIGURAZIONE/profilo_utente3.png

Una volta visualizzato un profilo utente nella relativa finestra di gestione, da questa è possibile impostare abilitazioni, funzioni e permessi dell’utente:

- nel riquadro *Ruolo* sulla sinistra sono visibili le abilitazioni o funzionalità utilizzabili, **compatibilmente con la licenza disponibile** (ad es. viene utilizzata la Sintesi Vocale)
- nel riquadro *Permessi* sulla destra sono visibili le abilitazioni consentite dai vari ruoli e le configurazioni dei singoli parametri (funzionalità attiva/non attiva o valore del parametro)

Ad esempio, in riferimento all'immagine precedente relativa all'utenza *po*:

- nel riquadro *Ruolo* è presente il flag su **PO** per la vista Normale (licenza abilitata di default), inoltre è presente il flag anche su **Sintesi** pertanto è necessario disporre anche della licenza per la Sintesi Vocale
- nel riquadro *Ruolo* non è presente il flag su **Admin** pertanto l'utenza *po* sarà abilitata solo all'accesso a TConsole ma non a questa interfaccia amministrativa

.. warning ::
    Se nel riquadro *Ruolo* si mette il flag su un ruolo ma non si dispone della relativa licenza, all'avvio di TConsole verrà restituito un errore di "licenza non disponibile" e TConsole non si potrà aprire.

- nel riquadro *Permessi* la voce **TConsole**, funzionalità **M2250** (console principale delle funzionalità telefoniche) è selezionata (la casella contiene la crocetta) quindi la funzionalità è utilizzata e i relativi parametri vengono considerati. Per deselezionare la voce fare clic con tasto destro del mouse
- tra i parametri della funzionalità **M2250**:

  - *BRAILLE = NO*: nella console principale la Barra Braille non è abilitata; il parametro viene comunque ignorato in quanto nel riquadro *Ruolo* NON è presente il flag su **Braille**. La funzionalità richiede la licenza per **Barra Braille** e il flag sul ruolo **Braille**. Ulteriori dettagli sulla configurazione della Barra Braille nella console principale sono descritti in :ref:`TConsole.ini Sezione BRAILLE`
  - *ABILITA SINTESI VOCALE = SI*: nella console principale la Sintesi Vocale è abilitata. La funzionalità, così come gli altri parametri correlati, richiede la licenza per **Sintesi Vocale** e il flag sul ruolo **Sintesi**. Ulteriori dettagli sulla configurazione della Sintesi Vocale sono descritti in :ref:`Rubint.ini RubEst.ini Sezione SYNTH`
  - *Rubrica Interna = SI*: la Rubrica Interna (F2) è abilitata e viene resa visibile, altrimenti di default è visibile solo la Rubrica Esterna (F3)
  - *CAMPO LAMPADE = NO*: il Campo Lampade non è abilitato; il parametro viene comunque ignorato in quanto nel riquadro *Ruolo* NON è presente il flag su **BLF**. La funzionalità richiede la licenza per il **Campo Lampade** e il flag sul ruolo **BLF**. Ulteriori dettagli sulla configurazione della Sintesi Vocale sono descritti in :ref:`Campo Lampade`
  - *Sintesi su Numeri = SI*: all'arrivo di una chiamata, la Sintesi Vocale (se abilitata) riproduce informazioni sul numero chiamante (*"0452224660 su linea 0"*) o, se il numero è presente in rubrica ed il lookup è abilitato, viene letto il nominativo contenuto in rubrica. Se settato a *NO* viene riprodotto un messaggio generico del tipo *"Chiamata entrante su linea 0"*
  - *Sintesi su Keypad = SI*: alla pressione di una delle cifre del tastierino numerico (su tastiera del PC o sulla console), la Sintesi Vocale (se abilitata) riproduce la cifra che viene di volta in volta digitata
  - *Blocca sintesi su Numeri dopo Risposta* (parametro non valorizzato, questo equivale a valorizzarlo a *NO*): al momento della risposta ad una chiamata, la Sintesi Vocale (se abilitata) riproduce informazioni sul numero chiamato (DNIS) e sul numero chiamante (CLID). Se valorizzato a *SI* la Sintesi Vocale non riproduce nulla al momento della risposta ad una chiamata

Analogamente, in riferimento alla seguente immagine, sempre relativa all'utenza *po*:

.. image:: /images/TCONSOLE/INSTALLAZIONE/CONFIGURAZIONE/profilo_utente4.png

- nel riquadro *Permessi*, sempre alla voce **TConsole**, la funzionalità **Rubrica** (funzionalità principali di Rubrica) è selezionata quindi la funzionalità è utilizzata e i relativi parametri vengono considerati
- tra i parametri della funzionalità **Rubrica**:

  - *modifica Rubrica Interna = NO*: se abilitata per la visualizzazione (vedi parametro *Rubrica Interna* nella funzionalità **M2250**), la Rubrica Interna è disponibile solo in lettura e non è possibile modificarla
  - *modifica Rubrica Esterna = SI*: è possibile modificare la Rubrica Esterna
  - *BRAILLE = NO*: la Barra Braille non è abilitata in Rubrica; il parametro viene comunque ignorato in quanto nel riquadro *Ruolo* NON è presente il flag su **Braille**. La funzionalità richiede la licenza per **Barra Braille** e il flag sul ruolo **Braille**. Ulteriori dettagli sulla configurazione della Barra Braille in Rubrica sono descritti in :ref:`Rubint.ini RubEst.ini Sezione BRAILLE`
  - *VISTA IN MODALITÀ IPO = NO*: la modalità IPO o IPO PLUS non è abilitata, pertanto TConsole si avvia solo nella vista Normale; il parametro viene comunque ignorato in quanto nel riquadro *Ruolo* NON è presente il flag su **IPO**. Per abilitare la vista IPO (TConsole si avvia in modalità IPO ed è possibile passare alla vista Normale e viceversa tramite combinazioni di tasti, descritte in :ref:`Vista`) impostare il parametro a *IPO*. Per abilitare la vista IPO PLUS (TConsole si avvia in modalità IPO PLUS ed è possibile passare alla vista Normale, vista IPO e viceversa tramite combinazioni di tasti, descritte in :ref:`Vista`) impostare il parametro a *PLUS*. **Solo per la vista IPO PLUS** sono disponibili alcuni parametri di configurazione descritti in :ref:`TConsole.ini`. La funzionalità richiede la licenza per **Vista IPO/IPO PLUS** e il flag sul ruolo **IPO**
  - *ABILITA SINTESI VOCALE = SI*: la Sintesi Vocale è abilitata in Rubrica. La funzionalità richiede la licenza per **Sintesi Vocale** e il flag sul ruolo **Sintesi**. Ulteriori dettagli sulla configurazione della Sintesi Vocale in Rubrica sono descritti in :ref:`Rubint.ini RubEst.ini Sezione SYNTH`
  - *vedi Note in grande = NO*: **solo nella vista Normale** è possibile, impostando il parametro a *NO*, suddividere verticalmente la sezione dei dettagli contatto di Rubrica Interna o Esterna, in modo da visualizzare i dettagli in due colonne (anziché un solo dettaglio per riga, uno sotto l'altro) permettendo di risparmiare spazio. Se impostato a *SI* viene visualizzato un solo dettaglio per riga, come nelle viste IPO e IPO PLUS. Ulteriori dettagli sulla configurazione dei dettagli contatto in Rubrica sono descritti in :ref:`Rubint.ini RubEst.ini Sezioni MASTER, DETAIL e DETAIL_IPO`

Per modificare uno di questi parametri fare doppio clic sulla voce interessata per aprire la finestra di modifica, inserire il nuovo valore e confermare cliccando su *OK* (vedi esempio nell'immagine seguente):

.. image:: /images/TCONSOLE/INSTALLAZIONE/CONFIGURAZIONE/profilo_utente5.png

In questo caso si è scelto di abilitare la vista IPO, pertanto è necessario anche mettere il flag su *IPO* nel riquadro *Ruolo*, oltre che disporre della relativa licenza.

Dopo aver impostato i permessi e assegnato funzioni e abilitazioni, per rendere effettive le operazioni effettuate cliccare su *Modifica*.

.. image:: /images/TCONSOLE/INSTALLAZIONE/CONFIGURAZIONE/profilo_utente6.png