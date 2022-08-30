Check service activation
======================

Il blocchetto \"Check service activation\" controlla se un servizio è o meno attivo, permettendo il salvataggio del valore in una variabile.
Da questo blocchetto possono partire sei freccette:

- Active = Attivo (obbligatorio)
- Outofservice = Fuori servizio
- Overtime = Fuori orario
- Active1, Active2, Active3 = sono 3 trattamenti del calendario disponibili se configurati

.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/BPM/BLOCCHETTI/checkservice.png

    
.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/BPM/BLOCCHETTI/checkservice_config.png

**Campi configurabili**

- **Seleziona servizio**: Il servizio a cui inoltrare la chiamata è selezionato dall'elenco dei servizi già definiti nell'OCC.
- **Nome variabile**: nome della variabile in cui salvare il risultato che potrà essere successivamente richiamata all'interno del processo