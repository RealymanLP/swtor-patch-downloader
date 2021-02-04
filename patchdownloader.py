from tkinter import filedialog
from tkinter import *
import tkinter as tkr
import socket
import wget
import json
import time
import os.path
import os
import zipfile
import urllib
import xml.dom.minidom
import sys

global zeit
global zeitx
zeitx = ""
global sekunden
sekunden = 0
yes = False

def bar_progress(current, total, width=80):
    global zeit
    global zeitx
    global sekunden
    zeit = int(time.time())
    if not zeit == zeitx:
        sekunden += 1
    currentx = int(current)
    totalx = int(total)
    leiste =     "  [                                                   ]"
    if int(currentx / totalx * 100) == 1 or int(currentx / totalx * 100) == 2:
        leiste = "  [.                                                  ]"
    if int(currentx / totalx * 100) == 3 or int(currentx / totalx * 100) == 4:
        leiste = "  [..                                                 ]"
    if int(currentx / totalx * 100) == 5 or int(currentx / totalx * 100) == 6:
        leiste = "  [...                                                ]"
    if int(currentx / totalx * 100) == 7 or int(currentx / totalx * 100) == 8:
        leiste = "  [....                                               ]"
    if int(currentx / totalx * 100) == 9:
        leiste = "  [.....                                              ]"
    if int(currentx / totalx * 100) == 10:
        leiste = " [.....                                              ]"
    if int(currentx / totalx * 100) == 11 or int(currentx / totalx * 100) == 12:
        leiste = " [......                                             ]"
    if int(currentx / totalx * 100) == 13 or int(currentx / totalx * 100) == 14:
        leiste = " [.......                                            ]"
    if int(currentx / totalx * 100) == 15 or int(currentx / totalx * 100) == 16:
         leiste = " [........                                          ]"
    if int(currentx / totalx * 100) == 17 or int(currentx / totalx * 100) == 18:
        leiste = " [.........                                          ]"
    if int(currentx / totalx * 100) == 19 or int(currentx / totalx * 100) == 20:
        leiste = " [..........                                         ]"
    if int(currentx / totalx * 100) == 21 or int(currentx / totalx * 100) == 22:
         leiste = " [...........                                       ]"
    if int(currentx / totalx * 100) == 23 or int(currentx / totalx * 100) == 24:
        leiste = " [............                                       ]"
    if int(currentx / totalx * 100) == 25 or int(currentx / totalx * 100) == 26:
        leiste = " [.............                                      ]"
    if int(currentx / totalx * 100) == 27 or int(currentx / totalx * 100) == 28:
        leiste = " [..............                                     ]"
    if int(currentx / totalx * 100) == 29 or int(currentx / totalx * 100) == 30:
        leiste = " [...............                                    ]"
    if int(currentx / totalx * 100) == 31 or int(currentx / totalx * 100) == 32:
        leiste = " [................                                   ]"
    if int(currentx / totalx * 100) == 33 or int(currentx / totalx * 100) == 34:
        leiste = " [.................                                  ]"
    if int(currentx / totalx * 100) == 35 or int(currentx / totalx * 100) == 36:
        leiste = " [..................                                 ]"
    if int(currentx / totalx * 100) == 37 or int(currentx / totalx * 100) == 38:
        leiste = " [...................                                ]"
    if int(currentx / totalx * 100) == 39 or int(currentx / totalx * 100) == 40:
        leiste = " [....................                               ]"
    if int(currentx / totalx * 100) == 41 or int(currentx / totalx * 100) == 42:
        leiste = " [.....................                              ]"
    if int(currentx / totalx * 100) == 43 or int(currentx / totalx * 100) == 44:
        leiste = " [......................                             ]"
    if int(currentx / totalx * 100) == 45 or int(currentx / totalx * 100) == 46:
        leiste = " [.......................                            ]"
    if int(currentx / totalx * 100) == 47 or int(currentx / totalx * 100) == 48:
        leiste = " [........................                           ]"
    if int(currentx / totalx * 100) == 49 or int(currentx / totalx * 100) == 50:
        leiste = " [.........................                          ]"
    if int(currentx / totalx * 100) == 51 or int(currentx / totalx * 100) == 52:
        leiste = " [..........................                         ]"
    if int(currentx / totalx * 100) == 53 or int(currentx / totalx * 100) == 54:
        leiste = " [...........................                        ]"
    if int(currentx / totalx * 100) == 55 or int(currentx / totalx * 100) == 56:
        leiste = " [............................                       ]"
    if int(currentx / totalx * 100) == 57 or int(currentx / totalx * 100) == 58:
        leiste = " [.............................                      ]"
    if int(currentx / totalx * 100) == 59 or int(currentx / totalx * 100) == 60:
        leiste = " [..............................                     ]"
    if int(currentx / totalx * 100) == 61 or int(currentx / totalx * 100) == 62:
        leiste = " [...............................                    ]"
    if int(currentx / totalx * 100) == 63 or int(currentx / totalx * 100) == 64:
        leiste = " [................................                   ]"
    if int(currentx / totalx * 100) == 65 or int(currentx / totalx * 100) == 66:
        leiste = " [.................................                  ]"
    if int(currentx / totalx * 100) == 67 or int(currentx / totalx * 100) == 68:
        leiste = " [..................................                 ]"
    if int(currentx / totalx * 100) == 69 or int(currentx / totalx * 100) == 70:
        leiste = " [...................................                ]"
    if int(currentx / totalx * 100) == 71 or int(currentx / totalx * 100) == 72:
        leiste = " [....................................               ]"
    if int(currentx / totalx * 100) == 73 or int(currentx / totalx * 100) == 74:
        leiste = " [.....................................              ]"
    if int(currentx / totalx * 100) == 75 or int(currentx / totalx * 100) == 76:
        leiste = " [......................................             ]"
    if int(currentx / totalx * 100) == 77 or int(currentx / totalx * 100) == 78:
        leiste = " [.......................................            ]"
    if int(currentx / totalx * 100) == 79 or int(currentx / totalx * 100) == 80:
        leiste = " [........................................           ]"
    if int(currentx / totalx * 100) == 81 or int(currentx / totalx * 100) == 82:
        leiste = " [.........................................          ]"
    if int(currentx / totalx * 100) == 83 or int(currentx / totalx * 100) == 84:
        leiste = " [..........................................         ]"
    if int(currentx / totalx * 100) == 85 or int(currentx / totalx * 100) == 86:
        leiste = " [...........................................        ]"
    if int(currentx / totalx * 100) == 87 or int(currentx / totalx * 100) == 88:
        leiste = " [............................................       ]"
    if int(currentx / totalx * 100) == 89 or int(currentx / totalx * 100) == 90:
        leiste = " [.............................................      ]"
    if int(currentx / totalx * 100) == 91 or int(currentx / totalx * 100) == 92:
        leiste = " [..............................................     ]"
    if int(currentx / totalx * 100) == 93 or int(currentx / totalx * 100) == 94:
        leiste = " [...............................................    ]"
    if int(currentx / totalx * 100) == 95 or int(currentx / totalx * 100) == 96:
        leiste = " [................................................   ]"
    if int(currentx / totalx * 100) == 97 or int(currentx / totalx * 100) == 98:
        leiste = " [.................................................  ]"
    if int(currentx / totalx * 100) == 99:
        leiste = " [.................................................. ]"
    if int(currentx / totalx * 100) == 100:
        leiste = "[...................................................]"
    try:
        speed = current / sekunden / 1000000
        speed = str(format(speed, '.2f'))
    except:
        speed = 0
    progress_message = f"{int(currentx / totalx * 100)}% {leiste} {current} / {total} [{speed}mb/s]"
    sys.stdout.write("\r" + progress_message)
    sys.stdout.flush()
    zeitx = zeit

def download_movies(saveloc, lwert, vnummerx, vwert, vnummer):
    global zeitx
    global sekunden
    if not lwert == "client" and not lwert == "main":
        print(f"Download of {vwert} {lwert} version {vnummerx} started!\nPress CTRL+C to stop.")
        if not os.path.exists(f"{saveloc}/movies_{lwert}_{vnummerx}.zip") == True:
            url = f"http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_{vnummerx}/movies_{lwert}_{vnummerx}.zip"
            try:
                zeitx = int(time.time())
                sekunden = 0
                wget.download(url, saveloc, bar=bar_progress)
                print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_{vnummerx}/movies_{lwert}_{vnummerx}.zip\n")
            except KeyboardInterrupt:
                print("\nYou stopped the download!")
                return
            except Exception as ex:
                exception = type(ex).__name__
                argumente = str(ex.args)
                if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                    print("\nNo Connection. Please try again!")
                    try:
                        log1_label.config(text="No connection.\nPlease try again!")
                    except:
                        pass
                    return
                else:
                    try:
                        log1_label.config(text="Version not found!")
                    except:
                        pass
                    print("\nVersion not found!\n")
                    return
        c = 0
        while True:
            c = int(c)+1
            if c < 10:
                c = "0" + str(c)         
            if not os.path.exists(f"{saveloc}/movies_{lwert}_{vnummerx}.z{c}") == True:
                url2 = f"http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_{vnummerx}/movies_{lwert}_{vnummerx}.z{c}"
                while True:
                    try:
                        zeitx = int(time.time())
                        sekunden = 0
                        wget.download(url2, saveloc, bar=bar_progress)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_{vnummerx}/movies_{lwert}_{vnummerx}.z{c}\n")
                        break
                    except KeyboardInterrupt:
                        print("\nYou stopped the download!")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            print("\nConnection lost. Trying again...")
                            time.sleep(5)
                        else:
                            try:
                                log1_label.config(text="Download finished!")
                            except:
                                pass
                            print("\nDownload finished!\n")
                            return
    else:
        print("Please select a language!")
        try:
            log1_label.config(text="Please select a language!")
        except:
            pass
        return  
                        
def download_movies0(saveloc, lwert, vnummerx, vwert, vnummer):
    global zeitx
    global sekunden
    if not lwert == "client" and not lwert == "main":
        print(f"Download of {vwert} {lwert} version 0to{vnummer} started!\nPress CTRL+C to stop.")
        if not os.path.exists(f"{saveloc}/movies_{lwert}_0to{vnummer}.zip") == True:
            url = f"http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_0to{vnummer}/movies_{lwert}_0to{vnummer}.zip"
            try:
                zeitx = int(time.time())
                sekunden = 0
                wget.download(url, saveloc, bar=bar_progress)
                print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_0to{vnummer}/movies_{lwert}_0to{vnummer}.zip\n")
            except KeyboardInterrupt:
                print("\nYou stopped the download!")
                return
            except Exception as ex:
                exception = type(ex).__name__
                argumente = str(ex.args)
                if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                    print("\nNo Connection. Please try again!")
                    try:
                        log1_label.config(text="No connection.\nPlease try again!")
                    except:
                        pass
                    return
                else:
                    try:
                        log1_label.config(text="Version not found!")
                    except:
                        pass
                    print("\nVersion not found!\n")
                    return
        c = 0
        while True:
            c = int(c)+1
            if c < 10:
                c = "0" + str(c)         
            if not os.path.exists(f"{saveloc}/movies_{lwert}_0to{vnummer}.z{c}") == True:
                url2 = f"http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_0to{vnummer}/movies_{lwert}_0to{vnummer}.z{c}"
                while True:
                    try:
                        zeitx = int(time.time())
                        sekunden = 0
                        wget.download(url2, saveloc, bar=bar_progress)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_0to{vnummer}/movies_{lwert}_0to{vnummer}.z{c}\n")
                        break
                    except KeyboardInterrupt:
                        print("\nYou stopped the download!")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            print("\nConnection lost. Trying again...")
                            time.sleep(5)
                        else:
                            try:
                                log1_label.config(text="Download finished!")
                            except:
                                pass
                            print("\nDownload finished!\n")
                            return
    else:
        try:
            log1_label.config(text="Please select a language!")
        except:
            pass
        print("Please select a language!")
        return    

def download_files(saveloc, lwert, vnummerx, vwert, vnummer):
    global zeitx
    global sekunden
    if not lwert == "client":
        print(f"Download of {vwert} {lwert} version {vnummerx} started! ({vnummer})\nPress CTRL+C to stop.")
        if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_{vnummerx}.zip") == True:
            url = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.zip"
            try:
                zeitx = int(time.time())
                sekunden = 0
                wget.download(url, saveloc, bar=bar_progress)
                print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.zip\n")
            except KeyboardInterrupt:
                print("\nYou stopped the download!")
                return
            except Exception as ex:
                exception = type(ex).__name__
                argumente = str(ex.args)
                if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                    print("\nNo Connection. Please try again!")
                    try:
                        log1_label.config(text="No connection.\nPlease try again!")
                    except:
                        pass
                    return
                else:
                    try:
                        log1_label.config(text="Version not found!")
                    except:
                        pass
                    print("\nVersion not found!\n")
                    return
        c = 0
        while True:
            c = int(c)+1
            if c < 10:
                c = "0" + str(c)
            if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_{vnummerx}.z{c}") == True:
                url2 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z{c}"
                while True:
                    try:
                        zeitx = int(time.time())
                        sekunden = 0
                        wget.download(url2, saveloc, bar=bar_progress)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z{c}\n")
                        break
                    except KeyboardInterrupt:
                        print("\nYou stopped the download!")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            print("\nConnection lost. Trying again...")
                            time.sleep(5)
                        else:
                            try:
                                log1_label.config(text="Download finished!")
                            except:
                                pass
                            print("\nDownload finished!\n")
                            return
    if lwert == "client":
        print(f"Download of {vwert} {lwert} version {vnummerx} started! ({vnummer})\nPress CTRL+C to stop.")
        if not os.path.exists(f"{saveloc}/retailclient_swtor_{vnummerx}.zip") == True:
            url = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.zip"
            try:
                zeitx = int(time.time())
                sekunden = 0
                wget.download(url, saveloc, bar=bar_progress)
                print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.zip\n")
            except KeyboardInterrupt:
                print("\nYou stopped the download!")
                return
            except Exception as ex:
                exception = type(ex).__name__
                argumente = str(ex.args)
                if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                    print("\nNo Connection. Please try again!")
                    try:
                        log1_label.config(text="No connection.\nPlease try again!")
                    except:
                        pass
                    return
                else:
                    try:
                        log1_label.config(text="Version not found!")
                    except:
                        pass
                    print("\nVersion not found!\n")
                    return
        c = 0
        while True:
            c = int(c)+1
            if c < 10:
                c = "0" + str(c)
            if not os.path.exists(f"{saveloc}/retailclient_swtor_{vnummerx}.z{c}") == True:
                url2 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z{c}"
                while True:
                    try:
                        zeitx = int(time.time())
                        sekunden = 0
                        wget.download(url2, saveloc, bar=bar_progress)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z{c}\n")
                        break
                    except KeyboardInterrupt:
                        print("\nYou stopped the download!")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            print("\nConnection lost. Trying again...")
                            time.sleep(5)
                        else:
                            try:
                                log1_label.config(text="Download finished!")
                            except:
                                pass
                            print("\nDownload finished!\n")
                            return

