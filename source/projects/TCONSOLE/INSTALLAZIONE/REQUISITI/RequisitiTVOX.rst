===========================
Requisiti per versioni TVOX
===========================

**Per le versioni TVOX è necessario utilizzare un telefono SNOM, che deve essere sottoposto a provisioning dalla centrale** (per questi aspetti, e per la configurazione del servizio di tipo Posto Operatore, si rimanda alla guida TVOX), che provvederà a caricare la corretta versione del firmware del telefono e ad impostare su di esso tutti i parametri opportuni.

- **il telefono deve essere configurato sul TVOX come dispositivo di tipo “SNOM PO”**
- non è necessario (comunque consigliato ai fini di teleassistenza) assegnare un IP statico a PC e telefono
- **deve essere garantita la completa visibilità tra telefono SNOM dedicato ed il PC (\**)**
- **una certa versione di TVOX è compatibile solo con determinate versioni di TConsole** (vedi :ref:`Tabella compatibilità TConsole TVOX`)

.. tip ::
    (**) la verifica di visibilità HTTP tra TVOX e telefono può venire effettuata accedendo in SSH al TVOX ed eseguendo il comando (ipotizzando che l’IP del telefono sia *172.16.112.161*):

    .. code-block:: shell

        wget 172.16.112.161
    
    Si deve ottenere una risposta del tipo *200 Ok*:

    .. code-block:: shell
    
        Connecting to 172.16.112.161:80... connected.
        HTTP request sent, awaiting response... 200 Ok

        [...]
    
    seguita dallo scaricamento del file *index.html*:

    .. code-block:: shell

        2020-03-17 14:55:28 (197 KB/s) - ‘index.html’ saved [20896/20896]

.. toctree::
    :maxdepth: 1

    TabellaCompatibilitaTConsoleTVOX
    RequisitiGenerali
    .. Requisiti
