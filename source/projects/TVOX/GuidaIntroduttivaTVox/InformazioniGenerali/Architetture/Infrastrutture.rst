.. _infrastruttura:

===========================
Tipologie di Infrastruttura
===========================

Dalla release 22.0.17 è stata introdotta la gestione della **Modalità di Lavoro**. Per saperne di più clicca :ref:`qui <modalitalavoro>`

Sistemi Pure Cloud
==================

Se vuoi che il tuo |tvox_pbx| o il tuo |tvox| siano completamente in cloud senza alcun tipo di rete privata virtuale o MPLS che 
colleghi i tuoi dispositivi aziendali, TVox Pure Cloud è la funzionalità che fa per te.

Con TVox Pure Cloud hai a disposizione una centrale erogata sulle piattaforme cloud pubbliche più note e ti basta una semplice connessione internet per poter collegare
dispositivi telefonici, gateway per linee isdn, citofoni, e altri hardware che desideri utilizzare.

Per installare un'istanza Pure Cloud innanzi tutto è necessario disporre di una licenza con modulo PURE_CLOUD.

Successivamente, bisogna assicurarsi di disporre di:

- un IP pubblico fisso assegnato all'istanza
- un dominio sul DNS pubblico che risolve l'IP pubblico fisso sopra citato

Questi parametri vanno **obbligatoriamente** configurati nella sezione *Sistema=>Configurazione di sistema=>Dominio*.

.. important:: **ATTENZIONE:** La configurazione dell'ip pubblico e del dominio va effettuata come prima cosa, prima ancora di attivare la licenza sull'istanza.
.. .. important:: La configurazione dell'ip pubblico e del dominio va effettuata come prima cosa, prima ancora di attivare la licenza sull'istanza. In questa fase non sarà ancora possibile attivare il pulsante di accesso via dominio. Questo sarà possibile solamente dopo l'attivazione licenza.

.. Questi parametri vanno **obbligatoriamente** configurati nella sezione *Sistema=>Configurazione di sistema=>Dominio* e attivando il pulsante "Accedi tramite dominio".

.. image:: /images/TVOX/PureCloud/01-domain-configuration_1.png
.. .. image:: /images/TVOX/PureCloud/01-domain-configuration.png

|br|

Networking
----------

Il server TVox Pure Cloud espone alcuni servizi, di conseguenza le seguenti costituiscono le regole da implementare in ingresso da Internet verso TVox:


+---------------+-----------------+----------------------------------------+
|    **Porta**  |  **Protocollo** |                 **Note**               |
+---------------+-----------------+----------------------------------------+
|      5060     |    UDP / TCP    |              Traffico SIP              |
+---------------+-----------------+----------------------------------------+
|      5061     |       TCP       |            Traffico SIP TLS            |
+---------------+-----------------+----------------------------------------+
|      5070     |    UDP / TCP    |   Traffico SIP - Monitoraggio Vendor   |
+---------------+-----------------+----------------------------------------+
|      5071     |       TCP       | Traffico SIP TLS - Monitoraggio Vendor |
+---------------+-----------------+----------------------------------------+
|  10000-20000  |       UDP       |           Traffico RTP / SRTP          |
+---------------+-----------------+----------------------------------------+
|      3478     |    UDP / TCP    |           Server STUN / TURN           |
+---------------+-----------------+----------------------------------------+
| 20001 - 30000 |       UDP       |      Traffico RTP via TURN Server      |
+---------------+-----------------+----------------------------------------+
|      443      |       TCP       | Traffico HTTPS / WEBRTC / Provisioning |
+---------------+-----------------+----------------------------------------+
|       80      |       TCP       |          Nginx / Let's Encrypt         |
+---------------+-----------------+----------------------------------------+



|br|



Sicurezza provisioning e SIP
----------------------------    
In ambiente cloud non è possibile affidarsi alla prestazione di auto-provisioning basato su DHCP.
E\' raccomandata l'abilitazione del provisioning sicuro via OCC dalla sezione *Impostazioni=>Avanzate=>Sicurezza* impostando il parametro "Sicurezza provisioning telefoni" con il valore "Sicuro e RPS".

In tal modo, nel caso si utilizzino dispositivi Yealink, sarò possibile sfruttare il provisioning via RPS (Redirect & Provisioning Service), servizio offerto da Yealink che consente il provisioning automatico del telefono al primo avvio (a seguito di un reset alle condizioni di fabbrica).

Contestualmente si raccomanda di impostare anche il livello di sicurezza per password SIP e utente. L'OCC impedirà di salvare utenti e interni con password che non rispettano adeguati standard di sicurezza.

.. warning:: **ATTENZIONE:** La modifica del parametro "Sicurezza e password utente" porta al riavvio del servizio di autenticazione. Per il tempo necessario al riavvio, non sarà possibile eseguire login.

.. image:: /images/TVOX/PureCloud/02-sicurezza-password-provisioning_2.png


Per eseguire il provisioning segui le indicazioni che trovi :ref:`qui <ProvisioningDispositivi>`


.. :doc:`Ambiente cloud AWS<CloudAWS>`

.. :doc:`Ambiente cloud Azure<./Cloud/CloudAzure>`

.. :doc:`Ambiente cloud Google<./Cloud/CloudGoogle>`

--------------

Sistemi Hybrid
==============


L'architettura di un sistema TVox si può definire **Hybrid/Private Cloud** nel caso in cui TVox sia posto in una infrastruttura cloud ma senza il modulo PURE CLOUD in licenza.

In tali condizioni, la fruizione di linee tradizionali attestate nella sede, l’utilizzo di dispositivi quali gateway ata (fax analogici, cordless, campane ecc) e terminali SIP che eseguono la registrazione su TVox è possibile solamente sfruttando un collegamento MPLS o VPN.

.. image:: /images/TVOX/HybridCloud/schema_hybrid.PNG



Si parla di architettura ibrida anche nel caso di TVox con licenza PURE CLOUD consentendo l’interconnessione di terminali sia in modalità pure cloud sia in modalità tradizionale.




------------------

Sistemi on Premise
==================

L'architettura è intesa come di tipo **On Premise** quando viene utilizzata l'infrastruttura IT dell'azienda, sia in modalità virtualizzata che su server fisico dedicato.

.. image:: /images/TVOX/OnPremise/schema_onprem.PNG

