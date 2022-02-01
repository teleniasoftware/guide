=========================
Caricare un Certicato SSL
=========================

Per la gestione dei certificati è necessario andare in OCC nella sezione *SISTEMA=> Accesso servizi=> Certificato SSL*

Carica certificato
==================

E\' possibile caricare un nuovo certificato o aggiornare il certificato corrente.

La catena di certificazione è composta da:

- *Chiave Privata*
- Certificato contenente la *Chiave Pubblica*
- Certificati intermedi (opzionali)


Il caricamento può avvenire in quattro modalità:


**File unico**, contenente l'intera catena di certificazione. Se crittografato, è necessario fornire anche una password. In questo caso sono supportati solo file crittografati in formato PKCS12 (pfx).  
   
    .. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/Certificati/SSL_File_Unico.JPG


**Chiave Privata e Certificato**, dove il certificato deve contenere almeno la *Chiave Pubblica*. Sia per il certificato che per la *Chiave Privata*, è possibile caricare file crittografati con password rispettando i formati supportati, ovvero PKCS12 per il certificato (pfx) e PKCS8 per la chiave privata.
    
    .. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/Certificati/SSL_Chiave_Privata.JPG


**File separati**, dove *Chiave Privata*, *Certificato con Chiave Pubblica* e *Certificati intermedi* vengono caricati separatamente.
    
    .. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/Certificati/SSL_File_Separati.JPG


**Certificato MCS**, pacchetto ZIP contenente il certificato generato dall'MCS; il pacchetto deve essere scaricato dall'interfaccia di gestione certificati su MCS e deve contenere almeno il file del certificato pubblico (.crt), il file della chiave privata (.key) e il file del certificato completo (.pem)
    
    .. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/Certificati/SSL_File_Separati.JPG


Richiesta firma certificato
===========================

In questa sezione è possibile generare e scaricare una nuova richiesta di firma del certificato certificato per il dominio richiesto.

.. important:: La richiesta deve essere inoltrata ad una CA (Certification Authority) la quale fornirà un certificato valido per il dominio specificato.


Integrazione Let's Encrypt
===========================

E\' anche possibile abilitare l'utilizzo di certificati SSL gratuiti forniti da Let's Encrypt.

   .. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/Certificati/LetSEncrypt.JPG

.. important:: **BEST PRACTICE:** Deve essere stato precedentemente configurato un nome di dominio risolto pubblicamente verso l'indirizzo IP pubblico del server. Inoltre la porta 80 deve essere aperta e raggiungibile dai server Let's Encrypt. Il server deve poter uscire verso internet per raggiungere i servizi Let's Encrypt. I certificati hanno durata di 90 giorni e verranno automaticamente rinnovati.
