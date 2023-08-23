.. _installazione_attivazione:
.. _conftel: https://guide22.teleniasoftware.com/it/22/projects/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/ConferenceRoom.html

===========================
Installazione e Attivazione
===========================

L'installazione di un'istanza TVox viene effettuata tramite un unico file di immagine ad oggi reso disponibile nelle seguenti modalità:

-  **File  .iso**  , nel caso si intenda procedere con installazione su server fisico o virtual machine privata
-  **AMI - Amazon Machine Image** , nel caso si intenda attivare un'istanza su ambiente cloud AWS


Su richiesta specifica, è possibile installare istanze TVox anche negli ambienti  *Microsoft Azure*  e  *Google Cloud* .

.. important:: Il processo di installazione è completamente automatizzato e prevede: |br| |br| 1. l'installazione del sistema operativo  **AlmaLinux 8.5 (Arctic Sphynx)** |br| 2. l'installazione dello strato applicativo.


Il procedimento di installazione non cambia a seconda del tipo di piattaforma che si deve implementare, ad esempio TVox Stand Alone in lan privata, TVox Branch Office, TVox in cloud o MCS. 

E\' nella fase di caricamento della licenza che si attiva opportunamente lo strato applicativo. La licenza attivata sull'istanza, quindi, determina il tipo di impianto.


.. warning:: Per installazioni di tipo **EFI** raccomandiamo di **disabilitare l'opzione di Secure Boot**. |br| |br| Questa opzione, se attiva, impedisce l'avvio di un processo che gestice la funzionalità di :ref:`conferenza telefonica <conferenceroom>` che risulta quindi non operativa.







.. toctree::
    :maxdepth: 1

    ./InstallazioneHW
    ./InstallazioneVM
    ./InstallazioneAWS
    ./AttivazioneLicenza
    ./ModalitaLavoro