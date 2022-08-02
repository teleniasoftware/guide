Text to Speech
======================

Il blocchetto \"Text to Speech\" permette la configurazione di un messaggio testuale che viene riprodotto con un Text-Recnognition precedentemente configurato

.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/BPM/BLOCCHETTI/tts.png

    
.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/BPM/BLOCCHETTI/tts_config.png

    
**Campi configurabili**

- **TTS Type**: Tipo di TTS configurato da utilizzare
- **Voce da utilizzare**: selezione delle voci configurate 
- **Profilo TTS**: profilo del TTS Configurato su Occ
- **Volume**: Livello di volume con il quale viene riprodotto il messaggio (default: Medio)
- **Velocità di riproduzione**: Velocità con la quale verrà riprodotto il messaggio (default: Media)
- **Testo**: testo del messaggio. Se si desidera, si possono utilizzare delle variabili passate all'interno del BPM 

Esempio di utilizzo di TTS con variabile:

.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/BPM/BLOCCHETTI/tts_esempio.png

In questo modo, verrà riprodotto il messaggio "Benvenuto **Mario Rossi** in Telenia Software."