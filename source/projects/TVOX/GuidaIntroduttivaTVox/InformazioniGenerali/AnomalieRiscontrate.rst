.. _Nota di VMWare: https://blogs.vmware.com/vsphere/2018/07/timekeeping-within-esxi.html

==============================
Principali Anomalie Riscontrate
==============================

I problemi di funzionamento del software Telenia possono essere riassunti nelle seguenti categorie:

- Problemi legati al network (es: problemi di eccessiva latenza nell’utilizzo di uplink basati su fibre channel o iscsi)
- Problemi legati alla mancanza di risorse hardware
- Problemi legati al tipo di hardware in uso nel bare-metal usato dall’Hypervisor
- Problemi legati al tipo di Hypervisor utilizzato (es: VMware/Citrix vs Hyper-V) e/o all’utilizzo di una versione obsoleta di questo
- Problemi legati al Timekeeping (es: de-sync del timing tra vm e bios del bare-metal causato da snapshot e/o politiche di backup)
  
Nei seguenti paragrafi breve descrizioni delle problematiche sopra evidenziate.


--------------------------

Anomalie legate al Network
==========================

**Descrizione problema:** Solitamente il problema si manifesta con la perdita di chiamate telefoniche, difficoltà nella gestione degli stream voce (voce interrotta e/o distorta, difficolta nelle conversazioni), improvvise interruzioni di chiamata.

**Soluzione:** Si consiglia di valutare con attenzione:

- il funzionamento della SAN (FC o ISCSI) e di utilizzare, a questo fine, dei tool di diagnostica come wireshark o tcpdump (è bene ricordare che, anche una minima perdita di pacchetti, in applicazioni di tipo real time, ha un grosso impatto a livello di erogazione di servizio – ciò non accade per altri servizi, per esempio server mail/http…)
- gli uplink, si ricorda che le VM Telenia DEVONO godere di uplink dedicato per evitare problemi di gestione di throughput di banda
  

-------------------------------------------------

Anomalie legate alla mancanza di risorse hardware
=================================================

**Descrizione problema:** Solitamente il problema si manifesta con il blocco delle applicazioni in running all’interno della guest VM.

**Soluzione:** Si consiglia di valutare con attenzione:

- risorse hardware messe a disposizione della VM (si ricorda che le VM Telenia necessitano di risorse hardware dedicate/reserved e NON in sharing)
- tipo di disco virtuale utilizzato (deve essere di tipo THICK e NON THIN), e deve essere un disco di tipo SSD ad alte prestazioni adatto a supportare applicazioni real time
- spazio disco disponibile per l’OS Guest (i sistemi Linux devono godere di una percentuale di spazio disco disponibile superiore al 50%)


-----------------------------------------------------------------------------

Anomalie legate al tipo di hardware nel bare metal utilizzato dall’Hypervisor
=============================================================================

**Descrizione problema:** Solitamente il problema si manifesta con difficoltà nella gestione degli stream voce (voce interrotta e/o distorta, difficolta nelle conversazioni), improvvise interruzioni di chiamata.

**Soluzione:** Si consiglia di valutare con attenzione:

- Tipo di CPU fisica installata sul bare-metal:
    - si sconsiglia di utilizzare la tecnologia hyper-threading a favore dei core fisici
    - o si sconsiglia l’utilizzo di processori diversi da quelli Intel (le cpu flags dei processori AMD potrebbero non essere completamente supportate dall’hypervisor e/o dal kernel linux delle VM e provocare improvvisi blocchi applicativi)
- Tipo di DAS (qualora non fosse presente una SAN) in utilizzo: al finire di mantenere un funzionamento accettabile delle applicazioni sono richiesti dischi con almeno IOPS pari a 20000
- Tipo di storage in uso nelle SAN: al fine di mantenere un funzionamento accettabile delle applicazioni sono richiesti dischi con almeno IOPS pari a 20000


------------------------------------------------

Anomalie legate al tipo di Hypervisor utilizzato
================================================

**Descrizione problema:** Solitamente il problema si manifesta con il blocco delle applicazioni in running all’interno dell’ OS guest e/o il crash della VM.

**Soluzione:** Si consiglia di valutare con attenzione:

- Tipo di hardware utilizzato:
    - questo DEVE essere supportato/certificato dall’owner della soluzione Hypevisor utilizzata (si ricorda che l’utilizzo di ambienti Hyper-V Microsoft, multi-purpose, non ne implica il supporto). Fare riferimento ai seguenti link per la verifica dell’hardware in uso:
        - Hyper-V Microsoft, https://docs.microsoft.com/it-it/windows-ser-ver/virtualization/hyper-v/system-requirements-for-hyper-v-on-win-dows (esiste un tool per la certificazione dell’hardware in uso e, in caso di problemi, Telenia software si riserva la possibilità di richiesta del report)
        - Vmware, https://www.vmware.com/resources/compatibil-ity/search.php
        - Citrix, http://hcl.xenserver.org/
