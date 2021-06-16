==============================
Configurazione Fault Tolerance
==============================

Di seguito i passi per la creazione del DSN di sistema di Fault Tolerance e le successive configurazioni:

- accedere agli **Strumenti di Amministrazione di Windows**, **ODBC di sistema**, versione a 32 bit: **ODBC Data Sources (32-bit)** (per S.O. a 64 bit si trova in *C:\\Windows\\SysWOW64\\odbcad32.exe*);
- spostarsi sulla scheda **DSN di sistema** e creare una nuova origine dati (clic su **Aggiungi...**);
- selezionare il tipo di driver **MySQL ODBC 5.1 Driver** (lo stesso tipo dell’origine dati predefinita *teleniadb*);
- impostare, nella voce **Data Source name** il valore *teleniadb_bk*;
- impostare, nella voce **Description** il valore *teleniadb backup*;
- impostare, nella voce **Server**, il valore *127.0.0.1* (Fault Tolerance in locale);
- modificare la porta preimpostata (3306) inserendo il valore 3366;
- impostare, nella voce **User**, il valore *cgrwin*;
- impostare, nella voce **Password**, il valore *console*;
- nella voce **Database** selezionare *tgest* dal menu a comparsa;
- cliccare su **Test Connection**: la risposta dev’essere *Connection Successful* entro pochi secondi;
- cliccare su **OK**;
- modificare il file *\[INSTALLDIR\]\\config\\Tsam.ini* ([#]_);
- impostare la voce **ALIAS2**\ =\ *teleniadb_bk* (è il **Data Source name** definito in precedenza);
- eventualmente modificare la voce **CHECKTIME** (timeout in secondi per la raggiungibilità del Server: se non si riceve risposta dal Server per un tempo superiore al valore impostato, si attiva il meccanismo di Fault Tolerance sul database definito in **ALIAS2**. Il timeout di default è 20 secondi.

**Esempio TSam.ini con Fault Tolerance:**

.. code-block:: ini
   
    [...]
    
    ALIAS1=teleniadb
    ALIAS2=teleniadb_bk
    DBG=NO
    CHECKTIME=20

.. rubric:: Note

.. [#] valore di default di *\[INSTALLDIR\]*: |tconsole_default_installdir|