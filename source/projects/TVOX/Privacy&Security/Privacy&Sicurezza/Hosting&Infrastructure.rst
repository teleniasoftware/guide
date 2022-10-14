.. _hosting:

========================
Hosting e Infrastruttura
========================

TVox è una piattaforma che può essere installata su infrastrutture ed hosting diversi a seconda delle esigenze.

In linea generale, le principali tipologie di hosting sono:

- Installazione su infrastruttura aziendale locale
- Installazione su datacenter privato
- Installazione su provider di servizio hosting web (ad esempio AWS, GCP...)


Compito del gestore dell'infrastruttura che ospita TVox è quello di definire le opportune regole di segregazione del sistema, rispettando i requisiti di funzionamento applicativo.

Tali requisiti, definiti come requisiti di rete, vengono descritti e consegnati dall'installatore e manutentore di TVox al gestore dell'infrastruttura.


.. note:: Basato su sistema operativo AlmaLinux, TVox implementa a bordo il servizio firewalld, un firewall basato su zone. E\' un sistema di sicurezza che monitora il traffico e intraprende specifiche azioni sulla base di un insieme di regole definite applicate contro i pacchetti in entrata.

    Questo firewall implementa una zona denominata "public" attiva sull'interfaccia di rete di TVox, che ha il compito di limitare l'accesso pubblico ai soli servizi necessari al corretto funzionamento dell'impianto




