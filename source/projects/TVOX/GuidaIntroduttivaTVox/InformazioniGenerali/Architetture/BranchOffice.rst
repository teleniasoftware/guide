==================
TVox Branch Office
==================

Un TVox che opera in modalità **Branch Office** svolge il ruolo di Failover PBX quando la comunicazione via rete con il TVox Master risulta interrotta. 

In questa condizione il TVox Branch Office si occupa dell'erogazione temporanea dei servizi telefonici limitatamente agli utenti della sede a cui è destinato. 

Il funzionamento del TVox Branch Office si basa sul fatto che tutti i dispositivi della sede remota hanno una doppia registrazione sempre attiva:
la principale sul TVox Master e la secondaria (di fallback) sul TVox Branch Office. 

Quando il TVox Master non è più raggiungibile il meccanismo di failover configurato sui dispositivi li porta ad utilizzare la seconda identità di registrazione attestata sul Branch Office.

.. important :: La configurazione del TVox Branch Office avviene attraverso il TVox Master garantendo la centralità di quest’ultimo nell’architettura dell’intero sistema. 
    
TVox Master e TVox Branch Office monitorano costantemente la loro raggiungibilità in rete e quando questa non è disponibile generano automaticamente degli allarmi. 