def download_exp_client(saveloc, lwert, vnummerx, vwert, vnummer, clientid):
    global zeitx
    global sekunden
    if True:
        print(f"Download of {vwert} version {vnummerx} started! ({vnummer})\nPress CTRL+C to stop.")
        if not os.path.exists(f"{saveloc}/retailclient_{clientid}_{vnummerx}.zip") == True:
            url = f"http://cdn-patch.swtor.com/patch/{clientid}/retailclient_{clientid}/retailclient_{clientid}_{vnummerx}/retailclient_{clientid}_{vnummerx}.zip"
            try:
                zeitx = int(time.time())
                sekunden = 0
                wget.download(url, saveloc, bar=bar_progress)
                print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/{clientid}/retailclient_{clientid}/retailclient_{clientid}_{vnummerx}/retailclient_{clientid}_{vnummerx}.zip\n")
            except KeyboardInterrupt:
                print("\nYou stopped the download!")
                return
            except Exception as ex:
                exception = type(ex).__name__
                argumente = str(ex.args)
                if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                    print("\nNo Connection. Please try again!")
                    try:
                        log1_label.config(text="No connection.\nPlease try again!")
                    except:
                        pass
                    return
                else:
                    try:
                        log1_label.config(text="Version not found!")
                    except:
                        pass
                    print("\nVersion not found!\n")
                    return
        c = 0
        while True:
            c = int(c)+1
            if c < 10:
                c = "0" + str(c)
            if not os.path.exists(f"{saveloc}/retailclient_{clientid}_{vnummerx}.z{c}") == True:
                url2 = f"http://cdn-patch.swtor.com/patch/{clientid}/retailclient_{clientid}/retailclient_{clientid}_{vnummerx}/retailclient_{clientid}_{vnummerx}.z{c}"
                while True:
                    try:
                        zeitx = int(time.time())
                        sekunden = 0
                        wget.download(url2, saveloc, bar=bar_progress)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/{clientid}/retailclient_{clientid}/retailclient_{clientid}_{vnummerx}/retailclient_{clientid}_{vnummerx}.z{c}\n")
                        break
                    except KeyboardInterrupt:
                        print("\nYou stopped the download!")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            print("\nConnection lost. Trying again...")
                            time.sleep(5)
                        else:
                            try:
                                log1_label.config(text="Download finished!")
                            except:
                                pass
                            print("\nDownload finished!\n")
                            return

def download_exp_client0(saveloc, lwert, vnummerx, vwert, vnummer, clientid):
    global zeitx
    global sekunden
    if True:
        print(f"Download of {vwert} {lwert} version 0to{vnummer} started! ({vnummer})\nPress CTRL+C to stop.")
        if not os.path.exists(f"{saveloc}/retailclient_{clientid}_0to{vnummer}.zip") == True:
            url = f"http://cdn-patch.swtor.com/patch/{clientid}/retailclient_{clientid}/retailclient_{clientid}_0to{vnummer}/retailclient_{clientid}_0to{vnummer}.zip"
            try:
                zeitx = int(time.time())
                sekunden = 0
                wget.download(url, saveloc, bar=bar_progress)
                print(f"\nDownloaded: http://cdn-patch.swtor.com/{clientid}/swtor/retailclient_{clientid}/retailclient_{clientid}_0to{vnummer}/retailclient_{clientid}_0to{vnummer}.zip\n")
            except KeyboardInterrupt:
                print("\nYou stopped the download!")
                return
            except Exception as ex:
                exception = type(ex).__name__
                argumente = str(ex.args)
                if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                    print("\nNo Connection. Please try again!")
                    try:
                        log1_label.config(text="No connection.\nPlease try again!")
                    except:
                        pass
                    return
                else:
                    try:
                        log1_label.config(text="Version not found!")
                    except:
                        pass
                    print("\nVersion not found!\n")
                    return
        c = 0
        while True:
            c = int(c)+1
            if c < 10:
                c = "0" + str(c)
            if not os.path.exists(f"{saveloc}/retailclient_{clientid}_0to{vnummer}.z{c}") == True:
                url2 = f"http://cdn-patch.swtor.com/patch/{clientid}/retailclient_{clientid}/retailclient_{clientid}_0to{vnummer}/retailclient_{clientid}_0to{vnummer}.z{c}"
                while True:
                    try:
                        zeitx = int(time.time())
                        sekunden = 0
                        wget.download(url2, saveloc, bar=bar_progress)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/{clientid}/retailclient_{clientid}/retailclient_{clientid}_0to{vnummer}/retailclient_{clientid}_0to{vnummer}.z{c}\n")
                        break
                    except KeyboardInterrupt:
                        print("\nYou stopped the download!")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            print("\nConnection lost. Trying again...")
                            time.sleep(5)
                        else:
                            try:
                                log1_label.config(text="Download finished!")
                            except:
                                pass
                            print("\nDownload finished!\n")
                            return

def download_files0(saveloc, lwert, vnummerx, vwert, vnummer):
    global zeitx
    global sekunden
    if not lwert == "client":
        print(f"Download of {vwert} {lwert} version 0to{vnummer} started! ({vnummerx})\nPress CTRL+C to stop.")
        if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_0to{vnummer}.zip") == True:
            url = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer}/assets_swtor_{lwert}_0to{vnummer}.zip"
            try:
                zeitx = int(time.time())
                sekunden = 0
                wget.download(url, saveloc, bar=bar_progress)
                print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer}/assets_swtor_{lwert}_0to{vnummer}.zip\n")
            except KeyboardInterrupt:
                print("\nYou stopped the download!")
                return
            except Exception as ex:
                exception = type(ex).__name__
                argumente = str(ex.args)
                if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                    print("\nNo Connection. Please try again!")
                    try:
                        log1_label.config(text="No connection.\nPlease try again!")
                    except:
                        pass
                    return
                else:
                    try:
                        log1_label.config(text="Version not found!")
                    except:
                        pass
                    print("\nVersion not found!\n")
                    return
        c = 0
        while True:
            c = int(c)+1
            if c < 10:
                c = "0" + str(c)
            if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_0to{vnummer}.z{c}") == True:
                url2 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer}/assets_swtor_{lwert}_0to{vnummer}.z{c}"
                while True:
                    try:
                        zeitx = int(time.time())
                        sekunden = 0
                        wget.download(url2, saveloc, bar=bar_progress)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer}/assets_swtor_{lwert}_0to{vnummer}.z{c}\n")
                        break
                    except KeyboardInterrupt:
                        print("\nYou stopped the download!")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            print("\nConnection lost. Trying again...")
                            time.sleep(5)
                        else:
                            try:
                                log1_label.config(text="Download finished!")
                            except:
                                pass
                            print("\nDownload finished!\n")
                            return
    if lwert == "client":
        print(f"Download of {vwert} {lwert} version 0to{vnummer} started! ({vnummerx})\nPress CTRL+C to stop.")
        if not os.path.exists(f"{saveloc}/retailclient_swtor_0to{vnummer}.zip") == True:
            url = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer}/retailclient_swtor_0to{vnummer}.zip"
            try:
                zeitx = int(time.time())
                sekunden = 0
                wget.download(url, saveloc, bar=bar_progress)
                print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer}/retailclient_swtor_0to{vnummer}.zip\n")
            except KeyboardInterrupt:
                print("\nYou stopped the download!")
                return
            except Exception as ex:
                exception = type(ex).__name__
                argumente = str(ex.args)
                if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                    print("\nNo Connection. Please try again!")
                    try:
                        log1_label.config(text="No connection.\nPlease try again!")
                    except:
                        pass
                    return
                else:
                    try:
                        log1_label.config(text="Version not found!")
                    except:
                        pass
                    print("\nVersion not found!\n")
                    return
        c = 0
        while True:
            c = int(c)+1
            if c < 10:
                c = "0" + str(c)
            if not os.path.exists(f"{saveloc}/retailclient_swtor_0to{vnummer}.z{c}") == True:
                url2 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer}/retailclient_swtor_0to{vnummer}.z{c}"
                while True:
                    try:
                        zeitx = int(time.time())
                        sekunden = 0
                        wget.download(url2, saveloc, bar=bar_progress)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer}/retailclient_swtor_0to{vnummer}.z{c}\n")
                        break
                    except KeyboardInterrupt:
                        print("\nYou stopped the download!")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            print("\nConnection lost. Trying again...")
                            time.sleep(5)
                        else:
                            try:
                                log1_label.config(text="Download finished!")
                            except:
                                pass
                            print("\nDownload finished!\n")
                            return

def download_files_pts(saveloc, lwert, vnummerx, vwert, vnummer):
    global zeitx
    global sekunden
    if not lwert == "client":
        print(f"Download of {vwert} {lwert} version {vnummerx} started! ({vnummer})\nPress CTRL+C to stop.")
        if not os.path.exists(f"{saveloc}/assets_swtor_test_{lwert}_{vnummerx}.zip") == True:
            url = f"http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_{vnummerx}/assets_swtor_test_{lwert}_{vnummerx}.zip"
            try:
                zeitx = int(time.time())
                sekunden = 0
                wget.download(url, saveloc, bar=bar_progress)
                print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_{vnummerx}/assets_swtor_test_{lwert}_{vnummerx}.zip\n")
            except KeyboardInterrupt:
                print("\nYou stopped the download!")
                return
            except Exception as ex:
                exception = type(ex).__name__
                argumente = str(ex.args)
                if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                    print("\nNo Connection. Please try again!")
                    try:
                        log1_label.config(text="No connection.\nPlease try again!")
                    except:
                        pass
                    return
                else:
                    try:
                        log1_label.config(text="Version not found!")
                    except:
                        pass
                    print("\nVersion not found!\n")
                    return
        c = 0
        while True:
            c = int(c)+1
            if c < 10:
                c = "0" + str(c)
            if not os.path.exists(f"{saveloc}/assets_swtor_test_{lwert}_{vnummerx}.z{c}") == True:
                url2 = f"http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_{vnummerx}/assets_swtor_test_{lwert}_{vnummerx}.z{c}"
                while True:
                    try:
                        zeitx = int(time.time())
                        sekunden = 0
                        wget.download(url2, saveloc, bar=bar_progress)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_{vnummerx}/assets_swtor_test_{lwert}_{vnummerx}.z{c}\n")
                        break
                    except KeyboardInterrupt:
                        print("\nYou stopped the download!")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            print("\nConnection lost. Trying again...")
                            time.sleep(5)
                        else:
                            try:
                                log1_label.config(text="Download finished!")
                            except:
                                pass
                            print("\nDownload finished!\n")
                            return
    if lwert == "client":
        print(f"Download of {vwert} {lwert} version {vnummerx} started! ({vnummer})\nPress CTRL+C to stop.")
        if not os.path.exists(f"{saveloc}/retailclient_publictest_{vnummerx}.zip") == True:
            url = f"http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_{vnummerx}/retailclient_publictest_{vnummerx}.zip"
            try:
                zeitx = int(time.time())
                sekunden = 0
                wget.download(url, saveloc, bar=bar_progress)
                print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_{vnummerx}/retailclient_publictest_{vnummerx}.zip\n")
            except KeyboardInterrupt:
                print("\nYou stopped the download!")
                return
            except Exception as ex:
                exception = type(ex).__name__
                argumente = str(ex.args)
                if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                    print("\nNo Connection. Please try again!")
                    try:
                        log1_label.config(text="No connection.\nPlease try again!")
                    except:
                        pass
                    return
                else:
                    try:
                        log1_label.config(text="Version not found!")
                    except:
                        pass
                    print("\nVersion not found!\n")
                    return
        c = 0
        while True:
            c = int(c)+1
            if c < 10:
                c = "0" + str(c)
            if not os.path.exists(f"{saveloc}/retailclient_publictest_{vnummerx}.z{c}") == True:
                url2 = f"http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_{vnummerx}/retailclient_publictest_{vnummerx}.z{c}"
                while True:
                    try:
                        zeitx = int(time.time())
                        sekunden = 0
                        wget.download(url2, saveloc, bar=bar_progress)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_{vnummerx}/retailclient_publictest_{vnummerx}.z{c}\n")
                        break
                    except KeyboardInterrupt:
                        print("\nYou stopped the download!")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            print("\nConnection lost. Trying again...")
                            time.sleep(5)
                        else:
                            try:
                                log1_label.config(text="Download finished!")
                            except:
                                pass
                            print("\nDownload finished!\n")
                            return

def download_files0_pts(saveloc, lwert, vnummerx, vwert, vnummer):
    global zeitx
    global sekunden
    if not lwert == "client":
        print(f"Download of {vwert} {lwert} version 0to{vnummer} started!\nPress CTRL+C to stop.")
        if not os.path.exists(f"{saveloc}/assets_swtor_test_{lwert}_0to{vnummer}.zip") == True:
            url = f"http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_0to{vnummer}/assets_swtor_test_{lwert}_0to{vnummer}.zip"
            try:
                zeitx = int(time.time())
                sekunden = 0
                wget.download(url, saveloc, bar=bar_progress)
                print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_0to{vnummer}/assets_swtor_test_{lwert}_0to{vnummer}.zip\n")
            except KeyboardInterrupt:
                print("\nYou stopped the download!")
                return
            except Exception as ex:
                exception = type(ex).__name__
                argumente = str(ex.args)
                if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                    print("\nNo Connection. Please try again!")
                    try:
                        log1_label.config(text="No connection.\nPlease try again!")
                    except:
                        pass
                    return
                else:
                    try:
                        log1_label.config(text="Version not found!")
                    except:
                        pass
                    print("\nVersion not found!\n")
                    return
        c = 0
        while True:
            c = int(c)+1
            if c < 10:
                c = "0" + str(c)
            if not os.path.exists(f"{saveloc}/assets_swtor_test_{lwert}_0to{vnummer}.z{c}") == True:
                url2 = f"http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_0to{vnummer}/assets_swtor_test_{lwert}_0to{vnummer}.z{c}"
                while True:
                    try:
                        zeitx = int(time.time())
                        sekunden = 0
                        wget.download(url2, saveloc, bar=bar_progress)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_0to{vnummer}/assets_swtor_test_{lwert}_0to{vnummer}.z{c}\n")
                        break
                    except KeyboardInterrupt:
                        print("\nYou stopped the download!")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            print("\nConnection lost. Trying again...")
                            time.sleep(5)
                        else:
                            try:
                                log1_label.config(text="Download finished!")
                            except:
                                pass
                            print("\nDownload finished!\n")
                            return
    if lwert == "client":
        print(f"Download of {vwert} {lwert} version 0to{vnummer} started!\nPress CTRL+C to stop.")
        if not os.path.exists(f"{saveloc}/retailclient_publictest_0to{vnummer}.zip") == True:
            url = f"http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_0to{vnummer}/retailclient_publictest_0to{vnummer}.zip"
            try:
                zeitx = int(time.time())
                sekunden = 0
                wget.download(url, saveloc, bar=bar_progress)
                print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_0to{vnummer}/retailclient_publictest_0to{vnummer}.zip\n")
            except KeyboardInterrupt:
                print("\nYou stopped the download!")
                return
            except Exception as ex:
                exception = type(ex).__name__
                argumente = str(ex.args)
                if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                    print("\nNo Connection. Please try again!")
                    try:
                        log1_label.config(text="No connection.\nPlease try again!")
                    except:
                        pass
                    return
                else:
                    try:
                        log1_label.config(text="Version not found!")
                    except:
                        pass
                    print("\nVersion not found!\n")
                    return
        c = 0
        while True:
            c = int(c)+1
            if c < 10:
                c = "0" + str(c)
            if not os.path.exists(f"{saveloc}/retailclient_publictest_0to{vnummer}.z{c}") == True:
                url2 = f"http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_0to{vnummer}/retailclient_publictest_0to{vnummer}.z{c}"
                while True:
                    try:
                        zeitx = int(time.time())
                        sekunden = 0
                        wget.download(url2, saveloc, bar=bar_progress)
                        print(f"\nDownloaded: http://cdn-patch.publictest.com/patch/publictest/retailclient_publictest/retailclient_publictest_0to{vnummer}/retailclient_publictest_0to{vnummer}.z{c}\n")
                        break
                    except KeyboardInterrupt:
                        print("\nYou stopped the download!")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            print("\nConnection lost. Trying again...")
                            time.sleep(5)
                        else:
                            try:
                                log1_label.config(text="Download finished!")
                            except:
                                pass
                            print("\nDownload finished!\n")
                            return

