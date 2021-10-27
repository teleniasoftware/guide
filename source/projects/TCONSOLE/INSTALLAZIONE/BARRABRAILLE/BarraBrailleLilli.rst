.. _Barra Braille Lilli:

===================
Barra Braille Lilli
===================

..
    TODO link a mdvbologna.it per download drivers???

TConsole è utilizzabile anche da operatori non vedenti per mezzo della Barra Braille Lilli (sia a 40 che a 80 caratteri).

Per installare la Barra Braille Lilli è sufficiente collegarla ad una porta USB del PC.

.. important :: Dopo aver collegato la barra al PC tramite il cavo USB in dotazione, verificare che il S.O. abbia riconosciuto il nuovo dispositivo (si devono muovere alcuni piedini). Se ciò non dovesse accadere, sostituire in *C:\\Windows\\System32\\* i tre files: *hidclass.sys*, *hidparse.sys*, *hidusb.sys* prelevati dal CD Driver fornito con la Barra Braille oppure dal pacchetto di installazione e utility TConsole fornito da Telenia, e riavviare il PC.

Nella finestra *Gestione dispositivi* (in Windows 10: clic col tasto destro sul menu Avvio, selezionare *Gestione dispositivi*) deve essere presente la voce *Human Interface Device (HID)* e tra queste verificare la presenza di un "Dispositivo di input USB" con descrizione (nel caso di barra a 40 caratteri) "MDV 408 USB".

.. image:: /images/TCONSOLE/INSTALLAZIONE/BARRABRAILLE/Gestione_dispositivi.png

La configurazione della barra e l’associazione dei tasti funzione a determinate funzioni del TConsole avviene tramite la sezione [BRAILLE] del file *Tconsole.ini* descritta in :ref:`TConsole.ini Sezione BRAILLE`.