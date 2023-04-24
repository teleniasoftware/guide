.. _conneettorexmlcsv:

.. _qui: https://guide.teleniasoftware.com/it/22/projects/TVOX/Gestione/Rubriche/RubricheEsterne/CampiRubricheEsterne.html

===================
Sorgente da file CSV/XML
===================

Il "sincronizzatore File" recupera i contatti scritti su file, che possono essere in formato xml oppure csv, e li importa nelle rubriche Tvox.
I campi disponibili all'interno del file template possono essere consultati  nella guida ai campi delle Rubriche esterne (documentate `qui`_).

Formato del file
===================

I file che il sincronizzatore leggerà possono essere di due formati:

•	XML (EG: exampleXML.xml): i campi verranno recuperati tutti utilizzando la tipologia \"Testo\" (anche per i numeri di telefono).
•	CSV (EG: exampleCSV.csv): i campi dovranno essere separati da \",\" o da \“;\” e essi verranno recuperati tutti utilizzando la tipologia \"Testo\" (anche per i numeri di telefono).

IL NOME DEL FILE DOVRA' ESSERE COSI' FORMATO:

T_CONTACT_{{YYYYMMDD}}_{{IndiceIncrementale}}.[xml, csv]
(es: T_CONTACT_20200304_1.csv)

• **T_CONTACT_ **: Prefisso del nome
• **{{YYYYMMDD}}** : Giorno di esportazione
• **{{IndiceIncrementale}}** : Indice incrementale per ordinare file esportati nello stesso giorno

Funzionamento del sincronizzatore
===================

All'avvio del sincronizzatore viene prima controllato se sono presenti file da importare: nel caso in cui non ci siano dei file, il sistema emetterà un allarme di assenza di file, nel caso contrario comincerà la lettura dei file. L'importazione verrà effettuata in maniera ordinata in base alla data di esportazione e dell'indice incrementale. Questo viene fatto per poter mantenere le ultime modifiche sui contatti.

Il comportamento del sincronizzatore varia a seconda del parametro “Disabilita la modalità di aggiornamento con file parziali” secondo queste modalità:

- **Parametro abilitato :** Vengono considerati i contatti presenti nel file come da inserire o aggiornare, nessun contatto precedentemente importato verrà cancellato.
- **Parametro disabilitato (default):** I contatti precedentemente importati verranno tutti cancellati ad ogni importazione. Tutti i contatti presenti solamente nei file vengono creati nella rubrica. Di conseguenza ogni import che verrà effettuato dovrà contenere la totalità dei contatti.

In quest'ultima modalità per ogni contatto già presente in rubrica viene recuperato, utilizzando l'\"unique_id\", il corrispettivo contatto:

• Se questo contatto è presente viene aggiornato sulla rubrica.
• Se questo contatto NON è presente viene cancellato dalla rubrica.

Gestione degli allarmi
===================

Ad ogni importazione verrà emesso un allarme di inizio e uno di fine sincronizzazione. Nel caso in cui ci sia un errore grave durante la fase di traduzione dei contatti dai file verso il formato Tvox, verrà emesso un ulteriore allarme in cui sarà scritto il campo “unique_id” del contatto che l’ha generato.
