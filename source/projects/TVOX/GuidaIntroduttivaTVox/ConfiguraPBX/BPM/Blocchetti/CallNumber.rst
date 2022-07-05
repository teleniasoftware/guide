Call Number
======================

Il blocchetto \"Call Number\" permette di effettuare una chiamata verso un numero.

.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/BPM/BLOCCHETTI/callnumber.png

.. important:: Questo blocchetto può avere più frecce con i seguenti valori, per gestire gli eventi della chiamata:

    - **noanswer** : nessuna risposta da parte del chiamato
    - **answer** : la chiamata ha ricevuto una risposta
    - **cancel** : la chiamata è stata rifiutata
    - **busy** : il numero chiamato è occupato
    - **congestion** : le linee sono sature e non si ha disponibilità telefonica
    - **chanunavail** : il canale telefonico non è disponibile 

.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/BPM/BLOCCHETTI/callnumber_config.png

**Campi configurabili**

- **Numero telefonico**: numero telefonico da chiamare; deve essere indicato il numero comprensivo di codice di accesso (se configurato)
- **Tempo di ring**: tempo massimo di ring espresso in secondi
- **Tentativi**: numero massimo di tentativi in attesa della risposta del numero chiamato, dopo il quale si va allo passo successivo
- **Abilitazione**: abilitazione da utilizzare per la chiamata in uscita
- **Registrazione della chiamata**: abilita/disabilita la registrazione della chiamata