dir_path = os.path.dirname(os.path.realpath(__file__))
dirs = os.listdir(dir_path)
for item in dirs:
    if item.endswith(".tmp"):
        os.remove(os.path.join(dir_path, item))
    if item.endswith(".zip"):
        os.remove(os.path.join(dir_path, item))
    if item.endswith(".z01"):
        os.remove(os.path.join(dir_path, item))
    if item.endswith(".patchmanifest"):
        os.remove(os.path.join(dir_path, item))
    if item.endswith(".solidpkg"):
        os.remove(os.path.join(dir_path, item))

if len(sys.argv) > 1:
    for i in sys.argv:
        if i.lower() == "live":
            vwert = "live"
        if i.lower() == "pts":
            vwert = "PTS"
        if i.lower() == "movies":
            vwert = "movies"
        if i.lower() == "liveqatest":
            vwert = "liveqatest"
        if i.lower() == "betatest":
            vwert = "betatest"
        if i.lower() == "cstraining":
            vwert = "cstraining"
        if i.lower() == "liveeptest":
            vwert = "liveeptest"

        if i.lower() == "ft=main":
            lwert = "main"
        if i.lower() == "ft=client":
            lwert = "client"
        if i.lower() == "ft=de_de":
            lwert = "de_de"
        if i.lower() == "ft=en_us":
            lwert = "en_us"
        if i.lower() == "ft=fr_fr":
            lwert = "fr_fr"

        if i.lower() == "pv=xtoy":
            uwert = "XtoY"
        if i.lower() == "pv=0toy":
            uwert = "0toY"

        if i.lower().startswith("save="):
            saveloc = i.lower().replace("save=","")

        if i.lower().startswith("version="):
            i = i.lower().replace("version=","")
            if "-" in i.lower():
                ij = i.split("-")
                v1 = int(ij[0])
                v2 = int(ij[1])
                for j in range(v1, v2+1):
                    if uwert == "XtoY":
                        vnummerx = f"{int(j)-1}to{j}"
                        vnummer = j
                        if vwert == "live":
                            download_files(saveloc, lwert, vnummerx, vwert, vnummer)
                        if vwert == "PTS":
                            download_files_pts(saveloc, lwert, vnummerx, vwert, vnummer)
                        if vwert == "movies":
                            download_movies(saveloc, lwert, vnummerx, vwert, vnummer)
                        if vwert == "liveqatest":
                            download_exp_client(saveloc, lwert, vnummerx, vwert, vnummer, vwert)
                        if vwert == "betatest":
                            download_exp_client(saveloc, lwert, vnummerx, vwert, vnummer, vwert)
                        if vwert == "cstraining":
                            download_exp_client(saveloc, lwert, vnummerx, vwert, vnummer, vwert)
                        if vwert == "liveeptest":
                            download_exp_client(saveloc, lwert, vnummerx, vwert, vnummer, vwert)
                    if uwert == "0toY":
                        vnummer = j
                        vnummerx = j
                        if vwert == "live":
                            download_files0(saveloc, lwert, vnummerx, vwert, vnummer)
                        if vwert == "PTS":
                            download_files0_pts(saveloc, lwert, vnummerx, vwert, vnummer)
                        if vwert == "movies":
                            download_movies0(saveloc, lwert, vnummerx, vwert, vnummer)
                        if vwert == "liveqatest":
                            download_exp_client0(saveloc, lwert, vnummerx, vwert, vnummer, vwert)
                        if vwert == "betatest":
                            download_exp_client0(saveloc, lwert, vnummerx, vwert, vnummer, vwert)
                        if vwert == "cstraining":
                            download_exp_client0(saveloc, lwert, vnummerx, vwert, vnummer, vwert)
                        if vwert == "liveeptest":
                            download_exp_client0(saveloc, lwert, vnummerx, vwert, vnummer, vwert)
                print("\n\nAll downloads finished!")
                sys.exit()
            else:
                if uwert == "XtoY":
                    vnummerx = f"{int(i)-1}to{i}"
                    vnummer = i
                if uwert == "0toY":
                    vnummer = i
                    vnummerx = i
    try:
        if vwert == "PTS":
            if uwert == "XtoY":
                download_files_pts(saveloc, lwert, vnummerx, vwert, vnummer)
                sys.exit()
            if uwert == "0toY":
                download_files0_pts(saveloc, lwert, vnummerx, vwert, vnummer)
                sys.exit()
        if vwert == "movies":
            if uwert == "XtoY":
                download_movies(saveloc, lwert, vnummerx, vwert, vnummer)
                sys.exit()
            if uwert == "0toY":
                download_movies0(saveloc, lwert, vnummerx, vwert, vnummer)
                sys.exit()
        if vwert == "live":
            if uwert == "XtoY":
                download_files(saveloc, lwert, vnummerx, vwert, vnummer)
                sys.exit()
            if uwert == "0toY":
                download_files0(saveloc, lwert, vnummerx, vwert, vnummer)
                sys.exit()
        if vwert == "liveqatest":
            if uwert == "0toY":
                download_exp_client0(saveloc, lwert, vnummerx, vwert, vnummer, vwert)
                sys.exit()
            if uwert == "XtoY":
                download_exp_client(saveloc, lwert, vnummerx, vwert, vnummer, vwert)
                sys.exit()
        if vwert == "betatest":
            if uwert == "0toY":
                download_exp_client0(saveloc, lwert, vnummerx, vwert, vnummer, vwert)
                sys.exit()
            if uwert == "XtoY":
                download_exp_client(saveloc, lwert, vnummerx, vwert, vnummer, vwert)
                sys.exit()
        if vwert == "cstraining":
            if uwert == "0toY":
                download_exp_client0(saveloc, lwert, vnummerx, vwert, vnummer, vwert)
                sys.exit()
            if uwert == "XtoY":
                download_exp_client(saveloc, lwert, vnummerx, vwert, vnummer, vwert)
                sys.exit()
        if vwert == "liveeptest":
            if uwert == "0toY":
                download_exp_client0(saveloc, lwert, vnummerx, vwert, vnummer, vwert)
                sys.exit()
            if uwert == "XtoY":
                download_exp_client(saveloc, lwert, vnummerx, vwert, vnummer, vwert)
                sys.exit()
        sys.exit()
    except:
        print(f"{os.path.basename(sys.argv[0])} [live/pts/movies/liveqatest/betatest/cstraining/liveeptest] [ft=] [pv=] [save=] [version=]"
              "\n\n"
              "SWTOR Patch Downloader\n"
              "ft - main/client/en_us/de_de/fr_fr\n"
              "pv - XtoY/0toY\n"
              "save - Location to save (use / instead of \\)\n"
              "version - The version ID, you want to download; to download more than one, use startversion-endversion (like 330-340)\n\n"
              f"Example: {os.path.basename(sys.argv[0])} live ft=main pv=xtoy save=d:/temp version=230-233")
        sys.exit()
#data = {}
#data['version'] = []
#data['version'].append({
#    'name': 'PTS'})
#data['build'] = []
#data['build'].append({
#    'name': 'XtoY'})
#data['saveto'] = []
#data['saveto'].append({
#    'name': 'd:\temp'})
#data['lang'] = []
#data['lang'].append({
#    'name': 'main'})

#with open('settings.json', 'w') as outfile:
#    json.dump(data, outfile)

#data = {}
#data['devmode'] = []
#data['devmode'].append({
#    'name': 'true'})

#with open('devmode.json', 'w') as outfile:
#    json.dump(data, outfile)

print("SWTOR Patch Downloader\n")

def dl_man():
    global zeitx
    global sekunden
    vwert = varA.get()
    uwert = varB.get()
    lwert = varC.get()
    vnummer = eingabefeld.get()
    saveloc = ordnerzeile.get()
    if saveloc == "":
        log1_label.config(text="Please enter the location,\nwhere you want to save the files!")
        return
    if vwert == "PTS" and uwert == "XtoY":
        data = {}
        data['version'] = []
        data['version'].append({
        'name': 'PTS'})
        data['build'] = []
        data['build'].append({
            'name': 'XtoY'})
        data['saveto'] = []
        data['saveto'].append({
            'name': saveloc})
        if lwert == "main":
            data['lang'] = []
            data['lang'].append({
                'name': "main"})
        if lwert == "de_de":
            data['lang'] = []
            data['lang'].append({
                'name': "de_de"})
        if lwert == "en_us":
            data['lang'] = []
            data['lang'].append({
                'name': "en_us"})
        if lwert == "fr_fr":
            data['lang'] = []
            data['lang'].append({
                'name': "fr_fr"})
        if lwert == "client":
            data['lang'] = []
            data['lang'].append({
                'name': "client"})
        with open('settings.json', 'w') as outfile:
            json.dump(data, outfile)
    if vwert == "Live" and uwert == "XtoY":
        data = {}
        data['version'] = []
        data['version'].append({
        'name': 'Live'})
        data['build'] = []
        data['build'].append({
            'name': 'XtoY'})
        data['saveto'] = []
        data['saveto'].append({
            'name': saveloc})
        if lwert == "main":
            data['lang'] = []
            data['lang'].append({
                'name': "main"})
        if lwert == "de_de":
            data['lang'] = []
            data['lang'].append({
                'name': "de_de"})
        if lwert == "en_us":
            data['lang'] = []
            data['lang'].append({
                'name': "en_us"})
        if lwert == "fr_fr":
            data['lang'] = []
            data['lang'].append({
                'name': "fr_fr"})
        if lwert == "client":
            data['lang'] = []
            data['lang'].append({
                'name': "client"})
        with open('settings.json', 'w') as outfile:
            json.dump(data, outfile)
    if vwert == "PTS" and uwert == "0toY":
        data = {}
        data['version'] = []
        data['version'].append({
        'name': 'PTS'})
        data['build'] = []
        data['build'].append({
            'name': '0toY'})
        data['saveto'] = []
        data['saveto'].append({
            'name': saveloc})
        if lwert == "main":
            data['lang'] = []
            data['lang'].append({
                'name': "main"})
        if lwert == "de_de":
            data['lang'] = []
            data['lang'].append({
                'name': "de_de"})
        if lwert == "en_us":
            data['lang'] = []
            data['lang'].append({
                'name': "en_us"})
        if lwert == "fr_fr":
            data['lang'] = []
            data['lang'].append({
                'name': "fr_fr"})
        if lwert == "client":
            data['lang'] = []
            data['lang'].append({
                'name': "client"})
        with open('settings.json', 'w') as outfile:
            json.dump(data, outfile)
    if vwert == "Live" and uwert == "0toY":
        data = {}
        data['version'] = []
        data['version'].append({
        'name': 'Live'})
        data['build'] = []
        data['build'].append({
            'name': '0toY'})
        data['saveto'] = []
        data['saveto'].append({
            'name': saveloc})
        if lwert == "main":
            data['lang'] = []
            data['lang'].append({
                'name': "main"})
        if lwert == "de_de":
            data['lang'] = []
            data['lang'].append({
                'name': "de_de"})
        if lwert == "en_us":
            data['lang'] = []
            data['lang'].append({
                'name': "en_us"})
        if lwert == "fr_fr":
            data['lang'] = []
            data['lang'].append({
                'name': "fr_fr"})
        if lwert == "client":
            data['lang'] = []
            data['lang'].append({
                'name': "client"})
        with open('settings.json', 'w') as outfile:
            json.dump(data, outfile)
    if vwert == "movies" and uwert == "XtoY":
        data = {}
        data['version'] = []
        data['version'].append({
        'name': 'movies'})
        data['build'] = []
        data['build'].append({
            'name': 'XtoY'})
        data['saveto'] = []
        data['saveto'].append({
            'name': saveloc})
        if lwert == "main":
            data['lang'] = []
            data['lang'].append({
                'name': "main"})
        if lwert == "de_de":
            data['lang'] = []
            data['lang'].append({
                'name': "de_de"})
        if lwert == "en_us":
            data['lang'] = []
            data['lang'].append({
                'name': "en_us"})
        if lwert == "fr_fr":
            data['lang'] = []
            data['lang'].append({
                'name': "fr_fr"})
        if lwert == "client":
            data['lang'] = []
            data['lang'].append({
                'name': "client"})
        with open('settings.json', 'w') as outfile:
            json.dump(data, outfile)
    if vwert == "movies" and uwert == "0toY":
        data = {}
        data['version'] = []
        data['version'].append({
        'name': 'movies'})
        data['build'] = []
        data['build'].append({
            'name': '0toY'})
        data['saveto'] = []
        data['saveto'].append({
            'name': saveloc})
        if lwert == "main":
            data['lang'] = []
            data['lang'].append({
                'name': "main"})
        if lwert == "de_de":
            data['lang'] = []
            data['lang'].append({
                'name': "de_de"})
        if lwert == "en_us":
            data['lang'] = []
            data['lang'].append({
                'name': "en_us"})
        if lwert == "fr_fr":
            data['lang'] = []
            data['lang'].append({
                'name': "fr_fr"})
        if lwert == "client":
            data['lang'] = []
            data['lang'].append({
                'name': "client"})
        with open('settings.json', 'w') as outfile:
            json.dump(data, outfile)
            
    if vwert == "PTS":
        if not lwert == "client":
            print(f"Download of Manifest {vwert} {lwert} started!\nPress CTRL+C to stop.")
            if not os.path.exists(f"{saveloc}/assets_swtor_test_{lwert}.patchmanifest") == True:
                url = f"http://manifest.swtor.com/patch/assets_swtor_test_{lwert}.patchmanifest"
                while True:
                    try:
                        zeitx = int(time.time())
                        sekunden = 0
                        wget.download(url, saveloc, bar=bar_progress)
                        print(f"\nDownloaded: http://manifest.swtor.com/patch/assets_swtor_test_{lwert}.patchmanifest\n")
                        log1_label.config(text="Download finished!")
                        print("Download finished!\n")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            print("\nNo connection. Please try again!")
                            log1_label.config(text="No connection.\nPlease try again!")
                            return
                        else:
                            log1_label.config(text="Version not found!")
                            print("\nVersion not found!\n")
                            return
            else:
                log1_label.config(text="File already exists!")
                print("\nFile already exists!\n")
        if lwert == "client":
            print(f"Download of Manifest {vwert} {lwert} started!\nPress CTRL+C to stop.")
            if not os.path.exists(f"{saveloc}/retailclient_publictest.patchmanifest") == True:
                url = f"http://manifest.swtor.com/patch/retailclient_publictest.patchmanifest"
                while True:
                    try:
                        zeitx = int(time.time())
                        sekunden = 0
                        wget.download(url, saveloc, bar=bar_progress)
                        print(f"\nDownloaded: http://manifest.swtor.com/patch/retailclient_publictest.patchmanifest\n")
                        log1_label.config(text="Download finished!")
                        print("Download finished!\n")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            print("\nNo connection. Please try again!")
                            log1_label.config(text="No connection.\nPlease try again!")
                        else:
                            log1_label.config(text="Version not found!")
                            print("\nVersion not found!\n")
                            return
            else:
                log1_label.config(text="File already exists!")
                print("\nFile already exists!\n")
    if vwert == "Live":
        if not lwert == "client":
            print(f"Download of Manifest {vwert} {lwert} started!\nPress CTRL+C to stop.")
            if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}.patchmanifest") == True:
                url = f"http://manifest.swtor.com/patch/assets_swtor_{lwert}.patchmanifest"
                while True:
                    try:
                        zeitx = int(time.time())
                        sekunden = 0
                        wget.download(url, saveloc, bar=bar_progress)
                        print(f"\nDownloaded: http://manifest.swtor.com/patch/assets_swtor_{lwert}.patchmanifest\n")
                        log1_label.config(text="Download finished!")
                        print("Download finished!\n")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            print("\nNo connection. Please try again!")
                            log1_label.config(text="No connection.\nPlease try again!")
                            return
                        else:
                            log1_label.config(text="Version not found!")
                            print("\nVersion not found!\n")
                            return
            else:
                log1_label.config(text="File already exists!")
                print("\nFile already exists!\n")
        if lwert == "client":
            print(f"Download of Manifest {vwert} {lwert} started!\nPress CTRL+C to stop.")
            if not os.path.exists(f"{saveloc}/retailclient_swtor.patchmanifest") == True:
                url = f"http://manifest.swtor.com/patch/retailclient_swtor.patchmanifest"
                while True:
                    try:
                        zeitx = int(time.time())
                        sekunden = 0
                        wget.download(url, saveloc, bar=bar_progress)
                        print(f"\nDownloaded: http://manifest.swtor.com/patch/retailclient_swtor.patchmanifest\n")
                        log1_label.config(text="Download finished!")
                        print("Download finished!\n")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            print("\nNo connection. Please try again!")
                            log1_label.config(text="No connection.\nPlease try again!")
                            return
                        else:
                            log1_label.config(text="Version not found!")
                            print("\nVersion not found!\n")
                            return
            else:
                log1_label.config(text="File already exists!")
                print("\nFile already exists!\n")
    if vwert == "movies":
        if not lwert == "client" and not lwert == "main":
            print(f"Download of Manifest {vwert} {lwert} started!\nPress CTRL+C to stop.")
            if not os.path.exists(f"{saveloc}/movies_{lwert}.patchmanifest") == True:
                url = f"http://manifest.swtor.com/patch/movies_{lwert}.patchmanifest"
                while True:
                    try:
                        zeitx = int(time.time())
                        sekunden = 0
                        wget.download(url, saveloc, bar=bar_progress)
                        print(f"\nDownloaded: http://manifest.swtor.com/patch/movies_{lwert}.patchmanifest\n")
                        log1_label.config(text="Download finished!")
                        print("Download finished!\n")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            print("\nNo connection. Please try again!")
                            log1_label.config(text="No connection.\nPlease try again!")
                            return
                        else:
                            log1_label.config(text="Version not found!")
                            print("\nVersion not found!\n")
                            return
            else:
                log1_label.config(text="File already exists!")
                print("\nFile already exists!\n")
        else:
            log1_label.config(text="Please select a language!")
    if vwert == "liveqatest":
        url = f"http://manifest.swtor.com/patch/retailclient_liveqatest.patchmanifest"
        print(f"Download of Manifest {vwert} {lwert} started!\nPress CTRL+C to stop.")
        if not os.path.exists(f"{saveloc}/retailclient_liveqatest.patchmanifest") == True:
            while True:
                try:
                    zeitx = int(time.time())
                    sekunden = 0
                    wget.download(url, saveloc, bar=bar_progress)
                    print(f"\nDownloaded: http://manifest.swtor.com/patch/retailclient_liveqatest.patchmanifest\n")
                    log1_label.config(text="Download finished!")
                    print("Download finished!\n")
                    return
                except Exception as ex:
                    exception = type(ex).__name__
                    argumente = str(ex.args)
                    if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                        print("\nNo connection. Please try again!")
                        log1_label.config(text="No connection.\nPlease try again!")
                        return
                    else:
                        log1_label.config(text="Version not found!")
                        print("\nVersion not found!\n")
                        return
        else:
            log1_label.config(text="File already exists!")
            print("\nFile already exists!\n")
    if vwert == "betatest":
        url = f"http://manifest.swtor.com/patch/retailclient_betatest.patchmanifest"
        print(f"Download of Manifest {vwert} {lwert} started!\nPress CTRL+C to stop.")
        if not os.path.exists(f"{saveloc}/retailclient_betatest.patchmanifest") == True:
            while True:
                try:
                    zeitx = int(time.time())
                    sekunden = 0
                    wget.download(url, saveloc, bar=bar_progress)
                    print(f"\nDownloaded: http://manifest.swtor.com/patch/retailclient_betatest.patchmanifest\n")
                    log1_label.config(text="Download finished!")
                    print("Download finished!\n")
                    return
                except Exception as ex:
                    exception = type(ex).__name__
                    argumente = str(ex.args)
                    if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                        print("\nNo connection. Please try again!")
                        log1_label.config(text="No connection.\nPlease try again!")
                        return
                    else:
                        log1_label.config(text="Version not found!")
                        print("\nVersion not found!\n")
                        return
        else:
            log1_label.config(text="File already exists!")
            print("\nFile already exists!\n")
    if vwert == "cstraining":
        url = f"http://manifest.swtor.com/patch/retailclient_cstraining.patchmanifest"
        print(f"Download of Manifest {vwert} {lwert} started!\nPress CTRL+C to stop.")
        if not os.path.exists(f"{saveloc}/retailclient_cstraining.patchmanifest") == True:
            while True:
                try:
                    zeitx = int(time.time())
                    sekunden = 0
                    wget.download(url, saveloc, bar=bar_progress)
                    print(f"\nDownloaded: http://manifest.swtor.com/patch/retailclient_cstraining.patchmanifest\n")
                    log1_label.config(text="Download finished!")
                    print("Download finished!\n")
                    return
                except Exception as ex:
                    exception = type(ex).__name__
                    argumente = str(ex.args)
                    if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                        print("\nNo connection. Please try again!")
                        log1_label.config(text="No connection.\nPlease try again!")
                        return
                    else:
                        log1_label.config(text="Version not found!")
                        print("\nVersion not found!\n")
                        return
        else:
            log1_label.config(text="File already exists!")
            print("\nFile already exists!\n")
    if vwert == "liveeptest":
        url = f"http://manifest.swtor.com/patch/retailclient_liveeptest.patchmanifest"
        print(f"Download of Manifest {vwert} {lwert} started!\nPress CTRL+C to stop.")
        if not os.path.exists(f"{saveloc}/retailclient_liveeptest.patchmanifest") == True:
            while True:
                try:
                    zeitx = int(time.time())
                    sekunden = 0
                    wget.download(url, saveloc, bar=bar_progress)
                    print(f"\nDownloaded: http://manifest.swtor.com/patch/retailclient_liveeptest.patchmanifest\n")
                    log1_label.config(text="Download finished!")
                    print("Download finished!\n")
                    return
                except Exception as ex:
                    exception = type(ex).__name__
                    argumente = str(ex.args)
                    if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                        print("\nNo connection. Please try again!")
                        log1_label.config(text="No connection.\nPlease try again!")
                        return
                    else:
                        log1_label.config(text="Version not found!")
                        print("\nVersion not found!\n")
                        return
        else:
            log1_label.config(text="File already exists!")
            print("\nFile already exists!\n")

