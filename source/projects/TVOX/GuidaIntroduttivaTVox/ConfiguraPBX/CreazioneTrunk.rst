===============
Creazione Trunk
===============


Definizioneeeeeee
============

Il SIP Trunking è una connessione telefonica esterna in arrivo da un ITSP , ovvero un internet telephony Service Provider, o fornitore di telefonia VoIP. 
 
Il SIP trunking si basa su linee voce che transitano sulla connessione IP e/o internet. 
 
Utilizza il protocollo standard SIP (Session Initiation Protocol).




--------------

Configurazione
===============

Per configurare un **Trunk VOIP** è necessario andare da OCC nella sezione *Canali => Telefono => Trunk*

.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/CreazioneTrunk/01_TRUNK_VOIP.JPG




**Possibili configurazione Trunk VOIP**

Esistono 3 possibili configurazioni ammesse 

#. Sulla base IP
#. TVOX si registra su Trunk
#. Trunk si registra su TVOX

Nella configurazione su **base IP**, l'autenticazione avviene solamente 
impostando l'indirizzo ip del trunk nella voce *Hostname o IP del dispositivo telefonico* .

.. important:: **BEST PRACTICE:** Per un concetto legato alla sicurezza, in ambiente cloud è sconsigliato utilizzare l'autenticazione sulla base IP, 

Nella configurazione dove **TVOX si registra su Trunk** 
è necessario impostare la stringa di registrazione così come riportato nella figura precedente .
Tale configurazione normalmente viene utilizzata per trunk Voip su internet 

.. important:: **BEST PRACTICE:** Quando la comunicazione avviene tramite ip pubblici, nelle impostazioni avanzate del trunk è importante togliere il flag dalla voce "peer to peer"
     
     .. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/CreazioneTrunk/02_TRUNK_VOIP.JPG

 
Nella configurazione dove **Trunk si registra su TVOX** 
è importante compilare le voci *Username* e *Password*. Nel campo *Hostname o IP del dispositivo telefonico* riportare la dicitura *dynamic*
Di norma tale configurazione viene utilizzata per trunk Voip collegati a linee ISDN tradizionali (Patton,Audicodes,etc) 



.. important:: **BEST PRACTICE:** Qualora si intenda esporre TVox Communication alla rete Internet occorre garantire l'opportuno livello di sicurezza dotandosi di appositi apparati di rete. Per vietare qualsiasi richiesta esterna che da Internet interessi il TVox Communication è necessario autorizzare sui sistemi di sicurezza le sole richieste provenienti dai sistemi VOIP coinvolti nella configurazione dei trunk. Il TVox Communication non consente comunicazioni VOIP anonime provenienti da Internet se non attraverso l'utilizzo di un Server SIP Proxy dedicato.


.. note:: **Peer to Peer:** Nel caso in cui la comunicazione sia Peer to Peer il canale RTP è direttamente instaurato tra i dispositivi, dinamicamente tale canale si instaura sul TVox quando il dispositivo richiede una funzionalità erogata sul PBX
     
.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/CreazioneTrunk/PEER_TO_PEER.JPG



