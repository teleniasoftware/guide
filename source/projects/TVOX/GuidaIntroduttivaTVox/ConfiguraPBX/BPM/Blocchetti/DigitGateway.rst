Digit Gateway
======================

Il blocchetto \"Digit Gateway\" riproduce un messaggio vocale interrompibile, per riceve un digit. In base alla scelta (digit da 0 a 9 oppure # o *) possono essere impostati diversi blocchi.
E' presente inoltre un'ulteriore scelta ("unmatch") che permette di precorrere una strada differente se la scelta non è valida.

.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/BPM/BLOCCHETTI/digitgateway.png

.. important::  **Scelta non valida:** Perchè la scelta non sia valida deve verificarsi una delle seguenti condizioni: 
    - Digit non disponibile (es. utente digita 5 quando le scelte possibili sono 1 o 2)
    - Timeout scaduto (es. timeout 5s e utente non digita nulla per 5s)

E' possibile impostare un numero di tentativi permessi in modo che l'utente possa riprovare.
Nel caso in cui i tentativi non siano scaduti viene ripetuto il blocchetto decrementando i tentativi disponibili.
Una volta che non sono presenti più tentativi viene intrapresa la strada "unmatch".
Per ogni caso di errore è possibile impostare un audio facoltativo che viene riprodotto al verificarsi dell'errore.

Esempio di configrazione:

.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/BPM/BLOCCHETTI/digitgateway_es.png

.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/BPM/BLOCCHETTI/digitgateway_config.png

**Campi configurabili**

- **Messaggio audio**: elenco a discesa nella quale è possibile selezionare uno dei Servizi configurati su OCC
- **Tempo di attesa**:
- **Numero di tentativi permessi**:
- **Timeout - file audio da riprodurre**:
- **Azione non valida - File audio da riprodurre**:
- **Tentativi esauriti - File audio da riprodurre**: