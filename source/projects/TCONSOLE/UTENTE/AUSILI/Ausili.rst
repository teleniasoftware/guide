=======================================
Ausili per operatori diversamente abili
=======================================

Sintesi Vocale
==============

Il posto operatore TConsole dispone di una Sintesi Vocale integrata nell'applicazione.

.. important:: La Sintesi Vocale è un modulo sottoposto a licenza.

Una volta configurata opportunamente, la Sintesi Vocale è in grado, tramite l'audio del PC, di:

- fornire un riscontro sonoro a fronte della digitazione di un numero nel tastierino numerico (*Keypad*)
- notificare l'operatore dell'arrivo di una nuova chiamata e fornire informazioni ad es. sul numero chiamante
- riprodurre i dettagli di un contatto consultato in Rubrica
- (premendo il pulsante *F4*) fornire informazioni sullo stato della Console: numero di chiamate in corso e loro stato (stato delle linee del Loop), postazione in Giorno/Notte etc.

.. important::
    Le configurazioni relative alla Sintesi Vocale sono descritte nel :ref:`Manuale Installazione`:
    
    - per la configurazione delle sezioni del programma in cui abilitare la Sintesi Vocale fare riferimento a :ref:`Profilo Utente`
    - per la configurazione dei campi da riprodurre nella ricerca o nella consultazione dei contatti di Rubrica fare riferimento alla :ref:`Rubint.ini RubEst.ini Sezione SYNTH` dei files *Rubint.ini* e *RubEst.ini*
    - per la configurazione del Mixer Telenia fare riferimento a :ref:`Sintesi Vocale`

.. note:: Essendo integrata nell'applicazione, la Sintesi Vocale di TConsole è in grado di notificare eventi telefonici (ad es. l'arrivo di una chiamata) anche quando il programma non è in primo piano o è stato ridotto a icona.

.. warning:: La Sintesi Vocale di TConsole **NON** è disponibile al di fuori del programma (ad es. per riprodurre il contenuto del Desktop del PC dopo aver ridotto TConsole a icona) o quando TConsole è stato chiuso.

Barra Braille
=============

TConsole può essere integrato a dispositivi Braille che consentono la lettura delle informazioni sullo stato della console telefonica da parte di operatori non vedenti.

I dispositivi Braille (Barre Braille) attualmente utilizzabili sono:

- MDV Lilli: MB408 (40 caratteri) e MB808 (80 caratteri)
- SISTEL: Barra Braille con chiavi 87/6

Con i dispositivi SISTEL è disponibile la sola funzione di visualizzazione, mentre con il dispositivo Lilli è possibile interagire con la console telefonica per mezzo di appositi tasti funzione presenti sulla Barra.

.. Il collegamento con la Barra è garantito da un’applicazione ausiliaria che si chiama BrailleDriver e che viene lanciato automaticamente da TConsole in fase di avvio. Se l’applicativo viene chiuso verrà rilanciato automaticamente dallo stesso TConsole.

Barra Braille Lilli
-------------------

La Barra Lilli, per la cui installazione e configurazione si rimanda al :ref:`Manuale Installazione` (vedi :ref:`Barra Braille Lilli`) è caratterizzata dall’insieme di caratteri Braille per la visualizzazione (output) e da un insieme di tasti funzionali per l’esecuzione di comandi (input): questo consente di inviare a TConsole l'equivalente di una combinazione di tasti, come se questi fossero stati premuti sulla tastiera del PC.

La Barra Lilli è caratterizzata dall’insieme di caratteri Braille per la visualizzazione (output) e da un insieme di tasti funzionali per l’esecuzione di comandi (input): questo consente di inviare a TConsole l'equivalente di una combinazione di tasti, come se questi fossero stati premuti sulla tastiera del PC.

.. important::
    Le configurazioni relative alla Barra Braille sono descritte nel :ref:`Manuale Installazione`:
    
    - per la configurazione delle sezioni del programma in cui abilitare la Barra Braille fare riferimento a :ref:`Profilo Utente`
    - per la configurazione dei campi da riprodurre nella ricerca o nella consultazione dei contatti di Rubrica fare riferimento alla :ref:`Rubint.ini RubEst.ini Sezione BRAILLE` dei files *Rubint.ini* e *RubEst.ini*
    - per la configurazione dei parametri principali della Barra e dei tasti funzione della Barra Braille Lilli fare riferimento alla :ref:`TConsole.ini Sezione BRAILLE` del file *TConsole.ini*
    - per l'installazione della Barra Braille Lilli fare riferimento a :ref:`Barra Braille Lilli`

Uso della Barra Braille Lilli
-----------------------------

**Display Braille**: le informazioni relative ai diversi stati del posto operatore TConsole sono riportate sul display Braille costituito, in base al modello, da 40 oppure da 80 caratteri di lettura costituiti ciascuno da 8 punti piezo-elettrici ed un pulsantino posto sopra i caratteri.

.. image:: /images/TCONSOLE/UTENTE/AUSILI/BarraBrailleLilli-pulsantini.png

Nella versione attuale i pulsantini posti sopra i caratteri non sono associati ad alcuna funzione.

**Tasti funzione**: nella parte frontale della Barra Braille è presente una tastiera suddivisa in tre sezioni (da sinistra verso destra):

- un gruppo di 5 tasti di controllo denominati *F5*, *F4*, *F3*, *F2*, *F1*
- un gruppo di 6 tasti più grandi: *Shift (L)*, *Left*, *Up*, *Down*, *Right*, *Shift (R)*: i due tasti *Shift (L)* e *Shift (R)* sono funzionalmente equivalenti e vengono utilizzati in combinazione con gli altri tasti per aumentare il numero delle funzionalità disponibili
- un gruppo di 5 tasti di controllo denominati *F6*, *F7*, *F8*, *F9*, *F10*

.. image:: /images/TCONSOLE/UTENTE/AUSILI/BarraBrailleLilli-tasti-funzione.png

Dati visualizzati sulla Barra Braille
-------------------------------------

Barra Braille Sistel
--------------------

.. .. image:: /images/TCONSOLE/UTENTE/CONSOLE/info.png
