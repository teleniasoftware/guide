Loop
======================

Il blocchetto \"Loop\" permette di eseguire un numero finito di volte una serie di operazioni.

.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/BPM/BLOCCHETTI/loop.png

    
.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/BPM/BLOCCHETTI/loop_config.png

**Campi configurabili**

- **Limite cicli**: Numero massimo di volte che il ciclo può essere eseguito.

Il parametro **Limite cicli** definisce il numero massimo di iterazioni, e le label **true** e **false** attribuite alle frecce uscenti definiscono rispettivamente la direzione da intraprendere nel caso in cui ci siano ancora iterazioni da eseguire, e nel caso in cui queste siano invece terminate.

In ogni momento, tra i task eseguiti ad ogni iterazione, è possibile uscire dal loop a fronte di un evento utilizzando ad esempio un blocchetto Condition gateway con una freccia uscente che instrada il flusso fuori dalla struttura del ciclo.
Lo stesso Loop può essere eseguito complessivamente più di una volta, ma va considerato che il contatore delle iterazioni si resetta solo al raggiungimento del Limite cicli, ossia nel momento in cui si esce dal ciclo seguendo la freccia uscente dal blocchetto Loop con label false.


.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/BPM/BLOCCHETTI/loop_esempio.png
