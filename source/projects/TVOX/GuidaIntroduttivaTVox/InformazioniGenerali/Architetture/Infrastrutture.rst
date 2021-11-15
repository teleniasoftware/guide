.. _infrastruttura:
===========================
Tipologie di Infrastruttura
===========================

------------------

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
..Questi parametri vanno **obbligatoriamente** configurati nella sezione *Sistema=>Configurazione di sistema=>Dominio* e attivando il pulsante "Accedi tramite dominio".

.. image:: /images/TVOX/PureCloud/01-domain-configuration_1.png
.. .. image:: /images/TVOX/PureCloud/01-domain-configuration.png


.. important:: **ATTENZIONE:** La configurazione dell'ip pubblico e del dominio va effettuata come prima cosa, prima ancora di attivare la licenza sull'istanza.
.. .. important:: La configurazione dell'ip pubblico e del dominio va effettuata come prima cosa, prima ancora di attivare la licenza sull'istanza. In questa fase non sarà ancora possibile attivare il pulsante di accesso via dominio. Questo sarà possibile solamente dopo l'attivazione licenza.


Il server TVox Pure Cloud espone i seguenti servizi:


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

Sicurezza provisioning e SIP
============================
In ambiente cloud non è possibile affidarsi alla prestazione di auto-provisioning basato su DHCP.
E\' raccomandata l'abilitazione del provisioning sicuro via OCC dalla sezione *Impostazioni=>Avanzate=>Sicurezza* impostando il parametro "Sicurezza provisioning telefoni" con il valore "Sicuro e RPS".

In tal modo, nel caso si utilizzino dispositivi Yealink, sarò possibile sfruttare il provisioning via RPS (Redirect & Provisioning Service), servizio offerto da Yealink che consente il provisioning automatico del telefono al primo avvio (a seguito di un reset alle condizioni di fabbrica.

Contestualmente si raccomanda di impostare anche il livello di sicurezza per password SIP e utente. L'OCC impedirà di salvare utenti e interni con password che non rispettano adeguati standard di sicurezza.

.. warning:: **ATTENZIONE:** La modifica del parametro "Sicurezza e password utente" porta al riavvio del servizio di autenticazione. Per il tempo necessario al riavvio, non sarà possibile eseguire login.

.. image:: /images/TVOX/PureCloud/02-sicurezza-password-provisioning.png


.. :doc:`Ambiente cloud AWS<CloudAWS>`

.. :doc:`Ambiente cloud Azure<./Cloud/CloudAzure>`

.. :doc:`Ambiente cloud Google<./Cloud/CloudGoogle>`

--------------

Sistemi Hybrid
==============





------------------

Sistemi on Premise
==================

