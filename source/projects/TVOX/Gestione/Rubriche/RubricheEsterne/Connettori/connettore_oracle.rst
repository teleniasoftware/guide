.. _conneettoreroacle:

.. _qui: https://guide.teleniasoftware.com/it/22/projects/TVOX/Gestione/Rubriche/RubricheEsterne/CampiRubricheEsterne.html

===================
Sorgente Oracle
===================

Il \"sincronizzatore Oracle\" recupera i contatti tramite una query sql su server oracle e li importa nelle rubriche TVox.


Parametri di configurazione:

•	**Host**: deve riportare l’ip/hostname del server oracle (es. oracle.myorg.com)
•	**Port**: porta del servizio oracle (es. 1521)
•	**Username/Password**: Credenziali di accesso al server oracle
•	**Nome del database**: Nome del database in cui eseguire la query di recupero contatti
•	**Numero minimo di contatti da importare**: Se la query ritorna un numero di record inferiore al valore impostato l’importazione non viene effettuata

.. image:: /images/TVOX/Gestione/Rubriche/config_oracle.jpg

La query sql deve mappare i nomi dei campi del database verso i campi del contatto TVox rispettando la sintassi di quest’ultimo. Il nome esatto dei campi è riportato alla guida ai campi delle Rubriche esterne (documentate `qui`_).

.. warning:: - I nomi dei campi TVox riportati nella query devono essere in minuscolo. 
    - La query sql non deve terminare con il carattere “;” 
    - La query sql deve riportare gli alias tra doppio apice


Query di esempio:

SELECT c_cli as \\"uid\\", t_rag_soc as \"name\", t_rag_soc as \"company\", t_des_con as \"surname\", t_ind as \"street_1\", t_loc as \"city_1\", prov as \"region_1\", cap as \"postcode_1\" , t_des_sede as \"note\", 'CELL' as \"tel_type_1\", t_tel as \"tel_value_1\", 'HOME' as \"tel_type_2\", t_tel2 as \"tel_value_2\", c_iva as \"custom_1\" FROM rubr_tvox

Funzionamento del sincronizzatore
===================

Al primo avvio il sincronizzatore esegue un tentativo di connessione al database per verificare la correttezza dei parametri impostati.
Nel caso che la connessione fallisca o la query non risulti valida l’importazione viene fermata.

Se la query impostata è valida si passa alla fase di importazione che decide per ogni contatto se crearlo o modificarlo in TVox. 

.. warning:: Tutti i contatti presenti in TVox e non ritornarti dalla query verranno cancellati.

Gestione degli allarmi
===================

Ad ogni importazione verrà emesso un allarme di inizio e uno di fine
sincronizzazione
