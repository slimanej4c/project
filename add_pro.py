import tkinter
from tkinter import *
from datetime import datetime
import time
#import data
import part_1
time1=""
import mysql.connector
import site_db
from site_db import *
go=site_db.sitedb()

class info_add_site:
    def __init__(self,root):
        self.root = root
        self.wroot = self.root.winfo_screenwidth() - 6
        self.hroot = self.root.winfo_screenheight() - 74

        self.root.geometry("%dx%d" % (self.wroot, self.hroot))

        vwidth3 = 100 / 1530 * 510 * self.wroot / 100
        wframe_width3_1 = round(vwidth3, 0)
        wframe_width3_2 = str(wframe_width3_1)[:-2]
        self.wframe3 = int(wframe_width3_2)

        vwidth5 = 100 / 1530 * 42 * self.wroot / 100
        wframe_width5_1 = round(vwidth5, 0)
        wframe_width5_2 = str(wframe_width5_1)[:-2]
        self.wframe5 = int(wframe_width5_2)

        vheight1 = 100 / 790 * 30 * self.hroot / 100
        hframe1_1 = round(vheight1, 0)
        hframe1_2 = str(hframe1_1)[:-2]
        self.hframe1 = int(hframe1_2)

        vheight2 = 100 / 790 * 720 * self.hroot / 100
        hframe2_1 = round(vheight2, 0)
        hframe2_2 = str(hframe2_1)[:-2]
        self.hframe2 = int(hframe2_2)

        vheight2_button = 100 / 790 * 10 * self.hroot / 100
        hframe2_1_button = round(vheight2_button, 0)
        hframe2_2_button = str(hframe2_1_button)[:-2]
        self.hframe2button = int(hframe2_2_button)

        vheight22 = 100 / 790 * 100 * self.hroot / 100
        hframe22_1 = round(vheight22, 0)
        hframe22_2 = str(hframe22_1)[:-2]
        self.hframe22 = int(hframe22_2)

        vheight3 = 100 / 790 * 40 * self.hroot / 100
        hframe3_1 = round(vheight3, 0)
        hframe3_2 = str(hframe3_1)[:-2]
        self.hframe3 = int(hframe3_2)

        vheight4 = 100 / 790 * 620 * self.hroot / 100
        hframe_canvas1 = round(vheight4, 0)
        hframe_canvas2 = str(hframe_canvas1)[:-2]
        self.hframe_canvas = int(hframe_canvas2)

        big_frame = Frame(self.root, width=self.wroot, height=self.hroot, bg="red")
        big_frame.grid(row=0, column=0)
        big_frame.grid_propagate(0)

        self.frame1 = Frame(big_frame, width=self.wroot, height=self.hframe1, bg="#055E33")
        self.frame1.grid(row=0, column=0, columnspan=2)
        self.frame1.grid_propagate(0)

        self.frame2 = Frame(big_frame, width=self.wroot, height=self.hframe2, bg="#F1F1F2")
        self.frame2.grid(row=1, column=0)
        self.frame2.grid_propagate(0)



        self.frame3 = Frame(big_frame, width=self.wroot, height=self.hframe3, bg="#27A9E1")
        self.frame3.grid(row=2, column=0, sticky=S)
        self.frame3.grid_propagate(0)

        self.frame11 = Frame(self.frame1, width=self.wframe3, height=self.hframe1, bg="#055E33")
        self.frame11.grid(row=0, column=0)
        self.frame11.grid_propagate(0)

        self.frame12 = Frame(self.frame1, width=self.wframe3, height=self.hframe1, bg="#055E33")
        self.frame12.grid(row=0, column=1)
        self.frame12.grid_propagate(0)

        self.frame13 = Frame(self.frame1, width=self.wframe3, height=self.hframe1, bg="#055E33")
        self.frame13.grid(row=0, column=2)
        self.frame13.grid_propagate(0)

    def ask_info(self):

        bretour = Button(self.frame1, text="retour",font=("arial",8))
        bretour.grid(row=0, column=2)
        """
        def retour():
            import part_1
            go_part_2 = build_site.part_2(self.root)
            go_part_2.global_()
            bretour.destroy()
        bretour.config(command=retour)"""

        vday=StringVar()
        vmonth = StringVar()
        vyear = StringVar()
        vname=StringVar()

        lvid=Label(self.frame2,width=10)
        lvid.grid(row=0,column=0)
        lday=Label(self.frame2,text="day",)
        lday.grid(row=0,column=1,pady=50)
        eday=Entry(self.frame2,textvariable=vday,width=8)
        eday.grid(row=0,column=2,pady=50)
        lmonth = Label(self.frame2, text="month")
        lmonth.grid(row=0, column=3, pady=50)
        emonth = Entry(self.frame2, textvariable=vmonth,width=8)
        emonth.grid(row=0, column=4, pady=50)
        lyear = Label(self.frame2, text="year:")
        lyear.grid(row=0, column=5, pady=50)
        eyear = Entry(self.frame2, textvariable=vyear,width=8)
        eyear.grid(row=0, column=6, pady=50)
        lvid = Label(self.frame2,width=13)
        lvid.grid(row=1, column=0)
        lname = Label(self.frame2, text="le titre de site  :")
        lname.grid(row=2, column=1)
        ename = Entry(self.frame2, textvariable=vname)
        ename.grid(row=2, column=2)
        def ajouter_site():
            day=eday.get()
            month=emonth.get()
            year=eyear.get()
            id_date=int(day+month+year)
            site_name = vname.get()
            ls_date.clear()
            go.lsdate()
            ls_site.clear()
            go.lssite()
            print("id_date herrr "+ str(id_date))
            print("herer liste date " +str(ls_date))
            print("herer liste dsite " + str(ls_site))
            if str(id_date) in str(ls_date) and ls_site ==[]:
                go.isite(id_date, site_name)
                goto_part1=part_1.part_1(self.root)
                goto_part1.global_()
                bretour.destroy()
            else:
                ls_site_sbd.clear()
                go.lssite_sbd()
                ls_site_d.clear()
                go.lssite_d()


                ls_site_sbd.append(site_name)

                for x in ls_site_sbd:
                    go.isite(id_date,x)




        ldate = Label(self.frame13, font=("arial", 15), bg="#055E33", fg="white")
        ldate.grid(row=0, column=0)
        ltime = Label(self.frame13, font=("arial", 15), bg="#055E33", fg="white")
        ltime.grid(row=0, column=1)
        ltime.grid_rowconfigure(100, weight=1)
        bname=Button(self.frame2,text="valider",command=ajouter_site,width=20)
        bname.grid(row=3,column=1,columnspan=3,pady=90)

        def tick():
            global time1
            date_now = time.strftime('%Y-%m-%d')
            time_now = time.strftime('%H:%M:%S')
            if time_now != time1:
                time1 = time_now

                ltime.config(text=time_now)
                ldate.config(text=date_now)
            ltime.after(200, tick)
        tick()
ls_site_d.clear()
go.lssite_d()

print(ls_site_d[-1])
