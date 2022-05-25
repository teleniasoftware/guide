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


|br|


Ritorno all’operatore di chiamata non risposta
==============================================

Nel caso di inoltro di una chiamata ad un utente interno, se l’utente chiamato non risponde entro un certo tempo (impostato sul PBX), la chiamata può ritornare all’operatore che l’ha inoltrata.

In questo caso:

- La console emette un tono di avviso
- l’opportuno indicatore **ICI** si attiva
- la linea si pone nello stato *Ritorno Lib*
- Per poter riprendere la chiamata:
   - cliccare sul pulsante **ICI** opportuno, oppure
   - cliccare sul pulsante **Linea** evidenziato, oppure
   - premere il corrispondente tasto **Ctrl + 0 .. 5 [Tn]**, oppure
   - premere il tasto **Più [Tn]**
- la linea si pone nello stato **Dest. Lib**, l’indicatore **Escl.Ch.ato** si accende e l’operatore torna in conversazione con l’utente chiamante
- rilasciare l’utente chiamato cliccando sul pulsante **Ril.Ch.ato** o premendo il tasto **Ctrl+Shift+F3** o **Asterisco [Tn]**
- la linea si pone nello stato *Risposta*


|br|




Ritorno all’operatore in ambiente TVOX
======================================

Nel caso di Utilizzo di TConsole in ambiente TVOX è possibile avere le seguenti tipologie di ritorno:

- **Ritorno per Non Rosposta**: Avviene quando un utente TVOX ha configurato nella sezione *Mobilità* un ritorno a Capolinea sul Servizio PO per *Attesa Superata*
- **Ritorno per Occupato**: Avviene quando un utente TVOX ha configurato nella sezione *Mobilità* un ritorno a Capolinea sul Servizio PO per *Interno Occupato*
- **Ritorno per Deviato**: Avviene quando un utente TVOX ha configurato nella sezione *Mobilità* un ritorno a Capolinea sul Servizio PO per *Sempre*
- **Ritorno Irregolare**: Avviene quando un utente TVOX ha configurato nella sezione *Mobilità* un ritorno a Capolinea sul Servizio PO *Interno non Attivo*
- **Ritorno Generico**: Avviene quando si ha un ritorno di tipo sconosciuto, oppure quando si ha un ritorno da un servizio, oppure quando viene effettuata la deviazione a PO direttamente sul telefono e non dalla sezione Mobilità di TVOX

Nel caso di ritorno al momento della risposta, la linea 1 del display del TConsole presenta le seguenti informazioni:

<CLID> <DNIS>-<REDIRECT FROM DN>


|br|




Attesa in catena (Solo per Nortel)
==================================

Dato il caso di un utente chiamante che desidera parlare sequenzialmente con più utenti, è possibile inoltrate la chiamata ad ogni singolo utente in modo tale che, quando una conversazione termina, la chiamata ritorni automaticamente all’operatore che potrà così inoltrarla all’utente successivo.

Per poter eseguire questa operazione:

- rispondere alla chiamata con la modalità già descritta

Eseguire l'inoltro della chiamata:

- selezionare il numero telefonico richiesto, utilizzando la tastiera numerica
- durante la selezione, l’indicatore **Escl. Ch.nte** si accende e il chiamante viene messo automaticamente in attesa
- al tono di libero la linea si pone nello stato *Dest.Lib.*
- l’operatore inoltra la chiamata senza consultazione premendo consecutivamente il pulsante **Attesa** o il tasto **Meno [Tn]** ed il pulsante **Rilascio** o il tasto **Invio [Tn]**
- la linea si pone nello stato *Attesa trasf.*
- alla risposta dell’utente chiamato la linea si pone nello stato *Attesa in Catena*
- quando l’utente chiamato chiude la conversazione, la linea si pone nello stato *In attesa*
- riprendere la chiamata:
   - cliccando sul pulsante **Linea** della linea nello stato *In Attesa*, oppure
   - premendo il corrispondente tasto **Ctrl + 0 .. 5 [Tn]**, oppure
   - premendo il tasto **Più [Tn]**
- la linea si pone nello stato *Risposta*
- è possibile terminare la chiamata con il pulsante **Rilascio** o il tasto **Invio [Tn]** oppure inoltrare la chiamata nella modalità più opportuna
  
Se l’utente chiamato non risponde:

- la console emette un tono di avviso
- la chiamata ritorna all’operatore
- la linea si pone nello stato *Attesa Dest.Lib.*
- è possibile gestire la chiamata come descritto nella modalità *Ritorno all’operatore di chiamata non risposta* descritta in precedenza.

|br|


Chiamata ad un numero interno o esterno
=======================================

