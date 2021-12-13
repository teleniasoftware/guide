================
Gruppi di Pickup
================

La funzionalità di Pick Up consente a un utente TVox Omnichannel Contact Center di prendere **una chiamata che sta squillando** su un telefono di un altro utente che **appartiene al medesimo gruppo di Pick Up**. 

Per accedere alla prestazione di Pick Up occorre seguire i seguenti passi:

- Verificare il codice di servizio necessario ad attivare la funzionalità di Pick Up (es. '**' (codice di default))

- Verificare la numerazione riservata ai gruppi di Pick Up (es. '5XX')

- Definire uno o più gruppi di Pick Up.

Per prendere una chiamata generica nell'ambito dei propri gruppi di Pick Up è sufficiente digitare il codice di servizio relativo (es. '**'); 
il TVox Omnichannel Contact Center in questo caso presenta all'utente l'ultima chiamata destinata ai suddetti gruppi. 

Nel caso in cui si vuole prendere la chiamata di uno specifico gruppo di Pick Up occorre digitare il codice di servizio 
seguito dal numero che identifica il gruppo di Pick Up; 
anche in questo caso il TVox Omnichannel Contact Center presenta all'utente l'ultima chiamata destinata al suddetto gruppo. 

Se si ha la necessità di prendere la chiamata che sta squillando su uno specifico interno di un utente che appartiene a uno dei propri gruppi 
occorre digitare il codice di servizio seguito dall'interno desiderato.

Configurazione Gruppo Pickup
----------------------------

La configurazione dei Gruppi di Pickup si trova nel seguente percorso:

    OCC->[CANALI]Telefono->Gruppi di Pickup

Per prima cosa è obbligatoria (obbligo rappresentato dall'* di colore rosso accanto al nome del parametro) la definizione della "Numerazione gruppi di Pick Up" che rappresenta il range della numerazione interna assegnabile ai Gruppi di Pick Up che si andranno a definire. 

Per tale numerazione è possibile specificare cifre da 0 a 9 e il carattere speciale X che indica un numero da 0 a 9. Ad esempio: 55X individua gruppi di Pick Up da 550 a 559.

Per la definizione di un gruppo di Pink Up si procede dal tasto [Nuovo].

I campi obbligatori per la definizione sono:

- **Nome** :   Nome associato al Gruppo di Pick Up. Se si utilizza il TVox Client è possibile accedere alla prestazione di Pick Up selezionando dal relativo menù a tendina il nome del gruppo.
- **Numero**: Numero da digitare dopo il codice di Pick Up (es. **) per effetture il Pick up di una chiamata che sta squillando sull'interno di uno degli utenti che appartengono al gruppo.

Successivamente si procede nell'associazione degli utenti a tale gruppo di Pick Up, cercandoli tra gli utenti già definiti sul Tvox dall'apposito campo "Seleziona un utente". 

Con un click sul campo, verrà proposto l'elenco degli utenti definiti su TVox e con un altro click si procede all'associazione.
Per eventuale disassociazione dell'utente si procede con un click sull'icona "X" in corrispondenza della riga dell'utente desiderto.

Al termine della configurazione del gruppo di Pickup si procede al salvataggio attraverso il tasto [SALVA]