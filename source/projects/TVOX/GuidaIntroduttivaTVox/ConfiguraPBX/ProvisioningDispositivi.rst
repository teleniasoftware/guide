.. _ProvisioningDispositivi:

============
Provisioning
============

Passiamo ora in rassegna gli argomenti che riguardano la configurazione dei dispositivi
telefonici che può essere gestita centralmente in TVox grazie al modulo di Provisioning dei
telefoni configurabile al menu *Canali=>Telefono=>modelli di telefono* e  *Canali=>Telefono=>interni*.

.. note:: Attraverso il modulo di Provisioning è possibile da TVox aggiornare il firmware e la configurazione dei telefoni in modalità centralizzata. Il provisioning si basa sull’associazione tra il MAC ADDRESS e l’interno assegnato al telefono. 



Provisioning dei dispositivi telefonici
=======================================

In questa sezione andremo ad illustrare come configurare gli interni / modelli di telefoni. 
Il percorso per accedere da OCC è *Canali=>Telefono=>modelli di telefono* e  *Canali=>Telefono=>interni*

**Modelli di telefono**

A livello di singolo modello possono essere configurati:

- **Impostazioni VOIP** (*modalità di trasporto, Modalità invio DTMF, Peer to Peer, Codec, etc...*)

- **Preferenze Telefono** (*autenticazione web, Localizzazione, NTP, etc...*)

- **Tasti Funzione** (*in base al tipo di modello*)

- **Espansione Tasti** (*in base al tipo di modello*)

- **Intervallo porte RTP**

- **Rubrica LDAP** (configurazione server LDAP per rubrica su telefono)


.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/CreazioneUtentiDispositivi/Modelli.JPG


.. note:: Qualora non sia disponibile il modulo di provisioning il modello applicato è di tipo *generico* ed è comunque disponibile al menu *Canali=>Telefono=>Dispositivo generico* 

.. important:: Il provisioning via https può essere eseguito se il certificato ssl usato da **TVOX** è validato dal telefono
               
               Questo avviene se:                
                 - il certificato è firmato da un certificatore *"trusted"* (es godaddy ecc)
                 
                 - il certificato è selfsigned e viene caricato sul telefono la rootCA di chi ha generato il certificato


**Gestione interni**

La gestione Interni definisce gli interni e la loro identità da associare ai telefoni SIP e agli ATA FXS collegati al TVox Omnichannel Contact Center.

Questa sezione permette l'amministrazione degli interni. 

Per ciascun interno definito sono visualizzati i seguenti parametri:

- l'utente assegnato all'interno. Se l'utente assegnato non esiste, il telefono associato all'interno può fare solo chiamate interne e di emergenza. Se l'utente assegnato è seguito dal carattere [*] significa che l'utente utilizza tale interno come secondario.

- l'utente che utilizza l'interno. Se questo utente è diverso dall'utente assegnato, il suo nome viene messo in evidenza con una bordatura di colore giallo   . Tale situazione si presenta quando un utente si sposta su un interno diverso da quello assegnatogli operando con il TVox Client.

- il modello configurato. E' il modello definito per l'interno nel momento in cui si associa un telefono ad un MAC Address quando si tratta di un telefono configurabile mediante provisioning.

- il modello presentato. Rappresenta la descrizione del telefono / ATA FXS. Tale informazione viene fornita al TVox Omnichannel Contact Center direttamente dal telefono durante la fase di registrazione. Se il modello è diverso da quello configurato è ricercabile e viene presentato evidenziando il nome con una bordatura di colore rosso   .

- lo stato SIP del telefono che può assumere i seguenti valori: 
       - Registrato: Il telefono associato funziona correttamente.
     - Non Controllato: Il telefono è registrato ma la sua raggiungibilità non viene controllata.
     - Non Registrato: in questo stato il telefono non può sicuramente ricevere chiamate.
     - Risponde in ritardo: il telefono può solo effettuare chiamate e in generale rappresenta uno stato transitorio verso la fase di registrazione o la completa non raggiungibilità. Se tale stato si presenta in modo frequente la risoluzione del disservizio va ricercata nella gestione della rete.
     - Non Raggiungibile: il telefono nello stato registrato non risulta più raggiungibile dal TVox Omnichannel Contact Center. In questo stato il telefono non può sicuramente ricevere chiamate.

- configurazione Peer to Peer: (P2P, non P2P). Fare riferimento al capitolo Comunicazione SIP della Guida TVox.

- abilitazione alla registrazione: indica se l'utente è abilitato (o meno) alla registrazione delle conversazioni, in tal caso viene persa l'abilitazione del Peer to Peer sull'interno dell'utente.

- MAC Address: l'indirizzo MAC associato al telefono configurato mediante provisioning.

- Indirizzo IP: l'IP recuperato dal TVox Omnichannel Contact Center nel corso dell'ultima registrazione del telefono. Un click sull'indirizzo IP permette di accedere all'eventuale interfaccia di amministrazione del telefono.



