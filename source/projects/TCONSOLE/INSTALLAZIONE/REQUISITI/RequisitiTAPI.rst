.. _Requisiti TAPI:

===========================
Requisiti per versioni TAPI
===========================

In queste versioni (Avaya, Cisco, Nortel, Innovaphone etc.) la comunicazione tra TConsole e telefono è delegata ai driver TAPI: **è quindi necessario verificare con il gestore del PBX la disponibilità di TAPI driver compatibili con il Sistema Operativo in uso** (in particolare per quanto riguarda l'utilizzo di versioni TAPI a 32 o a 64 bit), dato che il controllo telefonico effettuato da TConsole è subordinato al corretto funzionamento delle TAPI.

..
 Inoltre, nel pacchetto di installazione TConsole viene fornito un tool (*TestTapiDevice.exe*) che permette di eseguire rapidamente (vedi :ref:`Utilizzo TestTapiDevice`), una volta installate le TAPI, la verifica della corretta comunicazione tra PC e telefono: **prima di procedere con l'installazione di TConsole** si richiede quindi di effettuare le seguenti operazioni preliminari:

 - **installazione delle TAPI**
 - **verifica del funzionamento delle TAPI tramite il** *TestTapiDevice*`**

 **In caso di esito positivo del test si potrà procedere con l'installazione TConsole.**

Inoltre, nel pacchetto di installazione TConsole viene fornito un tool (*TestTapiDevice.exe*) che permette di eseguire rapidamente (vedi :ref:`Utilizzo TestTapiDevice`), una volta installate le TAPI, la verifica della corretta comunicazione tra PC e telefono.

.. important :: 
    **Prima di procedere con l'installazione di TConsole** si richiede quindi di effettuare le seguenti operazioni preliminari:
    
    - installazione delle TAPI
    - verifica del funzionamento delle TAPI tramite il *TestTapiDevice*
    
    **In caso di esito positivo del test si potrà procedere con l'installazione TConsole.**
