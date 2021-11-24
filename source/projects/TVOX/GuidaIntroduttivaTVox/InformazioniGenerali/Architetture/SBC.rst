========
TVox SBC
========

TVox **SBC** è una componente infrastrutturale che può essere utilizzata quando il TVox Master è posizionato in datacenter (modalità pure cloud con MCS) e si vogliono gestire le sedi dotate di linee PSTN o centrali telefoniche locali che hanno la necessità di comunicare con il TVox Master senza obbligare il cliente a stabilire una VPN.

In questo caso TVox SBC viene installato **presso la sede del cliente** e la sua funzione è di connettere le centrali locali SIP o le linee PSTN al datacenter.

Requisiti
=========

SBC può avere una o più interfacce Ethernet utilizzate per garantire piena visibilità verso il TVox Master e gli apparati locali (Gateway SIP o Centrali VoIP) che deve interconnettere.

.. image:: /images/SBC/sbc_product.png
   :scale: 60%
   :align: center