- Tipo di versione utilizzata dell’Hypervisor:
    - Questa DEVE supportare la versione del OS guest Linux utilizzato



------------------------------------------------

Anomalie legate al Timekeeping
================================================
    
**Descrizione problema:** Solitamente il problema si manifesta con il blocco delle applicazioni in running nell’OS guest e/o crash del cluster applicativo.
    
**Soluzione:** Si consiglia di valutare con attenzione:
    
- Gestione del sync del clock tra bare metal e VM2 (vedi `Nota di VMWare`_):
    - È imperativo che l’host bare-metal e le VM Telenia siano in sync per evitare problemi sul cluster active-passive
- Gestione delle politiche di backup:
    - Snapshot, l’utilizzo di questa funzionalità provoca un de-sync tra clock dell’host bare metal e OS guest generando malfunzionamenti degli applicativi (il de-sync è dovuto al momentaneo freeze della VM)
    - Politiche di backup per gli hypervisor (es: Veeam), è necessario effettuare i backup con le dovute attenzioni non utilizzando la feature di ‘quiesce’ che implica un freeze momentaneo delle VM interessate provocando un de-sync tra clock dell’host bare metal e VM generando malfunzionamenti degli applicativi)



-------------------

Tabella riassuntiva
===================

In tabella vengono riassunti le anomalie evidenziate:    

+-----------------------------+--------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
|  **Problema**               |  **Effetto**                                                                                           |  **Soluzione**                                                                                         |
+-----------------------------+--------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
|  Anomalie legate            |  • Perdita di chiamate                                                                                 |  • Uplink dedicato                                                                                     |
|  |br| al network            |  • Problemi di voce                                                                                    |  • Utilizzo di tool di diagnostica                                                                     |
+-----------------------------+--------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
|  Anomalie legate            |  • Nei log di sistema |br| della VM viene notificato errore |br| “kernel: dahdi: Detected time shift.” |  • Risorse reserved nelle VM                                                                           |
|  |br| alla mancanza         |                                                                                                        |  • Disco SSD di tipo thick |br| ad alte prestazioni in grado di supportare |br| applicazioni real time |
|  |br| di risorse hardware   |                                                                                                        |  • Spazio disponibile per l’os guest > 50%                                                             |
+-----------------------------+--------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
|  Anomalie legate            |  • Perdita di chiamate                                                                                 |  • Disabilitazione Hyperthreading                                                                      |
|  |br| al tipo di HARDWARE   |  • Problemi di voce                                                                                    |  • Uso dei soli Core                                                                                   |
|  |br| in uso nel bare-metal |  • Blocco software Telenia |br| causato da per mancanza di |br| disponibilità hardware della VM        |  • Utilizzo di processori Intel                                                                        |
|  |br| usato dall’Hypervisor |                                                                                                        |                                                                                                        |
+-----------------------------+--------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
|  Anomalie legate            |  • Perdita di chiamate                                                                                 |  • Utilizzo di solo hardware |br| certificato dall’owner della soluzione |br| Hypervisor               |
|  |br| al tipo di HYPERVISOR |  • Problemi di voce                                                                                    |    (in caso di |br| soluzioni Hyper-V verrà |br| richiesto invio del report ottenuto, |br|             |
|  |br| utilizzato e/o        |  • Blocco software Telenia |br| causato alla mancata presenza di |br| VM TOOLS di ottimizzazione e/o   |    come output, del tool |br| specifico sviluppato da Microsoft)                                       |
|  |br| all’utilizzo di una   |    |br| ad incorretta gestione, |br| da parte dell’HYPER-VISOR, |br| della versione di OS linux        |  • Supporto alla versione dell’OS guest |br| Linux utilizzato                                          |
|  |br| versione obsoleta     |                                                                                                        |                                                                                                        |
|  |br| di questo             |                                                                                                        |                                                                                                        |
+-----------------------------+--------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
|  Anomalie legate            |  • Blocco software Telenia causato |br| da desync del bios real time |br| clock del bare metal e VM    |  • Sync tra clock dell’host bare metal |br| e OS guest                                                 |
|  |br| al Timekeeping        |                                                                                                        |  • Disabilitazione della funzionalità |br| quiesce in caso di backup)                                  |
|                             |                                                                                                        |  • Non utilizzare la funzionalità Snapshot                                                             |
+-----------------------------+--------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+