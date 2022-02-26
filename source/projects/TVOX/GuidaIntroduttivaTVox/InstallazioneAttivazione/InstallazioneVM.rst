.. _installazionevm:

==================================
Installazione su ambiente virtuale
==================================

L'installazione in un ambiente basato su Hypervisor è molto simile all'installazione su server fisico. 


La differenza sta nel fatto che, prima di lanciare l'installazione, va creata e configurata nelle sue componenti essenziali una virtual machine. Le componenti che vanno specificate sono:

- **Sistema operativo**: Linux 64 bit (se disponbile scegliere come tipologia Almalinux)
- **Caratteristiche hardware**: cpu, memoria ram, capacità HD vanno opportunamente dimensionati in base al tipo di impianto da realizzare. In particolare, è importante tenere presente la tipologia di storage da assegnare che deve essere di tipo SSD ad alte prestazioni.
- **CD/DVD Drive**: va agganciato ad esso il file ISO e il drive va impostato come attivo al boot

In tal modo, alla partenza della virtual machine verrà avviata automaticamente l'installazione, che seguirà da qui in poi gli stessi step descritti nella sezione :ref:`installazionehw`.


.. note:: Fare riferimento alla sezione :ref:`policy_hypervisor` per le linee guida da seguire per la gestione di ambienti Hypervisor nel caso ospitino applicazioni software fornite da Telenia Software

