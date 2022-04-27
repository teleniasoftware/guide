.. _Tasti ICI:

==============================================
Tasti ICI (solo per Nortel CIU o Nortel M2250)
==============================================

Le informazioni relative alle etichette associate ai dieci tasti ICI della console sono contenute nel file di configurazione *\[INSTALLDIR\]\\TConsole.ini* ([1]_). Ogni record è costituito da un codice (*ICI*) che corrisponde al numero del tasto ICI (la numerazione parte da zero) e da una descrizione. Per modificare la descrizione da riportare sulla console va modificato il secondo campo in corrispondenza della ICI considerata.

.. code-block:: ini

    [ICI]
    ; 	Key=Desc,Desc_IPO+,Braille_short,Braille_long,Sintesi,
    0=Esterna,ES,ICI1,Ch Esterna,Chiamata Esterna,
    2=Pickup,PK,ICI3,ICI3,ICI3,
    4=Ritorno,RT,ICI5,ICI5,ICI5,
    5=Interna,IN,ICI6, Ch Interna,Chiamata Interna,
    6=Entrante,EN,ICI7,Ch Entrante,Chiamata Entrante,

Nell'esempio riportato, nella riga 0 la dicitura:

.. code-block:: ini

    0=Esterna,ES,ICI1,Ch Esterna,Chiamata Esterna,

indica rispettivamente:

- numero ordinale (*Key*) del tasto ICI: *0* (primo tasto ICI **in alto**)
- stringa (*Desc*) presentata in vista Normale: *Esterna*
- stringa (*Desc_IPO*) presentata in vista IPO e IPO PLUS: *ES*
- stringa breve (*Braille_short*) presentata sulla barra Braille: *ICI1*
- stringa lunga (*Braille_long*) presentata sulla Barra Braille: *Ch Esterna*
- stringa letta (*Sintesi*) dalla Sintesi Vocale: *Chiamata Esterna*

.. rubric:: Note

.. [1] valore di default di *\[INSTALLDIR\]*: |tconsole_default_installdir|