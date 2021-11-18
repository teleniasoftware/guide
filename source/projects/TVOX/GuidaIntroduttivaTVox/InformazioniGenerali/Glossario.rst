.. _Customer Journey: http://tdoc.teleniasoftware.com/it/latest/projects/CustomerJourney.html
.. _TVox Data Model: http://tdoc.teleniasoftware.com/it/latest/projects/PersonalizzaMonitoraggioServizi/PersonalizzaMonitoraggioServizi.html
.. _Popup Manager: http://tdoc.teleniasoftware.com/it/latest/projects/PopupSchedaContatto/PopupSchedaContatto.html

=========
Glossario
=========

+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| ASR / STT                         | | Automatic Speech Recognition / Speech To Text: Riconoscimento di un testo a partire da una voce                       |
|                                   | | (riconoscimento vocale)                                                                                               |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| Branch Office                     | TVox che svolge il ruolo di Failover PBX per una sede remota che non raggiunge il TVox Master                           |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| CCBS                              | Completion of Calls to Busy Subscriber: servizio di prenotazione chiamata su occupato                                   |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| CJ                                | Customer Journey: Insieme delle interazioni multicanale del cliente con il |tvox|                                       |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| CLID                              | Calling Line Identifier: identifica il numero telefonico dell'utente chiamante                                          |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------+
|                                   | | Sistema TVox che consiste di due macchine TVox (Master e Slave), in continua comunicazione                            |
|                                   | | (sincronizzazione) tra loro: sul TVox Master sono attivi i processi principali per il funzionamento                   |
|                                   | | del sistema (ad es. Asterisk per la parte telefonica), mentre sul TVox Slave la sincronizzazione                      |
| Continuous Monitoring & Reporting | | rende disponibili i dati necessari al monitoraggio del sistema e all'estrazione della reportistica                    |
|                                   | | (ad es. CDR, Data Model et.).                                                                                         |
|                                   | | Il TVox Slave svolge anche il ruolo di Failover PBX eleggendosi a nuovo Master qualora il TVox                        |
|                                   | | Master dovesse rendersi indisponibile                                                                                 |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| DHCP                              | Dynamic Host Configuration Protocol                                                                                     |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| DM                                | | Data Model: Consente l'accesso ai dati TVox, consentendo ad es. la creazione di report e dashboard                    |
|                                   | | personalizzati oltre alla reportistica già disponibile in |tvox|                                                      |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| DNIS                              | Dialed Number Identification Service: identifica il numero telefonico digitato dall'utente chiamante                    |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| DNS                               | Domain Name System                                                                                                      |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| Data Retention                    | Strategia di mantenimento (definizione dei limiti temporali) dei dati all'interno del TVox                              |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| Disaster Recovery                 | | TVox che svolge il ruolo di Failover PBX per la sede principale in caso di evento che rende                           |
|                                   | | indisponibile il TVox Master                                                                                          |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| Hostname                          | Nome identificativo di TVox all'interno della rete                                                                      |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| IP TVox                           | Indirizzo IP che identifica il TVox                                                                                     |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| In House                          | | Modalità di accesso alle funzionalità TVox (TVox Client o TVox Team App) da rete interna                              |
|                                   | | all'infrastruttura TVox (rete locale)                                                                                 |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| Insight                           | Insight Server: TVox che mette a disposizione le dashboard evolute per il monitoraggio del |tvox|                       |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| KB                                | | Knowledge Base: Funzionalità TVox che mette a disposizione contenuti consultabili e organizzati                       |
|                                   | | in categorie e sottocategorie                                                                                         |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| LDAP                              | | Lightweight Directory Access Protocol: è un protocollo standard per l'interrogazione e la modifica                    |
|                                   | | dei servizi di directory che gestiscono informazioni condivise disponibili tramite la rete                            |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| Master                            | | In un sistema di Continuous Monitoring & Reporting è il TVox che funge da sistema telefonico ATTIVO,                  |
|                                   | | oppure indica il TVox di riferimento per un TVox Branch Office o Disaster Recovery                                    |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| Notification Service              | | Consente di richiamare uno o più Web Service di terze parti, notificando gli eventi di chiamata                       |
|                                   | | e le relative informazioni                                                                                            |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| OCC                               | TVox Omnichannel Manager: Interfaccia WEB di amministrazione di TVox                                                    |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| Omnichannel RTD                   | Omnichannel Real Time Display                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| PBX IP/IP di nodo                 | | In un sistema di Continuous Monitoring & Reporting è l'indirizzo IP condiviso (IP virtuale) tra                       |
|                                   | | TVox Master e TVox Slave. È l'IP al quale fare riferimento per fruire dei servizi TVox                                |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| PD                                | Power Dialer: Strumento di generazione automatica di chiamate outbound per il                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| Peer to Peer (P2P)                | Comunicazione audio / video ove i canali RTP sono stabiliti direttamente tra i due interlocutori                        |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| Popup Manager                     | | Consente di invocare script (ad es. per eseguire popup) a fronte di chiamate ricevute dagli utenti                    |
|                                   | | di un servizio                                                                                                        |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| RDP                               | Remote Desktop Protocol                                                                                                 |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| RTP                               | Real-time Transport Protocol                                                                                            |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| SIP                               | Session Initiation Protocol                                                                                             |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| SIP-URI                           | Rappresenta lo schema di indirizzamento SIP per chiamare un altro soggetto attraverso il protocollo SIP                 |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| SMTP                              | Simple Mail Transfer Protocol                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| SOAP                              | Simple Object Access Protocol                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| SRTP                              | Secure Real-time Transport Protocol                                                                                     |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| SSH                               | Secure Shell                                                                                                            |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| Security Update                   | | Sistema di verifica della consistenza della licenza TVox: attivazione, validità, aggiunta/rimozione                   |
|                                   | | di moduli, abilitazione all'upgrade                                                                                   |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| Slave                             | In un sistema di Continuous Monitoring & Reporting è il TVox che funge da sistema telefonico PASSIVO                    |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| Smartworking                      | | Modalità di accesso alle funzionalità TVox (TVox Client o TVox Team App) da rete esterna                              |
|                                   | | all'infrastruttura TVox (internet)                                                                                    |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| TConsole                          | | Applicazione multipiattaforma (per S.O. Windows) per la gestione del Posto Operatore (centralinista)                  |
|                                   | | da parte di operatori telefonici vedenti, ipo vedenti e non vedenti                                                   |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| TLS                               | Transport Layer Security                                                                                                |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| TTS                               | Text To Speech: Sintetizzazione vocale della voce a partire da un testo scritto                                         |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------+
|                                   | | Applicazione Client del TVox; funge da Unified Communication Client per gli utenti TVox                               |
|                                   | | e da Contact Center Client per gli agenti di Contact Center.                                                          |
| TVox Client                       | | Il TVox Client è previsto di default per gli agenti di Contact Center mentre è sottoposto a Licenza                   |
|                                   | | per gli utenti base.                                                                                                  |
|                                   | | È accessibile direttamente aprendo una finestra di Chrome (|client|)                                                  |
|                                   | | oppure installando l'applicazione WinWeb (|winweb|)                                                                   |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------+
|                                   | | Mediant Communication System: TVox che consente di accedere tramite semplice connettività internet                    |
| TVox MCS                          | | alle funzionalità del TVox in sede, senza esporre direttamente quest'ultimo su internet.                              |
|                                   | | È necessario per fruire di TVox Team App (sia in house che in Smartworking) e della Widget                            |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------+
|                                   | | Session Border Control: TVox utilizzato per interconnessione tra il TVox principale posizionato                       |
| TVox SBC                          | | in Data Center e sedi periferiche che devono comunicare con il TVox principale,                                       |
|                                   | | senza necessità di stabilire una VPN                                                                                  |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------+
|                                   | | TVox che consente di estendere le funzionalità del TVox PBX fornendo servizi quali                                    |
| TVox Support                      | | il canale mail (ticketing), Customer Journey o Insight.                                                               |
|                                   | | Può consistere a sua volta di un sistema ridondato, con un TVox Support Master                                        |
|                                   | | ed un TVox Support Slave ed un TVox Support di nodo                                                                   |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| TVox TQM                          | | Telenia Queue Manager: TVox che svolge la funzione di gestione delle chiamate                                         |
|                                   | | per servizi di tipo Posto Operatore                                                                                   |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| TVox Team App                     | | Applicazione (disponibile sia per Android che per iOS)                                                                |
|                                   | | che consente di estendere i servizi TVox ad utenti in mobiità                                                         |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| WebPhone                          | Dispositivo di tipo WEB (cuffie collegate al PC) e controllabile tramite TVox Client                                    |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| WebRTC                            | | Web Real-Time Communication: tecnologia che consente ad applicazioni web di trasmettere flusso                        |
|                                   | | audio o video in modalità Peer to Peer e senza richiedere l'installazione di plugin o altri software                  |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| Widget                            | Form web tramite il quale i clienti possono comunicare utilizzando i canali messi a disposizione da TVox                |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------+

