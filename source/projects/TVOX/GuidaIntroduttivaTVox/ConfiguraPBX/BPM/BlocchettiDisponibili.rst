Blocchetti disponibili
======================

Il BPM mette a disposizione le seguenti tipologie di blocchetto:

.. toctree::
    :maxdepth: 2

    ./Blocchetti/StartStop 
    ./Blocchetti/Play 
    ./Blocchetti/CallNumber 
    ./Blocchetti/CloseCall 
    ./Blocchetti/LoadService 
    ./Blocchetti/LoadServiceADV
    ./Blocchetti/DigitGateway
    ./Blocchetti/GetDigits
    ./Blocchetti/PlayDigits
    ./Blocchetti/StartRecording
    ./Blocchetti/StopRecording


+--------------------------+---------------------------------------------------------------------------------------------------------+
| Blocchetto               | Descrizione                                                                                             | 
+==========================+=========================================================================================================+ 
| Text to Speech           | riproduce un testo facendo text-recognition                                                             | 
+--------------------------+---------------------------------------------------------------------------------------------------------+
| Condition gateway        | valuta una condizione tipo if e segue frecce diverse in base all'esito vero o falso                     | 
+--------------------------+---------------------------------------------------------------------------------------------------------+
| GET Request              | interroga un servizio esterno disponibile in HTTP                                                       | 
+--------------------------+---------------------------------------------------------------------------------------------------------+
| Set variable value       | calcola un valore e lo memorizza in una variabile                                                       | 
+--------------------------+---------------------------------------------------------------------------------------------------------+
| Free text ASR            | ascolta la voce dell'utente e trascrive quanto detto in forma testuale                                  | 
+--------------------------+---------------------------------------------------------------------------------------------------------+
| Switch                   | osserva il valore di una variabile e segue la freccia etichettata con quel valore                       | 
+--------------------------+---------------------------------------------------------------------------------------------------------+
| SQL Database query       | esegue una query SQL su un database e ne salva il risultato in una variabile                            | 
+--------------------------+---------------------------------------------------------------------------------------------------------+
| Calendar check           | controlla un calendario tra quelli configurati sul TVOX                                                 | 
+--------------------------+---------------------------------------------------------------------------------------------------------+
| Transfer to Voicemail    | carica la casella vocale                                                                                | 
+--------------------------+---------------------------------------------------------------------------------------------------------+
| Send Alarm               | invia un allarme con testo e priorità impostati                                                         | 
+--------------------------+---------------------------------------------------------------------------------------------------------+
| Custom PHP code          | esegue un codice scritto custom in PHP per il blocchetto                                                | 
+--------------------------+---------------------------------------------------------------------------------------------------------+
| Check service activation | controlla se un servizio è o meno attivo                                                                | 
+--------------------------+---------------------------------------------------------------------------------------------------------+
| Access call variable     | fornisce accesso in lettura e scrittura alle variabili di chiamata, mappandole a variabili locali       | 
+--------------------------+---------------------------------------------------------------------------------------------------------+