.. _Installazione TConsole:

======================
Installazione TConsole TODO
======================

Se il S.O. è Windows Seven o superiore è necessario avviare l’installazione come amministratore (clic con il tasto destro del mouse, **Esegui come Amministratore**) anche se l’utente Windows utilizzato ha privilegi di amministratore del sistema.

Seguire i seguenti passaggi:
    • configurare il S.O. Windows disabilitando tutte le opzioni di risparmio energetico, stand-by e screen-saver (verificare con l’amministratore di sistema che tali modifiche non vengano sovrascritte in seguito dall’eventuale applicazione di Group Policy a livello di Active Directory);
    • collegare la chiave USB di protezione software (rossa) al PC e attendere l’installazione automatica dei relativi driver (tale chiave deve rimanere sempre collegata per permettere l’avvio di TConsole);
    • spostarsi nella cartella (ipotizzando di aver estratto i files di setup in C:\Telenia_Setup):

C:\Telenia_Setup\TConsole V5.7.27\

ed eseguire (tasto destro del mouse, “Esegui come Amministratore”) il file setup.exe

(in alternativa: aprire una finestra di CMD come Amministratore, spostarsi nel percorso indicato ed eseguire setup.exe)

    • dalla pagina iniziale cliccare su Avanti;
    • accettare il contratto di licenza cliccando su Sì;
    • definire la cartella (d’ora in poi indicata con [INSTALLDIR]) di destinazione (se non già esistente, verrà creata automaticamente):
    • (consigliato) accettare quella preimpostata (C:\Telenia\TConsole), oppure
    • specificarne una diversa (ad es. C:\Program Files (x86)\Telenia\TConsole), oppure
    • cliccare sul tasto Sfoglia e sceglierne un’altra già esistente;
    • confermare cliccando su Avanti;
    • confermare l’installazione Server/Standalone cliccando su Avanti;
    • nella schermata Parametri TConsole selezionare il tipo di Centrale e Posto Operatore; confermare con Next;
    • impostare i parametri relativi alla tipologia selezionata (per i dettagli si rimanda a §5.4 Impostazione parametri fondamentali) e premere Next;

N.B.: vengono ora installati ulteriori componenti di terze parti attraverso i rispettivi wizard; se dovesse tornare in primo piano la finestra (sfondo blu) di Installazione TConsole, non chiuderla (eventualmente ridurla a icona), ritornare al wizard del componente e procedere fino al completamento dei seguenti passi:

    • alla pagina di installazione di Borland Database Engine 5.5 cliccare su Avanti;
    • alla successiva pagina di completamento dell’installazione (BDE 5.5) cliccare su Fine;
    • alla pagina Borland Runtime Environment 5.0 cliccare su Avanti;
    • alla successiva pagina di completamento dell’installazione (BRE 5.5) cliccare su Fine;
    • alla pagina di installazione ViaVoice TTS - Italiano cliccare su Avanti;
    • confermare la cartella di destinazione cliccando su Avanti;
    • se il S.O. è Windows 10 potrebbe comparire il messaggio Machine OS cannot be determinated - X86, ignorarlo e si chiuderà automaticamente entro qualche secondo;
    • alla successiva pagina di completamento dell’installazione (TTS) cliccare su Fine;

    • al termine dell’installazione:
    • se il S.O. in uso è precedente a Windows 7, lasciare selezionata l’opzione Riavvia il computer adesso e premere su Fine;
    • per S.O. Windows 7 o successivi, selezionare Non riavviare il computer (e premere su Fine) per completare l’installazione con i punti successivi;

N.B.: verifica delle abilitazioni cartella di installazione per S.O. Windows 7 o successivi:

    • accedere alla cartella d’installazione del programma (default C:\Telenia\TConsole);
    • selezionare la cartella Telenia e, con il tasto destro del mouse, selezionare Proprietà;
    • selezionare il pannello Sicurezza (o Protezione);
    • se non già presente, aggiungere l’utente/gruppo Everyone, abilitando il Controllo completo;
    • confermare le modifiche cliccando su Applica, quindi su OK e al termine riavviare il computer.

.. toctree::
    :maxdepth: 1

    .. TipologieInstallazione
    InstallazioneMySQL
    .. InstallazioneTConsole
    InstallazioneServerStandalone