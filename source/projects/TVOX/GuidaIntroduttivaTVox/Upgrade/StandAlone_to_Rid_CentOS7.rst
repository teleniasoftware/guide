==================================================
TVOX Stand Alone to TVOX Ridondato (S.O. CentOS 7)
==================================================

.. |tvox21_licenza| image:: /images/TVOX/Upgrade/LicenzaOCC.PNG
.. |tvox10_26_licenza| image:: /images/TVOX/Upgrade/LicenzaManager.PNG
.. |Network_reset01| image:: /images/TVOX/Upgrade/Network_reset01.PNG
.. |Network_reset02| image:: /images/TVOX/Upgrade/Network_reset02.PNG
.. |Network_reset03| image:: /images/TVOX/Upgrade/Network_reset03.PNG 
.. |Network_reset04| image:: /images/TVOX/Upgrade/Network_reset04.PNG
.. |Network_reset05| image:: /images/TVOX/Upgrade/Network_reset05.PNG
.. |Hosts| image:: /images/TVOX/Upgrade/Hosts.PNG
.. |FaultTolerance01| image:: /images/TVOX/Upgrade/FT01.PNG
.. |FaultTolerance02| image:: /images/TVOX/Upgrade/FT02.PNG
.. |SincroFT| image:: /images/TVOX/Upgrade/SincroFT.PNG
.. |SincroMonitor| image:: /images/TVOX/Upgrade/SincroMonitor.PNG
.. |FileSystem| image:: /images/TVOX/Upgrade/FileSystem.PNG
.. |Updater| image:: /images/TVOX/Upgrade/Updater.PNG
.. |Check_Mongo01| image:: /images/TVOX/Upgrade/Check_Mongo01.PNG
.. |Check_Mongo02| image:: /images/TVOX/Upgrade/Check_Mongo02.PNG    
.. |Replicazione_rel22| image:: /images/TVOX/Upgrade/Replicazione_rel22.PNG 
.. |Monitor_22| image:: /images/TVOX/Upgrade/Monitor_22.PNG 



Qui troverai le informazioni necessarie per eseguire un upgrade alla release 22 partendo da un sistema Stand Alone e arrivando poi ad un sistema ridondato su Sistema operativo CentOS 7.

.. important:: La creazione del cluster ti serve per ridurre al minimo il tempo di disservizio dovuto all'applicazione delle patch. 
    Se hai un impianto Stand Alone devi sapere che quando viene applicata una patch, l'impianto stesso risulta indisponibile. 
    Se invece crei un cluster potrai applicare le patch di upgrade su una delle due macchine, permettendo al tuo cliente di continuare a fruire del TVOX e delle sue funzionalità.
    
**Legenda**
 .. code-block:: ini

    TVOX 1: macchina TVOX in produzione
    TVOX 2: nuova macchina TVOX ridondata che dovrà essere creata exnovo
    FT: Fault Tolerance
    Lista check UAT: lista test case da eseguire
    DB: database


Predisposizione ambiente in produzione
======================================

Come prima cosa andiamo a predisporre l'ambiente per creare il cluster.

- Assieme al tuo cliente prepara la *lista check UAT*. In fase di redazione della lista dei test UAT da eseguire, è buona prassi condividerla con il cliente, in modo che tu possa integrarla in base all'impianto presente ed al suo utilizzo. Ti riportiamo un esempio di check list standard.
- Esegui le prove presenti nella *lista check UAT* così da accertarti della *bontà* del sistema in tutte le sue componenti.
- Chiedi al tuo cliente due nuovi indirizzi IP disponbili sulla rete dove risiede il TVOX. Questi IP saranno poi gli IP fisici che verranno associati alle macchine TVOX 1 e TVOX 2.
- Richiedi al supporto tecnico di Telenia l'espansione della licenza alla funzione FT per TVOX 1 e la creazione di nuova licenza sempre in FT per TVOX 2.
- Esegui una snapshot TVOX 1. E\' consigliato eseguire la snapshot con macchina spenta ed escludendo la memoria.

.. important:: **Ricordati che è importante avere una snapshot per eventuali rollback.** 
    
    Nel caso non ci siano le condizioni per eseguire snapshot, contatta il supporto tecnico di Telenia prima di procedere con qualsiasi attività, per valutare azioni alternative. 
    

**Trasformazione Impianto in modalità Fault Tolerance:** passiamo ora alla creazione del cluster nella versione del tuo cliente.

- Se hai un TVOX versione 21 devi andare da *OCC* in *SISTEMA -> Security update* e fare un check disponibilità licenza. Una volta rilevata la modifica devi dare conferma alla richiesta di riavvio processi.
  
