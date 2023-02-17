.. _smtp:

===================
Configurazione SMTP
===================

**SMTP** o **Simple Mail Transfer Protocol**, abilita la piattaforma ad inviare e-mail attraverso il server specificato per la notifica di allarmi, documenti, fax e messaggi di segreteria telefonica.

In OCC nella sezione *SISTEMA - Configurazione Sistema - SMTP*

.. image:: /images/TVOX/Sistema/ConfigurazioneSistema/SMTP/SMTP.png

In tale sezione si dovranno definire:

- **Server** (Nome o indirizzo IP del server SMTP richiesto dalla piattaforma per inviare e-mail)

- **Indirizzo E-mail** (L’indirizzo e-mail dovrebbe corrispondere all’indirizzo e-mail/alias dell’account, per il quale sono forniti i dettagli di autenticazione)

.. warning:: L’indirizzo e-mail deve corrispondere ad una definita casella di posta su SMTP che memorizza ogni e-mail inviata dalla piattaforma e quelle non inviate con successo a causa di errori (i.e. destinatario non corretto). Questa casella di posta deve essere gestita dall’amministratore della piattaforma per correggere tutti gli errori riportati.

- **Porta** (Porta SMTP in ascolto sul server. A seconda della scelta fatta la porta sarà selezionata automaticamente)

.. warning:: Solitamente SMTP lavora sulle porte 25 (porta SMTP non-criptata predefinita),465 (criptazione SSL avviata automaticamente prima di ogni livello di comunicazione SMTP) e587 (è quasi come la porta standard SMTP. La criptazione SSL può essere avviata da un comando STARTTLS a livello SMTP se il server SMTP la supporta e il proprio ISP non filtra le risposte EHLO dal server)

- **Tipo di Connessione sicura** (Abilita l’autenticazione SMTP in differenti modalità di criptazione a seconda del Server SMTP)


     - *SSL*  (Fornisce un modo per criptare il canale di comunicazione tra il computer e il server SMTP)
     - *STARTTLS*  (E’ un modo per prendere una connessione esistente non sicura e aggiornarla ad una sicura utilizzando SSL/TLS)
     - *Nessuno* (Il sistema prevede anche di non dare gradi di sicurezza, ma ormai nessun server accetta la connessione non sicura sulla porta 25)

.. warning:: Attualmente il nostro sistema SMTP prevede la connessione con STARTTLS o SSL, non prevede ancora la possibilità di connettersi con il nuovo standard OAouth 2.0


- **Autenticazione** (Attivare sempre l'autenticazione e compilare “Username e Password” con le credenziali della casella e-mail. Di default si presenterà disattiva)

Cliccando sul pulsante “SALVA” comparirà un pop-up di corretto salvataggio. 

Lo stesso feedback indicherà la corretta connessione al server che utilizzerà queste proprietà per collegarsi e inviare le e-mail.

Per confermare l’esito positivo della configurazione è possibile eseguire un test di invio indicando un indirizzo destinatario nel riquadro “Test Configurazione SMTP”.

Questa configurazione è utile anche per le segnalazioni inviate da TVox Client per recapitarle ad un destinatario che deve analizzarle.

In OCC nella sezione *IMPOSTAZIONI - Avanzate -  TVox Client -  Segnalazioni -  Impostazioni*

Abilitare e impostare una e-mail di destinazione.

.. image:: /images/TVOX/Sistema/ConfigurazioneSistema/SMTP/segnalazioni.png
