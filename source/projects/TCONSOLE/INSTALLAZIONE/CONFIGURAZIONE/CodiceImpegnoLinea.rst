.. _Codice Impegno Linea:

====================
Codice Impegno Linea
====================

Per effettuare la chiamata con il codice di impegno linea corretto occorre aver configurato correttamente:

- tabella range DN (*rangedn*) definendo l’intervallo di numerazione interna della centrale
- parametro *ACOD_RUB_EXT* nel file *\[INSTALLDIR\]\\config\\tabparam* ([1]_) inserendo il codice di impegno linea (valore di default: *0*)
- la definizione della tabella delle reti (*tabrete*) con i relativi codici di impegno linea
- la definizione del tipo di rete nei dettagli contatto di Rubrica Esterna (F3)

.. important :: Le tabelle *rangedn* e *tabrete* si trovano nel database *tgest* di TConsole.

Per la chiamata effettuata da Rubrica Interna o Esterna verso il numero **principale** di un contatto (F12) viene utilizzato il codice di impegno linea (parametro *pref_rete*) definito nella tabella delle reti (*tabrete*) e associato alla rete specificata per il contatto da chiamare. Di default, in *tabrete* sono già presenti la rete **Interna** (nessun codice di impegno) e la rete **Esterna** (Pubblica) (codice di impegno: *0*).

Per la chiamata effettuata da Rubrica Interna o Esterna verso uno dei numeri **alternativi** di un contatto (Shift+F12, Ctrl+F12, Alt+F12), da Post-IT (F9) o dall’elenco delle chiamate entranti ricevute (Ctrl+E), se il numero da chiamare **non** è compreso nel Range DN (tabella *rangedn*), viene utilizzato il codice di impegno linea definito nel parametro *ACOD_RUB_EXT*. Il range DN di default è *0-999999*.

Per la chiamata effettuata da tastierino numerico (Keypad) o dall’elenco delle chiamate uscenti effettuate (Ctrl+U) non viene **mai** anteposto nessun codice di impegno linea per cui, se è necessario, occorre digitarlo manualmente.

.. important :: Per Nortel alle chiamate effettuate dall’elenco delle chiamate uscenti (Ctrl+U) viene anteposto l’*ACOD_RUB_EXT* come per il Post-IT.

.. tip ::
    L'installazione TConsole di default prevede l'utilizzo del codice di impegno linea *0*. **Se nella centrale non è previsto alcun codice di impegno linea per le chiamate outbound**, è sufficiente:
    
    - in *\[INSTALLDIR\]\\config\\tabparam* ([1]_) rimuovere lo *0* impostando il parametro *ACOD_RUB_EXT* al valore vuoto (o trattino):
     .. code-block:: ini

        rubrica        ACOD_RUB_EXT         -

    - nella tabella delle reti (*tabrete*) impostare a *NULL* il parametro *pref_rete* per la rete **Esterna** (Pubblica):
     .. image:: /images/TCONSOLE/INSTALLAZIONE/CONFIGURAZIONE/tabrete_pref_rete_NULL.png

    - non è necessario modificare il range DN di default *0-999999* (tabella *rangedn*)

.. rubric:: Note

.. [1] valore di default di *\[INSTALLDIR\]*: |tconsole_default_installdir|