Regole e convenzioni dei processi
=================================

Di norma, ogni blocchetto può avere una singola freccia in uscita, e una o più frecce in ingresso. Questo perché, altrimenti, più frecce in uscita da un blocchetto darebbero vita ad una situazione ambigua in cui non è possibile determinare il prossimo step da eseguire. 


Ci sono tuttavia alcune eccezioni a questa regola, relative a blocchetti che di fatto "sdoppiano" il flusso definendo due (o più) possibili strade, che verranno percorse in corrispondenza di determinate condizioni. In questi casi, è necessario fare doppio click sulle frecce uscenti dal blocchetto,e digitare nel campo che compare il valore che si vuole associare a quella freccia. Nel dettaglio, si tratta dei seguenti blocchetti:
   
    - *Digit Gateway*: permette di seguire direzioni diverse in base al digit selezionato dall'utente. Le frecce devono chiamarsi come il digit che si vuole associare a quel ramo del processo.
    - *Condition Gateway*: permette di verificare una condizione (tipo if) e intraprendere due strade a seconda di esito vero o falso. Le due frecce uscenti devono chiamarsi true e false.
    - *Switch*: permette di osservare una variabile e intraprendere strade diverse in base al suo valore attuale. Le frecce si devono chiamare esattamente come il valore che si vuole causi l'esecuzione di quel ramo.

.. important:: **BEST PRACTICE:**  Ogni processo deve necessariamente iniziare con un blocchetto di tipo **start**, la cui icona è un cerchio sottile. Il blocchetto **stop**, rappresentato da un cerchio più spesso, indica il termine del processo, ed è preferibilmente presente in ogni mappa disegnata. 

