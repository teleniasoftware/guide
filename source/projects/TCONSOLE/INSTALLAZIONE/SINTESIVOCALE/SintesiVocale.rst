.. _Sintesi Vocale:

==============
Sintesi Vocale
==============

Il **Mixer Telenia** è un ausilio per l’operatore ipovedente o non vedente che utilizza il telefono con le soluzioni sviluppate da Telenia Software per gli addetti al centralino.

Al fine di permettere all’operatore l’ascolto dei segnali audio prodotti dal telefono e dal Personal Computer è stato sviluppato il dispositivo Mixer Telenia.

Mixer Telenia permette di miscelare il segnale audio del telefono con la Sintesi Vocale prodotta dalla scheda audio del Personal Computer.

Questo documento descrive il contenuto del kit Mixer Telenia e le modalità di installazione.

Contenuto del kit Mixer Telenia
===============================

1. n. 1 dispositivo Mixer Telenia;
2. n. 1 cavo a spirale per telefono;
3. n. 1 cavo di prolunga stereo (Jack stereo maschio - Jack stereo maschio);
4. n. 1 cavo USB per alimentazione mixer.

Installazione per Windows 7 e successivi
----------------------------------------

Dopo aver installato TConsole sul Personal Computer del Posto Operatore, collegare il mixer come illustrato in figura:

.. image:: /images/TCONSOLE/INSTALLAZIONE/SINTESIVOCALE/collegamenti_mixer.png

Non sono necessari settaggi particolari nella configurazione del PC.

Se necessario, regolare il volume del PC affinché la voce della sintesi non crei troppo disturbo alla voce della conversazione.

.. important :: Quando anche aumentando al massimo il volume del PC la sintesi risulta essere troppo bassa, può essere utilizzato il cavo USB in dotazione da collegare all’apposito connettore al fine di amplificare l’audio (**il cavo di prolunga stereo va comunque mantenuto collegato**).

Configurazione Jumper Mixer
===========================

Per eseguire una corretta configurazione del mixer, su configurazioni diverse da quelle presentate di seguito, può essere necessario dotarsi di un multimetro digitale in grado di misurare la resistenza. Per identificare i pin del microfono è necessario trovare i due pin che avranno tra loro la maggior resistenza possibile (superiore a 100 Ohm). Al contrario la coppia di pin che presenterà un basso valore di resistenza sarà la coppia di pin dell’altoparlante.

Per la regolazione del volume del mixer, fare riferimento al componente R5 presente all’interno secondo lo schema che segue:

.. _Componente R5:

.. image:: /images/TCONSOLE/INSTALLAZIONE/SINTESIVOCALE/componente_R5.png

Prendendo come riferimento i 3 punti che formano un triangolo, abbiamo l’orientamento per aumentare o diminuire il volume.

**Di seguito si presenta la configurazione dei Jumper del Mixer Telenia per le varie Centrali ed i possibili modelli di telefono associati all’utilizzo della cornetta o a diversi modelli di cuffia.**

Snom 300 / 320
--------------

Configurazione dei Jumper del Mixer utilizzato con il **telefono Snom 320 e la cornetta**:

.. image:: /images/TCONSOLE/INSTALLAZIONE/SINTESIVOCALE/jumper_Snom320_cornetta.png

Questa configurazione può essere utilizzata anche con il **telefono Snom 300 e cuffia Snom A100M**.

Configurazione dei Jumper del Mixer utilizzato con il **telefono Snom 320 e cuffia Jabra**:

.. image:: /images/TCONSOLE/INSTALLAZIONE/SINTESIVOCALE/jumper_Snom320_cuffia_Jabra.png

Snom 715 / 720
--------------

Configurazione dei Jumper del Mixer utilizzato con il **telefono Snom 720 e la cornetta**:

.. image:: /images/TCONSOLE/INSTALLAZIONE/SINTESIVOCALE/jumper_Snom720_cornetta.png

Questa configurazione può essere utilizzata anche con il **telefono Snom 715 e cuffia Snom A100M**.

.. tip :: Per sentire correttamente la Sintesi Vocale in cornetta, oltre alla giusta configurazione dei Jumper bisogna collegare anche il cavo USB, altrimenti la voce della sintesi resta bassa e non si sente in cornetta.

Configurazione dei Jumper del Mixer utilizzato con il telefono **Snom 720 e cuffia Jabra**:

.. image:: /images/TCONSOLE/INSTALLAZIONE/SINTESIVOCALE/jumper_Snom720_cuffia_Jabra.png

Per sentire correttamente la sintesi vocale in cuffia, oltre alla giusta configurazione dei Jumper bisogna collegare anche il cavo USB, altrimenti la voce della sintesi resta bassa e non si sente in cuffia.

Configurazione dei Jumper del Mixer utilizzato con il **telefono Snom 715 e cuffia Gequdio WA9002**:

.. image:: /images/TCONSOLE/INSTALLAZIONE/SINTESIVOCALE/jumper_Snom_D715_cuffia_GEQUDIO_WA9002.png

Avaya IP Phone 1616-L BLK
-------------------------

Configurazione dei Jumper del Mixer utilizzato con il **telefono Avaya iP Phone 1616-L BLK e la cornetta**:

.. image:: /images/TCONSOLE/INSTALLAZIONE/SINTESIVOCALE/jumper_Avaya1616L_cornetta.png

Nortel PC-CIU
-------------

Configurazione dei Jumper del Mixer utilizzato con il **telefono Nortel PC-CIU e la cornetta**:

.. image:: /images/TCONSOLE/INSTALLAZIONE/SINTESIVOCALE/jumper_NortelPCCIU_cornetta.png

Si necessita la regolazione audio da componente R5 (vedi :ref:`Componente R5`) per trovare la giusta regolazione dell’audio della sintesi. Si consiglia audio su PC basso.

Cisco IP Phone 7940
-------------------

Configurazione dei Jumper del Mixer utilizzato con il **telefono Cisco IP Phone 7940 e la cornetta**:

.. image:: /images/TCONSOLE/INSTALLAZIONE/SINTESIVOCALE/jumper_Cisco7940_cornetta.png

Configurazione dei Jumper del Mixer utilizzato con il telefono Cisco IP Phone 7940 e la cuffia Plantronics:

.. image:: /images/TCONSOLE/INSTALLAZIONE/SINTESIVOCALE/jumper_Cisco7940_cuffia_Plantronics.png