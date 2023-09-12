.. _installazionehw:

==========================
Installazione su HW fisico
==========================

Le piattaforme Hardware su cui installare il TVOX possono essere di tipologia Tower o Rack purché dotate di una scheda di rete e di dispositivo DVD/ROM necessario nella fase di installazione.

Per assicurare un buon livello di sicurezza sono consigliate piattaforme dotate di:

- Alimentatore ridondato **HOT-PLUG**.
- **Raid 1 Hardware** con dischi HOT-PLUG realizzati con Controller RAID compatibili Linux (ES: Perc/Sas H200, H700).
- **Gruppo di continuità**.

Il dimensionamento della piattaforma TAM/TVox dipende dai seguenti fattori:

- Numero dei dispositivi SIP (Telefoni SIP e/o ATA FXS).
- Numero di chiamate contemporanee gestite dal sistema.
- Servizi erogati dal TVox: base (PBX) ed evoluti (TQM, Contact Center, VOICE RECORDING, LANFAX, multicanalità).

.. note:: Nell'area del sito *www.teleniasoftware.com* dedicata ai partner è disponibile il configuratore dimensionamento risorse


Per procedere all’installazione è possibile scaricare il setup aggiornato del sistema TVox Communication
attraverso il seguente link: http://www.teleniasoftware.it/download/tvox/iso.php e masterizzare l’immagine ISO su un supporto DVD Dual Layer da 8.5 Gb.

.. note:: E\' altresì possibile l'installazione via USB utilizzando un qualsiasi programma che esegua la scrittura RAW dell'ISO direttamente sul drive USB come suggerito in questo link: https://wiki.centos.org/HowTos/InstallFromUSBkey 
        
        Ad esempio il seguente programma può essere utile per scrivere l'ISO su un drive USB http://www.netbsd.org/~martin/rawrite32/download.html dopo aver scaricato l'eseguibile è sufficiente selezionare il file .iso desiderato e procedere alla scrittura su USB facendo attenzione che tale operazione fa perdere tutto il contenuto eventualmente presente su quel drive.
