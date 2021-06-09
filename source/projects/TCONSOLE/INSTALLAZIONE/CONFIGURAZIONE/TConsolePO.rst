.. _TConsole.ini Sezione PO:

=========================
TODO TConsole.ini Sezione [PO]
=========================

TODO DISPLAY_ACTIVE_STATE
--------------------
Solo per TConsole su PBX Avaya-M2250/CIU è possibile abilitare/disabilitare la segnalazione dello stato attivo della console Avaya-M2250/CIU

TODO TAPI_CALL_ON_BUSY_CODE
----------------------
Tale parametro va settato con il codice configurato su PBX per trasferire le chiamate anche su occupato. Tale codice verrà anteposto ad ogni chiamata da rubrica, da Post-IT ed in fase di trasferta dal Keypad. IMPORTANTE!! Valorizzare con - se non si vuole utilizzare alcun codice. Se viene settato con un codice errato (non esistente su PBX) si ottiene l’anomalia di impossibilità di trasferire le chiamate.
Es:
TAPI_CALL_ON_BUSY_CODE=*60 (settato con un codice)
TAPI_CALL_ON_BUSY_CODE=- (non settato)

TODO LINE_0_TOP=SI/NO 
----------------------
	SI: 	inversione, rispetto alla situazione di default, della visualizzazione dell’ordine delle 
		linee entranti: "0" in alto "5" in basso
	NO: 	le linee entrati mantegono l’ordine di default ossia "0" in basso e "5" in alto

IPO_PLUS_ICI_TOP (SI/NO)
	SI: 	- porta all’aumento in altezza (da 46 a 55) del carattere sulle text di numeri in 
		ingresso/uscita 
		- allinea i 3 riquadri EN-IN-RT alla prima linea in alto
	NO: 	si mantengono dimensioni e posizionamenti EN-IN-RT di default

IPO_PLUS_TIME (SI/NO)
	SI: 	per abilitare l’orologio sulla vista IPO-PLUS
	NO:	si mantiene la visualizzazione di default priva di orologio per lasciare maggior spazio 
		sul monitor


.. TODO serve la nota????????

.. rubric:: Note

.. [1] valore di default di *\[INSTALLDIR\]*: |tconsole_default_installdir|