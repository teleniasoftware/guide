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

Esempio di configurazione:

.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/BPM/BLOCCHETTI/digitgateway_es.png


**Campi configurabili**

- **Messaggio audio**: Il messaggio vocale da riprodurre è selezionato tra quelli definiti nel menù TVox -> Messaggi vocali.
- **Tempo di attesa**: Indica il tempo massimo di attesa.
- **Numero di tentativi permessi**: Numero massimo di ripetizioni consentite per il blocchetto.
- **Timeout - file audio da riprodurre**: Eventuale messaggio da riprodurre a fronte della scadenza del Tempo di attesa.
- **Azione non valida - File audio da riprodurre**: Eventuale messaggio da riprodurre a fronte di una scelta errata.
- **Tentativi esauriti - File audio da riprodurre**: Eventuale messaggio da riprodurre a fronte di tentativi esauriti
- 

.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/BPM/BLOCCHETTI/digitgateway_config.png
