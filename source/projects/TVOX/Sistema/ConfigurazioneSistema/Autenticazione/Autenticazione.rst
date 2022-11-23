.. _qui: http://guide.teleniasoftware.com/it/22/projects/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/PrimiPassi/SMTPAllarmi.html

.. _autenticazione&sicurezza:

==========================
Autenticazione e Sicurezza
==========================

La prestazione di Autenticazione a due fattori si basa sulla generazione di un codice TOTP (Time-based One-time Password) ad opera di un'applicazione 
(Microsoft Autenticator, Google Autenticator, Duo mobile, etc) che prevede la generazione di questo tipo di codice.

Inoltre, è prevista anche la possibilità di generare il codice TOPT tramite mail inviata da TVox nel caso in cui si voglia lasciare la possibilità all'utente di poter eseguire l'operazione di login nel caso in cui non dovesse avere accesso al proprio smartphone.

 
Uno dei requisiti per poter attivare l\'autenticazione a due fattori su TVox è quello di aver configurato su Occ-> Sistema -> Data/Ora un server NTP (Network Time Protocol).

Quando si installa un TVox i valori di default sono i seguenti:

 .. image:: /images/TVOX/Sistema/ConfigurazioneSistema/AccessoSicurezza/conf_ntp.png


.. note:: I valori dei server Primari e Secondari possono essere personalizzati a piacere


La necessità di avere un server NTP configurato è data dal fatto che la generazione del codice TOTP da parte delle applicazioni su smartphone deve essere precisa su base temporale. Quindi client, App di generazione codice TOTP ed il server TVox devono avere un orario più preciso possibile.

Un secondo requisito per la generazione del codice TOTP mediante email è la configurazione SMTP (documentata `qui`_).

Per configurare la funzionalità di autenticazione a doppio fattore con TOTP ci rechiamo su Occ->Sistema->Autenticazione e Sicurezza:


 .. image:: /images/TVOX/Sistema/ConfigurazioneSistema/AccessoSicurezza/conf_autenticazione.png

Il fattore di autenticazione può essere abilitato singolarmente per le seguenti applicazioni:

- Webclient
- Occ
- Insight
- RTD
- Customer Portal

.. warning:: L'autenticazione a due fattori non è disponibile per accessi eseguiti tramite TVox Team App. 

Ad esempio, per configurare l'autenticazione a due fattori per il WebClient andremo a selezionare dal menu a tendina corrispondente il valore "Doppio Fattore con TOTP":

 .. image:: /images/TVOX/Sistema/ConfigurazioneSistema/AccessoSicurezza/esempio1.png


Selezionando almeno una delle opzioni per l'autenticazione a due fattori verranno successivamente mostrate altre due opzioni: 
 
 - **Configurazione TOTP:** sezione che permette di personalizzare le impostazioni dell'autenticazione TOTP abilitando la possibilià di invio email e la durata di validità del Token espresso in minuti.
 - **Configurazione utenti email:** sezione che, abilitando l'opzione di invio email, mette in evidenza gli utenti che non hanno configurata una mail sulla loro anagrafica. 

Una volta effettuata la configurazione, al primo accesso via webclient verrà presentata una schermata di questo tipo:

 .. image:: /images/TVOX/Sistema/ConfigurazioneSistema/AccessoSicurezza/esempio2.png

Scansioniamo tramite l'applicazione che si desidera associare (ad esempio Google Authenticator) ed una volta associato il dispositivo all'utenza, da questo momento in poi possiamo inserire il codice TOTP per accedere al webclient:

.. image:: /images/TVOX/Sistema/ConfigurazioneSistema/AccessoSicurezza/esempio3.png


.. warning:: Una volta applicata la funzionalità di accesso a due fattori, questa è valida per tutti gli utenti TVox che faranno accesso a quell'applicazione. 

Per l'utente, inoltre, nella sezione Anagrafica su OCC è disponibile un pulsante "Reset QR Code" per consentire all'utente di ripetere l'associazione dell'App di autenticazione tramite smartphone. 
Inoltre, è possibile disabilitare per il singolo utente l'autenticazione a due fattori TOTP.

.. image:: /images/TVOX/Sistema/ConfigurazioneSistema/AccessoSicurezza/esempio4.png

