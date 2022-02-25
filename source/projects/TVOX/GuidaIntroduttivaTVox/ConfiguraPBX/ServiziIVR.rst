===========
BPM
===========

Il **Business Process Manager** è uno strumento che permette di creare processi aziendali attraverso un'interfaccia grafica. 
L'ambiente di progettazione si compone di diversi blocchetti (definiti anche task) che possono essere posizionati in una mappa e collegati fra loro da delle frecce. 

La configurazione di un blocchetto permette di definire i parametri di esecuzione della funzione che questo implementa, 
mentre il collegamento delle frecce permette di definire il flusso logico del processo. 

Il **BPM** permette la configurazione di processi legati al canale telefonico, definendo quindi *IVR, VOICEBOT* o sistemi simili.

.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/BPM/BPM.PNG

Creazione processi
==================

Si accede da OCC andando nel menù *GESTIONE => Business Process*. E\' possibile scegliere se modificare un processo esistente, o crearne uno nuovo. 
Il processo di creazione propone un'interfaccia in cui vanno inserite informazioni generali relative al processo, e dettagli del servizio telefonico a cui questo sarà associato.


.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/BPM/BPM_DETTAGLIO.PNG


Una volta confermato il form, si visualizza l'interfaccia di progettazione del processo.

.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/BPM/BPM_INTERFACCIA.PNG

L'interfaccia si compone dei seguenti elementi:

- *Palette*: posizionata sulla sinistra, contiene i blocchetti (o meglio, le tipologie di blocchetto disponibili) e le funzionalità dell'editor
- *Area di progettazione*: ospita i blocchetti e le frecce della mappa
- *Pannello di configurazione*: compare quando si configura un blocchetto, ed è sostanzialmente un form di impostazioni
- *Tasti di salvataggio e validazione*: posizionati in alto a destra, permettono azioni verso il server

.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/BPM/BPM_ELEMENTI.PNG

Per posizionare un nuovo blocchetto, la tipologia scelta va trascinata dalla palette verso l'ambiente di progettazione. In alternativa si può fare click prima sull'icona del blocchetto scelto, e poi nel punto in cui lo si vuole creare. 
Per collegare due blocchetti tra loro, si può scegliere la freccia dal menù a comparsa che si visualizza facendo click sul primo blocchetto, e fare click poi sul blocchetto di destinazione. In alternativa, si può usare lo strumento freccia disponibile in palette.


Una volta posizionato un blocchetto, è possibile configurarlo. Per fare questo, si fa click con il tasto destro sopra al blocchetto. Compare un pannello di impostazioni sulla destra, il cui form si caratterizza per campi diversi in base ai parametri di configurazione che si possono definire per l'azione associata a quel blocchetto. Facendo click sul tasto di conferma, si impostano i valori inseriti, e compare una stringa di anteprima sul blocchetto, che ha la funzionalità di ricordare il più possibile di quanto sia stato configurato per quell'elemento, senza che sia necessario aprire di nuovo il pannello di configurazione per vedere quale sia l'azione svolta.

Regole e convenzioni dei processi
=================================

Di norma, ogni blocchetto può avere una singola freccia in uscita, e una o più frecce in ingresso. Questo perché, altrimenti, più frecce in uscita da un blocchetto darebbero vita ad una situazione ambigua in cui non è possibile determinare il prossimo step da eseguire. 


Ci sono tuttavia alcune eccezioni a questa regola, relative a blocchetti che di fatto "sdoppiano" il flusso definendo due (o più) possibili strade, che verranno percorse in corrispondenza di determinate condizioni. In questi casi, è necessario fare doppio click sulle frecce uscenti dal blocchetto,e digitare nel campo che compare il valore che si vuole associare a quella freccia. Nel dettaglio, si tratta dei seguenti blocchetti:
   
    - *Digit Gateway*: permette di seguire direzioni diverse in base al digit selezionato dall'utente. Le frecce devono chiamarsi come il digit che si vuole associare a quel ramo del processo.
    - *Condition Gateway*: permette di verificare una condizione (tipo if) e intraprendere due strade a seconda di esito vero o falso. Le due frecce uscenti devono chiamarsi true e false.
    - *Switch*: permette di osservare una variabile e intraprendere strade diverse in base al suo valore attuale. Le frecce si devono chiamare esattamente come il valore che si vuole causi l'esecuzione di quel ramo.

.. important:: **BEST PRACTICE:**  Ogni processo deve necessariamente iniziare con un blocchetto di tipo **start**, la cui icona è un cerchio sottile. Il blocchetto **stop**, rappresentato da un cerchio più spesso, indica il termine del processo, ed è preferibilmente presente in ogni mappa disegnata. 


