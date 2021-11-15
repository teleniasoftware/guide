===============
Networking
===============


.. important::
  TVox MCS, essendo un server che va esposto su internet, deve risiedere in una DMZ e *non deve avere alcun tipo di visibilità verso le LAN locali*.

  Per il corretto funzionamento della fonia WebRTC le richieste http di TVox Web Client, TVox Team e TVox **non** devono transitare da un proxy.

---------------
MCS
---------------

Porte in ingresso da Internet a MCS:
------------------------------------

+----------------+-------------+---------------------------------------+---------------------------------------------------------------+
| Protocollo     | Porte       |              Servizio                 |                   Note e limitazioni                          |
+================+=============+=======================================+===============================================================+
|   UDP/TCP      |     3478    |            Stun/turn server           |                                                               |
+----------------+-------------+---------------------------------------+---------------------------------------------------------------+
|     UDP        | 10000–20000 |             RTP SRTP DTLS             |                                                               |
+----------------+-------------+---------------------------------------+---------------------------------------------------------------+
|   UDP/TCP      |     1194    | Server OpenVPN per tunnel VPN da TVox | Limitabile ai soli IP pubblici dei TVox se conosciuti         |
+----------------+-------------+---------------------------------------+---------------------------------------------------------------+
|     TCP        |      80     |         HTTP redirect to HTTPS        |                                                               |
+----------------+-------------+---------------------------------------+---------------------------------------------------------------+
|     TCP        |     443     |    HTTPS TVox WebClient / Teams App   |                                                               |
+----------------+-------------+---------------------------------------+---------------------------------------------------------------+
|     TCP        |      22     |                  SSH                  | Solo per gli IP di amministrazione e IP pubblici Telenia      |
|                |             |                                       | |br| (79.8.39.108/32 e 93.39.91.217/32)                       |
+----------------+-------------+---------------------------------------+---------------------------------------------------------------+

Porte in uscita da MCS a Internet:
----------------------------------

+------------+------------+-------------------------+-----------------------------------------------------------------+
| Protocollo |  Porte     |         Servizio        |                        Note e limitazioni                       |
+============+============+=========================+=================================================================+
|     TCP    |   443      |          HTTPS          | Richiesto per:                                                  |
|            |            |                         |                                                                 |
|            |            |                         | * Accesso license server Telenia                                |
|            |            |                         | * Integrazione Let’s Encrypt                                    |
+------------+------------+-------------------------+-----------------------------------------------------------------+
|   UDP/TCP  |   53       |           DNS           |                                                                 |
+------------+------------+-------------------------+-----------------------------------------------------------------+
|     TCP    | 25,465,587 | Invio e-mail di allarme | Limitabile all’IP del servizio di posta e alla porta utilizzata |
+------------+------------+-------------------------+-----------------------------------------------------------------+
|     UDP    |     123    |        NTP              |                                                                 |
+------------+------------+-------------------------+-----------------------------------------------------------------+


.. note::
  Per garantire il supporto di Telenia dev'essere consentito l'accesso dagli ip pubblici 79.8.39.108 e 93.39.91.217.

----
TVox
----

Porte in uscita da TVox a MCS:
------------------------------

+------------+-------------+------------------+--------------------+
| Protocollo |    Porte    |     Servizio     | Note e limitazioni |
+============+=============+==================+====================+
|   UDP/TCP  |     3478    | Stun/turn server |                    |
+------------+-------------+------------------+--------------------+
|     UDP    | 10000–20000 |   RTP SRTP DTLS  |                    |
+------------+-------------+------------------+--------------------+
|   UDP/TCP  |     1194    |  tunnel OpenVPN  |                    |
+------------+-------------+------------------+--------------------+

Porte in uscita da TVox a Internet:
-----------------------------------

+------------+---------------+----------------------------------+------------------------------------------------------------------+
| Protocollo |     Porte     |             Servizio             |                        Note e limitazioni                        |
+============+===============+==================================+==================================================================+
|     TCP    |      443      |              HTTPS               | Accesso license server Telenia                                   |
+------------+---------------+----------------------------------+------------------------------------------------------------------+
|   UDP/TCP  |       53      |               DNS                |                                                                  |
+------------+---------------+----------------------------------+------------------------------------------------------------------+
|     TCP    |  25,465,587   |     Invio e-mail di allarme      |  Limitabile all’IP del servizio di posta e alla porta utilizzata |
+------------+---------------+----------------------------------+------------------------------------------------------------------+
|     UDP    |     123       |               NTP                |                                                                  |
+------------+---------------+----------------------------------+------------------------------------------------------------------+

