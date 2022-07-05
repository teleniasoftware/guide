Regole e convenzioni dei processi
=================================

Di norma, ogni blocchetto può avere una singola freccia in uscita, e una o più frecce in ingresso. Questo perché, altrimenti, più frecce in uscita da un blocchetto darebbero vita ad una situazione ambigua in cui non è possibile determinare il prossimo step da eseguire. 


Ci sono tuttavia alcune eccezioni a questa regola, relative a blocchetti che di fatto "sdoppiano" il flusso definendo due (o più) possibili strade, che verranno percorse in corrispondenza di determinate condizioni. In questi casi, è necessario fare doppio click sulle frecce uscenti dal blocchetto,e scegliere il valore che si vuole associare a quella freccia. Nel dettaglio, si tratta dei seguenti blocchetti:
   
    - *Digit Gateway*: permette di seguire direzioni diverse in base al digit selezionato dall'utente. In base alla scelta (digit da 0 a 9 oppure # o *) possono essere impostati diversi blocchi. E\' presente inoltre un'ulteriore scelta (\"unmatch\") che permette di precorrere una strada differente se la scelta non è valida.
    - *Condition Gateway*: permette di verificare una condizione (tipo if) e le frecce uscenti possono avere come valore true o false.
    - *Switch*: permette di controllare una variabile e intraprendere strade diverse in base al suo valore attuale. Le frecce si devono chiamare esattamente come il valore che si vuole causi l'esecuzione di quel ramo.

.. important:: **BEST PRACTICE:**  Ogni processo deve necessariamente iniziare con un blocchetto di tipo **start**, la cui icona è un cerchio sottile. In un processo BMP non è possibile avere più start. Il blocchetto **stop**, rappresentato da un cerchio più spesso, indica il termine del processo. Può non essere presente, ma è preferibile, ed al contrario dello start in un processo BPM è possibile inserire più blocchetti di **stop**

.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/BPM/BPM_start_stop.png