|tvox21_licenza|


- Se invece hai un TVOX versione antecedente alla 21 devi andare da *Application Manager* in *System -> License* e premere sul pulsante [Upload license] caricando il file con estensione .lic fornito da Telenia. Al termine dovrai riavviare la macchina.

|tvox10_26_licenza| 

**N.B.** Ricordati di avvisare il tuo cliente per informarlo che da questo momento si avrà un *fermo macchina*, dovuto alla riconfigurazione degli indirizzamenti IP.

- Dopo aver caricato la licenza, collegati in shell SSH con utenza di root su TVOX 1 ed esegui il cambio IP digitando il comando:

        .. code-block:: shell

                network_reset
        

- Si aprirà in shell un menù dove dovrai impostare i parametri di rete (IP, netmask, gateway, nome host e DNS)

        |Network_reset01| 

        |Network_reset02| 

        |Network_reset03| 

        |Network_reset04| 

        |Network_reset05| 


.. note:: Dovrai cambiare l\'IP così da rendere disponibile quello assegnato originalmente a TVOX 1 come IP di nodo del futuro cluster. 
    
    Se nel TVOX hai impostato il nome di dominio, accertati che il file /etc/hosts sia configurato correttamente.
    
    Deve essere presente una riga con riportato *<indirizzo IP TVOX> <nome di dominio>* (esempio 172.16.95.71 tam.teleniasoftware.com). 

    Questo vuol dire che se sei in configurazione Stand Alone, l'IP TVOX coinciderà con l'IP fisico della macchina, mentre in configurazione FT coinciderà con l'IP di Nodo TVOX (deve essere presente su entrambe le macchine TVOX). 
    
    Ecco un esempio di configurazione FT dove l'ip 172.16.95.70 rappresenta l'ip fisico dela macchina, mentre l'ip 172.16.95.71 rappresenta l'ip di nodo:

        |Hosts|

    Se noti che la configurazione non è corretta da shell SSH esegui il comando 
    
        .. code-block:: shell

            write_config.php network



- Esegui ora il reboot di TVOX 1 ed una volta ripartito, vai a configurare la sezione FT, alzando al massimo la banda di replicazione ([1]_)
  Da *Application Manager* menù *Configurazione -> Rete -> Interfacce di Rete* 


     |FaultTolerance01|

  e  *Configurazione -> Rete -> Faul Tolerance* 

     |FaultTolerance02|

- Riavvia nuovamente il TVOX 1.

- Se sei arrivato a questo punto puoi avvisare il cliente della ripresa in servizio del sistema.
- Esegui assieme i test presenti in *lista check UAT*, per confermare che la creazione del cluster non ha modificato il fuznionamento dell'impianto.
- Adesso è ora di installare TVOX 2 assegnando il secondo dei due nuovi IP forniti e caricando la licenza.
- Riavvia il TVOX 2 e alla ripartenza configura la sezione FT su TVOX 2, come hai fatto precedentemente con il TVOX 1.
- Una volta configurata la sezione cluster del TVOX 2, riavvialo.
- Ora sincronizza le macchine andando nell'\ *Application Manager* del TVOX 2 nel menù *Sistema -> Replicazione* e selezionando la voce [Sincronizzazione completa]


    |SincroFT| 



**Passiamo ora a verificare che le macchine siano sincronizzate**

- Vai nel TVOX master nell'\ *Application Manager* menù *Monitor* e verifica che DB e File System siano sincronizzati

    |SincroMonitor| 

- Fai poi controllo sui calendari seguendo quanto indicato nella prossima nota.

.. note:: **Check allineamento calendari**
    Per verificare che i calendari siano allineati bisogna andare da shell SSH sempre con utenza di root sia su macchina master che slave, effettuare un dump db calendari
    e comparare le dimensioni. Se sono le medesime, i calendari sono allineati altrimenti quello valido è quello del master.
    Per eseguire il dump dei calendaro è necessario scrivere il comando indicato qui sotto. Il dump verrà salvato nella cartella /tmp e sarà denominato *calendar.sql*
    
        .. code-block:: shell

            /usr/bin/pg_dump --clean -U davical_dba davical_administrators -f /tmp/calendar.sql"

    
- Ora verifichiamo che le chat siano sincronizzate

.. note:: **Check allineamento chat** 
    Dovrai eseguire i seguenti comandi sempre da shell SSH con utenza di root sia su macchina master che su macchina slave.
    - Comando per accesso cli gestione chat da eseguire: 
  
        .. code-block:: shell 
            
            mongo

    - Esempio di output         

        |Check_Mongo01| 
  
    - Comando per interrogare lo stato di *salute* del cluster chat: 
  
        .. code-block:: shell 
            
            rs.status()

    - Esempio di output (dove l'ip 172.31.21.175 rappresenta l'ip della macchina in stato *master* e l'ip 172.31.21.106 rappresenta l'ip della macchina in stato *slave*)       

        |Check_Mongo02| 
  
