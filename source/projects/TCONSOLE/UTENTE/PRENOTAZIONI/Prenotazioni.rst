=============================
Prenotazioni (altri contesti)
=============================

.. _Prenotazioni VIP:

Prenotazioni V.I.P. (solo per Nortel)
=====================================

Il modulo V.I.P. permette di gestire un particolare gruppo di utenti privilegiati. Tramite questa applicazione si potranno inserire i dati di quei particolari utenti della centrale che hanno esigenza di chiamare il Posto Operatore immediatamente, evitando eventuali code di attesa.

Tali utenti, chiamando i numeri dei risponditori automatici presenti nella Centrale, verranno evasi immediatamente da un Posto Operatore.

.. important::
    La funzionalità è disponibile **solo con centrale Nortel** (parametro *TYPE=NORTEL_M1250* o *NORTEL_M2250* o *NORTEL_CIU* nel file :ref:`TConsole.ini`) e richiede la presenza di un server TSAM.

    Per la configurazione lato TSAM si rimanda al manuale di installazione TSAM.

..
    Configurazione lato TSAM
    ------------------------

Gestione lato TConsole
----------------------

.. important:: La funzionalità è disponibile solo nella :ref:`Vista Normale`.

.. Per abilitare TConsole alla gestione V.I.P. è necessario aver installato il servizio :ref:`TConsoleServer` (vedi :ref:`Chiamate VIP`) ed aver impostato nel file *tabparam* della postazione il parametro *ABILITA_PMI=SI* (vedi :ref:`ABILITA_PMI`), oltre che l'IP del TConsoleServer (vedi :ref:`TCONSOLE_SERVER`).

Per abilitare TConsole alla gestione V.I.P. è necessario aver installato il servizio :ref:`TConsoleServer` (vedi :ref:`Chiamate VIP`) ed aver opportunamente impostato nel file *tabparam* della postazione TConsole i seguenti parametri:

- *ABILITA_PMI=SI* (vedi :ref:`ABILITA_PMI`)
- TCONSOLE_SERVER con l'IP del TConsoleServer (vedi :ref:`TCONSOLE_SERVER`).

Una volta lanciato l’applicativo TConsole apparirà il form sottostante con la finestra *Prenotazioni VIP* in primo piano, finestra che può essere spostata, ridimensionata e messa in trasparenza.

.. image:: /images/TCONSOLE/UTENTE/PRENOTAZIONI/ChiamateVIP.png

La finestra *Prenotazioni VIP* si si sovrappone alla solita finestra di gestione della console, e riporta le informazioni relative alla richiesta VIP:

- indicatore del numero di chiamate in coda VIP
- **PO_ID**: numero identificativo del PO ([#]_) che sta rispondendo alla chiamata VIP: il valore è vuoto se nessun operatore ha ancora risposto alla chiamata VIP
- **Priorità**: livello di priorità dell’utente VIP (*1*\ =priorità massima)
- **Interno**: interno che ha richiesto la chiamata VIP
- **Descrizione**: nominativo che ha richiesto la chiamata VIP

Sono presenti inoltre due pulsanti:

- pulsante di risposta alla chiamata VIP: di norma disabilitato, si abilita solo all'arrivo di una chiamata VIP
- pulsante per disattivare/attivare la segnalazione sonora delle chiamate VIP in attesa di risposta

All’arrivo di una chiamata V.I.P. viene emesso dal PC un suono ripetitivo e l’opportuno indicatore del numero di chiamate in coda si incrementa di una unità.

.. image:: /images/TCONSOLE/UTENTE/PRENOTAZIONI/ChiamateVIP-prenotazioni.png

Per rispondere ad una chiamata V.I.P. cliccare con il tasto di pickup posto a destra dell’indicatore delle chiamate in coda. A questo punto il PO è in comunicazione con l’utente privilegiato e può gestire la chiamata secondo le normali procedure.

Al termine della chiamata, per chiuderne definitivamente la gestione, verrà richiesto di confermare la cancellazione dell’istanza:

- premendo *Sì* il record relativo alla chiamata appena gestita verrà eliminato, e la chiamata sparirà dalla coda
- premendo *No* il record relativo a tale chiamata rimarrà visualizzato, mantenendo la chiamata in coda, e potrà essere preso in carico nuovamente da altri operatori

.. rubric:: Note

.. [#] numero identificativo della postazione: significativo nel caso di postazioni multiple per poterle distinguere (vedi parametro :ref:`ID` nel file *TConsole.ini*)