.. _Tasti FLEX:

==========
Tasti FLEX
==========

Le informazioni relative alle etichette associate ai dieci tasti FLEX della console sono contenute nel file di configurazione *\[INSTALLDIR\]\\TConsole.ini* ([1]_). Ogni record è costituito da un codice (*Flex*) che corrisponde al numero del tasto FLEX (la numerazione parte da zero e dal primo FLEX in basso verso l’alto) e da una descrizione. Per modificare la descrizione da riportare sulla console va modificato il secondo campo in corrispondenza del tasto FLEX considerato.

Il numero da chiamare va inserito preceduto dal carattere *@* (chiocciola) e, se si tratta di un numero esterno, deve includere l’eventuale codice di impegno linea richiesto (vedi FLEX 1 nell’esempio seguente, in cui il codice di impegno linea è *0* e il numero esterno da chiamare è *0452224600*).

.. image:: /images/TCONSOLE/INSTALLAZIONE/CONFIGURAZIONE/tasti_FLEX.png

.. code-block:: ini

    [FLEX]
    ;	Key=Desc,Desc_IPO+,[<tipo>numero],
    0=,,,
    1=Telenia,TELN,@00452224600,
    2=,,,
    3=,,,
    4=,,,
    5=,,,
    6=,,,
    7=,,,
    8=NOTTE/GIOR,NOTTE,@*502330,
    9=,,,

Nell'esempio riportato, nella riga 1 la dicitura:

.. code-block:: ini

    1=Telenia,TELN,@00452224600,

indica rispettivamente:

- numero ordinale (*Key*) del tasto FLEX: *1* (secondo tasto ICI **dal basso**)
- stringa (*Desc*) presentata **in vista Normale e in vista IPO**: *Telenia*
- stringa (*Desc_IPO+*) presentata **solo in vista IPO PLUS**: *TELN*
- numero da chiamare, comprensivo di codice di impegno linea (*0*): *00452224600*

.. important ::
    Nel caso di configurazione TConsole TVOX (vedi :ref:`Parametri TVox`) è importante inserire in un tasto FLEX il numero da chiamare per commutare il servizio da "Notte" al contesto "Attivo" ("Giorno"), e dal contesto "Attivo" a "Notte". In questo caso (per dettagli si rimanda alla guida |tvox_pbx|) il numero da chiamare è nel formato: *codice di servizio TVox "Servizio in stato Notte"* ([2]_) seguito dal numero associato al servizio.

    Pertanto, con riferimento all’esempio indicato in precedenza (vedi FLEX 8):

    - codice di servizio TVox per “Servizio in stato Notte”: *\ *50*
    - numero associato al servizio di tipo Posto Operatore: *2330*
    - numero da chiamare per mettere il servizio in stato Notte/Attivo: *\ *502330*
    - contenuto del FLEX: *8=NOTTE/GIOR,NOTTE,@*502330,*

.. tip ::
    Sempre nella configurazione TConsole TVOX, i FLEX da 0 a 5 non sono visibili poiché sono coperti dai pulsanti utilizzati per le funzioni TQM ("Login", "Logout" etc.), ma rimangono sempre attivabili tramite le combinazioni di tasti predefinite (*SHIFT+F1*, *SHIFT+F2* etc. - vedi :ref:`Flex`).

.. rubric:: Note

.. [1] valore di default di *\[INSTALLDIR\]*: |tconsole_default_installdir|

.. [2] pagina *Impostazioni | Avanzate | Canale Telefonico | Codici di servizio* (valore di default: *\*50*). Il codice di servizio deve inoltre essere **abilitato** nel dialplan generale di |tvox_pbx|