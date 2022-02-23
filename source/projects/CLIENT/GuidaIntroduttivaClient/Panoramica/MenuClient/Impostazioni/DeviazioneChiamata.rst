.. _deviazione:

===================
Deviazione Chiamata
===================

Questa sezione presenta la configurazione delle deviazioni che sono attive per l'utente.

.. tip::  **Best Practice**  |br| Per gestire correttente la deviazione chiamate e poter avere un riscontro su TVox delle deviazioni stesse è necessario che la configurazione sia effettuata via OCC o via client e NON direttamente sul dispositivo telefonico in uso.

L'utente ha la possibilità di definire il trattamento di deviazione delle chiamate, distinte tra interne ed esterne, verso le seguenti destinazioni alternative:

*  **Chiama altro numero** : inoltra le chiamate ad un numero telefonico interno o esterno.
*  **Ritorna al capolinea** : inoltra le chiamate al Posto Operatore, ove disponibile.
*  **Riaggancio** : la chiamata viene chiusa.
*  **Casella vocale** : inoltra le chiamata alla segreteria telefonica dell'utente, ove disponibile.

E\’ possibile attivare la deviazione specificandone la condizione in cui si verifica:


*  **Da Telefono** (possibile solo se il dispoitivo telefonico eè un dispositivo SIP fisico): la deviazione di chiamata si intende attivata per qualsiasi contesto.

.. important:: Quando la deviazione di chiamata da telefono viene attivata le altre deviazioni perdono di significato.

*  **Sempre** : la deviazione di chiamata si intende attivata per qualsiasi contesto.
*  **Interno non attivo** : (interno non registrato su TVox Omnichannel Contact Center) gestisce la deviazione di chiamata quando si verificano problemi di connettività o raggiungibilità del terminale telefonico dell'utente (ES: soft phone non attivo o non registrato).
*   **Interno occupato** : attiva la deviazione di chiamata quando l’utente è già impegnato in una conversazione.
*  **Attesa superata** : va indicato il tempo di ring scaduto il quale si attiva la deviazione di chiamata.
*   **Non presente** : se l'utente non ha avviato il TVox Client sulla propria postazione di lavoro.


.. image:: /images/CLIENT/MenuClient/Impostazioni/client_deviazione_chiamata.PNG

|br|


