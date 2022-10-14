.. _accesscontrol:

=======================
Controllo degli Accessi
=======================

Come sistema di comunicazione aziendale TVox assume un ruolo fondamentale nella quotidianità operativa e nella gestione di dati. Per questi motivi, la sicurezza è tenuta in particolare attenzione.

Uno dei punti cardine in tal senso è il tema della sicurezza degli accessi al sistema, che riguarda principalmente la definizione di opportuni criteri di robustezza per le password degli utenti e dei dispositivi.

Tutte le password definite su TVox vengono salvate internamente e crittografate tramite algoritmo SHA-256.

Veniamo ai criteri di definizione della sicurezza per le password.

------------------------------

**Protezione dell'accesso all'interfaccia di amministrazione OCC attraverso l'utilizzo di password sicura per l'utente admin** 

La configurazione di TVox viene effettuata completamente attraverso l'interfaccia web OCC, per cui è importante scegliere per l'utente admin una password con criteri di sicurezza molto elevati

La password dell'utente admin può essere modificata come mostrato di seguito

|br|

.. image:: /images/TVOX/Privacy&Security/adminpwd1.PNG


|br|

.. image:: /images/TVOX/Privacy&Security/adminpwd2.PNG


------------------------------


**Protezione dell'accesso per gli utenti di sistema (utenti di risposta, agenti di contact center, utenti posto operatore)** 


La procedura di autenticazione degli utenti sulle applicazioni di lavoro (Tvox Client, Tvox Team, OCC, RTD) può avvenire nelle seguenti modalità:

- inserimento di username e password personali definite localmente su TVox (Autenticazione locale)
- inserimento di username e password personali definite su LDAP esterno opportunamente agganciato a Tvox (Autenticazione su server LDAP esterno)

In entrambi i casi precedenti, è possibile attivare la modalità di autenticazione a 2 fattori gestita tramite una qualsiasi app per la generazione di un codice TOTP, ad esempio microsoft authenticator, google authenticator, duo mobile o similari, ma anche via mail una volta che il codice è stato memorizzato sull'app (questo al fine di consentire il login ad un utente che ha scordato o smarrito lo smartphone).

Se si opta per l'autenticazione locale, è raccomandata la scelta di definire un livello di sicurezza massimo per le password degli utenti attraverso il parametro Sicurezza Password Utente disponibile in OCC nella sezione *Sistema - Configurazione di sistema - Autenticazione e Sicurezza* nel riquadro *Sicurezza Password e Provisioning*.

|br|

.. image:: /images/TVOX/Privacy&Security/userpwd.PNG


Nel caso di autenticazione locale, è possibile stabilire anche la gestione della scadenza temporale delle password ogni 45 giorni.


.. important:: Nel caso di Autenticazione su server LDAP esterno i criteri di sicurezza e gestione delle password sono definiti e gestiti sul server LDAP stesso



------------------------------


**Protezione dell'accesso per i dispositivi SIP** 

Così come per gli utenti, anche i dispositivi SIP hanno bisogno di una password per effettuare la registrazione su TVox. Anche in questo caso, si raccomanda la scelta di definire password con livello di sicurezza elevato.

Per i dispositivi SIP, come per gli utenti, è possibili stabilire il livello di sicurezza che le password devono rispettare

|br|

.. image:: /images/TVOX/Privacy&Security/sippwd.PNG









