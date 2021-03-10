======
Titolo
======

Sottotitolo
===========

*Testo in italic*

**Testo in grassetto** 

Descrizione normale del capitolo, se voglio creare un nuovo paragrafo basta saltare una riga.

Ecco questo è un nuovo paragrafo.

Lista puntata:
--------------

- Elemento
- Elemento
- Elemento

Lista numerata:
---------------

#. Elemento
#. Elemento
#. Elemento

.. important:: Questo è un testo importante

.. tip:: Questo è un testo suggerimento

.. note:: Questo è un testo nota

.. warning:: Questo è un warning

Lista a campi:
--------------

:Authors:
    Lorenzo Bellani, R&D software developer
:Contatto:
    lbellani@teleniasoftware.com
:Versione: 1.0 18/06/2020

Tabelle:
--------

=====  =====  ======
   Inputs     Output
------------  ------
  A      B    A or B
=====  =====  ======
False  False  False
True   False  True
False  True   True
True   True   True
=====  =====  ======

+------------+------------+-----------+
| Header 1   | Header 2   | Header 3  |
+============+============+===========+
| body row 1 | column 2   | column 3  |
+------------+------------+-----------+
| body row 2 | Cells may span columns.|
+------------+------------+-----------+
| body row 3 | Cells may  | - Cells   |
+------------+ span rows. | - contain |
| body row 4 |            | - blocks. |
+------------+------------+-----------+

Linea di separazione
--------------------

Testo prima della linea di separazione

--------------------------

Testo dopo la linea di separazione

Immagini:
---------

Le immagini vanno messe in una cartella, nel nostro caso la cartella /images e posso metterla della dimensione e nella posizione che preferisco

.. image:: /images/LOGOTVOX.png

IFrame
-------

possiamo creare un iframe che punta a qualsiasi sito, e anche che racchiude un video da youtube.
Per poter mostrare il video da youtube bisogna essere proprietari del video e permettere l'esecuzione del video tramite iframe

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/SIpgmI5Py2Q" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