..
	- IP TVox: Indirizzo IP che identifica il TVox
	- PBX IP/IP di nodo: In un sistema di Continuous Monitoring & Reporting è l'indirizzo IP condiviso (IP virtuale) tra TVox Master e TVox Slave. È l'IP al quale fare riferimento per fruire dei servizi TVox
	- Continuous Monitoring & Reporting: Sistema TVox che consiste di due macchine TVox (Master e Slave), in continua comunicazione (sincronizzazione) tra loro: sul TVox Master sono attivi i processi principali per il funzionamento del sistema (ad es. Asterisk per la parte telefonica), mentre sul TVox Slave la sincronizzazione rende disponibili i dati necessari al monitoraggio del sistema e all'estrazione della reportistica (ad es. CDR, Data Model et.). Il TVox Slave svolge anche il ruolo di Failover PBX eleggendosi a nuovo Master qualora il TVox Master dovesse rendersi indisponibile
	- Hostname: Nome identificativo di TVox all'interno della rete
	- Master: In un sistema di Continuous Monitoring & Reporting è il TVox che funge da sistema telefonico ATTIVO, oppure indica il TVox di riferimento per un TVox Branch Office o Disaster Recovery
	- Slave: In un sistema di Continuous Monitoring & Reporting è il TVox che funge da sistema telefonico PASSIVO
	- Branch Office: TVox che svolge il ruolo di Failover PBX per una sede remota che non raggiunge il TVox Master
	- Disaster Recovery: TVox che svolge il ruolo di Failover PBX per la sede principale in caso di evento che rende indisponibile il TVox Master
	- TVox Support: TVox che consente di estendere le funzionalità del TVox PBX fornendo servizi quali il canale mail (ticketing), Customer Journey o Insight. Può consistere a sua volta di un sistema ridondato, con un TVox Support Master ed un TVox Support Slave ed un IP Support di nodo
	- TVox SBC: Session Border Control: TVox utilizzato per interconnessione tra il TVox principale posizionato in Data Center e sedi periferiche che devono comunicare con il TVox principale, senza necessità di stabilire una VPN
	- TVox MCS: Mediant Communication System: TVox che consente di accedere tramite semplice connettività internet alle funzionalità del TVox in sede, senza esporre direttamente quest'ultimo su internet. È necessario per fruire di TVox Team App (sia in house che in Smartworking) e della Widget
	- TVox TQM: Telenia Queue Manager: TVox che svolge la funzione di gestione delle chiamate del servizio di tipo Posto Operatore
	- OCC: TVox Omnichannel Manager: Interfaccia WEB di amministrazione di TVox
	- CJ: Customer Journey: Insieme delle interazioni multicanale del cliente con il |tvox|. È consultabile in un'apposita sezione del TVox Client
	- Insight: Insight Server: TVox che mette a disposizione le dashboard evolute per il monitoraggio del |tvox|
	- DM: Data Model: Consente l'accesso ai dati TVox, consentendo ad es. la creazione di report e dashboard personalizzati oltre alla reportistica già disponibile in |tvox|
	- Popup Manager: Consente di invocare script (ad es. per eseguire popup) a fronte di chiamate ricevute dagli utenti di un servizio
	- TTS: Text To Speech: Sintetizzazione vocale della voce a partire da un testo scritto
	- ASR: Automatic Speech Recognition: (sinonimo di STT) Riconoscimento di un testo a partire da una voce (riconoscimento vocale)
	- STT: Speech To Text: (sinonimo di ASR) Riconoscimento di un testo a partire da una voce (riconoscimento vocale)
	- Notification Service: Consente di richiamare uno o più Web Service di terze parti, notificando gli eventi di chiamata e le relative informazioni
	- KB: Knowledge Base: Funzionalità TVox che mette a disposizione contenuti consultabili e organizzati in categorie e sottocategorie
	- PD: Power Dialer: Strumento di generazione automatica di chiamate outbound per il |tvox|
	- Widget: Form web tramite il quale i clienti possono comunicare utilizzando i canali messi a disposizione da TVox
	- Data Retention: Strategia di mantenimento (definizione dei limiti temporali) dei dati all'interno del TVox
	- Security Update: Sistema di verifica della consistenza della licenza TVox: attivazione, validità, aggiunta/rimozione di moduli etc.
	- Omnichannel RTD: Omnichannel Real Time Display
	- TVox Client: Applicazione Client del TVox; funge da Unified Communication Client per gli utenti TVox e da Contact Center Client per gli agenti di Contact Center. Il TVox Client è previsto di default per gli agenti di Contact Center mentre è sottoposto a Licenza per gli utenti base. È accessibile direttamente aprendo una finestra di Chrome oppure installando l'applicazione WinWeb
	- WebRTC: Web Real-Time Communication
	- WebPhone: Dispositivo di tipo WEB (cuffie collegate al PC) e controllabile tramite TVox Client
	- TVox Team App: Applicazione (disponibile sia per Android che per iOS) che consente di estendere i servizi TVox ad utenti in mobiità
	- TConsole: Applicazione multipiattaforma (per S.O. Windows) per operatori telefonici vedenti, ipo vedenti e non vedenti
	- Smartworking: Modalità di accesso alle funzionalità TVox (TVox Client o TVox Team App) da rete esterna all'infrastruttura TVox (internet)
	- In House: Modalità di accesso alle funzionalità TVox (TVox Client o TVox Team App) da rete interna all'infrastruttura TVox (rete locale)
	- SIP: Session Initiation Protocol
	- RTP: Real-time Transport Protocol
	- TLS: Transport Layer Security
	- SRTP: Secure Real-time Transport Protocol
	- Peer to Peer (P2P): Comunicazione audio / video ove i canali RTP sono stabiliti direttamente tra i due interlocutori
	- SMTP: Simple Mail Transfer Protocol
	- SSH: Secure Shell
	- DHCP: Dynamic Host Configuration Protocol
	- DNS: Domain Name System
	- DNIS: Dialed Number Identification Service: identifica il numero telefonico digitato dall'utente chiamante
	- CLID: Calling Line Identifier: identifica il numero telefonico dell'utente chiamante
	- SIP-URI: Rappresenta lo schema di indirizzamento SIP per chiamare un altro soggetto attraverso il protocollo SIP
	- SOAP: Simple Object Access Protocol
	- LDAP: Lightweight Directory Access Protocol: è un protocollo standard per l'interrogazione e la modifica dei servizi di directory che gestiscono informazioni condivise disponibili tramite la rete
	- RDP: Remote Desktop Protocol
	- CCBS: Completion of Calls to Busy Subscriber: servizio di prenotazione chiamata su occupato