def dl_solid():
    global zeitx
    global sekunden
    vwert = varA.get()
    uwert = varB.get()
    lwert = varC.get()
    vnummer = eingabefeld.get()
    saveloc = ordnerzeile.get()
    yes = False
    if vnummer == "":
        log1_label.config(text="Please enter the version number,\nyou want to download!")
        return
    if saveloc == "":
        log1_label.config(text="Please enter the location,\nwhere you want to save the files!")
        return
    if vwert == "PTS" and uwert == "XtoY":
        data = {}
        data['version'] = []
        data['version'].append({
        'name': 'PTS'})
        data['build'] = []
        data['build'].append({
            'name': 'XtoY'})
        data['saveto'] = []
        data['saveto'].append({
            'name': saveloc})
        if lwert == "main":
            data['lang'] = []
            data['lang'].append({
                'name': "main"})
        if lwert == "de_de":
            data['lang'] = []
            data['lang'].append({
                'name': "de_de"})
        if lwert == "en_us":
            data['lang'] = []
            data['lang'].append({
                'name': "en_us"})
        if lwert == "fr_fr":
            data['lang'] = []
            data['lang'].append({
                'name': "fr_fr"})
        if lwert == "client":
            data['lang'] = []
            data['lang'].append({
                'name': "client"})
        with open('settings.json', 'w') as outfile:
            json.dump(data, outfile)
    if vwert == "Live" and uwert == "XtoY":
        data = {}
        data['version'] = []
        data['version'].append({
        'name': 'Live'})
        data['build'] = []
        data['build'].append({
            'name': 'XtoY'})
        data['saveto'] = []
        data['saveto'].append({
            'name': saveloc})
        if lwert == "main":
            data['lang'] = []
            data['lang'].append({
                'name': "main"})
        if lwert == "de_de":
            data['lang'] = []
            data['lang'].append({
                'name': "de_de"})
        if lwert == "en_us":
            data['lang'] = []
            data['lang'].append({
                'name': "en_us"})
        if lwert == "fr_fr":
            data['lang'] = []
            data['lang'].append({
                'name': "fr_fr"})
        if lwert == "client":
            data['lang'] = []
            data['lang'].append({
                'name': "client"})
        with open('settings.json', 'w') as outfile:
            json.dump(data, outfile)
    if vwert == "PTS" and uwert == "0toY":
        data = {}
        data['version'] = []
        data['version'].append({
        'name': 'PTS'})
        data['build'] = []
        data['build'].append({
            'name': '0toY'})
        data['saveto'] = []
        data['saveto'].append({
            'name': saveloc})
        if lwert == "main":
            data['lang'] = []
            data['lang'].append({
                'name': "main"})
        if lwert == "de_de":
            data['lang'] = []
            data['lang'].append({
                'name': "de_de"})
        if lwert == "en_us":
            data['lang'] = []
            data['lang'].append({
                'name': "en_us"})
        if lwert == "fr_fr":
            data['lang'] = []
            data['lang'].append({
                'name': "fr_fr"})
        if lwert == "client":
            data['lang'] = []
            data['lang'].append({
                'name': "client"})
        with open('settings.json', 'w') as outfile:
            json.dump(data, outfile)
    if vwert == "Live" and uwert == "0toY":
        data = {}
        data['version'] = []
        data['version'].append({
        'name': 'Live'})
        data['build'] = []
        data['build'].append({
            'name': '0toY'})
        data['saveto'] = []
        data['saveto'].append({
            'name': saveloc})
        if lwert == "main":
            data['lang'] = []
            data['lang'].append({
                'name': "main"})
        if lwert == "de_de":
            data['lang'] = []
            data['lang'].append({
                'name': "de_de"})
        if lwert == "en_us":
            data['lang'] = []
            data['lang'].append({
                'name': "en_us"})
        if lwert == "fr_fr":
            data['lang'] = []
            data['lang'].append({
                'name': "fr_fr"})
        if lwert == "client":
            data['lang'] = []
            data['lang'].append({
                'name': "client"})
        with open('settings.json', 'w') as outfile:
            json.dump(data, outfile)
    if vwert == "movies" and uwert == "XtoY":
        data = {}
        data['version'] = []
        data['version'].append({
        'name': 'movies'})
        data['build'] = []
        data['build'].append({
            'name': 'XtoY'})
        data['saveto'] = []
        data['saveto'].append({
            'name': saveloc})
        if lwert == "main":
            data['lang'] = []
            data['lang'].append({
                'name': "main"})
        if lwert == "de_de":
            data['lang'] = []
            data['lang'].append({
                'name': "de_de"})
        if lwert == "en_us":
            data['lang'] = []
            data['lang'].append({
                'name': "en_us"})
        if lwert == "fr_fr":
            data['lang'] = []
            data['lang'].append({
                'name': "fr_fr"})
        if lwert == "client":
            data['lang'] = []
            data['lang'].append({
                'name': "client"})
        with open('settings.json', 'w') as outfile:
            json.dump(data, outfile)
    if vwert == "Live" and uwert == "0toY":
        data = {}
        data['version'] = []
        data['version'].append({
        'name': 'movies'})
        data['build'] = []
        data['build'].append({
            'name': '0toY'})
        data['saveto'] = []
        data['saveto'].append({
            'name': saveloc})
        if lwert == "main":
            data['lang'] = []
            data['lang'].append({
                'name': "main"})
        if lwert == "de_de":
            data['lang'] = []
            data['lang'].append({
                'name': "de_de"})
        if lwert == "en_us":
            data['lang'] = []
            data['lang'].append({
                'name': "en_us"})
        if lwert == "fr_fr":
            data['lang'] = []
            data['lang'].append({
                'name': "fr_fr"})
        if lwert == "client":
            data['lang'] = []
            data['lang'].append({
                'name': "client"})
        with open('settings.json', 'w') as outfile:
            json.dump(data, outfile)

    if "." in vnummer:
        if vwert == "Live":
            for i in range(len(items)):
                if str(vnummer) == str(items[i][0]):
                    yes = True
                    yes1 = i
                    if lwert == "main":
                        ww = 2
                    if lwert == "client":
                        ww = 3
                    if lwert == "en_us":
                        ww = 4
                    if lwert == "de_de":
                        ww = 5
                    if lwert == "fr_fr":
                        ww = 6
                    break
            try:
                yes1 = yes1
            except:
                print("\nVersion not found!")
                log1_label.config(text="Version not found!")
                return
        else:
            print("\nYou can only use version numbers for Live-versions! Please use version IDs instead.")
            log1_label.config(text="Error! See console.")
            return

    if yes:
        vnummer2 = items[yes1][ww]
        if uwert == "XtoY":
            vnummer1 = int(vnummer2) - 1
            vnummerx = f"{vnummer1}to{vnummer2}"
        if uwert == "XtoY":
            if lwert == "client":
                print(f"Download of Solidpkg {vwert} {lwert} version {vnummerx} started! ({vnummer})\nPress CTRL+C to stop.")
                if not os.path.exists(f"{saveloc}/retailclient_swtor_{vnummerx}.solidpkg") == True:
                    url = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}.solidpkg"
                    while True:
                        try:
                            zeitx = int(time.time())
                            sekunden = 0
                            wget.download(url, saveloc, bar=bar_progress)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}.solidpkg\n")
                            log1_label.config(text="Download finished!")
                            print("Download finished!\n")
                            return
                        except KeyboardInterrupt:
                            print("\nYou stopped the download!")
                            return
                        except Exception as ex:
                            exception = type(ex).__name__
                            argumente = str(ex.args)
                            if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                                print("\nNo connection. Please try again!")
                                log1_label.config(text="No connection.\nPlease try again!")
                                return
                            else:
                                log1_label.config(text="Version not found!")
                                print("\nVersion not found!\n")
                                return
                else:
                    log1_label.config(text="File already exists!")
                    print("\nFile already exists!\n")
            if not lwert == "client":
                print(f"Download of Solidpkg {vwert} {lwert} version {vnummerx} started! ({vnummer})\nPress CTRL+C to stop.")
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_{vnummerx}.solidpkg") == True:
                    url = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}.solidpkg"
                    while True:
                        try:
                            zeitx = int(time.time())
                            sekunden = 0
                            wget.download(url, saveloc, bar=bar_progress)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}.solidpkg\n")
                            log1_label.config(text="Download finished!")
                            print("Download finished!\n")
                            return
                        except KeyboardInterrupt:
                            print("\nYou stopped the download!")
                            return
                        except Exception as ex:
                            exception = type(ex).__name__
                            argumente = str(ex.args)
                            if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                                print("\nNo connection. Please try again!")
                                log1_label.config(text="No connection.\nPlease try again!")
                                return
                            else:
                                log1_label.config(text="Version not found!")
                                print("\nVersion not found!\n")
                                return
                else:
                    log1_label.config(text="File already exists!")
                    print("\nFile already exists!\n")
        if uwert == "0toY":
            if lwert == "client":
                print(f"Download of Solidpkg {vwert} {lwert} version 0to{vnummer2} started! ({vnummer})\nPress CTRL+C to stop.")
                if not os.path.exists(f"{saveloc}/retailclient_swtor_0to{vnummer2}.solidpkg") == True:
                    url = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer2}.solidpkg"
                    while True:
                        try:
                            zeitx = int(time.time())
                            sekunden = 0
                            wget.download(url, saveloc, bar=bar_progress)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer2}.solidpkg\n")
                            log1_label.config(text="Download finished!")
                            print("Download finished!\n")
                            return
                        except KeyboardInterrupt:
                            print("\nYou stopped the download!")
                            return
                        except Exception as ex:
                            exception = type(ex).__name__
                            argumente = str(ex.args)
                            if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                                print("\nNo connection. Please try again!")
                                log1_label.config(text="No connection.\nPlease try again!")
                                return
                            else:
                                log1_label.config(text="Version not found!")
                                print("\nVersion not found!\n")
                                return
                else:
                    log1_label.config(text="File already exists!")
                    print("\nFile already exists!\n")
            if not lwert == "client":
                print(f"Download of Solidpkg {vwert} {lwert} version 0to{vnummer2} started! ({vnummer})\nPress CTRL+C to stop.")
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_0to{vnummer2}.solidpkg") == True:
                    url = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer2}.solidpkg"
                    while True:
                        try:
                            zeitx = int(time.time())
                            sekunden = 0
                            wget.download(url, saveloc, bar=bar_progress)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer2}.solidpkg\n")
                            log1_label.config(text="Download finished!")
                            print("Download finished!\n")
                            return
                        except KeyboardInterrupt:
                            print("\nYou stopped the download!")
                            return
                        except Exception as ex:
                            exception = type(ex).__name__
                            argumente = str(ex.args)
                            if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                                print("\nNo connection. Please try again!")
                                log1_label.config(text="No connection.\nPlease try again!")
                                return
                            else:
                                log1_label.config(text="Version not found!")
                                print("\nVersion not found!\n")
                                return
                else:
                    log1_label.config(text="File already exists!")
                    print("\nFile already exists!\n")
    
    vnummer2 = int(vnummer) -1
    vnummerx = str(vnummer2) + "to" + str(vnummer)
    if vwert == "PTS":
        if uwert == "XtoY":
            if lwert == "client":
                print(f"Download of Solidpkg {vwert} {lwert} version {vnummerx} started!\nPress CTRL+C to stop.")
                if not os.path.exists(f"{saveloc}/assets_swtor_test_{lwert}_{vnummerx}.solidpkg") == True:
                    url = f"http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_{vnummerx}.solidpkg"
                    while True:
                        try:
                            zeitx = int(time.time())
                            sekunden = 0
                            wget.download(url, saveloc, bar=bar_progress)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_{vnummerx}.solidpkg\n")
                            log1_label.config(text="Download finished!")
                            print("Download finished!\n")
                            return
                        except KeyboardInterrupt:
                            print("\nYou stopped the download!")
                            return
                        except Exception as ex:
                            exception = type(ex).__name__
                            argumente = str(ex.args)
                            if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                                print("\nNo connection. Please try again!")
                                log1_label.config(text="No connection.\nPlease try again!")
                                return
                            else:
                                log1_label.config(text="Version not found!")
                                print("\nVersion not found!\n")
                                return
                else:
                    log1_label.config(text="File already exists!")
                    print("\nFile already exists!\n")
            if not lwert == "client":
                print(f"Download of Solidpkg {vwert} {lwert} version {vnummerx} started!\nPress CTRL+C to stop.")
                if not os.path.exists(f"{saveloc}/assets_swtor_test_{lwert}_{vnummerx}.solidpkg") == True:
                    url = f"http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_{vnummerx}.solidpkg"
                    while True:
                        try:
                            zeitx = int(time.time())
                            sekunden = 0
                            wget.download(url, saveloc, bar=bar_progress)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_{vnummerx}.solidpkg\n")
                            log1_label.config(text="Download finished!")
                            print("Download finished!\n")
                            return
                        except KeyboardInterrupt:
                            print("\nYou stopped the download!")
                            return
                        except Exception as ex:
                            exception = type(ex).__name__
                            argumente = str(ex.args)
                            if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                                print("\nNo connection. Please try again!")
                                log1_label.config(text="No connection.\nPlease try again!")
                                return
                            else:
                                log1_label.config(text="Version not found!")
                                print("\nVersion not found!\n")
                                return
                else:
                    log1_label.config(text="File already exists!")
                    print("\nFile already exists!\n")
        if uwert == "0toY":
            if lwert == "client":
                print(f"Download of Solidpkg {vwert} {lwert} version 0to{vnummer} started!\nPress CTRL+C to stop.")
                if not os.path.exists(f"{saveloc}/assets_swtor_test_{lwert}_0to{vnummer}.solidpkg") == True:
                    url = f"http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_0to{vnummer}.solidpkg"
                    while True:
                        try:
                            zeitx = int(time.time())
                            sekunden = 0
                            wget.download(url, saveloc, bar=bar_progress)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_0to{vnummer}.solidpkg\n")
                            log1_label.config(text="Download finished!")
                            print("Download finished!\n")
                            return
                        except KeyboardInterrupt:
                            print("\nYou stopped the download!")
                            return
                        except Exception as ex:
                            exception = type(ex).__name__
                            argumente = str(ex.args)
                            if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                                print("\nNo connection. Please try again!")
                                log1_label.config(text="No connection.\nPlease try again!")
                                return
                            else:
                                log1_label.config(text="Version not found!")
                                print("\nVersion not found!\n")
                                return
                else:
                    log1_label.config(text="File already exists!")
                    print("\nFile already exists!\n")
            if not lwert == "client":
                print(f"Download of Solidpkg {vwert} {lwert} version 0to{vnummer} started!\nPress CTRL+C to stop.")
                if not os.path.exists(f"{saveloc}/assets_swtor_test_{lwert}_0to{vnummer}.solidpkg") == True:
                    url = f"http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_0to{vnummer}.solidpkg"
                    while True:
                        try:
                            zeitx = int(time.time())
                            sekunden = 0
                            wget.download(url, saveloc, bar=bar_progress)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_0to{vnummer}.solidpkg\n")
                            log1_label.config(text="Download finished!")
                            print("Download finished!\n")
                            return
                        except KeyboardInterrupt:
                            print("\nYou stopped the download!")
                            return
                        except Exception as ex:
                            exception = type(ex).__name__
                            argumente = str(ex.args)
                            if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                                print("\nNo connection. Please try again!")
                                log1_label.config(text="No connection.\nPlease try again!")
                                return
                            else:
                                log1_label.config(text="Version not found!")
                                print("\nVersion not found!\n")
                                return
                else:
                    log1_label.config(text="File already exists!")
                    print("\nFile already exists!\n")
    if vwert == "Live":
        if uwert == "XtoY":
            if lwert == "client":
                print(f"Download of Solidpkg {vwert} {lwert} version {vnummerx} started!\nPress CTRL+C to stop.")
                if not os.path.exists(f"{saveloc}/retailclient_swtor_{vnummerx}.solidpkg") == True:
                    url = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}.solidpkg"
                    while True:
                        try:
                            zeitx = int(time.time())
                            sekunden = 0
                            wget.download(url, saveloc, bar=bar_progress)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}.solidpkg\n")
                            log1_label.config(text="Download finished!")
                            print("Download finished!\n")
                            return
                        except KeyboardInterrupt:
                            print("\nYou stopped the download!")
                            return
                        except Exception as ex:
                            exception = type(ex).__name__
                            argumente = str(ex.args)
                            if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                                print("\nNo connection. Please try again!")
                                log1_label.config(text="No connection.\nPlease try again!")
                                return
                            else:
                                log1_label.config(text="Version not found!")
                                print("\nVersion not found!\n")
                                return
                else:
                    log1_label.config(text="File already exists!")
                    print("\nFile already exists!\n")
            if not lwert == "client":
                print(f"Download of Solidpkg {vwert} {lwert} version {vnummerx} started!\nPress CTRL+C to stop.")
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_{vnummerx}.solidpkg") == True:
                    url = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}.solidpkg"
                    while True:
                        try:
                            zeitx = int(time.time())
                            sekunden = 0
                            wget.download(url, saveloc, bar=bar_progress)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}.solidpkg\n")
                            log1_label.config(text="Download finished!")
                            print("Download finished!\n")
                            return
                        except KeyboardInterrupt:
                            print("\nYou stopped the download!")
                            return
                        except Exception as ex:
                            exception = type(ex).__name__
                            argumente = str(ex.args)
                            if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                                print("\nNo connection. Please try again!")
                                log1_label.config(text="No connection.\nPlease try again!")
                                return
                            else:
                                log1_label.config(text="Version not found!")
                                print("\nVersion not found!\n")
                                return
                else:
                    log1_label.config(text="File already exists!")
                    print("\nFile already exists!\n")
        if uwert == "0toY":
            if lwert == "client":
                print(f"Download of Solidpkg {vwert} {lwert} version 0to{vnummer} started!\nPress CTRL+C to stop.")
                if not os.path.exists(f"{saveloc}/retailclient_swtor_0to{vnummer}.solidpkg") == True:
                    url = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer}.solidpkg"
                    while True:
                        try:
                            zeitx = int(time.time())
                            sekunden = 0
                            wget.download(url, saveloc, bar=bar_progress)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer}.solidpkg\n")
                            log1_label.config(text="Download finished!")
                            print("Download finished!\n")
                            return
                        except KeyboardInterrupt:
                            print("\nYou stopped the download!")
                            return
                        except Exception as ex:
                            exception = type(ex).__name__
                            argumente = str(ex.args)
                            if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                                print("\nNo connection. Please try again!")
                                log1_label.config(text="No connection.\nPlease try again!")
                                return
                            else:
                                log1_label.config(text="Version not found!")
                                print("\nVersion not found!\n")
                                return
                else:
                    log1_label.config(text="File already exists!")
                    print("\nFile already exists!\n")
            if not lwert == "client":
                print(f"Download of Solidpkg {vwert} {lwert} version 0to{vnummer} started!\nPress CTRL+C to stop.")
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_0to{vnummer}.solidpkg") == True:
                    url = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer}.solidpkg"
                    while True:
                        try:
                            zeitx = int(time.time())
                            sekunden = 0
                            wget.download(url, saveloc, bar=bar_progress)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer}.solidpkg\n")
                            log1_label.config(text="Download finished!")
                            print("Download finished!\n")
                            return
                        except KeyboardInterrupt:
                            print("\nYou stopped the download!")
                            return
                        except Exception as ex:
                            exception = type(ex).__name__
                            argumente = str(ex.args)
                            if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                                print("\nNo connection. Please try again!")
                                log1_label.config(text="No connection.\nPlease try again!")
                                return
                            else:
                                log1_label.config(text="Version not found!")
                                print("\nVersion not found!\n")
                                return
                else:
                    log1_label.config(text="File already exists!")
                    print("\nFile already exists!\n")
    if vwert == "liveqatest":
        if uwert == "0toY":
            print(f"Download of Solidpkg {vwert} version 0to{vnummer} started!\nPress CTRL+C to stop.")
            if not os.path.exists(f"{saveloc}/retailclient_liveqatest_0to{vnummer}.solidpkg") == True:
                url = f"http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_0to{vnummer}.solidpkg"
                while True:
                    try:
                        zeitx = int(time.time())
                        sekunden = 0
                        wget.download(url, saveloc, bar=bar_progress)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_0to{vnummer}.solidpkg\n")
                        log1_label.config(text="Download finished!")
                        print("Download finished!\n")
                        return
                    except KeyboardInterrupt:
                            print("\nYou stopped the download!")
                            return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            print("\nNo connection. Please try again!")
                            log1_label.config(text="No connection.\nPlease try again!")
                            return
                        else:
                            log1_label.config(text="Version not found!")
                            print("\nVersion not found!\n")
                            return
            else:
                log1_label.config(text="File already exists!")
                print("\nFile already exists!\n")

        if uwert == "XtoY":
            print(f"Download of Solidpkg {vwert} version {vnummerx} started!\nPress CTRL+C to stop.")
            if not os.path.exists(f"{saveloc}/retailclient_liveqatest_{vnummerx}.solidpkg") == True:
                url = f"http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_{vnummerx}.solidpkg"
                while True:
                    try:
                        zeitx = int(time.time())
                        sekunden = 0
                        wget.download(url, saveloc, bar=bar_progress)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_{vnummerx}.solidpkg\n")
                        log1_label.config(text="Download finished!")
                        print("Download finished!\n")
                        return
                    except KeyboardInterrupt:
                            print("\nYou stopped the download!")
                            return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            print("\nNo connection. Please try again!")
                            log1_label.config(text="No connection.\nPlease try again!")
                            return
                        else:
                            log1_label.config(text="Version not found!")
                            print("\nVersion not found!\n")
                            return
            else:
                log1_label.config(text="File already exists!")
                print("\nFile already exists!\n")

    if vwert == "betatest":
        if uwert == "0toY":
            print(f"Download of Solidpkg {vwert} version 0to{vnummer} started!\nPress CTRL+C to stop.")
            if not os.path.exists(f"{saveloc}/retailclient_betatest_0to{vnummer}.solidpkg") == True:
                url = f"http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_0to{vnummer}.solidpkg"
                while True:
                    try:
                        zeitx = int(time.time())
                        sekunden = 0
                        wget.download(url, saveloc, bar=bar_progress)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_0to{vnummer}.solidpkg\n")
                        log1_label.config(text="Download finished!")
                        print("Download finished!\n")
                        return
                    except KeyboardInterrupt:
                            print("\nYou stopped the download!")
                            return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            print("\nNo connection. Please try again!")
                            log1_label.config(text="No connection.\nPlease try again!")
                            return
                        else:
                            log1_label.config(text="Version not found!")
                            print("\nVersion not found!\n")
                            return
            else:
                log1_label.config(text="File already exists!")
                print("\nFile already exists!\n")

        if uwert == "XtoY":
            print(f"Download of Solidpkg {vwert} version {vnummerx} started!\nPress CTRL+C to stop.")
            if not os.path.exists(f"{saveloc}/retailclient_betatest_{vnummerx}.solidpkg") == True:
                url = f"http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_{vnummerx}.solidpkg"
                while True:
                    try:
                        zeitx = int(time.time())
                        sekunden = 0
                        wget.download(url, saveloc, bar=bar_progress)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_{vnummerx}.solidpkg\n")
                        log1_label.config(text="Download finished!")
                        print("Download finished!\n")
                        return
                    except KeyboardInterrupt:
                            print("\nYou stopped the download!")
                            return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            print("\nNo connection. Please try again!")
                            log1_label.config(text="No connection.\nPlease try again!")
                            return
                        else:
                            log1_label.config(text="Version not found!")
                            print("\nVersion not found!\n")
                            return
            else:
                log1_label.config(text="File already exists!")
                print("\nFile already exists!\n")

    if vwert == "cstraining":
        if uwert == "0toY":
            print(f"Download of Solidpkg {vwert} version 0to{vnummer} started!\nPress CTRL+C to stop.")
            if not os.path.exists(f"{saveloc}/retailclient_cstraining_0to{vnummer}.solidpkg") == True:
                url = f"http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_0to{vnummer}.solidpkg"
                while True:
                    try:
                        zeitx = int(time.time())
                        sekunden = 0
                        wget.download(url, saveloc, bar=bar_progress)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_0to{vnummer}.solidpkg\n")
                        log1_label.config(text="Download finished!")
                        print("Download finished!\n")
                        return
                    except KeyboardInterrupt:
                            print("\nYou stopped the download!")
                            return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            print("\nNo connection. Please try again!")
                            log1_label.config(text="No connection.\nPlease try again!")
                            return
                        else:
                            log1_label.config(text="Version not found!")
                            print("\nVersion not found!\n")
                            return
            else:
                log1_label.config(text="File already exists!")
                print("\nFile already exists!\n")
                
        if uwert == "XtoY":
            print(f"Download of Solidpkg {vwert} version {vnummerx} started!\nPress CTRL+C to stop.")
            if not os.path.exists(f"{saveloc}/retailclient_cstraining_{vnummerx}.solidpkg") == True:
                url = f"http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_{vnummerx}.solidpkg"
                while True:
                    try:
                        zeitx = int(time.time())
                        sekunden = 0
                        wget.download(url, saveloc, bar=bar_progress)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_{vnummerx}.solidpkg\n")
                        log1_label.config(text="Download finished!")
                        print("Download finished!\n")
                        return
                    except KeyboardInterrupt:
                        print("\nYou stopped the download!")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            print("\nNo connection. Please try again!")
                            log1_label.config(text="No connection.\nPlease try again!")
                            return
                        else:
                            log1_label.config(text="Version not found!")
                            print("\nVersion not found!\n")
                            return
            else:
                log1_label.config(text="File already exists!")
                print("\nFile already exists!\n")
                
    if vwert == "liveeptest":
        if uwert == "0toY":
            print(f"Download of Solidpkg {vwert} version 0to{vnummer} started!\nPress CTRL+C to stop.")
            if not os.path.exists(f"{saveloc}/retailclient_liveeptest_0to{vnummer}.solidpkg") == True:
                url = f"http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_0to{vnummer}.solidpkg"
                while True:
                    try:
                        zeitx = int(time.time())
                        sekunden = 0
                        wget.download(url, saveloc, bar=bar_progress)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_0to{vnummer}.solidpkg\n")
                        log1_label.config(text="Download finished!")
                        print("Download finished!\n")
                        return
                    except KeyboardInterrupt:
                        print("\nYou stopped the download!")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            print("\nNo connection. Please try again!")
                            log1_label.config(text="No connection.\nPlease try again!")
                            return
                        else:
                            log1_label.config(text="Version not found!")
                            print("\nVersion not found!\n")
                            return
            else:
                log1_label.config(text="File already exists!")
                print("\nFile already exists!\n")
                
        if uwert == "XtoY":
            print(f"Download of Solidpkg {vwert} version {vnummerx} started!\nPress CTRL+C to stop.")
            if not os.path.exists(f"{saveloc}/retailclient_liveeptest_{vnummerx}.solidpkg") == True:
                url = f"http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_{vnummerx}.solidpkg"
                while True:
                    try:
                        zeitx = int(time.time())
                        sekunden = 0
                        wget.download(url, saveloc, bar=bar_progress)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_{vnummerx}.solidpkg\n")
                        log1_label.config(text="Download finished!")
                        print("Download finished!\n")
                        return
                    except KeyboardInterrupt:
                        print("\nYou stopped the download!")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            print("\nNo connection. Please try again!")
                            log1_label.config(text="No connection.\nPlease try again!")
                            return
                        else:
                            log1_label.config(text="Version not found!")
                            print("\nVersion not found!\n")
                            return
            else:
                log1_label.config(text="File already exists!")
                print("\nFile already exists!\n")
    if vwert == "movies":
        if uwert == "XtoY":
            if not lwert == "client" and not lwert == "main":
                print(f"Download of Solidpkg {vwert} {lwert} version {vnummerx} started!\nPress CTRL+C to stop.")
                if not os.path.exists(f"{saveloc}/movies_{lwert}_{vnummerx}.solidpkg") == True:
                    url = f"http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_{vnummerx}.solidpkg"
                    while True:
                        try:
                            zeitx = int(time.time())
                            sekunden = 0
                            wget.download(url, saveloc, bar=bar_progress)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_{vnummerx}.solidpkg\n")
                            log1_label.config(text="Download finished!")
                            print("Download finished!\n")
                            return
                        except KeyboardInterrupt:
                            print("\nYou stopped the download!")
                            return
                        except Exception as ex:
                            exception = type(ex).__name__
                            argumente = str(ex.args)
                            if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                                print("\nNo connection. Please try again!")
                                log1_label.config(text="No connection.\nPlease try again!")
                                return
                            else:
                                log1_label.config(text="Version not found!")
                                print("\nVersion not found!\n")
                                return
                else:
                    log1_label.config(text="File already exists!")
                    print("\nFile already exists!\n")
            else:
                log1_label.config(text="Please select a language!")
        if uwert == "0toY":
            if not lwert == "client" and not lwert == "main":
                print(f"Download of Solidpkg {vwert} version 0to{vnummer} started!\nPress CTRL+C to stop.")
                if not os.path.exists(f"{saveloc}/movies_{lwert}_0to{vnummer}.solidpkg") == True:
                    url = f"http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_0to{vnummer}.solidpkg"
                    while True:
                        try:
                            zeitx = int(time.time())
                            sekunden = 0
                            wget.download(url, saveloc, bar=bar_progress)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_0to{vnummer}.solidpkg\n")
                            log1_label.config(text="Download finished!")
                            print("Download finished!\n")
                            return
                        except KeyboardInterrupt:
                            print("\nYou stopped the download!")
                            return
                        except Exception as ex:
                            exception = type(ex).__name__
                            argumente = str(ex.args)
                            if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                                print("\nNo connection. Please try again!")
                                log1_label.config(text="No connection.\nPlease try again!")
                                return
                            else:
                                log1_label.config(text="Version not found!")
                                print("\nVersion not found!\n")
                                return
                else:
                    log1_label.config(text="File already exists!")
                    print("\nFile already exists!\n")
                    
            else:
                log1_label.config(text="Please select a language!")

