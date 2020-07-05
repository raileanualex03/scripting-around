from cx_Freeze import setup, Executable 
import sys

base = None

if (sys.platform == "win32"):
     	  base = "Win32GUI"
setup(name = "DownloadsCleaner" , 
      version = "0.1" , 
      description = "" ,
      executables = [Executable("script2.pyw", base=base)]) 