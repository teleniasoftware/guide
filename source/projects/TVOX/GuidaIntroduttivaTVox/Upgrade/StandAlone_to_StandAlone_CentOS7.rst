================================================================
TVOX Stand Alone da Release 21 o inferiore a Release 22 CentOS 7
================================================================

In questa sessione ti andiamo ad indicare le manovre che devi eseguire in un contesto di upgrade TVOX in configurazione Stand Alone che prevede la creazione di un cluster. 

La creazione del cluster ti serve per ridurre al minimo il tempo di disservizio dovuto all'applicazione delle patch.


- Assieme al tuo cliente prepara la *CHECK UAT*. In fase di redazione della lista dei test UAT da eseguire, è buona prassi condividerla con il tuo cliente, in modo che tu possa integrarla in base all'impianto presente ed al suo utilizzo. Ti riportiamo un esempio di check list standard.
- Esegui *CHECK UAT* così da accertarti della *bontà* del sistema in tutte le sue componenti. 
- Esegui una Snapshot TVOX 1. E\' consigliato eseguire la snapshot con macchina spenta ed escludendo la memoria.

.. important:: **Ricordati che è importante avere una snapshot per eventuali rollback.** 
    
    Nell'eventualità non fosse possibile eseguire snapshot delle macchine, chiama Telenia prima di procedere con qualsiasi attività per valutare azioni alternative. 


- Esegui l'upgrade TVOX a release 22.0.X.

.. note:: Ricordati di lanciare la patch in modalità screen e riavviare la macchina ad ogni patch applicata 

- Al termine dell'applicazione della patch avrai l'output

            .. code-block:: shell

                Update completed! 
                Please REBOOT the machine! 

- **Se non avessi questo output contatta Telenia prima di eseguire qualsiali manovra**
- Esegui il Reboot di TVOX.
- Esegui *CHECK UAT*.
- Ora puoi far eliminare la snapshot creata precedentemente.


.. note:: Le attività riportate prevedono un fermo macchina dovuto all'applicazione delle patch. Nel caso questa manovra non sia possibile applicare procedura di upgrade TVOX ridondato.


.. warning:: Se non vi sono impedimenti legati alla disponibilità delle risorse hardaware (esigenza di liberare spazio disco), si consiglia di eliminare la snapshot dopo una settimana in modo da consolidare le prove di funzionalità.


.. important:: Nel caso nasca la necessità di *rollback* prima di ripristinare la snapshot è necessario contattare Telenia per l'eventuale recupero log per successiva analisi.
     

