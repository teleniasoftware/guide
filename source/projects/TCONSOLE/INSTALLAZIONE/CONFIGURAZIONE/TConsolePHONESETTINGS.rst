.. _TConsole.ini Sezione PHONE_SETTINGS:
.. _sito di SNOM: https://service.snom.com/display/wiki/D-Series+Settings

=====================================
TConsole.ini Sezione [PHONE_SETTINGS]
=====================================

**Per il TConsole di tipo SIP SNOM**, per risolvere il problema che, nel caso di una chiamata trasferita da un Telefono SNOM verso un numero esterno, venga abbattuta la prima chiamata e rigenerata una seconda, settare il seguente parametro a *on* (valore di default):

.. code-block:: ini

    attended_transfer_on_ringing=on

.. tip :: In questa sezione, oltre ai parametri già presenti di default per il corretto funzionamento di TConsole, è possibile configurare altri parametri (vedi `sito di SNOM`_) che verranno impostati sul telefono ([1]_) al momento dell'avvio di TConsole.

.. rubric:: Note

.. [1] per mantenerli anche alla chiusura di TConsole, questi parametri vanno memorizzati agendo sull'interfaccia web del telefono: https://service.snom.com/display/wiki/How+do+snom+phones+handle+setting+changes