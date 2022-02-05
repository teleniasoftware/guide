====================
Stanze di Conferenza
====================

La prestazione telefonica di Conferenza permette la comunicazione simultanea tra più
interlocutori ed è accessibile con una numerazione riservata.

TVox Omnichannel Contact Center realizza un sistema di audio conferenza con numero di partecipanti illimitato

E\' possibile definire conferenze di due tipologie:

**Privata** 

E\' una conferenza associata ad un utente.
In questo caso la prestazione di conferenza è gestita dall'utente che 
la possiede, trasferendo direttamente gli interlocutori al numero 
che identifica la stanza di conferenza. 
L'utente entra in conferenza componendo il numero associato alla stanza 
di conferenza. 
Se si ha la necessità di aggiungere interlocutori alla conferenza 
è sufficiente mettere in attesa la chiamata di conferenza, 
chiamare i nuovi interlocutori e trasferirli direttamente
nella propria stanza. 
Per rientrare in conferenza basta riprendere dall'attesa la chiamata. 
La definizione delle stanze di conferenza privata è accessibile dalla
sezione Avanzate del dettaglio utente.

**Pubblica** 

E\' una conferenza accessibile da chiunque chiamando il numero ad essa
associato e fornendo il PIN di accesso richiesto. 


Configurazione Conferenza pubblica
----------------------------------

Una nuova Stanza di Conferenza Pubblica è configurabile da OCC nella sezione *Canali=>Telefono=>Conferenze*

.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/Conferenza/Pubblica.PNG


E\' obbligatorio definire i seguenti campi:


Parametro Generale:

  **Numerazione Conferenze**: Numerazione da assegnare alle stanze di conferenza pubbliche e/o private. Tale numerazione è necessaria per poter attivare agli utenti TVox Omnichannel Contact Center la prestazione telefonica di conferenza pubblica e privata

Parametri Specifici della Stanza Conferenza:

  **Nome**: descrizione identificativa della conferenza

  **Numero associato**: numero interno da associare alla conferenza; questo numero deve far parte delle numerazioni definite dal parametro "Numerazione Conferenze"

I rimanenti parametri di configurazione Stanza di Conferenza sono da definire qual'ora siano di interesse e si suggerisce la lettura dell' Help On Line su ogni singolo parametro.

.. important:: **BEST PRACTICE:** E\' fortemente consigliato l'utilizzo dei parametri PIN sia Utente che Amministratore per ovvie ragioni di Sicurezza

E\' possibile associare al numero di conferenza pubblica una regola di ingresso al fine di permettere l'accesso alla conferenza anche chiamando dall'esterno.  

Configurazione Conferenza privata
---------------------------------

Una nuova Stanza di Conferenza Privata è configurabile da OCC nella sezione *Utenti*, in Edit di un Utente, nel TAB *PBX*


.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/Conferenza/Privata.PNG


E\' obbligatorio definire i seguenti campi:

  **Numero Associato**: numero interno da associare alla conferenza; questo numero deve far parte delle numereazioni definite dal parametro **Numerazione Conferenze**
  
  **PIN Utente**: codice numerico richiesto all'utente quando trasferisce con consultazione gli interlocutori nella propria stanza di conferenza oppure un utente chiama autonomamente la stanza privata di un altro utente ed è stato informato del codice da utilizzare. In caso di trasferta diretta (blind transfert) invece questo PIN non viene richiesto.

I rimanenti parametri di configurazione Stanza di Conferenza sono da definire qual'ora siano di interesse e si suggerisce la lettura dell' Help On Line su ogni singolo parametro.