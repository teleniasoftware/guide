.. _Vista IPO:

=========
Vista IPO
=========

Nella vista in modalità IPO, per facilitare la lettura da parte dell’operatore, la finestra principale di TConsole è stata sdoppiata in due finestre distinte, entrambe visualizzate a tutto schermo, facilmente commutabili da una all’altra:

- finestra Console
- finestra Rubrica (Interna od Esterna)

Per questo motivo i contesti disponibili sono solamente Rubrica (*F3*), detta anche Rubrica Esterna e, opzionalmente, Rubrica Interna (*F2*).

Il passaggio da una finestra all’altra avviene nelle seguenti modalità:

- dalla finestra Console alla finestra Rubrica mediante i tasti *F2* (Rubrica Interna) o *F3* (Rubrica Esterna)
- dalla finestra Rubrica alla finestra Console con il tasto *F4* (per entrambi i tipi  di rubrica)

.. important:: Per quanto riguarda la Rubrica le logiche descritte di seguito fanno sempre riferimento alla Rubrica *F3*, detta anche Rubrica Esterna. La Rubrica Interna *F2* segue le stesse logiche di funzionamento.

Pannelli della Console
======================

Tutte le funzionalità descritte nella :ref:`Vista Normale` della parte di controllo della console/telefono sono facilmente riscontrabili anche in questa vista ed ugualmente disponibili, anche se indicatori e pannelli sono stati riorganizzati al fine di dare maggiore leggibilità all’operatore.
Vengono di seguito riportate le sostanziali differenze rispetto alla Vista Normale.

.. image:: /images/TCONSOLE/UTENTE/VISTAIPO/vistaIPO.png

Rubrica
-------

Questo è un pannello riepilogativo, nel quale viene riportato solamente il nominativo dell’ultima ricerca effettuata o, se è abilitato il lookup in rubrica (vedi :ref:`ABILITA_POPUP`), il nominativo associato al CLID della chiamata entrante corrente.

.. image:: /images/TCONSOLE/UTENTE/VISTAIPO/pannelloRubricaIPO.png

Stato
-----

In questo pannello sono riportate data e ora corrente del PC; tale informazione è comunque disponibile nella Barra di stato dell’applicazione, ma in questa maniera risulta più accessibile ad un operatore ipovedente.

.. image:: /images/TCONSOLE/UTENTE/VISTAIPO/pannelloStatoIPO.png

Rubrica
=======

.. image:: /images/TCONSOLE/UTENTE/VISTAIPO/RubricaIPO.png

Il contesto Rubrica in modalità IPO si compone delle seguenti parti:

- campi di selezione per la ricerca dei nominativi
- dettaglio dei nominativi trovati
- quantità di nominativi ricercati
- tasto di ricerca (da tastiera tasto *[Invio]* **non del tastierino numerico**)
- tasto di ricerca alternativa (da tastiera *F11* - vedi parametro :ref:`RIC_ALT`)
- tasto per la composizione automatica dei numeri telefonici (da tastiera *F12* - vedi parametro :ref:`F12`)
- funzioni per la manutenzione della Rubrica (inserimento/modifica dei contatti o impostazione dei colori)

Al contrario della Vista Normale, in questo caso **non** è presente la sezione **MASTER** che riepiloga i risultati della ricerca: i nominativi trovati, uno alla volta, vengono visualizzati subito nel dettaglio e si possono scorrere con le freccette *Su*/*Giù*.

Non è inoltre possibile modificare un contatto tramite clic con il tasto destro del mouse.

Tutte le funzionalità richiamabili tramite combinazione di tasti descritte nella :ref:`Vista Normale` rimangono disponibili e invariate:

- ricerca dei nominativi
- composizione automatica dei numeri ad essi associati
- inserimento/modifica dei contatti

.. important:: Tutti i parametri per la configurazione dei campi di ricerca e di visualizzazione (etichetta visualizzata e ordine di presentazione) sono descritti in :ref:`RubInt.ini e RubEst.ini`.