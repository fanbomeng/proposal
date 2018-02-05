#!/usr/bin/python
# -*- coding: utf-8 -*-
import MySQLdb as mdb
import sys
import matplotlib.pyplot as plt
#try:
con = mdb.connect('localhost','root','3235667','testdb2');
with con:
     year=[2007,2008,2009,2010,2011,2012,2013,2014]
     cur=con.cursor()


     cur.execute("select sum(Age_Adjusted_Death_Rate) from q3 group by year")
     rowsM=cur.fetchall()
     rowtotal=[]
     for row in rowsM:
         rowtotal.append(row[0]/10)





     cur.execute("select Age_Adjusted_Death_Rate from q3 where Race_Ethnicity='Black Non-Hispanic' and sex='M' and Leading_Cause='Diseases of Heart (I00-I09, I11, I13, I20-I51)'")
     rowsM=cur.fetchall()
     cur.execute("select Age_Adjusted_Death_Rate from q3 where Race_Ethnicity='Black Non-Hispanic' and sex='F' and Leading_Cause='Diseases of Heart (I00-I09, I11, I13, I20-I51)'")
     rowsF=cur.fetchall()
     rowBlack_Non_Hispanic_hearttmp=[x + y for x, y in zip(rowsM,rowsM)]
     rowBlack_Non_Hispanic_heart=[]
     for row in rowBlack_Non_Hispanic_hearttmp:
         rowBlack_Non_Hispanic_heart.append(row[0])


     cur.execute("select Age_Adjusted_Death_Rate from q3 where Race_Ethnicity='Black Non-Hispanic' and sex='M' and Leading_Cause='Malignant Neoplasms (Cancer: C00-C97)'")
     rowsM=cur.fetchall()
     cur.execute("select Age_Adjusted_Death_Rate from q3 where Race_Ethnicity='Black Non-Hispanic' and sex='F' and Leading_Cause='Malignant Neoplasms (Cancer: C00-C97)'")
     rowsF=cur.fetchall()
     rowBlack_cancertmp=[x + y for x, y in zip(rowsM,rowsM)]
     rowBlack_cancer=[]
     for row in rowBlack_cancertmp:
         rowBlack_cancer.append(row[0])


     cur.execute("select Age_Adjusted_Death_Rate from q3 where Race_Ethnicity='White Non-Hispanic ' and sex='M' and Leading_Cause='Diseases of Heart (I00-I09, I11, I13, I20-I51)'")
     rowsMW=cur.fetchall()
     cur.execute("select Age_Adjusted_Death_Rate from q3 where Race_Ethnicity='White Non-Hispanic ' and sex='F' and Leading_Cause='Diseases of Heart (I00-I09, I11, I13, I20-I51)'")
     rowsFW=cur.fetchall()
     rowWhite_Non_Hispanic_hearttmp=[x + y for x, y in zip(rowsMW,rowsMW)]
     rowWhite_Non_Hispanic_heart=[]
     for row in rowWhite_Non_Hispanic_hearttmp:
         rowWhite_Non_Hispanic_heart.append(row[0])


     cur.execute("select Age_Adjusted_Death_Rate from q3 where Race_Ethnicity='White Non-Hispanic ' and sex='M' and Leading_Cause='Malignant Neoplasms (Cancer: C00-C97)'")
     rowsMW=cur.fetchall()
     cur.execute("select Age_Adjusted_Death_Rate from q3 where Race_Ethnicity='White Non-Hispanic ' and sex='F' and Leading_Cause='Malignant Neoplasms (Cancer: C00-C97)'")
     rowsFW=cur.fetchall()
     rowWhite_cancertmp=[x + y for x, y in zip(rowsMW,rowsMW)]
     rowWhite_cancer=[]
     for row in rowWhite_cancertmp:
         rowWhite_cancer.append(row[0])




     cur.execute("select Age_Adjusted_Death_Rate from q3 where Race_Ethnicity='Hispanic' and sex='M' and Leading_Cause='Diseases of Heart (I00-I09, I11, I13, I20-I51)'")
     rowsMW=cur.fetchall()
     cur.execute("select Age_Adjusted_Death_Rate from q3 where Race_Ethnicity='Hispanic ' and sex='F' and Leading_Cause='Diseases of Heart (I00-I09, I11, I13, I20-I51)'")
     rowsFW=cur.fetchall()
     rowHispanic_hearttmp=[x + y for x, y in zip(rowsMW,rowsMW)]
     rowHispanic_heart=[]
     for row in rowHispanic_hearttmp:
         rowHispanic_heart.append(row[0])


     cur.execute("select Age_Adjusted_Death_Rate from q3 where Race_Ethnicity='Hispanic ' and sex='M' and Leading_Cause='Malignant Neoplasms (Cancer: C00-C97)'")
     rowsMW=cur.fetchall()
     cur.execute("select Age_Adjusted_Death_Rate from q3 where Race_Ethnicity='Hispanic ' and sex='F' and Leading_Cause='Malignant Neoplasms (Cancer: C00-C97)'")
     rowsFW=cur.fetchall()
     rowHispanic_cancertmp=[x + y for x, y in zip(rowsMW,rowsMW)]
     rowHispanic_cancer=[]
     for row in rowHispanic_cancertmp:
         rowHispanic_cancer.append(row[0])



     plt.plot(year,rowtotal)
     plt.plot(year,rowBlack_Non_Hispanic_heart)
     plt.plot(year,rowWhite_Non_Hispanic_heart)
     plt.plot(year,rowHispanic_heart)
     plt.plot(year,rowBlack_cancer)
     plt.plot(year,rowWhite_cancer)
     plt.plot(year,rowHispanic_cancer)
     plt.legend(['City Sum Age Adjusted Death Rate Scale(1/10)','Black Non Hispanic Diseases of Heart', 'White Non Hispanic Disease of Heart','Hispanic Disease of Heart','Black Non Hispanic Cancer','White Non Hispanic Cancer','Hispanic Cancer'], loc=7,prop={'size': 6})
     plt.savefig('plot1.pdf')
if con:
    con.close()
