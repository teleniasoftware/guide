=========================================
Configurare la sezione SMTP e gli Allarmi
=========================================

Configurazione SMTP
====================
In OCC nella sezione  *SISTEMA=> Configurazione di Sistema => SMTP* si abilita la piattaforma ad inviare e-mail attraverso il server specificato per la notifica di allarmi, documenti, fax e messaggi di segreteria telefonica.

.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/SMTP-Allarmi/SMTP.PNG



In tale sezione si dovranno definire:

- **Server** (Nome o indirizzo IP del server SMTP richiesto dalla piattaforma per inviare e-mail)

- **Indirizzo E-mail** (L'indirizzo e-mail dovrebbe corrispondere all'indirizzo e-mail/alias dell'account, per il quale sono forniti i dettagli di autenticazione)

.. warning:: L'indirizzo e-mail deve corrispondere ad una definita casella di posta su SMTP che memorizza ogni e-mail inviata dalla piattaforma e quelle non inviate con successo a causa di errori (i.e. destinatario non corretto). Questa casella di posta deve essere gestita dall'amministratore della piattaforma per correggere tutti gli errori riportati.

- **Porta** (Porta SMTP in ascolto sul server)

.. warning:: Solitamente SMTP lavora sulle porte 25 (porta SMTP non-criptata predefinita),465 (criptazione SSL avviata automaticamente prima di ogni livello di comunicazione SMTP) e587 (è quasi come la porta standard SMTP. La criptazione SSL può essere avviata da un comando STARTTLS a livello SMTP se il server SMTP la supporta e il proprio ISP non filtra le risposte EHLO dal server)

- **Tipo di Connessione sicura** (Abilita l'autenticazione SMTP in differenti modalità di criptazione a seconda del Server SMTP. 
  
       - *SSL* fornisce un modo per criptare il canale di comunicazione tra il computer e il server SMTP. 
       - *STARTTL* è un modo per prendere una connessione esistente non sicura e aggiornarla ad una sicura utilizzando SSL/TLS)

- **Username e password** (nel caso sia abilitata l'autenticazione)


Configurazione Allarmi
======================

E\' possibile profilare utenti destinati alla visualizzazione dello stato della piattaforma di sistema e degli avvisi di allarme generati dal TVox.

La gestione degli allarmi avviene puntando alla sezione TSAM (https://ip_TVOX/tsam).

In tale sezione è possibile:

- avere il **monitor degli allarmi generati**
  
  .. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/SMTP-Allarmi/Monitor_Allarmi.PNG

- **configurare gli allarmi** generati (in termini di priorità, descrizione, associazione a famiglie, etc.)
  
  .. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/SMTP-Allarmi/Configurazione_Allarmi.PNG

- **configurare destinatari allarmi** selezionando le utenze configurate sul TVOX oppure inserendo utenze esterne
  
  .. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/SMTP-Allarmi/Destinatari.PNG

- **configurare liste allarmi** dove si va ad associare un insieme di allarmi a i vari destinatari creati al punto precedente
  
  .. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/SMTP-Allarmi/Liste_Allarmi.PNG







