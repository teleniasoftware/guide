.. _Customer Journey: http://tdoc.teleniasoftware.com/it/latest/projects/CustomerJourney.html
.. _TVox Data Model: http://tdoc.teleniasoftware.com/it/latest/projects/PersonalizzaMonitoraggioServizi/PersonalizzaMonitoraggioServizi.html
.. _Popup Manager: http://tdoc.teleniasoftware.com/it/latest/projects/PopupSchedaContatto/PopupSchedaContatto.html

=========
Glossario
=========

..
	+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
	| **Termine**       | **Definizione**                                                                                                                                                                     |
	+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
	| IP TVox           | Indirizzo IP che identifica il TVox.                                                                                                                                                |
	+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
	| Hostname          | Nome identificativo di TVox all'interno della rete                                                                                                                                  |
	+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
	| Master            | In un sistema di Continuous Monitoring & Reporting è il TVox che funge da sistema telefonico ATTIVO, |br| oppure indica il TVox di riferimento per un TVox Branch Office o Disaster |
	|                   | Recovery.                                                                                                                                                                           |
	+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
	| Slave             | In un sistema di Continuous Monitoring & Reporting è il TVox che funge da sistema telefonico PASSIVO.                                                                               |
	+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
	| Branch Office     | TVox che svolge il ruolo di Failover PBX per una sede remota che non raggiunge il TVox Master.                                                                                      |
	+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
	| Disaster Recovery | TVox che svolge il ruolo di Failover PBX per la sede principale in caso di evento che rende indisponibile il TVox Master.                                                           |
	+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
	| OCC               | TVox Omnichannel Manager: interfaccia WEB di amministrazione di TVox                                                                                                                |
	+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
	|                   |                                                                                                                                                                                     |
	+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
	|                   |                                                                                                                                                                                     |
	+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
	|                   |                                                                                                                                                                                     |
	+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
	|                   |                                                                                                                                                                                     |
	+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
	|                   |                                                                                                                                                                                     |
	+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
	|                   |                                                                                                                                                                                     |
	+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
	|                   |                                                                                                                                                                                     |
	+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
	|                   |                                                                                                                                                                                     |
	+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
	|                   |                                                                                                                                                                                     |
	+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
	|                   |                                                                                                                                                                                     |
	+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
	|                   |                                                                                                                                                                                     |
	+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

- IP TVox: Indirizzo IP che identifica il TVox
- PBX IP/IP di nodo: In un sistema di Continuous Monitoring & Reporting è l'indirizzo IP condiviso (IP virtuale) tra TVox Master e TVox Slave. E' l'IP al quale fare riferimento per fruire dei servizi TVox
- Continuous Monitoring & Reporting: Sistema TVox che consiste di due macchine TVox (Master e Slave), in continua comunicazione (sincronizzazione) tra loro: sul TVox Master sono attivi i processi principali per il funzionamento del sistema (ad es. Asterisk per la parte telefonica), mentre sul TVox Slave la sincronizzazione rende disponibili i dati necessari al monitoraggio del sistema e all'estrazione della reportistica (ad es. CDR, Data Model et.). Il TVox Slave svolge anche il ruolo di Failover PBX eleggendosi a nuovo Master qualora il TVox Master in funzione dovesse rendersi indisponibile
- Hostname: Nome identificativo di TVox all'interno della rete
- Master: In un sistema di Continuous Monitoring & Reporting è il TVox che funge da sistema telefonico ATTIVO, oppure indica il TVox di riferimento per un TVox Branch Office o Disaster Recovery
- Slave: In un sistema di Continuous Monitoring & Reporting è il TVox che funge da sistema telefonico PASSIVO
- Branch Office: TVox che svolge il ruolo di Failover PBX per una sede remota che non raggiunge il TVox Master
- Disaster Recovery: TVox che svolge il ruolo di Failover PBX per la sede principale in caso di evento che rende indisponibile il TVox Master
- TVox Support: TVox che consente di estendere le funzionalità del TVox PBX fornendo servizi quali il canale mail (ticketing), Customer Journey o Insight. Può consistere a sua volta di un sistema ridondato, con un TVox Support Master ed un TVox Support Slave ed un IP Support di nodo
- TVox SBC: Session Border Control
- TVox MCS: Mediant Communication System
- TVox TQM: Telenia Queue Manager
- OCC: TVox Omnichannel Manager: interfaccia WEB di amministrazione di TVox
- Customer Journey (CJ): vedi `Customer Journey`_
- Insight: Insight Server
- Data Model (DM): vedi `TVox Data Model`_
- Popup Manager: vedi `Popup Manager`_
- Text To Speech (TTS): sintetizzazione vocale della voce a partire da un testo scritto
- Automatic Speech Recognition (ASR) / Speech To Text (STT): riconoscimento di un testo a partire da una voce (riconoscimento vocale)
- Notification Service: 
- Knowledge Base: 
- Power Dialer
- Widget
- Data Retention
- Security Update
- Omnichannel RTD 
- TVox Client: Chrome o WinWeb
- WebRTC
- WebPhone
- TVox Team App
- TConsole
- Smartworking
- In House 
- SIP 
- RTP 
- TLS 
- SRTP 
- Peer to Peer (P2P) 
- SMTP 
- SSH 
- DHCP 
- DNS 
- DNIS 
- CLID 
- SIP-URI 
- SOAP 
- LDAP 
- RDP 
- CCBS 
