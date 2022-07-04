Gestione delle variabili
========================

Lo strumento rende possibile operare in maniera molto simile a come si fa con uno script programmato con codice. 

.. important:: La gestione delle variabili avviene tramite diversi blocchetti, ma sempre secondo le seguenti regole comuni:   
    
    - Per salvare un valore in una variabile, si scrive il nome di quella variabile nel campo Variable Name di un blocchetto. Alla sua esecuzione, il valore verrà scritto nella variabile se questa già esiste (sovrascrivendo il valore precedente); se questa non esiste, verrà creata, ed è l'unico modo per istanziare una nuova variabile.
    - Per accedere ad una variabile esistente, si utilizza all'interno di un campo di configurazione il nome della variabile tra parentesi graffe.
    - Per scrivere o leggere variabili di chiamata, si utilizza il blocchetto dedicato a questa funzione, e si associa una variabile di chiamata con una locale, in lettura o scrittura.
    
    .. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/BPM/BPM_VARIABILI.png