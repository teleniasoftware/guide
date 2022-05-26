==============
Avaya CM R.6.2
==============

Licenze AES
===========

Con l'introduzione della release 6.2 di ACM non è più possibile utilizzare AVAYA IP Softphone come service provider TAPI lato PC.

L'utilizzo del TConsole in ambito AVAYA 6.2 deve prevedere una licenza *AES 6.X BSC TSAPI (X>=2)*; 

l'opzione Campo Lampade necessita anch'essa di una licenza *AES 6.X BSC TSAPI (X>=2)* per singolo Posto Operatore.

Quindi se ad esempio servono tre Posto Operatori di cui due con il Campo Lampade le licenze *AES 6.X BSC TSAPI (X>=2)*necessarie sono 5.

In questo modo possiamo garantire la massima efficienza a ciascun P.O. dotato di campo lampade avendo un connettore dedicato TSAPI per l'accesso su richiesta allo 
stato telefonico degli utenti di centrale. 


Installazione di Avaya AES TSAPI client
=======================================

Avaya AES TSAPI client si installa sul PC che ospita Tconsole come descritto nelle pagine seguenti.

La cartella compressa contiene i TSAPI Tools tra cui l'applicazione TSAPI Test.

.. image:: /images/TCONSOLE/INSTALLAZIONE/REQUISITI/InstallazioneAvayaTSAPI01.PNG

.. image:: /images/TCONSOLE/INSTALLAZIONE/REQUISITI/InstallazioneAvayaTSAPI02.PNG

.. image:: /images/TCONSOLE/INSTALLAZIONE/REQUISITI/InstallazioneAvayaTSAPI03.PNG

.. Esempio::
    AES: <ip-address del server AES> 
    port number 450

Premere il tasto  Add to list


.. image:: /images/TCONSOLE/INSTALLAZIONE/REQUISITI/InstallazioneAvayaTSAPI04.PNG

    Premere il tasto Install


.. image:: /images/TCONSOLE/INSTALLAZIONE/REQUISITI/InstallazioneAvayaTSAPI05.PNG


Verifica funzionamento TSAPI
=============================

Ad installazione terminata lancia re l'applicazione TSAPI test

.. Esempio:: 
    USR: Telenia
    PWD: xxxxxxxxxxx

Eseguire una chiamata (Es. da 5000 a 5009) per verificare il buon  funzionamento della  comunicazione TSAPI..


.. image:: /images/TCONSOLE/INSTALLAZIONE/REQUISITI/TestTsapiDevice.png