- L'ultimo check da eseguire riguarda l'allineamento file system 


.. note:: **Check allineamento file system**
    Quando esegui una sincronizzazione devi sapere che l'indicatore presente sul master che segnala la sincronizzazione file system, nel caso sia in stato OK e di colore verde, sta ad indicare che la sincronizzazione del file system è in corso, 
    ma nel caso di prima sincronizzazione potrebbe essere che i tempi di completa sincronizzazione siano elevati. Il tempo è legato dal contenuto presente in /opt/telenia_data/sync e può essere di dimensioni cospicue sopprattuto nel caso di registrazioni vocali.

    - Verificare che sia partito il task di sincronizzazione del file system, eventualmente triggerarlo lanciando un *setperms.sh* sulla master
    - Verifica capienza cartella /opt/telenia_data/sync tramite comando: 

        .. code-block:: shell

            du -h --max-depth=1 /opt/telenia_data/sync/

    Il confronto da quanto ottenuto sul slave dovrebbe essere simile a quanto presente su master. 
    Ecco un esempio di output che otterai.

    |FileSystem|


**Verifica funzionamento macchina Ridondata**: sei arrivato al termine delle configurazioni e dei check. Ti resta solo da eseguire lo switch di nodo e provare anche il funzionamento della macchina ridondata.

- Esegui il reboot di TVOX 1 (Nuova master TVOX 2, slave TVOX 1).
- Esegui su con TVOX 2 in stato *master* i test presenti nella *lista check UAT*.


Upgrade TVOX a rel. 22
=======================

Passiamo ora ad illustare le manovre che dovrai eseguire per aggiornare l'impianto del tuo cliente alla versione 22.

- Fai fare una snapshot della slave TVOX 1 pre upgrade a release 22.
- Esegui l'upgrade TVOX 1 a release 22. 

.. note:: Ricordati di eseguire la patch in modalità screen

- Al termine dell'applicazione della patch avrai l'output

            |Updater|

- **Se non avessi questo output contatta il supporto tecnico di Telenia prima di eseguire qualsiasi manovra**
- Fai un reboot del TVOX 2  (Nuova master TVOX 1, slave TVOX 2)
- Esegui i test presenti nella *lista check UAT* in produzione su TVOX 1 in rel. 22.
- Al termine dei test vai ad eseguire l'upgrade del TVOX 2 a rel. 22.

.. note:: Ricordati di lanciare la patch in modalità screen

- Al termine dell'applicazione della patch avrai l'output

            |Updater|

- **Se non avessi questo output contatta il supporto tecnico di Telenia prima di eseguire qualsiasi manovra**
- Fai un reboot del TVOX 2 e poi da *OCC* del TVOX 2, andando in *SISTEMA* -> *Configurazione di sistema* -> "Replicazione" esegui la sincronizzazione degli ultimi 2 mesi, scegliendo la voce *Configurazione e ultimi 2 mesi* dal menu *Replicazione* e premendo poi il pulsante [Start].

            |Replicazione_rel22|


 
**Verifica sincronizzazione TVOX Rel.22:** passiamo ora a verificare che le macchine siano sincronizzate.

- Vai nel TVOX master in *OCC* nella sezione *SISTEMA* -> *Monitor di sistema* e verifica che DB e File System e chat siano sincronizzati.

            |Monitor_22|


**Verifica funzionamento macchina Ridondata**: sei arrivato al termine delle configurazioni e dei check. Ti resta solo da eseguire lo switch di nodo e provare anche il funzionamento della macchina ridondata.

- Esegui il Reboot di TVOX 1 (Nuova Master TVOX 2, Slave TVOX 1).
- Esegui *Lista check UAT* in produzione su TVOX 1.
- Ora puoi far eliminare le snapshot create precedentemente.


.. warning:: Se non vi sono impedimenti legati alla disponibilità delle risorse hardaware (esigenza di liberare spazio disco), si consiglia di eliminare la snapshot dopo una settimana.


.. important:: Nel caso nasca la necessità di *rollback*, prima di ripristinare la snapshot contatta il supporto tecnico di Telenia per l'eventuale recupero log per successiva analisi.
     


.. rubric:: Note

.. [1] Il valore da impostare è da chiedere al cliente in base alle prestazioni di network dell'infrastruttura dove risiedono i TVOX.