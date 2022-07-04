Validazione e salvataggio
=========================


Per salvare il diagramma, si fa click sul tasto salva in alto a destra. 
Il progetto viene esportato in un file e viene caricato sul server, con notifica di avvenuto upload. 

.. note:: Nonostante il diagramma si possa salvare sempre (al fine di non precludere la possibilità di memorizzare i progressi di un progetto ancora in fase di sviluppo), è possibile richiedere una validazione della mappa. Con l'apposito tasto posto a fianco del tasto di salvataggio, si carica temporaneamente il file di progetto sul server, che ne esegue una validazione e ritorna l'elenco di errori e warning. Questi funzionano come descritto di seguito:

.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/BPM/BPM_ERROR.png

- *ERRORI*: sono di fatto incorrettezze sintattiche e logiche che porterebbero con altissima probabilità al fallimento di un eventuale tentativo di esecuzione. Vengono visualizzati sulla mappa in corrispondenza del blocchetto a cui sono associati, con un'icona rossa. Spostando il puntatore del mouse sopra all'icona, è possibile leggere il testo dell'errore rilevato. Si sconsiglia fortemente la messa in produzione di processi contenenti errori.
- *WARNING*: sono problemi logici del processo che potrebbero essere migliorati, ma che potrebbero anche non bloccarne l'esecuzione. Vengono visualizzati sulla mappa in corrispondenza del blocchetto a cui sono associati, con un'icona arancio. Spostando il puntatore del mouse sopra all'icona, è possibile leggere il testo del warning rilevato. Si consiglia di mettere in produzione processi che contengano al più un numero limitato di warning.
