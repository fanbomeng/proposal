#!/usr/bin/python
# -*- coding: utf-8 -*-
import MySQLdb as mdb
import sys
import matplotlib.pyplot as plt
#try:
con = mdb.connect('localhost','root','3235667','testdb2');
with con:
     year=['2015','2016','2017']
     Xlable=['01-06 2015','07-12 2015','01-06 2016','07-12 2016','01-06 2017','07-12 2017']
     cur=con.cursor()
     tmp='%'
     monthrange1=['01','02','03','04','05','06']
     monthrange2=['07','08','09','10','11','12']
     averagevalue=[]
     '01''%''2015'
     for Year in year:
         tmpmonthvalue=0
         numbercercle=0
         for Month1 in monthrange1:
#             tmpstring=Month1+tmp+Year
#             print(tmpstring)
             cur.execute("select avg(Residual_Free_Chlorine) from q3water where (Sample_Date like '%s') and Residual_Free_Chlorine>0" %(Month1+tmp+Year))
             print("select avg(Residual_Free_Chlorine) from q3water where (Sample_Date like '%s') and Residual_Free_Chlorine>0" %(Month1+tmp+Year))
             numb=cur.fetchone()
#             if type(numb)==type(None):
#                 continue
#             print(numb[0])
             try:
                numbercercle=numbercercle+1
                tmpmonthvalue=tmpmonthvalue+numb[0]
             except:
                 print("one Null")
         averagevalue.append(tmpmonthvalue/numbercercle)
         numbercercle=0
         for Month1 in monthrange2:
             cur.execute("select avg(Residual_Free_Chlorine) from q3water where (Sample_Date like '%s') and Residual_Free_Chlorine>0" %(Month1+tmp+Year))
             numb=cur.fetchone()
#             if type(numb)==type(None):
#                 continue
             try:
                 tmpmonthvalue=tmpmonthvalue+numb[0]
                 numbercercle=numbercercle+1
             except:
                 print("one Null")
         averagevalue.append(tmpmonthvalue/numbercercle)
     plt.plot(Xlable,averagevalue,'ro')
     plt.legend(['Average Residual Free Chlorine'])
     plt.savefig('plot2.pdf')
 #    cur.execute("select Age_Adjusted_Death_Rate from q3 where Race_Ethnicity='Black Non-Hispanic' and sex='M' and Leading_Cause=%s" %trail)
 #    rowsM=cur.fetchall()
 #    cur.execute("select Age_Adjusted_Death_Rate from q3 where Race_Ethnicity='Black Non-Hispanic' and sex='F' and Leading_Cause='Diseases of Heart (I00-I09, I11, I13, I20-I51)'")
 #    rowsF=cur.fetchall()
 #    rowBlack_Non_Hispanic_hearttmp=[x + y for x, y in zip(rowsM,rowsM)]
 #    rowBlack_Non_Hispanic_heart=[]
 #    for row in rowBlack_Non_Hispanic_hearttmp:
 #        rowBlack_Non_Hispanic_heart.append(row[0])




 #    plt.plot(year,rowHispanic_cancer)
 #    plt.legend(['City Sum Age Adjusted Death Rate Scale(1/10)','Black Non Hispanic Diseases of Heart', 'White Non Hispanic Disease of Heart','Hispanic Disease of Heart','Black Non Hispanic Cancer','White Non Hispanic Cancer','Hispanic Cancer'], loc=7,prop={'size': 6})
 #    plt.savefig('plot1.pdf')
if con:
    con.close()
