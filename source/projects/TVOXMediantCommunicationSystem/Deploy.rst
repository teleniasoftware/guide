======
Deploy
======

TVox MCS è distribuito attraverso un'appliance in formato ISO scaricabile dal seguente link:
http://www.teleniasoftware.it/download/tvox/iso.php

.. note::
  Su richiesta è disponibile l'immagine in formato compatibile con le seguenti infrastrutture cloud:

  - Amazon Web Servicse (AWS)
  - Google Cloud Platform (GCP)
  - Microsoft Azure

Il sistema operativo dell'appliance ha già subito un processo di hardening attraverso la disabilitazione di servizi non necessari e degli algoritmi HTTPS non sicuri.

.. warning:: Al termine dell'installazione va cambiata la password di admin.

.. note::
  La configurazione MCS è delegata ad una apposita utenza che ai fini di sicurezza potrà accedere solo alla sezione MCS e non accedere alla configurazione del sistema.


.. warning::
  IPS, IDS e Application control sono prestazioni che devono essere erogate da servizi esterni.

.. note::
  Il servizio HTTPS accetta esclusivamente i protocolli TLSv1.0 e superiori.