def check_date():
    global zeitx
    global sekunden
    vwert = varA.get()
    uwert = varB.get()
    lwert = varC.get()
    vnummer = eingabefeld.get()
    saveloc = os.getcwd()
    saveloc2 = ordnerzeile.get()
    if vnummer == "":
        log1_label.config(text="Please enter the version number,\nyou want to see!")
        return
    if vwert == "PTS" and uwert == "XtoY":
        data = {}
        data['version'] = []
        data['version'].append({
        'name': 'PTS'})
        data['build'] = []
        data['build'].append({
            'name': 'XtoY'})
        data['saveto'] = []
        data['saveto'].append({
            'name': saveloc2})
        if lwert == "main":
            data['lang'] = []
            data['lang'].append({
                'name': "main"})
        if lwert == "de_de":
            data['lang'] = []
            data['lang'].append({
                'name': "de_de"})
        if lwert == "en_us":
            data['lang'] = []
            data['lang'].append({
                'name': "en_us"})
        if lwert == "fr_fr":
            data['lang'] = []
            data['lang'].append({
                'name': "fr_fr"})
        if lwert == "client":
            data['lang'] = []
            data['lang'].append({
                'name': "client"})
        with open('settings.json', 'w') as outfile:
            json.dump(data, outfile)
    if vwert == "Live" and uwert == "XtoY":
        data = {}
        data['version'] = []
        data['version'].append({
        'name': 'Live'})
        data['build'] = []
        data['build'].append({
            'name': 'XtoY'})
        data['saveto'] = []
        data['saveto'].append({
            'name': saveloc2})
        if lwert == "main":
            data['lang'] = []
            data['lang'].append({
                'name': "main"})
        if lwert == "de_de":
            data['lang'] = []
            data['lang'].append({
                'name': "de_de"})
        if lwert == "en_us":
            data['lang'] = []
            data['lang'].append({
                'name': "en_us"})
        if lwert == "fr_fr":
            data['lang'] = []
            data['lang'].append({
                'name': "fr_fr"})
        if lwert == "client":
            data['lang'] = []
            data['lang'].append({
                'name': "client"})
        with open('settings.json', 'w') as outfile:
            json.dump(data, outfile)
    if vwert == "PTS" and uwert == "0toY":
        data = {}
        data['version'] = []
        data['version'].append({
        'name': 'PTS'})
        data['build'] = []
        data['build'].append({
            'name': '0toY'})
        data['saveto'] = []
        data['saveto'].append({
            'name': saveloc2})
        if lwert == "main":
            data['lang'] = []
            data['lang'].append({
                'name': "main"})
        if lwert == "de_de":
            data['lang'] = []
            data['lang'].append({
                'name': "de_de"})
        if lwert == "en_us":
            data['lang'] = []
            data['lang'].append({
                'name': "en_us"})
        if lwert == "fr_fr":
            data['lang'] = []
            data['lang'].append({
                'name': "fr_fr"})
        if lwert == "client":
            data['lang'] = []
            data['lang'].append({
                'name': "client"})
        with open('settings.json', 'w') as outfile:
            json.dump(data, outfile)
    if vwert == "Live" and uwert == "0toY":
        data = {}
        data['version'] = []
        data['version'].append({
        'name': 'Live'})
        data['build'] = []
        data['build'].append({
            'name': '0toY'})
        data['saveto'] = []
        data['saveto'].append({
            'name': saveloc2})
        if lwert == "main":
            data['lang'] = []
            data['lang'].append({
                'name': "main"})
        if lwert == "de_de":
            data['lang'] = []
            data['lang'].append({
                'name': "de_de"})
        if lwert == "en_us":
            data['lang'] = []
            data['lang'].append({
                'name': "en_us"})
        if lwert == "fr_fr":
            data['lang'] = []
            data['lang'].append({
                'name': "fr_fr"})
        if lwert == "client":
            data['lang'] = []
            data['lang'].append({
                'name': "client"})
        with open('settings.json', 'w') as outfile:
            json.dump(data, outfile)
    if vwert == "movies" and uwert == "XtoY":
        data = {}
        data['version'] = []
        data['version'].append({
        'name': 'movies'})
        data['build'] = []
        data['build'].append({
            'name': 'XtoY'})
        data['saveto'] = []
        data['saveto'].append({
            'name': saveloc2})
        if lwert == "main":
            data['lang'] = []
            data['lang'].append({
                'name': "main"})
        if lwert == "de_de":
            data['lang'] = []
            data['lang'].append({
                'name': "de_de"})
        if lwert == "en_us":
            data['lang'] = []
            data['lang'].append({
                'name': "en_us"})
        if lwert == "fr_fr":
            data['lang'] = []
            data['lang'].append({
                'name': "fr_fr"})
        if lwert == "client":
            data['lang'] = []
            data['lang'].append({
                'name': "client"})
        with open('settings.json', 'w') as outfile:
            json.dump(data, outfile)
    if vwert == "movies" and uwert == "0toY":
        data = {}
        data['version'] = []
        data['version'].append({
        'name': 'movies'})
        data['build'] = []
        data['build'].append({
            'name': '0toY'})
        data['saveto'] = []
        data['saveto'].append({
            'name': saveloc2})
        if lwert == "main":
            data['lang'] = []
            data['lang'].append({
                'name': "main"})
        if lwert == "de_de":
            data['lang'] = []
            data['lang'].append({
                'name': "de_de"})
        if lwert == "en_us":
            data['lang'] = []
            data['lang'].append({
                'name': "en_us"})
        if lwert == "fr_fr":
            data['lang'] = []
            data['lang'].append({
                'name': "fr_fr"})
        if lwert == "client":
            data['lang'] = []
            data['lang'].append({
                'name': "client"})
        with open('settings.json', 'w') as outfile:
            json.dump(data, outfile)

    if "." in vnummer:
        if vwert == "Live":
            for i in range(len(items)):
                if str(vnummer) == str(items[i][0]):
                    yes = True
                    yes1 = i
                    if lwert == "main":
                        ww = 2
                    if lwert == "client":
                        ww = 3
                    if lwert == "en_us":
                        ww = 4
                    if lwert == "de_de":
                        ww = 5
                    if lwert == "fr_fr":
                        ww = 6
                    break
            try:
                yes1 = yes1
            except:
                print("\nVersion not found!")
                log1_label.config(text="Version not found!")
                return
        else:
            print("\nYou can only use version numbers for Live-versions! Please use version IDs instead.")
            log1_label.config(text="Error! See console.")
            return

        if yes:
            print(f"Version released on: {items[yes1][1]}")
            log1_label.config(text=f"Version released on: {items[yes1][1]}")
            return
    
    vnummer2 = int(vnummer) -1
    vnummerx = str(vnummer2) + "to" + str(vnummer)
    if vwert == "PTS":
        if uwert == "XtoY":
            if not lwert == "client":
                if not os.path.exists(f"{saveloc}/assets_swtor_test_{lwert}_{vnummerx}.zip") == True:
                    url = f"http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_{vnummerx}/assets_swtor_test_{lwert}_{vnummerx}.zip"
                    try:
                        zeitx = int(time.time())
                        sekunden = 0
                        wget.download(url, saveloc, bar=bar_progress)
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            print("\nNo connection. Please try again!")
                            log1_label.config(text="No connection.\nPlease try again!")
                            return
                        else:
                            log1_label.config(text="Version not found!")
                            print("\nVersion not found!\n")
                            return
                ZipFile = zipfile.ZipFile(f"{saveloc}/assets_swtor_test_{lwert}_{vnummerx}.zip", "r")
                if lwert == "main":
                    x = ZipFile.getinfo("assets_swtor_test_main.version").date_time
                if lwert == "de_de":
                    x = ZipFile.getinfo("assets_swtor_test_de_de.version").date_time
                if lwert == "en_us":
                    x = ZipFile.getinfo("assets_swtor_test_en_us.version").date_time
                if lwert == "fr_fr":
                    x = ZipFile.getinfo("assets_swtor_test_fr_fr.version").date_time
                print("\nFile created on: " + str(x[2]) + "." + str(x[1]) + "." + str(x[0]) + "\n")
                log1_label.config(text="File created on: " + str(x[2]) + "." + str(x[1]) + "." + str(x[0]))
            if lwert == "client":
                if not os.path.exists(f"{saveloc}/retailclient_publictest_{vnummerx}.zip") == True:
                    url = f"http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_{vnummerx}/retailclient_publictest_{vnummerx}.zip"
                    try:
                        zeitx = int(time.time())
                        sekunden = 0
                        wget.download(url, saveloc, bar=bar_progress)
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            print("\nNo connection. Please try again!")
                            log1_label.config(text="No connection.\nPlease try again!")
                            return
                        else:
                             log1_label.config(text="Version not found!")
                             print("\nVersion not found!\n")
                             return
                ZipFile = zipfile.ZipFile(f"{saveloc}/retailclient_publictest_{vnummerx}.zip", "r")
                x = ZipFile.getinfo("retailclient_publictest.version").date_time
                print("\nFile created on: " + str(x[2]) + "." + str(x[1]) + "." + str(x[0]) + "\n")
                log1_label.config(text="File created on: " + str(x[2]) + "." + str(x[1]) + "." + str(x[0]))
        if uwert == "0toY":
            if not lwert == "client":
                if not os.path.exists(f"{saveloc}/assets_swtor_test_{lwert}_0to{vnummer}.zip") == True:
                    url = f"http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_0to{vnummer}/assets_swtor_test_{lwert}_0to{vnummer}.zip"
                    try:
                        zeitx = int(time.time())
                        sekunden = 0
                        wget.download(url, saveloc, bar=bar_progress)
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            print("\nNo connection. Please try again!")
                            log1_label.config(text="No connection.\nPlease try again!")
                            return
                        else:
                             log1_label.config(text="Version not found!")
                             print("\nVersion not found!\n")
                             return
                ZipFile = zipfile.ZipFile(f"{saveloc}/assets_swtor_test_{lwert}_0to{vnummer}.zip", "r")
                if lwert == "main":
                    x = ZipFile.getinfo("assets_swtor_test_main.version").date_time
                if lwert == "de_de":
                    x = ZipFile.getinfo("assets_swtor_test_de_de.version").date_time
                if lwert == "en_us":
                    x = ZipFile.getinfo("assets_swtor_test_en_us.version").date_time
                if lwert == "fr_fr":
                    x = ZipFile.getinfo("assets_swtor_test_fr_fr.version").date_time
                print("\nFile created on: " + str(x[2]) + "." + str(x[1]) + "." + str(x[0]) + "\n")
                log1_label.config(text="File created on: " + str(x[2]) + "." + str(x[1]) + "." + str(x[0]))
            if lwert == "client":
                if not os.path.exists(f"{saveloc}/retailclient_publictest_0to{vnummer}.zip") == True:
                    url = f"http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_0to{vnummer}/retailclient_publictest_0to{vnummer}.zip"
                    try:
                        zeitx = int(time.time())
                        sekunden = 0
                        wget.download(url, saveloc, bar=bar_progress)
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            print("\nNo connection. Please try again!")
                            log1_label.config(text="No connection.\nPlease try again!")
                            return
                        else:
                             log1_label.config(text="Version not found!")
                             print("\nVersion not found!\n")
                             return
                ZipFile = zipfile.ZipFile(f"{saveloc}/retailclient_publictest_0to{vnummer}.zip", "r")
                x = ZipFile.getinfo("retailclient_publictest.version").date_time
                print("\nFile created on: " + str(x[2]) + "." + str(x[1]) + "." + str(x[0]) + "\n")
                log1_label.config(text="File created on: " + str(x[2]) + "." + str(x[1]) + "." + str(x[0]))
    if vwert == "movies":
        if uwert == "XtoY":
            if not lwert == "main" and not lwert == "client":
                if not os.path.exists(f"{saveloc}/movies_{lwert}_{vnummerx}.zip") == True:
                    url = f"http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_{vnummerx}/movies_{lwert}_{vnummerx}.zip"
                    try:
                        zeitx = int(time.time())
                        sekunden = 0
                        wget.download(url, saveloc, bar=bar_progress)      
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            print("\nNo connection. Please try again!")
                            log1_label.config(text="No connection.\nPlease try again!")
                            return
                        else:
                             log1_label.config(text="Version not found!")
                             print("\nVersion not found!\n")
                             return
                ZipFile = zipfile.ZipFile(f"{saveloc}/movies_{lwert}_{vnummerx}.zip", "r")
                if lwert == "de_de":
                    x = ZipFile.getinfo("movies_de_de.version").date_time
                if lwert == "en_us":
                    x = ZipFile.getinfo("movies_en_us.version").date_time
                if lwert == "fr_fr":
                    x = ZipFile.getinfo("movies_fr_fr.version").date_time
                print("\nFile created on: " + str(x[2]) + "." + str(x[1]) + "." + str(x[0]) + "\n")
                log1_label.config(text="File created on: " + str(x[2]) + "." + str(x[1]) + "." + str(x[0]))
            else:
                log1_label.config(text="Please select a language!")
        if uwert == "0toY":
            if not lwert == "main" and not lwert == "client":
                if not os.path.exists(f"{saveloc}/movies_{lwert}_0to{vnummer}.zip") == True:
                    url = f"http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_0to{vnummer}/movies_{lwert}_0to{vnummer}.zip"
                    try:
                        zeitx = int(time.time())
                        sekunden = 0
                        wget.download(url, saveloc, bar=bar_progress)
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            print("\nNo connection. Please try again!")
                            log1_label.config(text="No connection.\nPlease try again!")
                            return
                        else:
                             log1_label.config(text="Version not found!")
                             print("\nVersion not found!\n")
                             return
                ZipFile = zipfile.ZipFile(f"{saveloc}/movies_{lwert}_0to{vnummer}.zip", "r")
                if lwert == "de_de":
                    x = ZipFile.getinfo("movies_de_de.version").date_time
                if lwert == "en_us":
                    x = ZipFile.getinfo("movies_en_us.version").date_time
                if lwert == "fr_fr":
                    x = ZipFile.getinfo("movies_fr_fr.version").date_time
                print("\nFile created on: " + str(x[2]) + "." + str(x[1]) + "." + str(x[0]) + "\n")
                log1_label.config(text="File created on: " + str(x[2]) + "." + str(x[1]) + "." + str(x[0]))
            else:
                log1_label.config(text="Please select a language!")
            if lwert == "client":
                if not os.path.exists(f"{saveloc}/retailclient_publictest_0to{vnummer}.zip") == True:
                    url = f"http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_0to{vnummer}/retailclient_publictest_0to{vnummer}.zip"
                    try:
                        zeitx = int(time.time())
                        sekunden = 0
                        wget.download(url, saveloc, bar=bar_progress)
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            print("\nNo connection. Please try again!")
                            log1_label.config(text="No connection.\nPlease try again!")
                            return
                        else:
                             log1_label.config(text="Version not found!")
                             print("\nVersion not found!\n")
                             return
                ZipFile = zipfile.ZipFile(f"{saveloc}/retailclient_publictest_0to{vnummer}.zip", "r")
                x = ZipFile.getinfo("retailclient_publictest.version").date_time
                print("\nFile created on: " + str(x[2]) + "." + str(x[1]) + "." + str(x[0]) + "\n")
                log1_label.config(text="File created on: " + str(x[2]) + "." + str(x[1]) + "." + str(x[0]))            
    if vwert == "Live":
        if uwert == "XtoY":
            if not lwert == "client":
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_{vnummerx}.zip") == True:
                    url = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.zip"
                    try:
                        zeitx = int(time.time())
                        sekunden = 0
                        wget.download(url, saveloc, bar=bar_progress)        
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            print("\nNo connection. Please try again!")
                            log1_label.config(text="No connection.\nPlease try again!")
                            return
                        else:
                             log1_label.config(text="Version not found!")
                             print("\nVersion not found!\n")
                             return
                ZipFile = zipfile.ZipFile(f"{saveloc}/assets_swtor_{lwert}_{vnummerx}.zip", "r")
                if lwert == "main":
                    x = ZipFile.getinfo("assets_swtor_main.version").date_time
                if lwert == "de_de":
                    x = ZipFile.getinfo("assets_swtor_de_de.version").date_time
                if lwert == "en_us":
                    x = ZipFile.getinfo("assets_swtor_en_us.version").date_time
                if lwert == "fr_fr":
                    x = ZipFile.getinfo("assets_swtor_fr_fr.version").date_time
                print("\nFile created on: " + str(x[2]) + "." + str(x[1]) + "." + str(x[0]) + "\n")
                log1_label.config(text="File created on: " + str(x[2]) + "." + str(x[1]) + "." + str(x[0]))
            if lwert == "client":
                if not os.path.exists(f"{saveloc}/retailclient_swtor_{vnummerx}.zip") == True:
                    url = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.zip"
                    try:
                        zeitx = int(time.time())
                        sekunden = 0
                        wget.download(url, saveloc, bar=bar_progress)
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            print("\nNo connection. Please try again!")
                            log1_label.config(text="No connection.\nPlease try again!")
                            return
                        else:
                             log1_label.config(text="Version not found!")
                             print("\nVersion not found!\n")
                             return
                ZipFile = zipfile.ZipFile(f"{saveloc}/retailclient_swtor_{vnummerx}.zip", "r")
                x = ZipFile.getinfo("retailclient_swtor.version").date_time
                print("\nFile created on: " + str(x[2]) + "." + str(x[1]) + "." + str(x[0]) + "\n")
                log1_label.config(text="File created on: " + str(x[2]) + "." + str(x[1]) + "." + str(x[0]))
        if uwert == "0toY":
            if not lwert == "client":
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_0to{vnummer}.zip") == True:
                    url = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer}/assets_swtor_{lwert}_0to{vnummer}.zip"
                    try:
                        zeitx = int(time.time())
                        sekunden = 0
                        wget.download(url, saveloc, bar=bar_progress)
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            print("\nNo connection. Please try again!")
                            log1_label.config(text="No connection.\nPlease try again!")
                            return
                        else:
                             log1_label.config(text="Version not found!")
                             print("\nVersion not found!\n")
                             return
                ZipFile = zipfile.ZipFile(f"{saveloc}/assets_swtor_{lwert}_0to{vnummer}.zip", "r")
                if lwert == "main":
                    x = ZipFile.getinfo("assets_swtor_main.version").date_time
                if lwert == "de_de":
                    x = ZipFile.getinfo("assets_swtor_de_de.version").date_time
                if lwert == "en_us":
                    x = ZipFile.getinfo("assets_swtor_en_us.version").date_time
                if lwert == "fr_fr":
                    x = ZipFile.getinfo("assets_swtor_fr_fr.version").date_time
                print("\nFile created on: " + str(x[2]) + "." + str(x[1]) + "." + str(x[0]) + "\n")
                log1_label.config(text="File created on: " + str(x[2]) + "." + str(x[1]) + "." + str(x[0]))
            if lwert == "client":
                if not os.path.exists(f"{saveloc}/retailclient_swtor_0to{vnummer}.zip") == True:
                    url = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer}/retailclient_swtor_0to{vnummer}.zip"
                    try:
                        zeitx = int(time.time())
                        sekunden = 0
                        wget.download(url, saveloc, bar=bar_progress)
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            print("\nNo connection. Please try again!")
                            log1_label.config(text="No connection.\nPlease try again!")
                            return
                        else:
                             log1_label.config(text="Version not found!")
                             print("\nVersion not found!\n")
                             return
                ZipFile = zipfile.ZipFile(f"{saveloc}/retailclient_swtor_0to{vnummer}.zip", "r")
                x = ZipFile.getinfo("retailclient_swtor.version").date_time
                print("\nFile created on: " + str(x[2]) + "." + str(x[1]) + "." + str(x[0]) + "\n")
                log1_label.config(text="File created on: " + str(x[2]) + "." + str(x[1]) + "." + str(x[0]))
    if vwert == "liveqatest":
        if uwert == "0toY":
            if not os.path.exists(f"{saveloc}/retailclient_liveqatest_0to{vnummer}.zip") == True:
                url = f"http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_0to{vnummer}/retailclient_liveqatest_0to{vnummer}.zip"
                try:
                    zeitx = int(time.time())
                    sekunden = 0
                    wget.download(url, saveloc, bar=bar_progress)
                except Exception as ex:
                    exception = type(ex).__name__
                    argumente = str(ex.args)
                    if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                        print("\nNo connection. Please try again!")
                        log1_label.config(text="No connection.\nPlease try again!")
                        return
                    else:
                        log1_label.config(text="Version not found!")
                        print("\nVersion not found!\n")
                        return
            ZipFile = zipfile.ZipFile(f"{saveloc}/retailclient_liveqatest_0to{vnummer}.zip", "r")
            x = ZipFile.getinfo("retailclient_liveqatest.version").date_time
            print("\nFile created on: " + str(x[2]) + "." + str(x[1]) + "." + str(x[0]) + "\n")
            log1_label.config(text="File created on: " + str(x[2]) + "." + str(x[1]) + "." + str(x[0]))
        if uwert == "XtoY":
            if not os.path.exists(f"{saveloc}/retailclient_liveqatest_{vnummerx}.zip") == True:
                url = f"http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_{vnummerx}/retailclient_liveqatest_{vnummerx}.zip"
                try:
                    zeitx = int(time.time())
                    sekunden = 0
                    wget.download(url, saveloc, bar=bar_progress)
                except Exception as ex:
                    exception = type(ex).__name__
                    argumente = str(ex.args)
                    if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                        print("\nNo connection. Please try again!")
                        log1_label.config(text="No connection.\nPlease try again!")
                        return
                    else:
                        log1_label.config(text="Version not found!")
                        print("\nVersion not found!\n")
                        return
            ZipFile = zipfile.ZipFile(f"{saveloc}/retailclient_liveqatest_{vnummerx}.zip", "r")
            x = ZipFile.getinfo("retailclient_liveqatest.version").date_time
            print("\nFile created on: " + str(x[2]) + "." + str(x[1]) + "." + str(x[0]) + "\n")
            log1_label.config(text="File created on: " + str(x[2]) + "." + str(x[1]) + "." + str(x[0]))
    if vwert == "betatest":
        if uwert == "0toY":
            if not os.path.exists(f"{saveloc}/retailclient_betatest_0to{vnummer}.zip") == True:
                url = f"http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_0to{vnummer}/retailclient_betatest_0to{vnummer}.zip"
                try:
                    zeitx = int(time.time())
                    sekunden = 0
                    wget.download(url, saveloc, bar=bar_progress)
                except Exception as ex:
                    exception = type(ex).__name__
                    argumente = str(ex.args)
                    if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                        print("\nNo connection. Please try again!")
                        log1_label.config(text="No connection.\nPlease try again!")
                        return
                    else:
                        log1_label.config(text="Version not found!")
                        print("\nVersion not found!\n")
                        return
            ZipFile = zipfile.ZipFile(f"{saveloc}/retailclient_betatest_0to{vnummer}.zip", "r")
            x = ZipFile.getinfo("retailclient_betatest.version").date_time
            print("\nFile created on: " + str(x[2]) + "." + str(x[1]) + "." + str(x[0]) + "\n")
            log1_label.config(text="File created on: " + str(x[2]) + "." + str(x[1]) + "." + str(x[0]))
        if uwert == "XtoY":
            if not os.path.exists(f"{saveloc}/retailclient_betatest_{vnummerx}.zip") == True:
                url = f"http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_{vnummerx}/retailclient_betatest_{vnummerx}.zip"
                try:
                    zeitx = int(time.time())
                    sekunden = 0
                    wget.download(url, saveloc, bar=bar_progress)
                except Exception as ex:
                    exception = type(ex).__name__
                    argumente = str(ex.args)
                    if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                        print("\nNo connection. Please try again!")
                        log1_label.config(text="No connection.\nPlease try again!")
                        return
                    else:
                        log1_label.config(text="Version not found!")
                        print("\nVersion not found!\n")
                        return
            ZipFile = zipfile.ZipFile(f"{saveloc}/retailclient_betatest_{vnummerx}.zip", "r")
            x = ZipFile.getinfo("retailclient_betatest.version").date_time
            print("\nFile created on: " + str(x[2]) + "." + str(x[1]) + "." + str(x[0]) + "\n")
            log1_label.config(text="File created on: " + str(x[2]) + "." + str(x[1]) + "." + str(x[0]))
    if vwert == "cstraining":
        if uwert == "0toY":
            if not os.path.exists(f"{saveloc}/retailclient_cstraining_0to{vnummer}.zip") == True:
                url = f"http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_0to{vnummer}/retailclient_cstraining_0to{vnummer}.zip"
                try:
                    zeitx = int(time.time())
                    sekunden = 0
                    wget.download(url, saveloc, bar=bar_progress)
                except Exception as ex:
                    exception = type(ex).__name__
                    argumente = str(ex.args)
                    if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                        print("\nNo connection. Please try again!")
                        log1_label.config(text="No connection.\nPlease try again!")
                        return
                    else:
                        log1_label.config(text="Version not found!")
                        print("\nVersion not found!\n")
                        return
            ZipFile = zipfile.ZipFile(f"{saveloc}/retailclient_cstraining_0to{vnummer}.zip", "r")
            x = ZipFile.getinfo("retailclient_cstraining.version").date_time
            print("\nFile created on: " + str(x[2]) + "." + str(x[1]) + "." + str(x[0]) + "\n")
            log1_label.config(text="File created on: " + str(x[2]) + "." + str(x[1]) + "." + str(x[0]))
        if uwert == "XtoY":
            if not os.path.exists(f"{saveloc}/retailclient_cstraining_{vnummerx}.zip") == True:
                url = f"http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_{vnummerx}/retailclient_cstraining_{vnummerx}.zip"
                try:
                    zeitx = int(time.time())
                    sekunden = 0
                    wget.download(url, saveloc, bar=bar_progress)
                except Exception as ex:
                    exception = type(ex).__name__
                    argumente = str(ex.args)
                    if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                        print("\nNo connection. Please try again!")
                        log1_label.config(text="No connection.\nPlease try again!")
                        return
                    else:
                        log1_label.config(text="Version not found!")
                        print("\nVersion not found!\n")
                        return
            ZipFile = zipfile.ZipFile(f"{saveloc}/retailclient_cstraining_{vnummerx}.zip", "r")
            x = ZipFile.getinfo("retailclient_cstraining.version").date_time
            print("\nFile created on: " + str(x[2]) + "." + str(x[1]) + "." + str(x[0]) + "\n")
            log1_label.config(text="File created on: " + str(x[2]) + "." + str(x[1]) + "." + str(x[0]))
    if vwert == "liveeptest":
        if uwert == "0toY":
            if not os.path.exists(f"{saveloc}/retailclient_liveeptest_0to{vnummer}.zip") == True:
                url = f"http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_0to{vnummer}/retailclient_liveeptest_0to{vnummer}.zip"
                try:
                    zeitx = int(time.time())
                    sekunden = 0
                    wget.download(url, saveloc, bar=bar_progress)
                except Exception as ex:
                    exception = type(ex).__name__
                    argumente = str(ex.args)
                    if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                        print("\nNo connection. Please try again!")
                        log1_label.config(text="No connection.\nPlease try again!")
                        return
                    else:
                        log1_label.config(text="Version not found!")
                        print("\nVersion not found!\n")
                        return
            ZipFile = zipfile.ZipFile(f"{saveloc}/retailclient_liveeptest_0to{vnummer}.zip", "r")
            x = ZipFile.getinfo("retailclient_liveeptest.version").date_time
            print("\nFile created on: " + str(x[2]) + "." + str(x[1]) + "." + str(x[0]) + "\n")
            log1_label.config(text="File created on: " + str(x[2]) + "." + str(x[1]) + "." + str(x[0]))
        if uwert == "XtoY":
            if not os.path.exists(f"{saveloc}/retailclient_liveeptest_{vnummerx}.zip") == True:
                url = f"http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_{vnummerx}/retailclient_liveeptest_{vnummerx}.zip"
                try:
                    zeitx = int(time.time())
                    sekunden = 0
                    wget.download(url, saveloc, bar=bar_progress)
                except Exception as ex:
                    exception = type(ex).__name__
                    argumente = str(ex.args)
                    if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                        print("\nNo connection. Please try again!")
                        log1_label.config(text="No connection.\nPlease try again!")
                        return
                    else:
                        log1_label.config(text="Version not found!")
                        print("\nVersion not found!\n")
                        return
            ZipFile = zipfile.ZipFile(f"{saveloc}/retailclient_liveeptest_{vnummerx}.zip", "r")
            x = ZipFile.getinfo("retailclient_liveeptest.version").date_time
            print("\nFile created on: " + str(x[2]) + "." + str(x[1]) + "." + str(x[0]) + "\n")
            log1_label.config(text="File created on: " + str(x[2]) + "." + str(x[1]) + "." + str(x[0]))

