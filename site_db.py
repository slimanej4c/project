import mysql.connector
ls_date=[]
ls_site=[]
ls_site_sbd=[]

ls_site_d=[]

class sitedb:

    def __init__(self):
        self.mydb=mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='slimane'
        )
        cur=self.mydb.cursor()
        cur.execute('create database if not exists qhse')

    def open_data(self):
        self.mydb=mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='slimane',
            database='qhse')
    def cdate(self):
        self.open_data()
        cur=self.mydb.cursor()
        cur.execute('create table if not exists date(id_date int(11) primary key)')
        self.mydb.close
        print("ok")
    def idate(self,date_now):
        self.open_data()
        cur = self.mydb.cursor()
        cur.execute('insert into date (id_date)values(%s)',(date_now,))
        self.mydb.commit()
        self.mydb.close()
        print('iddd')
    def lsdate(self):

        self.open_data()
        cur=self.mydb.cursor()
        cur.execute('select * from date ')
        sdate=cur.fetchall()
        for x in list(sdate):
            ls_date.append(x[0])
        self.mydb.close()
    ###################################################################################################################
    def site(self):
        self.open_data()
        cur=self.mydb.cursor()
        cur.execute('create table if not exists site (id int(11) primary key auto_increment,id_date int(11),site_name varchar (25) ,constraint fkid_site foreign key(id_date) references date(id_date) on delete cascade on update cascade )')
        self.mydb.close()

    def isite(self,id_date,site_name):
        self.open_data()
        cur = self.mydb.cursor()
        cur.execute('insert into site (id_date,site_name)values(%s,%s)',(id_date,site_name,))
        self.mydb.commit()
        self.mydb.close()
    def lssite(self):
        self.open_data()
        cur = self.mydb.cursor()
        cur.execute('select site_name  from site ')
        sdate = cur.fetchall()
        for x in list(sdate):
            ls_site.append(x[0])
        self.mydb.close()
    def dsite(self,id_date):
        self.open_data()
        cur = self.mydb.cursor()
        cur.execute('delete from site where id_date=%s ',(id_date,))
        self.mydb.commit()
        self.mydb.close()
    def lssite_sbd(self):
        ls_site_d.clear()
        go.lssite_d()


        self.open_data()
        cur = self.mydb.cursor()
        cur.execute('select site_name  from site where id_date=%s',(ls_site_d[-1],))
        sdate = cur.fetchall()
        for x in list(sdate):
            ls_site_sbd.append(x[0])
        self.mydb.close()


    def lssite_d(self):
        self.open_data()
        cur = self.mydb.cursor()
        cur.execute('select id_date  from site')
        sdate = cur.fetchall()
        for x in list(sdate):
            ls_site_d.append(x[0])
        self.mydb.close()

go=sitedb()
go.cdate()
go.site()


