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