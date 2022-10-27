#!/usr/bin/python3
# -*- coding: utf-8 -*-

import easygui as eg

directorio = eg.diropenbox(msg="Abrir directorio:",
                           title="Control: diropenbox",
                           default='/home/antonio')
  
eg.msgbox(directorio, "diropenbox", ok_button="Continuar")
  
extension = ["*.py","*.pyc"]

archivo = eg.fileopenbox(msg="Abrir archivo",
                         title="Control: fileopenbox",
                         default='',
                         filetypes=extension)
                           
eg.msgbox(archivo, "fileopenbox", ok_button="Continuar")
  
archivo = eg.filesavebox(msg="Guardar archivo",
                         title="Control: filesavebox",
                         default='',
                         filetypes=extension)
                           
eg.msgbox(archivo, "filesavebox", ok_button="Continuar")