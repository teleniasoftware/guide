.. _conneettoremysql:

.. _qui: https://guide.teleniasoftware.com/it/22/projects/TVOX/Gestione/Rubriche/RubricheEsterne/CampiRubricheEsterne.html


===================
Sorgente MySql
===================

Il \"sincronizzatore Mysql\" recupera i contatti tramite una query sql su server mysql o mariadb e li importa nelle rubriche TVox.

Parametri di configurazione:

•	**Host**: deve riportare l’ip/hostname del server mysql (es. mysql.myorg.com)
•	**Port**: porta del servizio mysql (es. 3306)
•	**Username/Password**: Credenziali di accesso al server mysql
•	**Nome del database**: Nome del database in cui eseguire la query di recupero contatti
•	**Numero minimo di contatti da importare**: Se la query ritorna un numero di record inferiore al valore impostato l’importazione non viene effettuata

.. image:: /images/TVOX/Gestione/Rubriche/config_mysql.jpg

La query sql deve mappare i nomi dei campi del database verso i campi del contatto TVox rispettando la sintassi di quest’ultimo. 
Il nome esatto dei campi è riportato alla guida ai campi delle Rubriche esterne (documentate `qui`_).

.. warning:: - I nomi dei campi TVox riportati nella query devono essere in minuscolo. 
    - La query sql non deve terminare con il carattere “;”

Query di esempio:

SELECT uuid_unique as \"uid\", first_name as \"name\", surname, second_name as \"othername\", company_name as \"company\", street, city, \"CELL\" as \"tel_type_1\", cell_number as \"tel_value_1\", \"HOME\" as \"tel_type_2\", home_number as \"tel_value_2\", \"FAX\" as \"tel_type_3\", fax as \"tel_value_3\", \"INTERNET_HOME\" as \"mail_type_1\", mail as \"mail_value_1\", \"individual\" as \"kind\, fiscal_code as \"custom_1\" FROM my_contact


Funzionamento del sincronizzatore
====================================

Al primo avvio il sincronizzatore esegue un tentativo di connessione al database per verificare la correttezza dei parametri impostati.
Nel caso che la connessione fallisca o la query non risulti valida l’importazione viene fermata.

Se la query impostata è valida si passa alla fase di importazione che decide per ogni contatto se crearlo o modificarlo in TVox. 

.. warning:: Tutti i contatti presenti in TVox e non ritornarti dalla query verranno cancellati.


Gestione degli allarmi
=======================

Ad ogni importazione verrà emesso un allarme di inizio e uno di fine sincronizzazione
