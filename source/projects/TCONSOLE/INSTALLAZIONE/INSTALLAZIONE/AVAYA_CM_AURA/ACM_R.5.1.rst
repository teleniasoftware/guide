=========
Avaya CM R.5.1
=========
L’accodamento simultaneo delle chiamate sui terminali dei P.O. è realizzato attraverso un sistema a doppia copertura, occorre quindi definire un Coverage Path relativo ad un Coverage Answer Group a cui appartengono tutti i terminali dedicati ai P.O. 

Il **Coverage Answer Group** deve essere inserito in un apposito Hunt Group indirizzato da un VDN configurato come attendant Vectoring e gestito tramite un vettore. 
Attraverso questa architettura tutte le chiamate indirizzate al servizio di **ATTENDANT** vengono presentate a tutti i telefoni dei P.O. e il primo che risponde svincola la chiamata consentendo agli altri P.O. di gestire le altre. Ogni P.O. è in grado di gestire fino a 5 chiamate contemporanee quindi un singolo servizio di **ATTENDANT* basato su un coverage Answer Group consente un massimo di 8 P.O. e una gestione di 40 chiamate contemporanee. 

Nel caso in cui i servizi **ATTENDANT** siano regolati da un calendario/orario occorre prevedere tale prestazione sull’AVAYA Communication Manager in modo da inoltrare le chiamate ai  P.O. solo nei giorni e negli orari desiderati.

L’Overflow viene gestito in tre modi:

- Attraverso l’emissione di un tono di occupato
- Il trasferimento su un numero alternativo
- Un annuncio di dissuasione se disponibile sull’AVAYA Communication Manager l’apposita scheda annunci.

La gestione Notte può essere attivata in due modalità 

- **AUTOMATICA** configurando sul Coverage Path un numero massimo di squilli trascorsi i quali la chiamata viene inoltrata ad un altro numero o gestita tramite un annuncio di dissuasione 
- **MANUALE** attraverso un tasto del TConsole preconfigurato per trasferire in modalità BLIND le chiamate in arrivo sul P.O. verso un numero alternativo. Tale modalità attiva lo stato NOTTE per tutti i P.O. 

.. image:: /images/TCONSOLE/INSTALLAZIONE/REQUISITI/Schema_Blocchi.PNG


Prerequisito terminale telefonico
=================================

L’utilizzo di TConsole è certificato con terminali telefonici di tipo 14xx o 16xx che potranno essere utilizzati con cuffia e dovranno essere configurati con almeno 6 tasti linea di cui 5 configurati in modalità bidirezionale e dedicati all’accodamento delle chiamate mentre il 6° monodirezionale per svincolare le chiamate.

Per ogni terminale telefonico deve essere prevista una licenza Avaya IP Softphone necessaria per  consentire al TConsole l’accesso a tutte le funzionalità telefoniche necessarie al P.O. L’Avaya IP Softphone stabilisce un link TAPI tra il TConsole e il terminale telefonico del P.O. consentendo l’accesso alle funzioni telefoniche attraverso tastiera, mouse e Display Braille e la traduzione degli eventi telefonici in Sintesi Vocale.

A tal proposito è necessario configurare la centrale con tipi di terminali correttamente
supportati dall’Avaya Soft Phone, infatti quest’ultimo permette il controllo solo di terminali digitali di tipo 24xx oppure di terminali IP della serie 46xx o 96xx. Quindi, anche se i terminali che si utilizzano sono di tipo 14xx o 16xx, dovranno essere configurati sulla centrale rispettivamente come 24xx e 46xx o 96xx.

.. image:: /images/TCONSOLE/INSTALLAZIONE/REQUISITI/InstallazioneAvayaIPSoftPhone01.PNG

.. image:: /images/TCONSOLE/INSTALLAZIONE/REQUISITI/InstallazioneAvayaIPSoftPhone02.PNG

.. image:: /images/TCONSOLE/INSTALLAZIONE/REQUISITI/InstallazioneAvayaIPSoftPhone03.PNG

.. image:: /images/TCONSOLE/INSTALLAZIONE/REQUISITI/InstallazioneAvayaIPSoftPhone04.PNG


Configurazione SoftPhone
========================

Lanciando per la prima volta il softphone vengono chieste delle configurazioni. Indipendentemente dalle configurazioni impostate si arriva poi a una pagina riassuntiva in cui si devono impostare i parametri come segue:

.. image:: /images/TCONSOLE/INSTALLAZIONE/REQUISITI/ConfigurazioneAvayaIPSoftPhone01.PNG

.. image:: /images/TCONSOLE/INSTALLAZIONE/REQUISITI/ConfigurazioneAvayaIPSoftPhone02.PNG

Impostare Configuration: *Control of Avaya Telephone (via the server)*. Nel caso invece si voglia usere il softphone impostare Configuration: *Road Warrior* e inserire la password.

Di seguito gli altri screenshot di configurazione dell’interno 641 usato come PO. Ricordiamo che il 641 è un telefono IP fisico.

.. image:: /images/TCONSOLE/INSTALLAZIONE/REQUISITI/ConfigurazioneAvayaIPSoftPhone03.PNG

.. image:: /images/TCONSOLE/INSTALLAZIONE/REQUISITI/ConfigurazioneAvayaIPSoftPhone04.PNG

.. image:: /images/TCONSOLE/INSTALLAZIONE/REQUISITI/ConfigurazioneAvayaIPSoftPhone05.PNG

.. image:: /images/TCONSOLE/INSTALLAZIONE/REQUISITI/ConfigurazioneAvayaIPSoftPhone06.PNG

