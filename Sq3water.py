#!/usr/bin/python
# -*- coding: utf-8 -*-
import MySQLdb as mdb
import sys
#try:
con = mdb.connect('localhost','root','3235667','testdb2');
with con:
     cur=con.cursor()
   #  cur.execute('DROP TABLE IF EXISTS Mytest')

     cur.execute("CREATE TABLE Q3water(Sample_Number VARCHAR(200),Sample_Date VARCHAR(200),Sample_Time time,Sample_Site VARCHAR(200),Sample_class VARCHAR(200),Location VARCHAR(200),Residual_Free_Chlorine float(3),Turbidity float(3),Fluoride float(3),Coliform VARCHAR(500),E_coli VARCHAR(50))")





#     cur.execute("CREATE TABLE Mytest(name1 VARCHAR(70),name2 VARCHAR(100))")
     #cur.execute("LOAD DATA LOCAL INFILE '/Users/FMENG/Desktop/Jobs/incubter/question2/trail2.csv' INTO TABLE Mytest FIELDS TERMINATED BY ',' ENCLOSED BY '\"' IGNORE 1 LINES ")
     cur.execute("LOAD DATA LOCAL INFILE '/Users/FMENG/Desktop/Jobs/incubter/proposal/Drinking_Water_Quality_Distribution_Monitoring_Data.csv' INTO TABLE Q3water FIELDS TERMINATED BY ','  ENCLOSED BY '\"' IGNORE 1 LINES")
  #   cur.execute("INSERT INTO Mytest(Id,FirstName,Lastname,Birthday) VALUES(1,'Fanbo','Meng',19891209)")
#except mdb.Error, e:
#    print("Error %d: %s" % (e.args[0],e.args[1]))
#    sys.exit(1)
#
#finally:
#
if con:
    con.close()
