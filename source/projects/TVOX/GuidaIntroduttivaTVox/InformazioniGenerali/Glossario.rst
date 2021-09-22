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
- CJ: Customer Journey
- Insight: Insight Server
- DM: Data Model
- Popup Manager: Consente di invocare script (ad es. per eseguire popup) a fronte di chiamate ricevute dagli utenti di un servizio
- TTS: Text To Speech
- ASR: Automatic Speech Recognition
- STT: Speech To Text
- Notification Service: Consente di richiamare uno o più Web Service di terze parti, notificando gli eventi di chiamata e le relative informazioni
- KB: Knowledge Base
- PD: Power Dialer
- Widget: Form web tramite il quale i clienti possono comunicare utilizzando i canali messi a disposizione da TVox
- Data Retention: Strategia di mantenimento (definizione dei limiti temporali) dei dati all'interno del TVox
- Security Update: Sistema di verifica della consistenza della licenza TVox: attivazione, validità, aggiunta/rimozione di moduli etc.
- Omnichannel RTD: Omnichannel Real Time Display
- TVox Client: Applicazione Client del TVox; funge da Unified Communication Client per gli utenti TVox e da Contact Center Client per gli agenti di Contact Center. Il TVox Client è previsto di default per gli agenti di Contact Center mentre è sottoposto a Licenza per gli utenti base. È accessibile direttamente aprendo una finestra di Chrome oppure installando l'applicazione WinWeb
- WebRTC: Web Real-Time Communication
- WebPhone: Dispositivo di tipo WEB (cuffie collegate al PC) e controllabile tramite TVox Client
- TVox Team App: Applicazione (disponibile sia per Android che per iOS) che consente di estendere i servizi TVox ad utenti in mobiità
- TConsole: Applicazione multipiattaforma (per S.O. Windows) per operatori telefonici vedenti, ipo vedenti e non vedenti
- Smartworking: 
- In House:
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

..  TTS: sintetizzazione vocale della voce a partire da un testo scritto
.. ASR/STT: riconoscimento di un testo a partire da una voce (riconoscimento vocale)
.. - Popup Manager: vedi `Popup Manager`_