Porte in ingresso da Internet a TVox:
-------------------------------------

Non è richiesta alcuna esposizione pubblica da Internet per la corretta interconnessione con il servizio offerto da MCS.

.. note::
  Se TVox deve instaurare trunk sip verso sistemi in cloud va garantita la comunicazione diretta verso tali sistemi.

--------------------
Postazioni operatori
--------------------

In modalità in-house, la comunicazione da TVox verso TVox Web Client o TVox Team deve essere di tipo LAN-to-LAN (no NAT).

.. note:: In assenza di visibilità LAN-to-LAN tra TVox e TVox Web Client / TVox Team i flussi audio e video dovranno necessariamente transitare attraverso Internet utilizzando il servizio Stun/Turn di TVox MCS.

Per limitare il traffico in uscita delle postazioni degli operatori è necessario consentire almeno le seguenti regole:


Da TVox Web Client / TVox Team a MCS:
---------------------------------

+------------+-------------+-----------------------+--------------------+
| Protocollo |    Porte    |       Servizio        | Note e limitazioni |
+============+=============+=======================+====================+
|     TCP    |     443     | HTTPS TVox Web Client |                    |
+------------+-------------+-----------------------+--------------------+
|   TCP/UDP  |     3478    |   Stun/Turn server    |                    |
+------------+-------------+-----------------------+--------------------+
|     UDP    | 10000-20000 |     RTP SRTP DTLS     |                    |
+------------+-------------+-----------------------+--------------------+

Da TVox Web Client / TVox Win Web Client / TVox Team a TVox in LAN:
-----------------------------------------

+------------+-------------+-----------------------+--------------------+
| Protocollo |    Porte    |        Servizio       | Note e Limitazioni |
+------------+-------------+-----------------------+--------------------+
|     TCP    |     443     | HTTPS TVox Web Client |                    |
+------------+-------------+-----------------------+--------------------+
|     UDP    | 10000-20000 |     RTP SRTP DTLS     |                    |
+------------+-------------+-----------------------+--------------------+

Da TVox Win Web Client a TVox in LAN:
-----------------------------------------

+------------+-----------+--------------------------+--------------------+
| Protocollo |   Porte   |         Servizio         | Note e Limitazioni |
+------------+-----------+--------------------------+--------------------+
|     TCP    |     80    | HTTP TVox Win Web Client |                    |
+------------+-----------+--------------------------+--------------------+
|     UDP    | 5060-5063 |            SIP           |                    |
+------------+-----------+--------------------------+--------------------+


Da TVox a TVox Web Client / TVox Win Web Client / TVox Team in LAN:
-----------------------------------------

+------------+-------------+----------------------+--------------------+
| Protocollo |    Porte    |       Servizio       | Note e limitazioni |
+============+=============+======================+====================+
|     UDP    |  1024-65536 |     RTP SRTP DTLS    |                    |
+------------+-------------+----------------------+--------------------+


.. note:: I **requisiti applicativi** per il TVox Win Web Client sono i seguenti: |br| **1.** Sistema operativo >= windows 8 e necessariamente a 64bit. |br| **2.** L'HW del sistema deve garantire il pieno supporto alla libreria QtWebEngine che si occupa del render OPENGL del client. Abbiamo riscontrato parecchie issue bug su driver intel parecchio datate come ad esempio Intel HD 530. In questo caso la libreria, a causa di una mala gestione dei drivers intel, è incompatibile producendo crash applicativi.

.. note:: I dispositivi **IOS** devono poter raggiungere i servizi di notifca PUSH di Apple. |br| Vedere https://support.apple.com/en-us/HT203609

.. note:: I dispositivi **Android** devono poter raggiungere i servizi di notifca PUSH di Android. |br| Vedere https://firebase.google.com/docs/cloud-messaging/concept-options#messaging-ports-and-your-firewall
