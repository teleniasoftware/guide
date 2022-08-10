.. _modalitalavoro:

==================
Modalità di lavoro
==================
Con il termine **modalità di lavoro** di TVox si intende la predisposizione del sistema a lavorare in un ambiente di tipo on prem, tipicamente senza necessità di una configurazione NAT 1:1, o a lavorare proprio in modalità NAT 1:1, consentendo in tal modo l'esposizione del sistema su internet.

Le differenze riguardano principalmente configurazioni legate a temi di sicurezza (grado di sicurezza delle password per utenti ad esempio), cosiccome a temi di provisioning e protocollo sip, fino a determinare alcune differenze nel modo in cui la componente server di TVox attiva i propri processi.

Quando devi installare e configurare un nuovo sistema TVox, ti verrà sempre richiesto di scegliere quale sarà la sua modalità di lavoro, che si distingue in


- **Pure Cloud (NAT 1:1)**
- **Standard**


.. important:: La scelta della modalità di lavoro di TVox è la prima configurazione che deve essere effettuata dopo aver attivato la licenza
    
    .. image:: /images/TVOX/ModalitaLavoro/ModalitaLavoro1.PNG


|br|

-------------------------------

Modalità Pure Cloud (NAT 1 a 1)
===============================


La modalità Pure Cloud (NAT 1:1) imposta TVox per funzionare in NAT 1: 1 e , in linea generale, pubblicamente accessibile via Internet.

E\' obbligatorio disporre di indirizzo IP pubblico statico da assegnare a TVox e da configurare nella sezione *OCC-Sistema-Configurazione di sistema-Dominio*.

E\' obbligatorio disporre di un dominio sul DNS pubblico che risolva l’IP pubblico sopra citato. Anche il dominio va configurato nella sezione *OCC-Sistema-Configurazione di sistema-Dominio*.
 
L'abilitazione della modalità Pure Cloud (NAT 1 a 1) imposterà di default le seguenti configurazioni:


**OCC - Sistema - Configurazione di sistema - Autenticazione e Sicurezza - Sicurezza Password e Provisioning** 

- Sicurezza password utente = Sicura
- Sicurezza password Sip = Sicura
- Sicurezza provisioning telefoni = sicuro+RPS abilitato
 

**Parametri per interni SIP** 

- Modalità di trasporto: TLS
- ICE NAT Traversal = Yes per i modelli Yealink supportati
- Peer 2 Peer = No
 
**Provisioning telefoni**
  
- Yealink: è disponibile il provisioning in modalità automatica tramite RPS
- Altri: l'url di provisioning deve essere impostato manualmente sul singolo telefono
- Tutti: tutti i telefoni devono essere ri-provisionati per ottenere i nuovi parametri SIP a seguito di modifiche configurative
 

**Controllo telefonico**
  
- Il controllo telefonico completo è supportato solo per Yealink con firmware >= 81.0.15
- Per tutti gli altri modelli è supportato solo il controllo telefonico parziale (click-to-dial, chiusura chiamata, trasferta cieca)
 

**Client MCS** 
  
Nel caso in cui si proceda a cambiare la modalità di lavoro da Standard a Pure Cloud, eventuali configurazioni di tipo client MCS verranno rimosse e non potranno essere recuperate
  

**Modalità "Smart Working"** 
  
Nel caso in cui si proceda a cambiare la modalità di lavoro da Standard a Pure Cloud, tutti i dispositivi WebRTC e App TVoxTeam saranno utilizzabili via internet. Per tale motivo, per tali dispositivi verrà abilitata la funzionalità "Smart Working".
 

**Server TURN/STUN** 
  
Verrà abilitato un server TURN/STUN co-residente. Questo ha la stessa funzione del server TURN/STUN fornito dal server MCS nel caso di modalità di lavoro Standard con TVox interconnesso a MCS.

|br|

-----------------

Modalità Standard
=================


La modalità cosiddetta Standard identifica un TVox installato ed operante su rete locale o su piattaforma cloud ma non esposto su internet tramite NAT 1 a 1.

Al momento della prima configurazione non vengono eseguite operazioni particolari, per cui a livello sicurezza e configurazioni di sistema si hanno le seguenti impostazioni di default:


**OCC – Sistema - Configurazione di sistema – Autenticazione e Sicurezza – Sicurezza Password e Provisioning** 

- Sicurezza password utente = Non sicura
- Sicurezza password Sip = Non sicura
- Sicurezza provisioning telefoni = Base


**Parametri per interni SIP** 

- Modalità di trasporto: UDP
- ICE NAT Traversal = No
- Peer 2 Peer = Yes


**Provisioning telefoni** 

Il provisioning è disponibile tramite configurazione manuale sui dispositivi dell’url di provisioning
se disponibile un server DHCP, è possibile configurare su di esso le opportune direttive per attivare il cosiddetto autoprovisioning


**Modalità "Smart Working"** 

La modalità smart working è attivabile sui singoli utenti per client e/o app TVox Team a fronte della disponibilità su TVox delle licenze di tipo smartworking e della realizzazione architetturale che prevede TVox collegato ad un MCS come descritto in guida
http://guide.teleniasoftware.com/it/22/projects/TVOXMediantCommunicationSystem/Prodotto.html


.. NOTE:: **Passaggio da modalità Pure Cloud a Standard** 
    Se si passa dalla modalità Pure Cloud alla modalità Standard verranno effettuate le seguenti operazioni:
      - Disabilitazione del supporto ICE per i telefoni Yealink
      - Disabilitato il server TURN/STUN co-residente
      - Disabilitato lo smart-working per tutti gli utenti
  

 
 
