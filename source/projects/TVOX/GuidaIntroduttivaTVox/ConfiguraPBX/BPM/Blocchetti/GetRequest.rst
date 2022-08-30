Get Request
======================

Il blocchetto \"Get Request\" permette di interrogare un servizio esterno e salvare il valore restituito in una variabile

.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/BPM/BLOCCHETTI/getrequest.png

    
.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/BPM/BLOCCHETTI/getrequest_config.png

**Campi configurabili**

- **Nome variabile**: nome della variabile da configurare che potrà essere successivamente richiamato all'interno del processo
- **Url**: indirizzo del webservice a cui effettuare la richiesta
- **Modalità http**: scelta fra il protocollo http o https 
- **Parametro chiave**: parametro da mappare all'interno del webservice
- **Parametro valore**: valore del parametro che può assumere un valore predefinito o essere passato tramite variabile di processo 
- **Username**: nome utente di autenticazione tramite Basic Authentication
- **Password**: password di autenticazione tramite Basic Authentication
- **Timeout**: Tempo massimo (in secondi) entro cui la richiesta tenterà una connessione verso l'Url configurato