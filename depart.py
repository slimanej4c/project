import tkinter
from tkinter import *
from datetime import datetime
import time
from tkinter import ttk
import time


#import pro_db

import site_db
from site_db import *
date_now = time.strftime('%d%m%Y')
go=site_db.sitedb()
go.lsdate()
if site_db.ls_date is  None:
    go.idate(date_now)
else:
    if int(date_now) in site_db.ls_date :
        print("ok it is")
        print(ls_date)
    else:
        go.idate(date_now)


"""
else:
    data.insert_date_id(date_now)
    data.list_site.clear()
    list_site = data.list_site
    data.list_id_date()

    data.insert_vsite(date_now, list_site)"""



class part_1:

    def __init__(self,root):
        self.root=root

    def widget_part_1(self):
        import part_1
        go_part_1=part_1.part_1(self.root)
        go_part_1.global_()


if __name__ == "__main__":
    root = Tk()
    depart=part_1(root)
    depart.widget_part_1()
    root.mainloop()