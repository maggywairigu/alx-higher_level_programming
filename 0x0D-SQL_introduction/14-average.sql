-- Computes the score average of all records in the table second_table of the database hbtn_0c_0 in your MySQL server.
-- Execute: cat 14-average.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
SELECT AVG(score) AS average FROM second_table;
