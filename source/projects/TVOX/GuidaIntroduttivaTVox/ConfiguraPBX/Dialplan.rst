========
Dialplan
========

In questa sezione verranno illustrate le configurazioni inerenti al *Dialplan* per poter definire gli instradamenti VOIP in uscita ed in ingresso al TVox.
Si andranno a definire:

- **Regiole di uscita**
- **Abilitazioni**
- **Filtri uscenti**
- **Regole d'ingresso**


Regole di uscita
=================

Le regole di uscita definiscono le logiche di instradamento delle chiamate uscenti.
In altre parole la regola di uscita associa ad una predefinita numerazione l'impegno di uno o più trunk OUTBOUND. 


Abilitazioni
============

Le Abilitazioni sono dei raggruppamenti di regole di uscita organizzati in modo da consentire alle risorse TVox Omnichannel Contact Center (utenti, agenti, etc..) una prefissata tipologia di traffico telefonico OUTBOUND. Il TVox Omnichannel Contact Center prevede un'abilitazione di default per la gestione automatica dei numeri di emergenza che per legge devono sempre essere accessibili da qualsiasi terminale telefonico.

.. important::  In ogni abilitazione creata il TVox Omnichannel Contact Center include quella relativa ai numeri di emergenza che sono definiti in maniera puntuale nell'omonima sezione. 


Filtri uscenti
==============

Il filtro uscente può essere associato solo ad utenti o ad agenti di Contact center e permette di definire un insieme di regole in modalità *Ammetti / Vieta * per configurare diversamente alcune numerazioni da quanto previsto dalle Abilitazioni.

Regole di ingresso
==================

Attraverso la configurazione delle regole di ingresso si definiscono le principali logiche di instradamento delle chiamate entranti.

La regola di ingresso associa le chiamate discriminate per numero chiamato (DNIS) e/o numero chiamante (CLID) ad una delle seguenti risorse TVox Omnichannel Contact Center:

- utente
- servizio
- numero di telefono (interno / esterno)
- casella FAX
- stanza di conferenza

Definendo le regole di ingresso posso quindi inoltrare il traffico telefonico entrante verso utenti (selezione passante), caselle FAX, stanze di conferenza e verso tutte le tipologie di servizi TVox Omnichannel Contact Center (IVR, di risposta e di Contact Center). E' inoltre possibile dirottare chiamate entranti verso numeri interni o esterni.

La regola di ingresso etichettata come **TRABOCCO** permette di gestire il traffico telefonico entrante NON associato ad alcuna regola di ingresso.

