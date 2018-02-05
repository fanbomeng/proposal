#!/usr/bin/python
# -*- coding: utf-8 -*-
import MySQLdb as mdb
import sys
#try:
con = mdb.connect('localhost','root','3235667','testdb2');
with con:
     cur=con.cursor()
   #  cur.execute('DROP TABLE IF EXISTS Mytest')

     cur.execute("CREATE TABLE Q3(Year VARCHAR(8),Leading_Cause VARCHAR(200),Sex VARCHAR(4),Race_Ethnicity VARCHAR(70),Deaths INT,Death_Rate INT,Age_Adjusted_Death_Rate INT)")





#     cur.execute("CREATE TABLE Mytest(name1 VARCHAR(70),name2 VARCHAR(100))")
     #cur.execute("LOAD DATA LOCAL INFILE '/Users/FMENG/Desktop/Jobs/incubter/question2/trail2.csv' INTO TABLE Mytest FIELDS TERMINATED BY ',' ENCLOSED BY '\"' IGNORE 1 LINES ")
     cur.execute("LOAD DATA LOCAL INFILE '/Users/FMENG/Desktop/Jobs/incubter/question3/New_York_City_Leading_Causes_of_Death.csv' INTO TABLE Q3 FIELDS TERMINATED BY ';'  ENCLOSED BY '\"' IGNORE 1 LINES")
  #   cur.execute("INSERT INTO Mytest(Id,FirstName,Lastname,Birthday) VALUES(1,'Fanbo','Meng',19891209)")
#except mdb.Error, e:
#    print("Error %d: %s" % (e.args[0],e.args[1]))
#    sys.exit(1)
#
#finally:
#
if con:
    con.close()
