.. _Installazione Client:

=========================
Installazione tipo Client
=========================

Il posto operatore TConsole può essere installato in modalità Client per essere collegato a:

- un’altra postazione TConsole configurata come Server (postazione Master)
- una postazione TSAM
- un Server SAM CGR (versione 6.2 o superiore)

**In questa modalità le informazioni di configurazione quali i profili utente e i parametri di sistema, i dati di rubrica ed altre eventuali applicazioni presenti sul Server potranno essere condivise da tutte le postazioni.**

.. In questa modalità le informazioni di configurazione quali i profili utente e i parametri di sistema, i dati di rubrica ed altre eventuali applicazioni Server (es. rubrica web, liste di selezione abbreviata) presenti sul Server potranno essere condivise da tutte le postazioni.

In una configurazione con due o più postazioni TConsole, **ciascuna di esse dovrà essere numerata univocamente a partire da 1** (vedi parametro :ref:`ID` nel file *TConsole.ini*) e dovrà essere connessa al Server per mezzo di una rete LAN.

.. important ::
    La postazione Server dovrà essere dotata di un indirizzo IP fisso (statico) al quale le postazioni Client faranno riferimento.

L’installazione di TConsole in questa modalità richiede quindi, oltre ai :ref:`Requisiti generali` e ai requisiti specifici di centrale, anche le seguenti configurazioni:

- indirizzo IP della macchina Server a cui fare riferimento
- nel caso che la licenza TConsole risieda sul Server, la porta TCP utilizzata dal programma *KeyServer*/*Authorization Server* presente sul Server, se diversa dalla porta di default (5500)
- numero di identificazione progressivo della postazione TConsole

Seguire le istruzioni per la :ref:`Installazione Server Standalone`.

**Al termine dell’installazione sarà necessario modificare il puntamento dell’ODBC di sistema dal database locale al database del Server:**

- accedere agli **Strumenti di Amministrazione di Windows**, **ODBC di sistema**, versione a 32 bit: **ODBC Data Sources (32-bit)** (per S.O. a 64 bit si trova in *C:\\Windows\\SysWOW64\\odbcad32.exe*);
- modificare, nella scheda **DSN di sistema**, l’origine dati **teleniadb** (clic su **Configura...**);
- impostare, nella voce **Server**, al posto di *localhost* (o al posto di *127.0.0.1*) l’indirizzo IP del Server;
- (solo se richiesto in caso di particolare configurazione del Server) nella voce **Port** eventualmente modificare la porta preimpostata (3366);
- nella voce **Database** selezionare (se non già presente) *tgest* dal menu a comparsa;
- cliccare su **Test Connection**: la risposta dev’essere **Connection Successful** entro pochi secondi;
- cliccare su **OK** e riavviare il computer.

**Da questo momento i profili utente e i dati di rubrica verranno recuperati dalla postazione Server che pertanto dovrà essere sempre raggiungibile.**

.. important :: Per gestire le situazioni di emergenza in cui viene persa la comunicazione con il Server, e consentire il funzionamento di TConsole anche in tali condizioni, è necessario:

 - configurare un secondo ODBC di backup (Fault Tolerance) con puntamento al database locale;
 - effettuare, *una tantum* (in fase di installazione) oppure periodicamente tramite procedure schedulate (vedi nota [1]_), la replica delle configurazioni dei profili utente e dei dati di rubrica dal Server alla postazione Client.

.. toctree::
    :maxdepth: 1

    ConfigurazioneFaultTolerance

.. rubric:: Note

.. [1] Per la replica delle configurazioni dei profili utente e della rubrica dal Server, e l’eventuale attivazione di una procedura schedulata, contattare il Service Desk Telenia.