Provisioning dei dispositivi nel caso di TVox Pure Cloud
========================================================

Come definito `nella sezione introduttiva <http://guide.teleniasoftware.com/it/22/projects/TVOX/GuidaIntroduttivaTVox/InformazioniGenerali/Architetture/Infrastrutture.html#sicurezza-provisioning-e-sip>`_, in ambiente cloud ci si affida esclusivamente a Yealink come vendor per dispositivi telefonici.

La configurazione della sezione :ref:`Modalità di lavoro <modalitalavoro>` come *Pure Cloud (NAT 1 a 1)* stabilisce che in OCC nella sezione *Configurazioni di sistema - Autenticazione e Sicurezza - Sicurezza Passwoord e Provisioning*, il parametro  **Sicurezza provisioning telefoni** sia impostato con il valore  **Sicuro e RPS**.

In tal modo sarà possibile sfruttare il provisioning via RPS (Redirect & Provisioning Service), servizio offerto da Yealink che consente il provisioning automatico del telefono al primo avvio (a seguito di un reset alle condizioni di fabbrica).

.. important:: **BEST PRACTICE:** Nella stessa sezione di OCC, verifica che anche i parametri **Sicurezza password utente** e **Sicurezza password SIP** siano impostati al grado più alto. L'OCC impedirà di salvare utenti e interni con password che non rispettano adeguati standard di sicurezza.

.. warning:: **ATTENZIONE:** La modifica del parametro "Sicurezza password utente" porta al riavvio del servizio di autenticazione. Per il tempo necessario al riavvio, non sarà possibile eseguire login al sistema.

.. image:: /images/TVOX/PureCloud/02-sicurezza-password-provisioning_2.png


Il tema principale che va tenuto in considerazione per il corretto funzionamento dei dispositivi SIP è il NAT traversal, tecnica utilizzata nel voip per la trasmissione del traffico audio RTP.

Il telefono deve supportare almeno uno dei seguenti protocolli, in ordine di preferenza:

- ICE rfc5245 (Interactive Connectivity Establishment)
- STUN rfc5389

Il supporto ad ICE permette il corretto funzionamento dei dispositivi in un numero maggiore di architetture NAT rispetto al solo STUN, quindi il suo utilizzo è preferibile.

.. important:: **BEST PRACTICE:** Verifica sempre che il modello Yealink prescelto per il tuo sistema TVox rispetti questi requisiti, soprattutto se intendi riutilizzare vecchi dispositivi recuperati da un impianto datato. Telenia è in grado di aiutarti nel definire quale sia l'accoppiata modello-firmware preferibile per consentirti una migliore esperienza d'uso.

Con la configurazione del provisioning sicuro, ad ogni interno creato su TVox viene fornito un URL di provisioning univoco.

.. .. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/CreazioneUtentiDispositivi/01-url-provisioning-purecloud.png


Nel caso di telefoni Yealink, è attivo il provisioning via `RPS <https://support.yealink.com/forward2download?path=ZIjHOJbWuW/DFrGTLnGyploAOxsQD/Xz/UplusSymbolq2lU036653TDiwrBfxz/BElK2gRiufplusSymbolXfMogMSzUeDNTfeK4uKrmJcySPdH5L6ZCVAIWLplusSymbollC7wlpLKz2kk42E24Q/8gRHNqUuQjL5uO4PYwC7Imh4ImwA/4cqC85uucVf7CWTgMYFEei8fLjhNLml5splusSymbolGQxnXU11oQ3XOigo=>`_. 

Si tratta di un servizio di Yealink che permette ad un telefono, alla prima accensione, di effettuare automaticamente una richiesta web per individuare il server TVox dal quale scaricare la sua configurazione, eliminando quindi la necessità di una pre-configurazione manuale.

Ricevuta tale informazione, il telefono invierà direttamente la richiesta di provisioning a tale url.

Per questioni di sicurezza, TVox permette una sola configurazione via RPS. Per provisionare nuovamente il telefono è necessario sbloccare manualmente il provisioning RPS tramite un apposito pulsante disponibile in OCC.

**Eseguire il provisioning di un telefono Yealink**

#. Crea l'interno su OCC - In questo modo viene creato l'url univoco di provisioning associato al MAC Address del telefono. Tale url viene comunicato da TVox al server RPS di Yealink
#. Togli dalla scatola il telefono, collegalo in rete ed accendilo
#. Attendi che la configurazione del telefono si completi (il telefono si riavvierà automaticamente alcune volte)
#. Il telefono si registra su TVox ed è disponibile all'utilizzo

.. tip:: Il provisioning via RPS è disponibile alla prima accensione o dopo un reset alle condizioni di fabbrica. Per ripetere questo tipo di configurazione, prima di procedere al reset devi sbloccare il provisioning RPS come indicato nella prossima immagine

.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/CreazioneUtentiDispositivi/02-provisioning-rps.png
