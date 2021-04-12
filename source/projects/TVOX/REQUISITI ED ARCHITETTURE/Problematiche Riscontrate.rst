=========================
Problematiche Riscontrate
=========================

I problemi di funzionamento del software Telenia possono essere riassunti nelle queste categorie:

- Problemi legati al network (es: problemi di eccessiva latenza nell’utilizzo di uplink ba-sati su fibre channel o iscsi)
- Problemi legati alla mancanza di risorse hardware
- Problemi legati al tipo di hardware in uso nel bare-metal usato dall’Hypervisor
- Problemi legati al tipo di Hypervisor utilizzato (es: VMware/Citrix vs Hyper-V) e/o all’utilizzo di una versione obsoleta di questo
- Problemi legati al Timekeeping (es: de-sync del timing tra vm e bios del bare-metal causato da snapshot e/o politiche di backup)
  
Nei seguenti paragrafi breve descrizioni delle problematiche sopra evidenziate.


--------------------------

Problemi legati al Network
==========================

**Descrizione problema:** Solitamente il problema si manifesta con la perdita di chiamate telefoni-che, difficoltà nella gestione degli stream voce (voce interrotta e/o distorta, difficolta nelle con-versazioni), improvvise interruzioni di chiamata.

**Soluzione:** Si consiglia di valutare con attenzione:

- il funzionamento della SAN (FC o ISCSI) e di utilizzare, a questo fine, dei tool di dia-gnostica come wireshark o tcpdump (è bene ricordare che, anche una minima per-dita di pacchetti, in applicazioni di tipo real time, ha un grosso impatto a livello di erogazione di servizio – ciò non accade per altri servizi, per esempio server mail/http… -)
- gli uplink, si ricorda che le VM Telenia DEVONO godere di uplink dedicato per evitare problemi di gestione di throughput di banda
  

-------------------------------------------------

Problemi legati alla mancanza di risorse hardware
=================================================

**Descrizione problema:** Solitamente il problema si manifesta con il blocco delle applicazioni in running all’interno della guest VM.

**Soluzione:** Si consiglia di valutare con attenzione:

- risorse hardware messe a disposizione della VM (si ricorda che le VM Telenia necessi-tano di risorse hardware dedicate/reserved e NON in sharing)
- tipo di disco virtuale utilizzato (deve essere di tipo THICK e NON THIN)
- spazio disco disponibile per l’OS Guest (i sistemi Linux devono godere di una percen-tuale di spazio disco disponibile superiore al 50%)


-----------------------------------------------------------------------------

Problemi legati al tipo di hardware nel bare metal utilizzato dall’Hypervisor
=============================================================================

**Descrizione problema:** Solitamente il problema si manifesta con difficoltà nella gestione degli stream voce (voce interrotta e/o distorta, difficolta nelle conversazioni), improvvise interruzioni di chiamata.

**Soluzione:** Si consiglia di valutare con attenzione:

- Tipo di CPU fisica installata sul bare-metal:
    - si sconsiglia di utilizzare la tecnologia hyper-threading a favore dei core fisici
    - o si sconsiglia l’utilizzo di processori diversi da quelli Intel (le cpu flags dei pro-cessori AMD potrebbero non essere completamente supportate dall’hypervisor e/o dal kernel linux delle VM e provocare improvvisi blocchi applicativi)
- Tipo di DAS (qualora non fosse presente una SAN) in utilizzo: al finire di mantenere un funzionamento accettabile delle applicazioni sono richiesti dischi con almeno IOPS pari a 20000
- Tipo di storage in uso nelle SAN: al fine di mantenere un funzionamento accettabile delle applicazioni sono richiesti dischi con almeno IOPS pari a 20000


------------------------------------------------

Problemi legati al tipo di Hypervisor utilizzato
================================================

**Descrizione problema:** Solitamente il problema si manifesta con il blocco delle applicazioni in running all’interno dell’ OS guest e/o il crash della VM.

**Soluzione:** Si consiglia di valutare con attenzione:

