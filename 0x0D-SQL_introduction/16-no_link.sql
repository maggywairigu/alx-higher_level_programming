-- Lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.
-- Execute: cat 16-no_link.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
SELECT score, name FROM second_table WHERE name != '' OR name IS NOT NULL ORDER BY score DESC;