def file_save():
    global zeitx
    global sekunden
    folder_selected = filedialog.askdirectory()
    folder_selected = str(folder_selected)
    folder_selected = folder_selected.replace("\\", "/")
    if not folder_selected == "":
        ordnerzeile.delete(0, END)
        ordnerzeile.insert(0, folder_selected)

def button_action():
    global zeitx
    global sekunden
    vwert = varA.get()
    uwert = varB.get()
    lwert = varC.get()
    vnummer = eingabefeld.get()
    saveloc = ordnerzeile.get()
    print(saveloc)
    if not os.path.isdir(saveloc):
        try:
            os.makedirs(saveloc)
        except Exception as e:
            print(e)
    yes = False
    if vnummer == "":
        log1_label.config(text="Please enter the version number,\nyou want to download!")
        return
    if saveloc == "":
        log1_label.config(text="Please enter the location,\nwhere you want to save the files!")
        return
    if vwert == "PTS" and uwert == "XtoY":
        data = {}
        data['version'] = []
        data['version'].append({
        'name': 'PTS'})
        data['build'] = []
        data['build'].append({
            'name': 'XtoY'})
        data['saveto'] = []
        data['saveto'].append({
            'name': saveloc})
        if lwert == "main":
            data['lang'] = []
            data['lang'].append({
                'name': "main"})
        if lwert == "de_de":
            data['lang'] = []
            data['lang'].append({
                'name': "de_de"})
        if lwert == "en_us":
            data['lang'] = []
            data['lang'].append({
                'name': "en_us"})
        if lwert == "fr_fr":
            data['lang'] = []
            data['lang'].append({
                'name': "fr_fr"})
        if lwert == "client":
            data['lang'] = []
            data['lang'].append({
                'name': "client"})
        with open('settings.json', 'w') as outfile:
            json.dump(data, outfile)
    if vwert == "Live" and uwert == "XtoY":
        data = {}
        data['version'] = []
        data['version'].append({
        'name': 'Live'})
        data['build'] = []
        data['build'].append({
            'name': 'XtoY'})
        data['saveto'] = []
        data['saveto'].append({
            'name': saveloc})
        if lwert == "main":
            data['lang'] = []
            data['lang'].append({
                'name': "main"})
        if lwert == "de_de":
            data['lang'] = []
            data['lang'].append({
                'name': "de_de"})
        if lwert == "en_us":
            data['lang'] = []
            data['lang'].append({
                'name': "en_us"})
        if lwert == "fr_fr":
            data['lang'] = []
            data['lang'].append({
                'name': "fr_fr"})
        if lwert == "client":
            data['lang'] = []
            data['lang'].append({
                'name': "client"})
        with open('settings.json', 'w') as outfile:
            json.dump(data, outfile)
    if vwert == "PTS" and uwert == "0toY":
        data = {}
        data['version'] = []
        data['version'].append({
        'name': 'PTS'})
        data['build'] = []
        data['build'].append({
            'name': '0toY'})
        data['saveto'] = []
        data['saveto'].append({
            'name': saveloc})
        if lwert == "main":
            data['lang'] = []
            data['lang'].append({
                'name': "main"})
        if lwert == "de_de":
            data['lang'] = []
            data['lang'].append({
                'name': "de_de"})
        if lwert == "en_us":
            data['lang'] = []
            data['lang'].append({
                'name': "en_us"})
        if lwert == "fr_fr":
            data['lang'] = []
            data['lang'].append({
                'name': "fr_fr"})
        if lwert == "client":
            data['lang'] = []
            data['lang'].append({
                'name': "client"})
        with open('settings.json', 'w') as outfile:
            json.dump(data, outfile)
    if vwert == "Live" and uwert == "0toY":
        data = {}
        data['version'] = []
        data['version'].append({
        'name': 'Live'})
        data['build'] = []
        data['build'].append({
            'name': '0toY'})
        data['saveto'] = []
        data['saveto'].append({
            'name': saveloc})
        if lwert == "main":
            data['lang'] = []
            data['lang'].append({
                'name': "main"})
        if lwert == "de_de":
            data['lang'] = []
            data['lang'].append({
                'name': "de_de"})
        if lwert == "en_us":
            data['lang'] = []
            data['lang'].append({
                'name': "en_us"})
        if lwert == "fr_fr":
            data['lang'] = []
            data['lang'].append({
                'name': "fr_fr"})
        if lwert == "client":
            data['lang'] = []
            data['lang'].append({
                'name': "client"})
        with open('settings.json', 'w') as outfile:
            json.dump(data, outfile)
    if vwert == "movies" and uwert == "XtoY":
        data = {}
        data['version'] = []
        data['version'].append({
        'name': 'movies'})
        data['build'] = []
        data['build'].append({
            'name': 'XtoY'})
        data['saveto'] = []
        data['saveto'].append({
            'name': saveloc})
        if lwert == "main":
            data['lang'] = []
            data['lang'].append({
                'name': "main"})
        if lwert == "de_de":
            data['lang'] = []
            data['lang'].append({
                'name': "de_de"})
        if lwert == "en_us":
            data['lang'] = []
            data['lang'].append({
                'name': "en_us"})
        if lwert == "fr_fr":
            data['lang'] = []
            data['lang'].append({
                'name': "fr_fr"})
        if lwert == "client":
            data['lang'] = []
            data['lang'].append({
                'name': "client"})
        with open('settings.json', 'w') as outfile:
            json.dump(data, outfile)
    if vwert == "movies" and uwert == "0toY":
        data = {}
        data['version'] = []
        data['version'].append({
        'name': 'movies'})
        data['build'] = []
        data['build'].append({
            'name': '0toY'})
        data['saveto'] = []
        data['saveto'].append({
            'name': saveloc})
        if lwert == "main":
            data['lang'] = []
            data['lang'].append({
                'name': "main"})
        if lwert == "de_de":
            data['lang'] = []
            data['lang'].append({
                'name': "de_de"})
        if lwert == "en_us":
            data['lang'] = []
            data['lang'].append({
                'name': "en_us"})
        if lwert == "fr_fr":
            data['lang'] = []
            data['lang'].append({
                'name': "fr_fr"})
        if lwert == "client":
            data['lang'] = []
            data['lang'].append({
                'name': "client"})
        with open('settings.json', 'w') as outfile:
            json.dump(data, outfile)
    if "." in vnummer:
        if vwert == "Live":
            for i in range(len(items)):
                if str(vnummer) == str(items[i][0]):
                    yes = True
                    yes1 = i
                    if lwert == "main":
                        ww = 2
                    if lwert == "client":
                        ww = 3
                    if lwert == "en_us":
                        ww = 4
                    if lwert == "de_de":
                        ww = 5
                    if lwert == "fr_fr":
                        ww = 6
                    break
            try:
                yes1 = yes1
            except:
                print("\nVersion not found!")
                log1_label.config(text="Version not found!")
                return
        else:
            print("\nYou can only use version numbers for Live-versions! Please use version IDs instead.")
            log1_label.config(text="Error! See console.")
            return
    if yes:
        vnummer2 = items[yes1][ww]
        if uwert == "XtoY":
            vnummer1 = int(vnummer2) - 1
            vnummerx = f"{vnummer1}to{vnummer2}"
            download_files(saveloc, lwert, vnummerx, vwert, vnummer)
            return
        if uwert == "0toY":
            download_files0(saveloc, lwert, vnummer, vwert, vnummer2)
            return
    
    vnummer2 = int(vnummer) -1
    vnummerx = str(vnummer2) + "to" + str(vnummer)
    if vwert == "PTS":
        if uwert == "XtoY":
            download_files_pts(saveloc, lwert, vnummerx, vwert, vnummer)
            return
        if uwert == "0toY":
            download_files0_pts(saveloc, lwert, vnummerx, vwert, vnummer)
            return
    if vwert == "movies":
        if uwert == "XtoY":
            download_movies(saveloc, lwert, vnummerx, vwert, vnummer)
            return
        if uwert == "0toY":
            download_movies0(saveloc, lwert, vnummerx, vwert, vnummer)
            return
    if vwert == "Live":
        if uwert == "XtoY":
            download_files(saveloc, lwert, vnummerx, vwert, vnummer)
            return
        if uwert == "0toY":
            download_files0(saveloc, lwert, vnummerx, vwert, vnummer)
            return
    if vwert == "liveqatest":
        if uwert == "0toY":
            download_exp_client0(saveloc, lwert, vnummerx, vwert, vnummer, vwert)
            return
        if uwert == "XtoY":
            download_exp_client(saveloc, lwert, vnummerx, vwert, vnummer, vwert)
            return
    if vwert == "betatest":
        if uwert == "0toY":
            download_exp_client0(saveloc, lwert, vnummerx, vwert, vnummer, vwert)
            return
        if uwert == "XtoY":
            download_exp_client(saveloc, lwert, vnummerx, vwert, vnummer, vwert)
            return
    if vwert == "cstraining":
        if uwert == "0toY":
            download_exp_client0(saveloc, lwert, vnummerx, vwert, vnummer, vwert)
            return
        if uwert == "XtoY":
            download_exp_client(saveloc, lwert, vnummerx, vwert, vnummer, vwert)
            return
    if vwert == "liveeptest":
        if uwert == "0toY":
            download_exp_client0(saveloc, lwert, vnummerx, vwert, vnummer, vwert)
            return
        if uwert == "XtoY":
            download_exp_client(saveloc, lwert, vnummerx, vwert, vnummer, vwert)
            return
        
