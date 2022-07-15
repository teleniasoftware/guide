Get Digits
======================

Il blocchetto \"Get Digits\" viene utilizzato per poter ricevere, all'interno di un processo, una serie di digit (da 0 a 9) terminata dal tasto # o dal numero massimo raggiunto. 


.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/BPM/BLOCCHETTI/getdigit.png

**Campi configurabili**

- **Messaggio audio**: Il messaggio vocale da riprodurre è selezionato tra quelli definiti nel menù TVox -> Messaggi vocali. Il messaggio audio è interrompibile
- **numero di cifre**: Indica il numero massimo di digit che sono accettabili nel nodo corrente
- **Nome variabile**: Indica il nome della variabile che conterrà i digit inseriti
- **Tempo di attesa**: Indica il tempo massimo di attesa.
- **Numero di tentativi permessi**: Numero massimo di ripetizioni consentite per il blocchetto.
- **Timeout - file audio da riprodurre**: Eventuale messaggio da riprodurre a fronte della scadenza del Tempo di attesa.
- **Tentativi esauriti - File audio da riprodurre**: Eventuale messaggio da riprodurre a fronte di tentativi esauriti
  

.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/BPM/BLOCCHETTI/getdigit_config.png


