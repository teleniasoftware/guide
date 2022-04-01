===========================
Come si presenta la console
===========================

L’installazione standard dell’applicazione fa in modo che, all’accensione del PC, TConsole venga avviato automaticamente. Normalmente, al suo avvio, TConsole prevede la procedura di autenticazione dell’utente, per mezzo della seguente finestra di login:

.. image:: /images/TCONSOLE/UTENTE/CONSOLE/console.png

L’utente deve inserire le proprie credenziali utente TConsole (username e password) configurate al momento dell'installazione.

.. come si attiva il "Modifica Password"???
.. NOTA: il pulsante "Modifica Password" è opzionale e, se presente, consente all’utente di cambiare la password associata al proprio identificativo.

..
 .. note :: L’avvio di TConsole può essere configurato in modo da eseguire automaticamente la procedura di autenticazione con un identicativo di utente predefinito.

.. note :: L’installazione standard prevede il login automatico a TConsole tramite un'utenza predefinita. È possibile modificare questa configurazione in modo da ripristinare la richiesta di autenticazione dell'utente.

..
 .. note :: Nella finestra di login è possibile verificare quali moduli TConsole sono disponibili: ad es. ####

TConsole è un’applicazione modulare e si presenta in modalità di visualizzazione, di seguito denominate **viste**, che differiscono in base alle prestazioni incluse ed alle configurazioni eseguite.

**Sono disponibili tre diverse viste**, che si differenziano per il livello di ingrandimento via via crescente:

..
    - **Vista Normale**: vista standard, sempre disponibile con il modulo TConsole base, per operatori normalmente vedenti
    - **Vista IPO**: vista opzionale destinata ad un operatore ipovedente; i caratteri sono ingranditi
    - **Vista IPO PLUS**: vista opzionale destinata ad un operatore ipovedente con caratteri ulteriormente ingranditi (vengono visualizzate le funzionalità principali)

- :ref:`Vista Normale`: vista standard, sempre disponibile con il modulo TConsole base, per operatori normalmente vedenti
- :ref:`Vista IPO`: vista opzionale destinata ad un operatore ipovedente; i caratteri sono ingranditi
- :ref:`Vista IPO PLUS`: vista opzionale destinata ad un operatore ipovedente con caratteri ulteriormente ingranditi (vengono visualizzate le funzionalità principali)

.. important :: Per disporre delle viste IPO e IPO PLUS è richiesta la presenza dell'apposita licenza.

Si riporta di seguito un esempio di vista Normale con l'indicazione delle diverse sezioni dell'interfaccia:

.. image:: /images/TCONSOLE/UTENTE/CONSOLE/vista_normale_sezioni.png

Titolo e Barra di Stato sono in comune a tutte e tre le viste.

**Nella vista Normale (e solamente in questa) possono essere presenti uno o più dei seguenti contesti**:

- Rubrica (F3): rubrica unificata, sempre disponibile e in grado di memorizzare sia numeri interni che esterni
- Rubrica Interna (F2): rubrica opzionale, in grado di memorizzare solo numeri interni (normalmente è la Rubrica Interna di un SAM/TSAM alla quale TConsole accede come Client)
- Campo lampade
.. - Rubrica Web
.. - Liste di selezione abbreviata
.. - Prenotazioni

**Nelle viste Ipo e Ipo Plus i contesti disponibili sono solo Rubrica (F3) e, opzionalmente, Rubrica Interna (F2)**.

In queste viste il contesto delle rubriche e la parte di controllo della Console sono visualizzate ognuna a schermo intero con la possibilità di commutare da una all’altra tramite opportune combinazioni di tasti (si rimanda alla sezione relativa del presente manuale).

In questo capitolo si prosegue descrivendo le parti comuni alle viste; successivamente verranno illustrate in dettaglio le viste stesse ed i contesti opzionali.

Titolo
======

Nel titolo dell’applicazione, oltre al nome del programma e del produttore del software, vengono riportate informazioni quali:

- numero della postazione: significativo nel caso di postazioni multiple per poterle distinguere (vedi parametro :ref:`ID` nel file *TConsole.ini*)
- utente: identificativo utilizzato per effettuare il login all’applicazione; ad utenti differenti si possono associare prestazioni e configurazioni differenti (vedi :ref:`Profilo Utente`)
- tipo della console/telefono utilizzato: evidenzia la codifica della console (a seconda dell'ambiente e della tipologia di installazione) attualmente in uso

.. _Barra di Stato:

Barra di Stato
==============

La barra di stato è divisa in cinque parti, nelle quali vengono rispettivamente visualizzate le seguenti informazioni:

- data odierna (del PC)
- ora corrente (del PC)
- icona (*"pallino"*) di connessione al dispositivo telefonico controllato: *"pallino verde"*: connessione funzionante, *"pallino rosso"*: connessione non funzionante (dispositivo non visibile da TConsole)
- icona (*"cilindro"*) di connessione al database: *"cilindro grigio"*: connessione corretta, *"cilindro con X rossa"*: connessione non funzionante
- icona (*"PC"*) di connessione al servizio :ref:`TConsoleServer` ([1]_): icona *"PC"*: connessione funzionante, icona *"PC con X rossa"*: connessione non funzionante
- icona *"altoparlante"*
- testo inviato all’eventuale :ref:`Barra Braille` collegata al PC (se abilitato il parametro :ref:`BRAILLE_STRING_ON_STATUS_BAR` nel file *TConsole.ini*)
- messaggio a scorrimento destinato ad una singola postazione TConsole della rete
- messaggio a scorrimento destinato a tutte le postazioni TConsole della rete

.. rubric:: Note

.. [1] affinché la relativa icona sia presente, il :ref:`Campo Lampade` deve essere abilitato a livello di :ref:`Profilo Utente`