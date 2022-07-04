Gestione delle variabili
========================

Lo strumento "Business Process" dà la possibilità di operare in maniera molto simile a come si farebbe con uno script, permettendo di dichiarare delle variabili da utilizzare all'interno del processo stesso.

La gestione delle variabili avviene tramite diversi blocchetti, ma sempre secondo le seguenti regole comuni:   
Per salvare un valore in una variabile, si scrive il nome di quella variabile nel campo "Nome variabile" di un blocchetto. Alla sua esecuzione, il valore verrà scritto nella variabile. Se questa già esiste,sovrascrivendo il valore precedente; se questa non esiste, verrà creata.

Per alcuni blocchetti che richiedono l'uso di una variabile già dichiarata, verrà presentato un menu con l'elenco delle variabili dichiarate in quel processo

.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/BPM/BPM_VARIABILI_elenco.png

Per utilizzare una variabile dichiarata su un blocchetto con un campo di testo (ad esempio TTS o Send Mail), è possibile richiamare la variabile inserendola fra parentesi graffe.

.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/BPM/BPM_VARIABILI_testo.png