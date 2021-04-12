==========================================
Performance Tuning
==========================================


Nella sezione Performance Tuning è possibile effettuare dei settings del sistema di support al fine di migliorarne le prestazioni.
I valori devono essere impostati sulla base delle caratteristiche HW della macchina support e dovranno essere effettuati seguendo gli help sui singoli parametri.
Il salvataggio dei parametri comporta il riavvio del servizio support con conseguente perdita della funzionalità support per alcuni secondi.

.. warning::  Impostazioni errate di questi valori possono portare ad elevato utilizzo delle CPU con conseguenti malfunzionamenti del sistema support

----------------------------

Istanze API support
============================
    Indica il numero di istanze contemporanee delle API support.
    Valore non settato indica che il numero delle istanze viene regolato automaticamente sulla base del dimensionamento macchina (default).
    E” possibile comunque forzare il numero delle istanze.
    Un impostazione diversa dal default è consigliata quando si hanno delle risposte lente da parte dei client nella fase di gestione dei ticket.
    Il valore da assegnare in questo caso è da calcolare sulla base del dimensionamento della macchina support seguendo la seguente formula:
    
    "**Max Istanze contemporanee API support**" = "**Numero di CPU del server Support**" / **4**
    
    Esempio: Se si ha un server support con 16 CPU si può arrivare ad impostare un valore massimo di 4.
    
    .. warning::  Impostando valori più elevati rispetto a quelli indicati dalla formula si potrebbe incorrere in malfunzionamenti o anomalie del server support


----------------------------

Job Worker support instances
============================

    Indica il numero di istanze contemporanee di elaborazione dei Job Support.
    Se il parametro è vuoto significa che il numero delle istanze viene regolato automaticamente sulla base del dimensionamento macchina (default).
    Solitamente questo valore non deve essere cambiato. E' possibile comunque forzare il numero di Job Worker impostando un valore numerico.
    Il valore da assegnare in questo caso è da calcolare sulla base del dimensionamento della macchina support seguendo la seguente formula:
    
    "**Max Istanze Job Worker support**" = "**Numero di CPU del server Support**" / **5**
    
    Esempio: Se si ha un server support con 16 CPU si può arrivare ad impostare un valore massimo di 3.
    
    .. warning:: Impostando valori più elevati rispetto a quelli indicati dalla formula si potrebbe incorrere in malfunzionamenti o anomalie del server support