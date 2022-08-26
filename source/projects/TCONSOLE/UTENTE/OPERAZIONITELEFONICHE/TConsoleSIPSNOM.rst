============================================
TConsole SIP SNOM e TConsole TVOX: particolarità di utilizzo
============================================

Nel caso di TConsole in modalità SIP SNOM (parametro *TYPE=SIP_SNOM* nel file :ref:`TConsole.ini`) e di TConsole in modalità TVOX (parametro *TYPE=SNOM* nel file :ref:`TConsole.ini`) vi sono delle piccole differenze nelle manovre di base. Di seguito sono descritte le differenze nell’utilizzo di TConsole SIP SNOM.

.. Nel caso di TConsole in modalità SIP SNOM (parametro *TYPE=SIP_SNOM* nel file :ref:`TConsole.ini`) e di TConsole in modalità TVOX (parametro *TYPE=SNOM* nel file :ref:`TConsole.ini`) o TVox con SoftPhone (parametro *TYPE=TVOX_SOFTPHONE* nel file :ref:`TConsole.ini`) vi sono delle piccole differenze nelle manovre di base. Di seguito sono descritte le differenze nell’utilizzo di TConsole SIP SNOM.

Composizione di un numero per effettuare una chiamata
=====================================================

Nel caso di Tconsole SIP SNOM, prima di iniziare ad effettuare una chiamata non è necessario impegnare una linea. Nel caso di console libera, basta iniziare a digitare il numero e segnalare il fine numero premendo il tasto **punto** (*.[Tn]*) del tastierino numerico.

Utilizzo del finenumero
=======================

A differenza delle altre modalità di configurazione TConsole, su TConsole SIP SNOM **è necessario segnalare la fine della digitazione del numero da chiamare** con il carattere **punto** (*.[Tn]*) del tastierino numerico.

In assenza della digitazione del punto, la chiamata **non** parte e il numero finora digitato rimane visualizzato nel Display TConsole (vedi :ref:`Display`), nella prima o seconda riga ("Linea sorgente" oppure "Linea destinazione") a seconda delle condizioni in cui si sta effettuando la chiamata.

Visualizzazione delle chiamate in coda
======================================

A differenza del TConsole in modalità TVOX, il TConsole SIP SNOM visualizza sulle linee del Loop (vedi :ref:`Loop`) eventuali chiamate in coda **solo se le chiamate stanno squillando sul telefono**. In questo modo, nel caso si abbiano più chiamate in ring è possibile scegliere a quale chiamata rispondere.

Utilizzo del telefono SNOM
==========================

Di seguito si riporta una breve guida all'utilizzo del telefono SNOM, nel caso di impossibilità di utilizzo di TConsole.

Attesa
------

- premere sul pulsante “linea” che a questo punto inizierà a lampeggiare
- per riprendere la chiamata premere nuovamente il pulsante “linea”

Trasferta senza consultazione (trasferta blind)
-----------------------------------------------

- premere il pulsante “transfer”
- digitare il numero
- confermare con il pulsante "spunta"

Trasferta con consultazione
---------------------------

- premere il pulsante per la seconda linea, a questo punto la prima linea inizierà a lampeggiare
- digitare il numero
- confermare con il pulsante "spunta"
- una volta avvenuta la comunicazione premere il pulsante "transfer"

Ripresa chiamata su occupato
----------------------------

- premere il pulsante “x” per abbattere la chiamata su occupato
- ripremere il pulsante "linea"

Ready - Not Ready (solo in modalità TVOX)
-----------------------------------------

- digitare il codice di servizio per impostare il cambio di stato (default: *2291*)
- confermare con il pulsante "spunta"
- il sistema riprodurrà sul telefono un messaggio pre-registrato che indica il cambio di stato

Notte - Giorno (solo in modalità TVOX)
--------------------------------------

- digitare il codice di servizio per impostare il cambio di stato (default: *\*50* seguito dal numero del servizio PO)
- confermare con il pulsante "spunta"
- il sistema riprodurrà sul telefono un messaggio pre-registrato che indica il cambio di stato del servizio
