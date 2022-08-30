Addressbook
======================

Il blocchetto \"Addressbook\" permette di recuperare una o più proprietà di un contatto di rubrica e di salvarle il valore in una variablie. Il nome della variabile sulla quale viene salvato il rusltato della ricerca sarà automaticamente modificato concatenando il nome della proprietà ricercata.

Esempio:

**Proprietà da recuperare:** Telefono (TEL),E-Mail (EMAIL)
**Variabile di ritorno:** contatto

Verranno generate due varibili: contatto-TEL, contatto-EMAIL. 

Da questo blocchetto partono due frecce con valore rispettivamente "single" e "none":

- **single**: significa che è stato trovato il contatto in rubrica.
- **none**: significa che non è stato trovato alcun contatto in rubrica.

.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/BPM/BLOCCHETTI/addressbook.png

    
.. image:: /images/TVOX/GuidaIntroduttivaTVox/ConfiguraPBX/BPM/BLOCCHETTI/addressbook_config.png

**Campi configurabili**

- **Modalità di lookup**: selezione del tipo di lookup che si desidera utilizzare per la ricerca in rubrica (**Lookup clid** viene utilizzato il CLID recuperato automaticamente dal processo. **Lookup personalizzata** permette inserire il nome di una variabile che contiente il CLID. **Proprietà** permette fare una ricerca per una proprietà diversa dal CLID. Sarà necessario selezionare la proprietà di ricerca e impostare il valore che deve avere la proprietà. Se il valore è contenuto a sua volta in una variabile basta non mettere il check sul campo Imposta come valore.)
- **Proprietà da recuperare**: permette di selezionare una o più proprietà di un contatto
- **Variabile di ritorno**: variabile in cui salvare la proprietà recuperata