L’operatore può effettuare una chiamata a qualsiasi numero interno o esterno al sistema telefonico; nel caso di numero esterno, è necessario conoscere il codice di accesso alle linee esterne (tipicamente 0).

- Impegnare una linea
   - cliccando sul pulsante **Linea** di una linea nello stato *Libero*, oppure
   - premendo il corrispondente tasto **Ctrl + 0 .. 5 [Tn]**, oppure
   - premendo il tasto **Più [Tn]**
- la linea si pone nello stato *Impegno*
- per chiamate esterne, digitare il codice di accesso (si sente il tono di centrale)
- selezionare il numero desiderato cliccando sui pulsanti del Keypad o premendo i tasti numerici del tastierino
- se l’utente è libero:
   - l’operatore sente il tono di libero
   - la linea si pone nello stato *In Chiamata*
   - alla risposta dell’utente la linea si pone nello stato *Risposta*
- se l’utente è occupato
   - l’operatore sente il tono di occupato
   - la linea si pone nello stato *Occupato*
- per terminare la chiamata cliccare sul pulsante **Rilascio** o premere il tasto **Invio [Tn]**.


|br|



Chiamata in conferenza
======================

L’operatore può effettuare, su richiesta di un utente interno o esterno, una conferenza con un massimo di sei utenti, operatore incluso. E’ possibile utilizzare un massimo di due giunzioni.

**Attivazione della conferenza**

.. note:: Si presuppone di avere già una chiamata in corso (entrante o uscente) corrispondente al primo partecipante alla conferenza

- selezionare il numero telefonico del partecipante successivo
- durante la selezione, l’indicatore **Escl. Ch.nte** si accende; gli altri partecipanti alla conferenza vengono messi automaticamente in attesa
- al tono di libero la linea si pone nello stato *Dest.Lib.*
- alla risposta del numero selezionato, la linea si pone nello stato *Estesa*
- per includere l’utente nella conferenza, cliccare sul pulsante **Conferenza** o premere il tasto **Ctrl+Shift+F1**
- l’indicatore **Escl. Ch.nte** si spegne e la linea si pone nello stato *Risposta*

Ripetere i passi elencati per ogni partecipante alla conferenza.

**Disattivazione temporanea**

E’ possibile abbandonare temporaneamente la conferenza, per esempio, per gestire altre chiamate. 

- cliccare sul pulsante **Rilascio** o premere il tasto **Invio [Tn]**
- la linea si pone nello stato *In Attesa*
- i partecipanti alla conferenza continuano ad essere in collegamento fra loro
- l’operatore può elaborare altre chiamate su altre linee.

**Riattivazione della conferenza**

- cliccando sul pulsante **Linea** della linea nello stato *In Attesa*, oppure
- premendo il corrispondente **tasto Ctrl + 0 .. 5 [Tn]**, oppure
- premendo il tasto **Più [Tn]**

**Rilascio della conferenza da parte del PO**

- cliccare sul pulsante **Ril.Ch.nte** o premere il tasto **Ctrl+Shift+F3**
- cliccare sul pulsante **Rilascio**o premere il tasto **Invio [Tn]**
- la linea si pone nello stato *Libero*

|br|





Inclusione (Solo per Nortel)
============================

Questa prestazione, opportunamente configurata sul PBX, consente di comunicare con utenti che risultano occupati in un’altra conversazione.

Al momento dell’inoltro di una chiamata ad un interno che risulta occupato:

- la linea si pone nello stato *Dest.Occ.*
- cliccare sul pulsante **Flex** che riporta la descrizione **Inclusione** o premere il relativo tasto **Shift+Fn**
- l’indicatore **Inclusione** si accende e la linea si pone nello stato *Estesa*
- l’operatore è in conferenza con l’utente chiamato ed il suo interlocutore

L’utente accetta la chiamata:

- quando l’interlocutore riaggancia l’indicatore **Inclusione** si spegne
- inoltrare la chiamata cliccando sul pulsante **Rilascio** o premendo il tasto **Invio [Tn]**
  
Se l’utente rifiuta la chiamata:

- rilasciare la conferenza cliccando sul pulsante **Ril.Ch.ato** o premendo il tasto **Ctrl+Shift+F3** o **Asterisco [Tn]**
- gli indicatori **Inclusione** e **Escl. Ch.nte** si spengono e la linea si pone nello stato *Risposta*
- l’operatore è nuovamente in conversazione con il chiamante.
  

.. note:: Premendo due volte Inclusione si va in comunicazione solo con il numero chiamato (e non con il suo interlocutore)







.. .. image:: /images/TCONSOLE/UTENTE/CONSOLE/info.png
