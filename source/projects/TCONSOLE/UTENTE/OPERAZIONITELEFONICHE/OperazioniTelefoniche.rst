==============================
Operazioni telefoniche di base
==============================

Vengono di seguito descritti alcuni esempi di operazioni telefoniche di base di maggior utilizzo.

.. note:: Con **[Tn]** si denota un tasto del tastierino numerico.

|br|


Postazione libera/occupata (disabilitato in ambiente TVOX)
==========================================================


E\’ possibile commutare lo stato della console da libera ad occupata e viceversa premendo il pulsante **Giorno/Notte** o il tasto **Ctrl+N**. Sul display di TConsole compaiono alternativamente i
messaggi *Libero* o *Occupato*.

Tale funzione è disabilitata in ambiente TVOX. La funzione **Giorno/Notte** viene abilitata come descritto nel cap 12.1.2

.. note:: (per console Nortel M2250/CIU): se tutte le console sono in stato *Occupato*, il PBX si pone automaticamente in servizio notturno e sul display di tutte le console compare il messaggio *Notte*.

.. Attention:: Nello stato  **Occupato**  o  **Notte**  la console non riceve chiamate.

|br|


Postazione Notte/Giorno (solo per TVOX)
=======================================

E\’ possibile commutare lo stato del servizio da *attivo* a *notte* digitando l’opportuno tasto **FLEX** configurato appositamente. Sul display di TConsole compaiono alternativamente i messaggi *Libero* o
*Notte*.

.. Attention:: Nello stato **Notte** la console non riceve chiamate.

|br|



PO Pronto/Non Pronto (solo per TVOX)
====================================

E\’ possibile commutare lo stato del PO da **Pronto** (Ready) o **Non Pronto** (not ready) digitando i rispettivi tasti *Ready* (ctrl+a) e *Not Ready* (ctrl+w).

.. Attention:: Nello stato **Not ready**, il PO non riceve le chiamate, ma ha la possibilità di vedere le chiamate in coda.

|br|




Risposta ad una chiamata
========================

Le chiamate vengono accodate nell’ordine di arrivo. Il tipo di chiamata viene segnalato dal relativo indicatore di chiamata in arrivo **ICI**:

- all’arrivo di una chiamata la console emette un tono
- l’opportuno indicatore **ICI** si attiva
- per rispondere alla chiamata, ci sono tre possibilità:
    - cliccare sul pulsante **ICI** (per dare priorità al tipo di chiamata), oppure
    - cliccare sul pulsante **Linea** evidenziato, oppure
    - premere il corrispondente tasto **Ctrl + 0 .. 5 [Tn]**, oppure
    - premere il tasto **Più [Tn]**
  
- la chiamata selezionata è risposta, il suono si interrompe e la linea relativa alla chiamata si pone nello stato *Risposta*.

|br|


Terminazione di una chiamata
============================

Per terminare una chiamata, cliccare sul pulsante **Rilascio** o premere il tasto **Invio [Tn]**: la linea occupata dalla chiamata si pone nello stato *Libero*.

|br|



Inoltro di una chiamata ad un numero occupato
=============================================


Se, dopo aver risposto ad una chiamata, l’operatore la inoltra ad un numero che risulta occupato, non accetta chiamate in coda o ne ha già una o più in coda, su indicazione dell’utente chiamante, la chiamata può essere rilasciata o messa in attesa per poi verificare periodicamente lo stato del numero destinazione.

**Selezione del numero**

- selezionare il numero telefonico richiesto, utilizzando la tastiera numerica
- durante la selezione, l’indicatore **Escl. Ch.nte** si accende e il chiamante viene messo automaticamente in attesa
- al tono di occupato, la linea si pone nello stato **Dest.Occ.**
- rilasciare il chiamato cliccando sul pulsante **Ril.Ch.ato** o premendo il tasto **Ctrl+Shift+F3** o **Asterisco [Tn]**
- l’indicatore **Escl. Ch.nte** si spegne e la linea si pone nello stato *Risposta*
- l’operatore torna in linea con il chiamante
  
**Chiamante disponibile all’attesa**

- se l’utente chiamante desidera attendere, mettere in attesa la chiamata premendo consecutivamente il pulsante **Attesa** o il tasto **Meno [Tn]** ed il pulsante **Rilascio** o il tasto **Invio [Tn]**
- la linea si pone nello stato *In Attesa*
- l’operatore può elaborare altre chiamate su altre linee

**Verifica periodica**

- per verificare periodicamente se l’utente si è liberato, cliccare sul pulsante **Linea** o premere il tasto **Ctrl + 0 .. 5 [Tn]** della linea che si trova nello stato *In Attesa* per riprendere l’utente in attesa
- selezionare nuovamente il numero destinatario

**Chiamante non disponibile all’attesa**

- terminare la chiamata con la modalità già descritta

|br|



Inoltro di una chiamata ad un numero libero
===========================================

Dopo aver risposto ad una chiamata, l’operatore può inoltrarla ad un numero che risulta libero. 

**Selezione del numero**

- selezionare il numero telefonico richiesto, utilizzando la tastiera numerica
- durante la selezione, l’indicatore **Escl. Ch.nte** si accende e il chiamante viene messo automaticamente in attesa
- al tono di libero la linea si pone nello stato **Dest.Lib.**
- l’operatore può inoltrare la chiamata in due modalità:
   - senza consultazione
      - cliccare immediatamente sul pulsante **Rilascio** o premere il tasto **Invio [Tn]** per completare la procedura di inoltro 
    .. note:: il PBX può essere impostato in modo da far tornare la chiamata all’operatore nel caso di mancata risposta

      - l’indicatore **Escl. Ch.nte** si spegne e la linea si pone nello stato *Libero*
   - con consultazione possono verificarsi le seguenti situazioni:
      - l’utente selezionato risponde ed accetta la chiamata
         - la linea si pone nello stato *Estesa*
         - completare la procedura di inoltro cliccando sul pulsante **Rilascio** o premendo il tasto **Invio [Tn]**
         - l’indicatore **Escl. Ch.nte** si spegne e la linea si pone nello stato *Libero*
      - l’utente selezionato non risponde o rifiuta la chiamata
         - se l’utente ha risposto, la linea si pone nello stato *Estesa*
         - rilasciare l’utente selezionato cliccando sul pulsante **Ril.Ch.ato** o premendo il tasto **Ctrl+Shift+F3** o **Asterisco [Tn]**
         - l’indicatore **Escl. Ch.nte** si spegne e la linea si pone nello stato *Risposta*
         - l’operatore è nuovamente in conversazione con il chiamante



Ritorno all’operatore di chiamata non risposta
==============================================

Ritorno all’operatore in ambiente TVOX
======================================

Attesa in catena (Solo per Nortel)
==================================

Chiamata ad un numero interno o esterno
=======================================

..
    Chiamata in conferenza
    ======================

Inclusione (Solo per Nortel)
============================

xxx

.. .. image:: /images/TCONSOLE/UTENTE/CONSOLE/info.png
