.. _menuutente:

===========
Menu Utente
===========

Il menu utente è il menu che si trova in corrispondenza del nome e cognome posizionato nella parte superiore destra del client.

.. image:: /images/CLIENT/menu_utente.PNG


In quest'area è sempre disponibile l'informazione relativa all'utente che ha eseguito il login (nome e cognome) accompagnato da un avatar di forma tonda che riporta l'iniziale del cognome ed una contornazione che rispecchia il logo di |client|. 

E\' riportato il dispositivo telefonico in uso dall'utente (verde se il dispositivo risulta correttamente collegato, rosso se il dispositivo ha problemi di connessione al server).

Sull'avatar inoltre è riportato in tempo reale lo stato di presence dell'utente.

.. tip:: La **Presence** indica lo stato di presenza e disponibilità dell'utente e si trova sempre abbinata all'avatar che rappresenta un utente TVox. Può assumere le seguenti colorazioni:  |br| |br| **VERDE** : l'utente è loggato con il |client| (o con |app|) e risulta libero telefonicamente |br| **ROSSO** : l'utente è loggato con il |client| e risulta occupato telefonicamente |br| **GIALLO** : l'utente è loggato con il |client|, risulta libero telefonicamente e sta utilizzando un profilo di tipo Agente posto in stato NR (Not Ready) con opportuno codice di attività che indica che l'utente è momentaneamente lontano dalla propria postazione |br| **GRIGIO** : l'utente non è loggato nè con |client| nè con |app|


Posizionando il puntatore del mouse in questa zona, viene automaticamente presentato il menu utente, che contiene le seguenti voci:

* **Profili di lavoro assegnati all'utente**: I profili sono presentati con un'etichetta impostata dall'amministratore di sistema che deve indicare in maniera chiara la loro rispettiva funzione, per permettere all'utente di selezionare il profilo corretto a seconda delle direttive di lavoro ricevute.  **Il profilo selezionato è riportato in grassetto** .
* **Dispositivi telefonici assegnati all'utente**: Vengono riportati tutti i dispositivi telefonici assegnati dall'amministratore di sistema all'utente. In grassetto è riportato il dispositivo telefonico in uso, eventuali altri dispositivi sono riportati con carattere senza evidenza e possono riportare una casella di spunta sulla loro destra. Nel caso in cui si spunti la casella su uno o più dei dispositivi aggiuntivi, TVox contattatterà l'utente anche su questi dispositivi quando l'utente stesso è chiamato sul canale telefonico.
* **Utilizza altro telefono**: Permette all'utente di prendere il controllo di un dispositivo non assegnato a sè stesso (ad esempio, se si sposta in sala riunioni e ha bisogno di utlizzare il telefono posto sul tavolo della sala)
* **Blocca telefono**: Permette all'utente di bloccare il proprio dispositivo telefonico fisico per le chiamate in uscita (per impedire, ad esempio, che altri utenti utilizzino tale dispositivo per effettuare chiamate che verrebbero addebitate a lui)
* **Invio SMS**: Se configurato, permette all'utente di compilare un form per l'invio di un sms ad un numero mobile
* **Abilita DND**: Se configurato, permette all'utente di porsi in stato Do Not Disturb. In tale stato, la presente dell'utente assume la colorazione rossa con barra orrizzontale bianca. Inoltre, viene evidenziato un contatore del tempo in tale stato con sfondo rosso sopra al campo di ricerca posto nella parte superiore sinistra del client.
* **Log Out**: Permette all'utente di effettuare l'operazione `<logout>`_ 