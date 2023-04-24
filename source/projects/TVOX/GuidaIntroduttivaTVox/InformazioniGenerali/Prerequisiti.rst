============
Prerequisiti
============

Il TVox Communication attivabile nella piattaforma TAM eroga i servizi telefonici utilizzando
una sola interfaccia fisica di rete.

Eventuali interfacce di rete aggiuntive possono essere utilizzate per management e/o per connettere a Provider VoIP remoti, per i quali non si ha la possibilità di farli accedere all'indirizzo principale


.. important:: E\' necessario che in una architettura distribuita su più server non esistano limitazioni altraffico di rete tra essi generato.

.. important:: E\' necessario inserire gli indirizzi IP assegnati ai sistemi TAM tra le eccezioni del Proxy per evitare la non raggiungibilità di tali sistemi.


Per l’attivazione di un TVox Communication occorre predisporre:

- Cavi di rete di categoria 5/6 per il collegamento di tutti gli apparati di rete.
- Cavi RJ11 per collegare dispositivi FAX o terminali BCA agli ATA .
- Cavi RJ11/RJ45 per collegare gli eventuali Voice/SMS/GSM Gateway alla rete PSTN (analogiche, BRI, PRI) e predisporre gli eventuali adattatori di impedenza.
- Alloggiamento negli eventuali armadi dei server dedicati alle piattaforme TVox (nel caso si stia parlando di hardware fisici).
- Piano di indirizzamento IP statico per le piattaforme TVox e gli eventuali gateway per l’interfacciamento alla rete voce, gsm, wifi etc.
- Piano di indirizzamento per i terminali telefonici consigliando la modalità DHCP se si vuole utilizzare al meglio il modulo di AUTOPROVISIONING per i telefoni supportati.
- Piano di numerazione interno da assegnare ai terminali telefonici specificando l’eventuale disponibilità della selezione passante.
- La definizione dei codici di accesso per l’accesso alla rete PSTN o ad eventuali altri sistemi telefonici connessi al TVox Communication.
- Definizione del Routing delle chiamate.
- Predisposizione dei messaggi vocali codificati in formato Windows WAVE (PCM, 8KHz, 16 Bit Mono) necessari al sistema.
- Diagrammi relativi ai servizi IVR che si intendono realizzare.
- Per ciascun utente che utilizzerà il sistema le seguenti informazioni: username, password, interni da associare, email, cellulare, abilitazioni di Unified Communication (es: chat, presence, sms, look-up su anagrafica) re direzione su numeri esterni, deviazione di chiamata, gruppi di risposta / skill, Classe di servizio (es: Abilitazione, Filtro, Registrazione conversazioni) gruppi di Pick-up, abilitazioni di Voicemail, Conferenza e definizione di caselle FAX ove disponibili.