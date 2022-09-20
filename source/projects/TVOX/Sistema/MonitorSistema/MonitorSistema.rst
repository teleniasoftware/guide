.. _monitorsistema:

========================
Monitor di Sistema
========================

In questa sezione illustreremo il monitoraggio ed utilizzo delle risorse e la visualizzazione degli ultimi allarmi. Tale prestazione è fruibile tramite OCC nella sezione SISTEMA => Monitor di sistema. Di seguito illustrati i diversi pannelli di monitoraggio del sistema TVOX.

- Data e ora di ultimo riavvio della macchina e suo stato (master o slave):

.. image:: /images/TVOX/Sistema/ConfigurazioneSistema/MonitorSistema/dataora.png

- Ultimi allarmi che si sono presentati sul sistema: 

.. image:: /images/TVOX/Sistema/ConfigurazioneSistema/MonitorSistema/allarmi.png

- Processi attivi, riportando l'utilizzo in percentuale di CPU e RAM:

.. image:: /images/TVOX/Sistema/ConfigurazioneSistema/MonitorSistema/processi_attivi.png

- Spazio su disco, indicando la ripartizione dei vari processi (ad esempio: log, database, backup, etc): 

.. image:: /images/TVOX/Sistema/ConfigurazioneSistema/MonitorSistema/storage.png

- Utilizzo della memoria e della memoria dedicata alle registrazioni delle conversazioni:

.. image:: /images/TVOX/Sistema/ConfigurazioneSistema/MonitorSistema/memoria.png

- Il flusso delle chiamate in termini di chiamate esterne ed interne:

.. image:: /images/TVOX/Sistema/ConfigurazioneSistema/MonitorSistema/chiamate.png

Le chiamate riparite per Trunk:

.. image:: /images/TVOX/Sistema/ConfigurazioneSistema/MonitorSistema/trunk.png

Carico CPU:

.. image:: /images/TVOX/Sistema/ConfigurazioneSistema/MonitorSistema/cpu.png

.. note::  Gli ultimi tre grafici mostrano i dati in tempo reale mantenendoli al suo interno per un massimo di 5 minuti. I grafici vengono popolati quando la pagina viene aperta.

Infine abbiamo lo stato dei telefoni e dei trunk configurati e registrati:

.. image:: /images/TVOX/Sistema/ConfigurazioneSistema/MonitorSistema/dispositivi.png


Nel caso di una macchina in configurazione Fault Tollerance verrà riportato anche il pannello che indica lo stato di allineamento e sincronizzazione verso la macchina slave. 

.. image:: /images/TVOX/Sistema/ConfigurazioneSistema/MonitorSistema/fault_tollerance.png

Per alcuni di questi monitor, è messa a disposizione una funzionalità di condivisione che permette di copiare il link del grafico ed incollarlo nell'RTD sfruttando il pannello \"iframe\".

.. image:: /images/TVOX/Sistema/ConfigurazioneSistema/MonitorSistema/iframe.png