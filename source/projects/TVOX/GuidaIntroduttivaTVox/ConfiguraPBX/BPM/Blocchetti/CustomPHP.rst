.. _qui: http://documentation.teleniasoftware.com/tivr/index.html

Custom PHP code
======================

Il blocchetto \"Custom PHP code\" permette di creare uno script PHP da utilizzare all'interno del processo.

.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/BPM/BLOCCHETTI/customphp.png

    
.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/BPM/BLOCCHETTI/customphp_config.png

**Campi configurabili**

- **Seleziona script**: Seleziona uno script PHP custom presente su TVox. Selezionando la prima voce "Nuovo" è possibile creare un nuovo file andandone a specificare il nome ed una descrizione


.. important:: 
    - Possono essere chiamate tutte le funzioni di TIVR (documentate `qui`_)
    - Non è possibile definire nuove funzioni all'interno dello script
    - Lo script può essere creato/modificato anche su OCC->Script->Custom PHP, dove è presente una schermata più ampia dell'editor


.. tip:: Per accedere ad una variabile settata da un blocchetto precedente, la sintassi è:
$value = $blade->getVar("nome-bpm-var");
dove nome-bpm-var è il nome variabile specificato nel campo "variable name" del blocchetto che l'ha settata, e $value è una variabile php relativa al blocchetto PHP CUSTOM in cui il valore letto verrà salvato.


.. tip::Per settare una variabile bpm (che sarà utilizzabile nei blocchetti successivi), la sintassi è:
$blade->setVar("nome-bpm-var",$value);
dove nome-bpm-var è il nome variabile, e $value è una variabile php relativa al blocchetto PHP CUSTOM il cui valore viene assegnato alla nuova variabile bpm.


.. tip::Si possono aggiungere più frecce in uscita al blocchetto, utilizzandolo anche come gateway. Per settare il valore della freccia da seguire, la sintassi è:
$blade->setDecisionVar($result);
dove $result è una variabile php relativa al blocchetto PHP CUSTOM in cui è contenuto il valore che il motore di esecuzione cercherà tra i nomi delle frecce per decidere quale seguire in uscita.


Nella schermata del BPM, selezionando uno script già presente, è possibile modificarlo:

.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/BPM/BLOCCHETTI/customphp_edit.png
