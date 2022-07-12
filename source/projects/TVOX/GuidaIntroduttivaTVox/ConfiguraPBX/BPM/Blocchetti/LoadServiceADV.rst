Load Service Advanced
======================

Il blocchetto \"Load Service Adv\" inoltra la chiamata verso un servizio presente su OCC->Gestione->Servizi, permettendo la personalizzazione di alcuni parametri.

.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/BPM/BLOCCHETTI/loadserviceadv.png


.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/BPM/BLOCCHETTI/loadserviceadv_config.png

**Campi configurabili**

- **Servizio**: elenco a discesa nella quale è possibile selezionare uno dei Servizi configurati su OCC
- **Etichetta aggiuntiva**: descrizione aggiuntiva per identificare il servizio corrente. Tale valore è aggiunto alla descrizione del servizio nei report storici e viene così presentato sul Web Client nel momento in cui la chiamata viene proposta all'operatore.
- **Priorità del servizio**: Identifica la priorità che il servizio assume per la chiamata che transita nel nodo corrente.
- **Numero massimo gestite dal servizio**:Impostazione del numero massimo chiamate gestite dal servizio per le chiamate che transitano nel nodo corrente.
- **Limite delle chiamate in attesa nel servizio**: Impostazione del limite delle chiamate in coda al servizio per le chiamate che transitano nel nodo corrente.
- **Limite proporzionale agli agenti loggati**: Impostazione del limite delle chiamate in coda proporzionale al numero di agenti loggati negli skillset configurati per le chiamate che transitano nel nodo corrente.
- **Registrazione della chiamata su servizio**: se selezionato, indica che la chiamata verrà registrata dal momento in cui l'operatore risponde.
- **Skillset 1**: Primo Skillset, in ordine di priorità, interessato alla distribuzione delle chiamate per il servizio selezionato. Se non viene indicato alcun valore sono automaticamente considerati tutti gli skillset configurati per il servizio corrente.
- **Skillset 2**: secondo ​Skillset, in ordine di priorità, interessato alla distribuzione delle chiamate per il servizio selezionato
- **Skillset 3**: terzo ​Skillset, in ordine di priorità, interessato alla distribuzione delle chiamate per il servizio selezionato
- **Skillset 4**: quarto Skillset, in ordine di priorità, interessato alla distribuzione delle chiamate per il servizio selezionato.
- **Skillset 5**: quinto Skillset, in ordine di priorità, interessato alla distribuzione delle chiamate per il servizio selezionato.