- Tipo di hardware utilizzato:
    - questo DEVE essere supportato/certificato dall’owner della soluzione Hypevisor utilizzata (si ricorda che l’utilizzo di ambienti Hyper-V Microsoft, multi-purpose, non ne implica il supporto). Fare riferimento ai seguenti link per la verifica dell’hardware in uso:
        - Hyper-V Microsoft, https://docs.microsoft.com/it-it/windows-ser-ver/virtualization/hyper-v/system-requirements-for-hyper-v-on-win-dows (esiste un tool per la certificazione dell’hardware in uso e, in caso di problemi, Telenia software si riserva la possibilità di richiesta del re-port)
        - Vmware, https://www.vmware.com/resources/compatibil-ity/search.php
        - Citrix, http://hcl.xenserver.org/
- Tipo di versione utilizzata dell’Hypervisor:
    - Questa DEVE supportare la versione del OS guest Linux utilizzato



------------------------------------------------

Problemi legati al Timekeeping
================================================
    
**Descrizione problema:** Solitamente il problema si manifesta con il blocco delle applicazioni in running nell’OS guest e/o crash del cluster applicativo.
    
**Soluzione:** Si consiglia di valutare con attenzione:
    
- Gestione del sync del clock tra bare metal e VM2:
    - È imperativo che l’host bare-metal e le VM Telenia siano in sync per evitare problemi sul cluster active-passive
- Gestione delle politiche di backup:
    - Snapshot, l’utilizzo di questa funzionalità provoca un de-sync tra clock dell’host bare metal e OS guest generando malfunzionamenti degli applicativi (il de-sync è dovuto al momentaneo freeze della VM)
    - Politiche di backup per gli hypervisor (es: Veeam), è necessario effettuare i backup con le dovute attenzioni non utilizzando la feature di ‘quiesce’ che im-plica un freeze momentaneo delle VM interessate provocando un de-sync tra clock dell’host bare metal e VM generando malfunzionamenti degli applicativi)



-------------------

Tabella riassuntiva
===================

In tabella vengono riassunti i problemi evidenziati:

+------------------------+----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Problema               | Effetto                                                                                      | Soluzione                                                                     |
+------------------------+----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Problemi legati        | • Perdita di chiamate                                                                        | • Uplink dedicato                                                             |
| al network             | • Problemi di voce                                                                           | • Utilizzo di tool di diagnostica                                             |
+------------------------+----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Problemi legati        | • Nei log di sistema della VM viene notificato errore “kernel: dahdi: Detected time shift. ” | • Risorse reserved nelle VM                                                   |
| alla mancanza          |                                                                                              | • Disco di tipo thick                                                         |
| di risorse hardware    |                                                                                              | • Spazio disponibile per l’os guest > 50%                                     |
+------------------------+----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Problemi legati        | • Perdita di chiamate                                                                        | • Disabilitazione Hyperthreading                                              |
| al tipo di HARDWARE    | • Problemi di voce                                                                           | • Uso dei soli Core                                                           |
| in uso nel bare-metal  | • Blocco software Telenia causato da per mancanza di di-sponibilità hardware della VM        | • Utilizzo di processori Intel                                                |
| usato dall’Hypervisor  |                                                                                              |                                                                               |
+------------------------+----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Problemi legati        | • Perdita di chiamate                                                                        | • Utilizzo di solo hardware certificato dall’owner della soluzione Hypervisor |
| al tipo di HY-PERVISOR | • Problemi di voce                                                                           |   (in caso di soluzioni Hyper-V verrà richiesto invio del report ottenuto,    |
| utilizzato e/o         | • Blocco software Telenia causato alla mancata presenza di VM TOOLS di ottimizza-zione e/o   |   come output, del tool specifico sviluppato da Microsoft)                    |
| all’utilizzo di una    |   ad incorretta gestione, da parte dell’HYPER-VISOR, della versione di OS linux              | • Supporto alla versione dell’OS guest Linux utilizzato                       |
| versione obsoleta      |                                                                                              |                                                                               |
| di questo              |                                                                                              |                                                                               |
+------------------------+----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Problemi legati        | • Blocco software Telenia causato da desync del bios real time clock del bare metal e VM     | • Sync tra clock dell’host bare metal e OS guest                              |
| al Timekeeping         |                                                                                              | • Disabilitazione della fun-zionalità quiesce in caso di backup)              |
|                        |                                                                                              | • Non utilizzare la funziona-lità Snapshot                                    |
+------------------------+----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+