xml = xml.dom.minidom.parse("patches.xml")
itemlist = xml.getElementsByTagName('patch')
items = []
for s in itemlist:
    itemsx = []
    itemsx.append(s.attributes['version'].value)
    itemsx.append(s.attributes['date'].value)
    itemsx.append(s.attributes['assets_swtor_main'].value)
    itemsx.append(s.attributes['retailclient_swtor'].value)
    itemsx.append(s.attributes['assets_swtor_en_us'].value)
    itemsx.append(s.attributes['assets_swtor_de_de'].value)
    itemsx.append(s.attributes['assets_swtor_fr_fr'].value)
    items.append(itemsx)

fenster = tkr.Tk()
fenster.title("SWTOR Patch Downloader")
fenster.geometry("430x480")
fenster.resizable(False, False)
ordnerzeile = tkr.Entry(fenster,width=42)

with open('settings.json') as json_file:
    data = json.load(json_file)
    for p in data['version']:
        if p["name"] == "PTS":
            ptsorlive = "PTS"
        if p["name"] == "Live":
            ptsorlive = "Live"
        if p["name"] == "movies":
            ptsorlive = "movies"
    for p in data['build']:
        if p["name"] == "XtoY":
            xtoxy = "XtoY"
        if p["name"] == "0toY":
            xtoxy = "0toY"
    for p in data['lang']:
        if p["name"] == "main":
            langf = "main"
        if p["name"] == "de_de":
            langf = "de_de"
        if p["name"] == "en_us":
            langf = "en_us"
        if p["name"] == "fr_fr":
            langf = "fr_fr"
        if p["name"] == "client":
            langf = "client"
    for p in data['saveto']:
        ps = str(p)
        ps = ps.replace("{'name': '", "")
        ps = ps.replace("'}", "")
        ordnerzeile.insert(0, ps)

