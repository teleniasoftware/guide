.. _campirubricheesterne:

===================
Campi rubriche esterne
===================

Significato dei singoli campi:

- **uid** : Id univoco
- **surname** : Cognome
- **name** : Nome
- **othername** : Altro nome
- **company** : Azienda
- **department** : Reparto
- **street** : Indirizzo
- **postcode** : CAP
- **city** : Città
- **region** : Regione
- **country** : Paese
- **tel{{x}}_value** : Valore numero di telefono
- **tel{{x}}_type** : Tipologia numero di telefono
- **tel{{x}}_id** : Id del numero di telefono
- **mail{{x}}_value** : Valore mail
- **mail{{x}}_type** : Tipologia mail
- **mail{{x}}_id** : Id della mail
- **web{{x}}_value** : Valore sito internet
- **web{{x}}_type** : Tipologia sito internet
- **web{{x}}_id** : Id sito internet
- **role** : Ruolo
- **category** : Categoria
- **vip** : Contatto VIP
- **note** : Note sul contatto
- **kind** : Tipologia del contatto
- **custom_1** : Campo custom 1
- **custom_2** : Campo custom 2
- **custom_3** : Campo custom 3
- **custom_4** : Campo custom 4
- **custom_5** : Campo custom 5
- **custom_6** : Campo custom 6
- **custom_7** : Campo custom 7
- **custom_8** : Campo custom 8
- **custom_9** : Campo custom 9
- **custom_10** : Campo custom 10
- **company_uuid_source** : Id dell'azienda

Dettagli sui valori da rispettare nel risultato della query:

1. Il campo \"uid\" di un contatto è l'id univoco che lo identifica. Viene utilizzato per recuperare, dalle rubriche del TVox, il relativo contatto da sincronizzare per poterlo aggiornare correttamente senza perdere i legami con altre feature.

2. Il campo \"kind\" può assumere due valori:

- **org** : indica un contatto di tipo AZIENDA
- **individual** : indica un contatto di tipo CONTATTO SINGOLO.

3. Il campo \"tel{{x}}_id\" deve essere univoco per ogni numero creato. Se questo numero viene modificato nella sorgente, deve mantenere lo stesso \"tel{{x}}_id\". Questo per poter recuperare lo specifico numero nonostante la modifica, in modo da non perdere i legami con
altre feature.

4. Il campo "tel{{x}}_type" può assumere solamente i seguenti valori:
   
- **WORK** : tipologia Lavoro
- **FAX** : tipologia Fax
- **HOME** : tipologia Casa
- **CELL** : tipologia Cellulare
- **MAIN** : tipologia Principale
- **CELL_WORK** : tipologia Cellulare (lavoro)
- **FAX_WORK** : tipologia Fax (lavoro)
- **FAX_HOME** : tipologia Fax (casa)
- **CELL_HOME** : tipologia Cellulare (casa)
- **OTHER** : tipologia Altro

5. Sono ammessi un massimo di 10 numeri di telefono

6. Il campo \"mail{{x}}_id\" deve essere univoco per ogni mail creata. Se questa mail viene modificata nella sorgente, deve mantenere lo stesso \"mail{{x}}_id\". Questo per poter recuperare la specifica mail nonostante la modifica, in modo da non perdere i legami con altre feature.

7. Il campo \"mail{{x}}_type\" può assumere solamente i seguenti valori:

- **INTERNET_HOME** : tipologia Email (casa)
- **INTERNET_WORK** : tipologia Email (lavoro)

8. Sono ammessi un massimo di 10 mail

9. Il campo \"web{{x}}_id\" deve essere univoco per ogni indirizzo di un sito web associato al contatto. Se questa indirizzo viene modificato nella sorgente, deve mantenere lo stesso \"web{{x}}_id\".
Questo per poter recuperare lo specifico indirizzo nonostante la modifica, in modo da non perdere i legami con altre feature.

10. Il campo \"web{{x}}_type\" può assumere solamente i seguenti valori:

- **HOME** : tipologia Sito Internet (casa)
- **WORK** : tipologia Sito Internet (lavoro)

11. Sono ammessi un massimo di 3 siti internet

12. Il campo \"company_uuid_source\" viene utilizzato per recuperare l'azienda associata ad un contatto. Questo campo deve essere valorizzato con l'\"unique_id\" dell'azienda a lui associata. Questo campo viene letto solo per i contatti che sono di tipo \"CONTATTO SINGOLO\" ossia con il campo \"kind\" uguale a \"individual\".

13. Il campo \"vip\" può assumere solamente due valori:

- **TRUE** : il contatto è VIP
- **FALSE** : il contatto non è VIP
