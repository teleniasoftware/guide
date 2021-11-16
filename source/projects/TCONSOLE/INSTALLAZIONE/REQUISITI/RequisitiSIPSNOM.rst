.. _sito di SNOM: https://service.snom.com/display/wiki/Deskphones+Firmware
.. _Wiki SNOM: https://service.snom.com/display/wiki/How+can+I+set+the+phone+to+admin+mode
.. _Action URLs: https://service.snom.com/display/wiki/Action+URLs
.. _Requisiti SIP SNOM:

===============================
Requisiti per versioni SIP SNOM
===============================

Per le versioni SIP è necessario utilizzare un telefono SNOM, che **non deve essere sottoposto a provisioning dalla centrale** (i dettagli sono descritti in seguito) ma deve avvalersi di un'opportuna versione del firmware in base alla release TConsole installata:

- **fino alla release TConsole 5.7.10 utilizzare firmware 8.7.3.19**
- **per release TConsole 5.7.11 - 5.7.19 utilizzare firmware 8.7.5.x**
- **per release TConsole 5.7.20 - 5.7.27 utilizzare firmware 8.7.5.x - 8.9.3.x**
- **dalla release TConsole 5.7.28 è possibile utilizzare, oltre al firmware 8.7.5.x-8.9.3.x, anche il firmware 10.1.64.14 o superiore**

.. tip:: I firmware indicati, e le procedure per il loro caricamento, sono disponibili nel `sito di SNOM`_).

.. warning:: Non è garantito il corretto funzionamento di TConsole nel caso si cerchi di utilizzare un firmware di versione diversa dalle versioni specificate in questo documento.

Deve essere garantita la completa visibilità, **agendo opportunamente sul Firewall di sistema se necessario**, tra telefono SNOM dedicato ed il PC su cui installare TConsole, in particolare:

- **PC e telefono devono avere IP statico o comunque staticamente assegnato**
- **il PC deve raggiungere sulla porta 80 (HTTP) (ad es. via browser) l'IP del telefono e del server SIP**
- **il telefono deve poter comunicare con il PC TConsole sulla porta 5452 TCP** (valore di default eventualmente modificabile, vedi :ref:`Parametri SIP SNOM`)

.. important::
  Se PC e telefono appartengono a LAN diverse è necessario garantire le medesime visibilità sulle porte indicate tra la LAN del telefono e la LAN del PC TConsole. In caso negativo si possono presentare tipicamente uno (o più) di questi comportamenti:

  - da TConsole si riesce a fare partire una chiamata, ma poi non si riesce a controllarla (occorre utilizzare il telefono) e non viene visualizzata nel loop (Linea 0, Linea 1, ...)
  - una chiamata in ingresso arriva sul telefono, ma su TConsole non compare nulla

Inoltre è necessario impostare sul telefono, accedendo via browser all'interfaccia web (*WUI*) di configurazione, alcuni parametri come indicato nelle figure che seguono (ipotizzando che l'IP del telefono sia *172.16.112.161*).

.. important:: Per impostare i seguenti parametri, l'interfaccia web del telefono deve essere impostata in *Admin Mode* (vedi `Wiki SNOM`_). Anche al termine della configurazione in fase di installazione l'interfaccia va lasciata in questa modalità, per consentire a TConsole di impostare i parametri necessari al corretto funzionamento (in particolare le `Action URLs`_, necessarie a TConsole per ricevere gli eventi telefonici dal dispositivo).

- scheda **Advanced | Update** (ad es. *http://172.16.112.161/advanced_update.htm*), in particolare verificare che **Update Policy** sia settato a: *Never update, do not load settings*

.. image:: /images/TCONSOLE/INSTALLAZIONE/REQUISITI/advanced_update.png

- scheda **Identity 1 | RTP** (ad es. *http://172.16.112.161/line_rtp.htm?l=1*)

.. image:: /images/TCONSOLE/INSTALLAZIONE/REQUISITI/line_rtp.png
.. .. warning:: Seppure sia possibile impostare più di una identità sul telefono SNOM, nella configurazione TConsole è possibile specificare una sola identità, che sarà l'interno utilizzato per effettuare e ricevere le chiamate tramite l'applicazione.

.. forse in ricezione funziona con tutte le identità? controllare le action urls
.. effettuate da TConsole può venire utilizzata solo una di queste identità, definita nella configurazione.

- scheda **Advanced | QoS/Security** (ad es. *http://172.16.112.161/advanced_qos_security.htm*), in particolare verificare che:

  - **Un-/Tag VLAN traffic to/from specific switch ports** sia settato a:  *off*
  - **Use hidden tags** sia settato a:  *off*
  - **Authentication Scheme** sia settato a: *Basic*

.. image:: /images/TCONSOLE/INSTALLAZIONE/REQUISITI/advanced_qos_security.png