Blocchetti disponibili
======================

Nella prima release, il BPM mette a disposizione le seguenti tipologie di blocchetto


+--------------------------+---------------------------------------------------------------------------------------------------------+
| Blocchetto               | Descrizione                                                                                             | 
+==========================+=========================================================================================================+
| Start                    | definisce l'inizio del processo                                                                         | 
+--------------------------+---------------------------------------------------------------------------------------------------------+
| Stop                     | definisce il termine del processo                                                                       | 
+--------------------------+---------------------------------------------------------------------------------------------------------+
| Play                     | riproduce un file audio                                                                                 | 
+--------------------------+---------------------------------------------------------------------------------------------------------+
| Transfer                 | gira la chiamata ad un numero specificato                                                               | 
+--------------------------+---------------------------------------------------------------------------------------------------------+
| Close call               | abbatte la chiamata                                                                                     | 
+--------------------------+---------------------------------------------------------------------------------------------------------+
| Load service             | carica un servizio di contact center                                                                    | 
+--------------------------+---------------------------------------------------------------------------------------------------------+
| Digit Gateway            | riproduce un file audio, poi riceve un digit e permette di seguire diverse frecce in base alla scelta   | 
+--------------------------+---------------------------------------------------------------------------------------------------------+
| Load Service advanced    | carica un servizio passando una serie di parametri di configurazione                                    | 
+--------------------------+---------------------------------------------------------------------------------------------------------+
| Get digits               | riceve una serie di digits terminata da # o dal raggiungimento di un limite massimo impostabile         | 
+--------------------------+---------------------------------------------------------------------------------------------------------+
| Play digits              | riproduce la serie di digits raccolta                                                                   | 
+--------------------------+---------------------------------------------------------------------------------------------------------+
| Start recording          | inizia la registrazione della chiamata                                                                  | 
+--------------------------+---------------------------------------------------------------------------------------------------------+
| Stop recording           | interrompe la registrazione della chiamata                                                              | 
+--------------------------+---------------------------------------------------------------------------------------------------------+
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

Validazione e salvataggio
=========================


Per salvare il diagramma, si fa click sul tasto salva in alto a destra. 
Il progetto viene esportato in un file e viene caricato sul server, con notifica di avvenuto upload. 

.. note:: Nonostante il diagramma si possa salvare sempre (al fine di non precludere la possibilità di memorizzare i progressi di un progetto ancora in fase di sviluppo), è possibile richiedere una validazione della mappa. Con l'apposito tasto posto a fianco del tasto di salvataggio, si carica temporaneamente il file di progetto sul server, che ne esegue una validazione e ritorna l'elenco di errori e warning. Questi funzionano come descritto di seguito:

.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/BPM/BPM_ERROR.png

- *ERRORI*: sono di fatto incorrettezze sintattiche e logiche che porterebbero con altissima probabilità al fallimento di un eventuale tentativo di esecuzione. Vengono visualizzati sulla mappa in corrispondenza del blocchetto a cui sono associati, con un'icona rossa. Spostando il puntatore del mouse sopra all'icona, è possibile leggere il testo dell'errore rilevato. Si sconsiglia fortemente la messa in produzione di processi contenenti errori.
- *WARNING*: sono problemi logici del processo che potrebbero essere migliorati, ma che potrebbero anche non bloccarne l'esecuzione. Vengono visualizzati sulla mappa in corrispondenza del blocchetto a cui sono associati, con un'icona arancio. Spostando il puntatore del mouse sopra all'icona, è possibile leggere il testo del warning rilevato. Si consiglia di mettere in produzione processi che contengano al più un numero limitato di warning.



Gestione della variabili
==========================

Lo strumento rende possibile operare in maniera molto simile a come si fa con uno script programmato con codice. 

.. important:: La gestione delle variabili avviene tramite diversi blocchetti, ma sempre secondo le seguenti regole comuni:   
    
    - Per salvare un valore in una variabile, si scrive il nome di quella variabile nel campo Variable Name di un blocchetto. Alla sua esecuzione, il valore verrà scritto nella variabile se questa già esiste (sovrascrivendo il valore precedente); se questa non esiste, verrà creata, ed è l'unico modo per istanziare una nuova variabile.
    - Per accedere ad una variabile esistente, si utilizza all'interno di un campo di configurazione il nome della variabile tra parentesi graffe.
    - Per scrivere o leggere variabili di chiamata, si utilizza il blocchetto dedicato a questa funzione, e si associa una variabile di chiamata con una locale, in lettura o scrittura.


.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/BPM/BPM_VARIABILI.png