welcome_label = tkr.Label(fenster)
log1_label = tkr.Label(fenster)

welcom_button = tkr.Button(fenster, text="Download Files", command=button_action, bd=3)
manbutton = tkr.Button(fenster, text="Download Manifest", command=dl_man, bd=3)
solidbutton = tkr.Button(fenster, text="Download Solidpkg", command=dl_solid, bd=3)
my_label = tkr.Label(fenster, text="  SWTOR Patch Downloader", font=('ARIAL', 10, 'bold'))
my_label2 = tkr.Label(fenster, text="Select the Patch Variant: ")
my_label3 = tkr.Label(fenster, text="Type the version number Y: ")
my_label4 = tkr.Label(fenster, text="Select the File Type: ")
my_label5 = tkr.Label(fenster, text="Choose the saving location: ")

A1 = "Live"
A2 = "PTS"
A3 = "movies"
A4 = "liveqatest"
A5 = "betatest"
A6 = "cstraining"
A7 = "liveeptest"
varA = tkr.StringVar()
varA.set(ptsorlive)
with open('devmode.json') as json_file:
    data = json.load(json_file)
    for p in data['devmode']:
        if p["name"] == "true":
            set1 = tkr.OptionMenu(fenster,varA,A1,A2,A3,A4,A5,A6,A7)
        else:
            set1 = tkr.OptionMenu(fenster,varA,A1,A2,A3)
set1.configure(font=("Arial",25))


B1 = "XtoY"
B2 = "0toY"
varB = tkr.StringVar()
varB.set(xtoxy)
set2 = tkr.OptionMenu(fenster,varB,B1,B2)
set2.configure(font=("Arial",25))

C1 = "main"
C2 = "client"
C3 = "en_us"
C4 = "de_de"
C5 = "fr_fr"
varC = tkr.StringVar()
varC.set(langf)
set3 = tkr.OptionMenu(fenster,varC,C1,C2,C3,C4,C5)
set3.configure(font=("Arial",25))

eingabefeld = tkr.Entry(fenster,width=5)
        

save_button = tkr.Button(fenster, text="Select Directory", command=file_save)
exit_button = tkr.Button(fenster, text="See creation date", command=check_date, bd=3)

my_label.place(x=110, y=5) 
my_label2.place(x=23, y=175) 
my_label3.place(x=23, y=240) 
my_label4.place(x=23, y=115)
my_label5.place(x=23, y=270)
eingabefeld.place(x=275, y=240)
save_button.place(x=45, y=300)
ordnerzeile.place(x=155, y=303)
welcom_button.place(x=40, y=355)
manbutton.place(x=40, y=400)
solidbutton.place(x=275, y=400)
exit_button.place(x=275, y=355)
log1_label.place(x=40, y=440)
set1.place(x=155, y=35) 
set3.place(x=250, y=100)
set2.place(x=250, y=165)

log1_label.config(text="Ready!")

tkr.mainloop()
