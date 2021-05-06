=========================
TODO Installazione di TConsole
=========================

Prima di procedere con l’installazione leggere con attenzione i prerequisiti del capitolo precedente.

L’installazione di TConsole può avvenire nelle seguenti modalità:

    • Server/Standalone
    • Client (di un altro TConsole o di TSAM)
    • Personalizzata

.. important::  Per la completa messa a punto del posto operatore TConsole è necessario fare riferimento ai parametri di funzionamento configurati nel PBX: il supporto di un tecnico di PBX risulta per questo motivo un requisito indispensabile. Assicurarsi di avere a disposizione l’apparecchio telefonico di utilizzo TConsole (come da requisiti indicati nel capitolo precedente) registrato sulla centrale, correttamente configurato e funzionante.

Hardware:
- CPU processore Intel Dual Core ≥ 2.0 GHz
- RAM ≥ 2GB
- HD ≥ 250 GB di spazio disponibile
- Unità DVD-ROM (16x) (se prevista installazione da CD/DVD)
- Scheda di rete C-LAN
- Scheda audio per Sintesi Vocale e segnalazioni acustiche
- 5 porte USB libere (per dongle, tastiera QWERTY, mouse, barra Braille, alimentazione mixer)
- Monitor 4/3 o 16/9 con risoluzione minima 1280*1024
- Tastiera QWERTY con tastierino numerico (keypad)
- Mouse

Opzionali:
- Monitor multimediale (o casse separate) per riproduzione Sintesi Vocale e segnalazioni acustiche
- Porta parallela (solo se si utilizza barra Braille Sistel)
- Per la barra Braille Sistel è necessario installare i driver separatamente utilizzando l’apposito setup ed è necessario disporre di una chiave SISTEL del tipo 87/6

Firewall di Windows: deve essere mantenuto attivo al momento dell’installazione affinchè vengano richieste le conferme per la creazione delle eccezioni o l’apertura di determinate porte durante la fase di installazione di MySQL e di TConsole. (si rimanda a §5.1.1 Installazione e configurazione del servizio MySQL e §5.1.2 Installazione e configurazione TConsole).

Antivirus di sistema: deve essere prevista la possibilità, una volta terminata l’installazione di TConsole, di creare un’eccezione per la cartella e gli eseguibili del programma (TConsole.exe). In base al tipo di centrale sono inoltre richiesti ulteriori requisiti che verranno illustrati di seguito.


.. toctree::
    :maxdepth: 2
 
    Requisiti
    Requisiti_Nortel
