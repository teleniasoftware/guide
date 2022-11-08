.. _conneettoresqlserver:

.. _qui: https://guide.teleniasoftware.com/it/22/projects/TVOX/Gestione/Rubriche/RubricheEsterne/CampiRubricheEsterne.html

===================
Sorgente SQLServer
===================

Il \"sincronizzatore Sqlserver\" recupera i contatti tramite una query sql su server microsoft sql server li importa nelle rubriche TVox.


Parametri di configurazione:

•	**Versione**: Versione del server sqlserver su cui ci si connette
•	**Host**: deve riportare l’ip/hostname del server sqlserver (es. sql.myorg.com)
•	**Port**: porta del servizio sqlserver
•	**Username/Password**: Credenziali di accesso al server sqlserver
•	**Nome del database**: Nome del database in cui eseguire la query di recupero contatti
•	**Numero minimo di contatti da importare**: Se la query ritorna un numero di record inferiore al valore impostato l’importazione non viene effettuata

.. image:: /images/TVOX/Gestione/Rubriche/config_sql.jpg


La query sql deve mappare i nomi dei campi del database verso i campi del contatto TVox rispettando la sintassi di quest’ultimo. Il nome esatto dei campi è riportato alla guida ai campi delle Rubriche esterne (documentate `qui`_).

.. warning:: I nomi dei campi TVox riportati nella query devono essere in minuscolo. La query sql deve terminare con il carattere “;”

Query di esempio:

SELECT CONVERT(VARCHAR(500), uid) AS uid, CONVERT(VARCHAR(500), NAME) AS name, CONVERT(VARCHAR(500), SURNAME) AS surname, CONVERT(VARCHAR(500), OTHERNAME) AS othername, CONVERT(VARCHAR(500), COMPANY) AS company, CONVERT(VARCHAR(500), DEPARTMENT) AS department, CONVERT(VARCHAR(500), STREET) AS street, CONVERT(VARCHAR(500), CITY) AS city, CONVERT(VARCHAR(500), REGION) AS region, CONVERT(VARCHAR(500), POSTCODE) AS postcode, CONVERT(VARCHAR(500), COUNTRY) AS country, CONVERT(VARCHAR(500), TEL_TYPE_1) AS tel_type_1, CONVERT(VARCHAR(500), TEL_VALUE_1) AS tel_value_1, CONVERT(VARCHAR(500), TEL_TYPE_2) AS tel_type_2, CONVERT(VARCHAR(500), TEL_VALUE_2) AS tel_value_2, CONVERT(VARCHAR(500), MAIL_TYPE_1) AS mail_type_1, CONVERT(VARCHAR(500), MAIL_VALUE_1) AS mail_value_1, IIF(VIP = 1, ‘TRUE’, ‘FALSE’) as vip, CONVERT(VARCHAR(500), CUSTOM_1) AS custom_1, CONVERT(VARCHAR(500), KIND) AS kind FROM my_contact;


Funzionamento del sincronizzatore
===================

Al primo avvio il sincronizzatore esegue un tentativo di connessione al database per verificare la correttezza dei parametri impostati.
Nel caso che la connessione fallisca o la query non risulti valida l’importazione viene fermata.

Se la query impostata è valida si passa alla fase di importazione che decide per ogni contatto se crearlo o modificarlo in TVox. Tutti i contatti presenti in TVox e non ritornarti dalla query verranno cancellati.

Gestione degli allarmi
===================


Ad ogni importazione verrà emesso un allarme di inizio e uno di fine
sincronizzazione
