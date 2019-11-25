import tkinter
from tkinter import *
from datetime import datetime
import time
from tkinter import ttk
import random
import site_db
from site_db import *
go=site_db.sitedb()

"""


import présentation
import processus
import processus_db"""

time1 = ""


class part_1:
    def __init__(self, root):

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

        self.frame22 = Frame(self.frame2, width=self.wroot, height=self.hframe22, bg="#38B449")
        self.frame22.grid(row=0, column=0)
        self.frame22.grid_propagate(0)

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

    def global_(self):

        #import askaddsite

        ldate = Label(self.frame13, font=("arial", 15), bg="#055E33", fg="white")
        ldate.grid(row=0, column=0)
        ltime = Label(self.frame13, font=("arial", 15), bg="#055E33", fg="white")
        ltime.grid(row=0, column=1)
        ltime.grid_rowconfigure(100, weight=1)

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


        def import_ask():
            import add_site
            add_site.info_add_site(self.root).ask_info()
            #cal_ask = askaddsite.info_add_site(self.root)
            #cal_ask.ask_info()

        ls_date.clear()
        go.lsdate()

        def add_site(self):
            frame_canvas = Frame(self.frame2, width=self.wroot - 10, height=self.hframe_canvas, bg="#F1F1F2")
            frame_canvas.grid(row=1, column=0)
            vsb = Scrollbar(frame_canvas, orient=VERTICAL)
            vsb.grid(row=0, column=1, rowspan=2, sticky=N + S)
            hsb = Scrollbar(frame_canvas, orient=HORIZONTAL)
            hsb.grid(row=1, column=0, columnspan=2, sticky=W + E)
            canvas_site = Canvas(frame_canvas, yscrollcommand=vsb.set, xscrollcommand=hsb.set, bg="#F1F1F2",
                                 width=self.wroot - 20, height=self.hframe_canvas)
            canvas_site.grid(row=0, column=0, sticky="news")
            canvas_site.grid_propagate(0)

            vsb.config(command=canvas_site.yview)
            hsb.config(command=canvas_site.xview)

            frame_canvas.grid_rowconfigure(0, weight=1)
            frame_canvas.grid_columnconfigure(0, weight=1)

            frame_canvas1 = Frame(canvas_site)
            ls_site_d.clear()
            go.lssite_d()
            ls_site_sbd.clear()


            if ls_site_d!=[] and ls_site_sbd!=0:
                    go.lssite_sbd()
                    n = 0
                    for i in range(len(ls_site_sbd)) :
                        k = i / 5
                        ii = str(k)
                        zz = int(re.search('^[0-9]', ii).group())

                        o = '0123456789abcdef'
                        oo = list(o)
                        m = random.randint(0, 15)
                        j = random.randint(10, 15)
                        d = random.randint(0, 15)
                        mm = oo[m]
                        jj = oo[j]
                        dd = oo[d]

                        mbg = "{}{}{}{}{}".format("#51", str(dd), str(mm), "A", str(jj))

                        if i <= 4:
                            vtext = ls_site_sbd[i]
                            bsite = Button(frame_canvas1, width=self.wframe5, height=self.hframe2button, text=vtext, bg=mbg,
                                           padx=0, pady=0)
                            bsite.grid(row=1, column=i)

                        if i % 5 == 0 and i > 4:
                            n = n + 1
                            f = 5 * zz
                            vtext = ls_site_sbd[i]
                            bsite = Button(frame_canvas1, width=self.wframe5, height=self.hframe2button, text=vtext, bg=mbg)
                            bsite.grid(row=1 + n, column=i - f)
                        if i % 5 != 0 and i > 4:
                            f = 5 * zz
                            vtext = ls_site_sbd[i]
                            bsite = Button(frame_canvas1, width=self.wframe5, height=self.hframe2button, text=vtext, bg=mbg)
                            bsite.grid(row=1 + n, column=i - f)

                        def goaddpro(bsite1):
                            import part_2
                            site_name = bsite1["text"]
                            gopart2=part_2.part_2(self.root,site_name,bsite1)
                            gopart2.global_()


                            """processus_db.create_pro(site_name)
                            go_part_3 = processus.part_3(self.root, site_name, bsite1)
                            go_part_3.processus_hse()"""
        
                        bsite["command"] = lambda bsite1=bsite: bsite.configure(command=goaddpro(bsite1))

                    canvas_site.create_window(0, 0, window=frame_canvas1)
                    frame_canvas1.update_idletasks()
                    canvas_site.config(scrollregion=canvas_site.bbox("all"))

            """cbsup.update()
            cbsup["values"] = list_site

        def delete_site():
            frame2 = Frame(self.root, width=self.wroot, height=self.hroot - 190, bg="#2C2206")
            frame2.grid(row=1, column=0)
            frame2.grid_propagate(0)
            sup = (vsup.get())
            data.delete_from_site(sup)
            part_2.global_(self)"""

        baddsite = Button(self.frame22, text="ajouter un site", width=25, height=6, command=import_ask)
        baddsite.grid(row=0, column=0)
        """
        lsup = Label(self.frame22, text="supprimer")
        lsup.grid(row=0, column=1)
        vsup = StringVar()
        cbsup = ttk.Combobox(self.frame22, textvariable=vsup)
        cbsup.grid(row=0, column=2)
        cbsup["values"] = list_site
        cbsup.current()

        bsup = Button(self.frame22, text="supprimer", command=delete_site)
        bsup.grid(row=0, column=3)"""

        add_site(self)