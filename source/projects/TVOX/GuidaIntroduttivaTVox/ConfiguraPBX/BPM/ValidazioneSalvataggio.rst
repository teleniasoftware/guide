Validazione e salvataggio
=========================


Per salvare il processo BPM, si fa click sul tasto salva in alto a destra. 
Il progetto viene contemporaneamente Validato e Salvato.

.. note:: Nonostante il diagramma si possa salvare sempre (al fine di non precludere la possibilità di memorizzare i progressi di un progetto ancora in fase di sviluppo), è possibile richiedere una validazione della mappa. L'apposito tasto "Valida Mappa" di fianco al tasto di salvataggio, verifica che la mappa sia Valida e ritorna gli errori errori ed i warning sui relativi blocchetti. Ad esempio:

.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/BPM/BPM_ERROR.png

- *ERRORI*: sono di fatto incorrettezze sintattiche e logiche che porterebbero con altissima probabilità al fallimento di un eventuale tentativo di esecuzione. Vengono visualizzati sulla mappa in corrispondenza del blocchetto a cui sono associati, con un'icona rossa. Spostando il puntatore del mouse sopra all'icona, è possibile leggere il testo dell'errore rilevato. Si sconsiglia fortemente la messa in produzione di processi contenenti errori. Esempi di errori sono: mancanza di frecce uscenti da un processo di Start, doppia freccia uscente da un processo che ne prevede una sola, etc.

.. note:: Casi di errore:

    - Nessun evento di start presente nel processo
    - Eventi di start multipli presenti
    - Nessuna freccia d'uscita dall'evento di start
    - Frecce multiple d'uscita dall'evento di start
    - Il blocchetto non supporta frecce multiple
    - Campi obbligatori non configurati
    - Frecce uscenti non configurate
    - Scelta non configurata
    - Frecce uscenti con la stessa configurazione


- *WARNING*: sono problemi logici del processo che potrebbero anche non bloccarne l'esecuzione. Vengono visualizzati sulla mappa in corrispondenza del blocchetto a cui sono associati con un'icona arancio. Spostando il puntatore del mouse sopra all'icona, è possibile leggere il testo del warning rilevato. Si consiglia di mettere in produzione processi che contengano warning. Esempi di warning sono: assenza di frecce entranti o uscenti in un blocchetto

.. note:: Casi di warning:
    
    - Nessun evento di End configurato
    - Nessuna freccia entrante per l'evento di end
    - Nessuna freccia entrante per questo task
    - Nessuna freccia uscente per questo task
    - Questo task presenta un loop infinito

 