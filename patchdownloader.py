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
                        wget.download(url, saveloc)
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
                        wget.download(url, saveloc)
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
                        wget.download(url, saveloc)
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
                        wget.download(url, saveloc)
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
                        wget.download(url, saveloc)
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
                    wget.download(url, saveloc)
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
                    wget.download(url, saveloc)
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
                    wget.download(url, saveloc)
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
                    wget.download(url, saveloc)
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
                            wget.download(url, saveloc)
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
                            wget.download(url, saveloc)
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
                            wget.download(url, saveloc)
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
                            wget.download(url, saveloc)
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
                            wget.download(url, saveloc)
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
                            wget.download(url, saveloc)
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
                            wget.download(url, saveloc)
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
                            wget.download(url, saveloc)
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
                            wget.download(url, saveloc)
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
                            wget.download(url, saveloc)
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
                            wget.download(url, saveloc)
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
                            wget.download(url, saveloc)
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
                        wget.download(url, saveloc)
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
                        wget.download(url, saveloc)
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
                        wget.download(url, saveloc)
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
                        wget.download(url, saveloc)
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
                        wget.download(url, saveloc)
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
                        wget.download(url, saveloc)
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
                        wget.download(url, saveloc)
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
                        wget.download(url, saveloc)
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
                            wget.download(url, saveloc)
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
                            wget.download(url, saveloc)
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
                        wget.download(url, saveloc)
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
                        wget.download(url, saveloc)
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
                        wget.download(url, saveloc)
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
                        wget.download(url, saveloc)
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
                        wget.download(url, saveloc)      
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
                        wget.download(url, saveloc)
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
                        wget.download(url, saveloc)
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
                        wget.download(url, saveloc)        
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
                        wget.download(url, saveloc)
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
                        wget.download(url, saveloc)
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
                        wget.download(url, saveloc)
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
                    print(url)
                    wget.download(url, saveloc)
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
                    wget.download(url, saveloc)
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
                    wget.download(url, saveloc)
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
                    wget.download(url, saveloc)
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
                    wget.download(url, saveloc)
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
                    wget.download(url, saveloc)
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
                    wget.download(url, saveloc)
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
                    wget.download(url, saveloc)
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
    folder_selected = filedialog.askdirectory()
    folder_selected = str(folder_selected)
    folder_selected = folder_selected.replace("\\", "/")
    if not folder_selected == "":
        ordnerzeile.delete(0, END)
        ordnerzeile.insert(0, folder_selected)

def button_action():
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
        if uwert == "XtoY":
            if not lwert == "client":
                print(f"Download of {vwert} version {vnummerx} started! ({vnummer})\nPress CTRL+C to stop.")
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_{vnummerx}.zip") == True:
                    url = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.zip"
                    try:
                        wget.download(url, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.zip\n")
                    except KeyboardInterrupt:
                        print("\nYou stopped the download!")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            print("\nNo Connection. Please try again!")
                            log1_label.config(text="No connection.\nPlease try again!")
                            return
                        else:
                            log1_label.config(text="Version not found!")
                            print("\nVersion not found!\n")
                            return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_{vnummerx}.z01") == True:
                    url2 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z01"
                    while True:
                        try:
                            wget.download(url2, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z01\n")
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
                                log1_label.config(text="Download finished!xy")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_{vnummerx}.z02") == True:
                    url3 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z02"
                    while True:
                        try:
                            wget.download(url3, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z02\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_{vnummerx}.z03") == True:
                    url4 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z03"
                    while True:
                        try:
                            wget.download(url4, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z03\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_{vnummerx}.z04") == True:
                    url5 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z04"
                    while True:
                        try:
                            wget.download(url5, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z04\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_{vnummerx}.z05") == True:
                    url6 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z05"
                    while True:
                        try:
                            wget.download(url6, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z05\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_{vnummerx}.z06") == True:
                    url7 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z06"
                    while True:
                        try:
                            wget.download(url7, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z06\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_{vnummerx}.z07") == True:
                    url8 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z07"
                    while True:
                        try:
                            wget.download(url8, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z07\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_{vnummerx}.z08") == True:
                    url9 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z08"
                    while True:
                        try:
                            wget.download(url9, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z08\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_{vnummerx}.z09") == True:
                    url10 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z09"
                    while True:
                        try:
                            wget.download(url10, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z09\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_{vnummerx}.z10") == True:
                    url11 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z10"
                    while True:
                        try:
                            wget.download(url11, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z10\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_{vnummerx}.z11") == True:
                    url12 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z11"
                    while True:
                        try:
                            wget.download(url12, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z11\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_{vnummerx}.z12") == True:
                    url13 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z12"
                    while True:
                        try:
                            wget.download(url13, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z12\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_{vnummerx}.z13") == True:
                    url14 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z13"
                    while True:
                        try:
                            wget.download(url14, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z13\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_{vnummerx}.z14") == True:
                    url15 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z14"
                    while True:
                        try:
                            wget.download(url15, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z14\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_{vnummerx}.z15") == True:
                    url16 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z15"
                    while True:
                        try:
                            wget.download(url16, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z15\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_{vnummerx}.z16") == True:
                    url17 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z16"
                    while True:
                        try:
                            wget.download(url17, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z16\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_{vnummerx}.z17") == True:
                    url18 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z17"
                    while True:
                        try:
                            wget.download(url18, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z17\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_{vnummerx}.z18") == True:
                    url19 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z18"
                    while True:
                        try:
                            wget.download(url19, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z18\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_{vnummerx}.z19") == True:
                    url20 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z19"
                    while True:
                        try:
                            wget.download(url20, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z19\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_{vnummerx}.z20") == True:
                    url21 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z20"
                    while True:
                        try:
                            wget.download(url21, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z20\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                log1_label.config(text="Download finished!")
                print("Download finished!\n")
            if lwert == "client":
                print(f"Download of {vwert} {lwert} version {vnummerx} started! ({vnummer})\nPress CTRL+C to stop.")
                if not os.path.exists(f"{saveloc}/retailclient_swtor_{vnummerx}.zip") == True:
                    url = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.zip"
                    try:
                        wget.download(url, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.zip\n")
                    except KeyboardInterrupt:
                        print("\nYou stopped the download!")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            print("\nNo Connection. Please try again!")
                            log1_label.config(text="No connection.\nPlease try again!")
                            return
                        else:
                            log1_label.config(text="Version not found!")
                            print("\nVersion not found!\n")
                            return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_{vnummerx}.z01") == True:
                    url2 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z01"
                    while True:
                        try:
                            wget.download(url2, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z01\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_{vnummerx}.z02") == True:
                    url3 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z02"
                    while True:
                        try:
                            wget.download(url3, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z02\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_{vnummerx}.z03") == True:
                    url4 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z03"
                    while True:
                        try:
                            wget.download(url4, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z03\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_{vnummerx}.z04") == True:
                    url5 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z04"
                    while True:
                        try:
                            wget.download(url5, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z04\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_{vnummerx}.z05") == True:
                    url6 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z05"
                    while True:
                        try:
                            wget.download(url6, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z05\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_{vnummerx}.z06") == True:
                    url7 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z06"
                    while True:
                        try:
                            wget.download(url7, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z06\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_{vnummerx}.z07") == True:
                    url8 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z07"
                    while True:
                        try:
                            wget.download(url8, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z07\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_{vnummerx}.z08") == True:
                    url9 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z08"
                    while True:
                        try:
                            wget.download(url9, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z08\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_{vnummerx}.z09") == True:
                    url10 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z09"
                    while True:
                        try:
                            wget.download(url10, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z09\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_{vnummerx}.z10") == True:
                    url11 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z10"
                    while True:
                        try:
                            wget.download(url11, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z10\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_{vnummerx}.z11") == True:
                    url12 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z11"
                    while True:
                        try:
                            wget.download(url12, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z11\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_{vnummerx}.z12") == True:
                    url13 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z12"
                    while True:
                        try:
                            wget.download(url13, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z12\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_{vnummerx}.z13") == True:
                    url14 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z13"
                    while True:
                        try:
                            wget.download(url14, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z13\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_{vnummerx}.z14") == True:
                    url15 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z14"
                    while True:
                        try:
                            wget.download(url15, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z14\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_{vnummerx}.z15") == True:
                    url16 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z15"
                    while True:
                        try:
                            wget.download(url16, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z15\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_{vnummerx}.z16") == True:
                    url17 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z16"
                    while True:
                        try:
                            wget.download(url17, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z16\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_{vnummerx}.z17") == True:
                    url18 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z17"
                    while True:
                        try:
                            wget.download(url18, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z17\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_{vnummerx}.z18") == True:
                    url19 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z18"
                    while True:
                        try:
                            wget.download(url19, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z18\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_{vnummerx}.z19") == True:
                    url20 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z19"
                    while True:
                        try:
                            wget.download(url20, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z19\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_{vnummerx}.z20") == True:
                    url21 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z20"
                    while True:
                        try:
                            wget.download(url21, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z20\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                log1_label.config(text="Download finished!")
                print("Download finished!\n")
        if uwert == "0toY":
            if not lwert == "client":
                print(f"Download of {vwert} version 0to{vnummer2} started! ({vnummer})\nPress CTRL+C to stop.")
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_0to{vnummer2}.zip") == True:
                    url = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer2}/assets_swtor_{lwert}_0to{vnummer2}.zip"
                    try:
                        wget.download(url, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer2}/assets_swtor_{lwert}_0to{vnummer2}.zip\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_0to{vnummer2}.z01") == True:
                    url2 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer2}/assets_swtor_{lwert}_0to{vnummer2}.z01"
                    while True:
                        try:
                            wget.download(url2, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer2}/assets_swtor_{lwert}_0to{vnummer2}.z01\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_0to{vnummer2}.z02") == True:
                    url3 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer2}/assets_swtor_{lwert}_0to{vnummer2}.z02"
                    while True:
                        try:
                            wget.download(url3, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer2}/assets_swtor_{lwert}_0to{vnummer2}.z02\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_0to{vnummer2}.z03") == True:
                    url4 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer2}/assets_swtor_{lwert}_0to{vnummer2}.z03"
                    while True:
                        try:
                            wget.download(url4, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer2}/assets_swtor_{lwert}_0to{vnummer2}.z03\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_0to{vnummer2}.z04") == True:
                    url5 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer2}/assets_swtor_{lwert}_0to{vnummer2}.z04"
                    while True:
                        try:
                            wget.download(url5, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer2}/assets_swtor_{lwert}_0to{vnummer2}.z04\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_0to{vnummer2}.z05") == True:
                    url6 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer2}/assets_swtor_{lwert}_0to{vnummer2}.z05"
                    while True:
                        try:
                            wget.download(url6, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer2}/assets_swtor_{lwert}_0to{vnummer2}.z05\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_0to{vnummer2}.z06") == True:
                    url7 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer2}/assets_swtor_{lwert}_0to{vnummer2}.z06"
                    while True:
                        try:
                            wget.download(url7, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer2}/assets_swtor_{lwert}_0to{vnummer2}.z06\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_0to{vnummer2}.z07") == True:
                    url8 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer2}/assets_swtor_{lwert}_0to{vnummer2}.z07"
                    while True:
                        try:
                            wget.download(url8, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer2}/assets_swtor_{lwert}_0to{vnummer2}.z07\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_0to{vnummer2}.z08") == True:
                    url9 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer2}/assets_swtor_{lwert}_0to{vnummer2}.z08"
                    while True:
                        try:
                            wget.download(url9, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer2}/assets_swtor_{lwert}_0to{vnummer2}.z08\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_0to{vnummer2}.z09") == True:
                    url10 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer2}/assets_swtor_{lwert}_0to{vnummer2}.z09"
                    while True:
                        try:
                            wget.download(url10, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer2}/assets_swtor_{lwert}_0to{vnummer2}.z09\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_0to{vnummer2}.z10") == True:
                    url11 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer2}/assets_swtor_{lwert}_0to{vnummer2}.z10"
                    while True:
                        try:
                            wget.download(url11, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer2}/assets_swtor_{lwert}_0to{vnummer2}.z10\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_0to{vnummer2}.z11") == True:
                    url12 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer2}/assets_swtor_{lwert}_0to{vnummer2}.z11"
                    while True:
                        try:
                            wget.download(url12, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer2}/assets_swtor_{lwert}_0to{vnummer2}.z11\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_0to{vnummer2}.z12") == True:
                    url13 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer2}/assets_swtor_{lwert}_0to{vnummer2}.z12"
                    while True:
                        try:
                            wget.download(url13, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer2}/assets_swtor_{lwert}_0to{vnummer2}.z12\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_0to{vnummer2}.z13") == True:
                    url14 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer2}/assets_swtor_{lwert}_0to{vnummer2}.z13"
                    while True:
                        try:
                            wget.download(url14, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer2}/assets_swtor_{lwert}_0to{vnummer2}.z13\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_0to{vnummer2}.z14") == True:
                    url15 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer2}/assets_swtor_{lwert}_0to{vnummer2}.z14"
                    while True:
                        try:
                            wget.download(url15, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer2}/assets_swtor_{lwert}_0to{vnummer2}.z14\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_0to{vnummer2}.z15") == True:
                    url16 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer2}/assets_swtor_{lwert}_0to{vnummer2}.z15"
                    while True:
                        try:
                            wget.download(url16, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer2}/assets_swtor_{lwert}_0to{vnummer2}.z15\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_0to{vnummer2}.z16") == True:
                    url17 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer2}/assets_swtor_{lwert}_0to{vnummer2}.z16"
                    while True:
                        try:
                            wget.download(url17, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer2}/assets_swtor_{lwert}_0to{vnummer2}.z16\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_0to{vnummer2}.z17") == True:
                    url18 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer2}/assets_swtor_{lwert}_0to{vnummer2}.z17"
                    while True:
                        try:
                            wget.download(url18, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer2}/assets_swtor_{lwert}_0to{vnummer2}.z17\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_0to{vnummer2}.z18") == True:
                    url19 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer2}/assets_swtor_{lwert}_0to{vnummer2}.z18"
                    while True:
                        try:
                            wget.download(url19, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer2}/assets_swtor_{lwert}_0to{vnummer2}.z18\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_0to{vnummer2}.z19") == True:
                    url20 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer2}/assets_swtor_{lwert}_0to{vnummer2}.z19"
                    while True:
                        try:
                            wget.download(url20, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer2}/assets_swtor_{lwert}_0to{vnummer2}.z19\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_0to{vnummer2}.z20") == True:
                    url21 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer2}/assets_swtor_{lwert}_0to{vnummer2}.z20"
                    while True:
                        try:
                            wget.download(url21, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer2}/assets_swtor_{lwert}_0to{vnummer2}.z20\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                log1_label.config(text="Download finished!")
                print("Download finished!\n")
            if lwert == "client":
                print(f"Download of {vwert} {lwert} version 0to{vnummer2} started! ({vnummer})\nPress CTRL+C to stop.")
                if not os.path.exists(f"{saveloc}/retailclient_swtor_0to{vnummer2}.zip") == True:
                    url = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer2}/retailclient_swtor_0to{vnummer2}.zip"
                    try:
                        wget.download(url, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer2}/retailclient_swtor_0to{vnummer2}.zip\n")
                    except KeyboardInterrupt:
                        print("\nYou stopped the download!")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            print("\nNo Connection. Please try again!")
                            log1_label.config(text="No connection.\nPlease try again!")
                            return
                        else:
                            log1_label.config(text="Version not found!")
                            print("\nVersion not found!\n")
                            return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_0to{vnummer2}.z01") == True:
                    url2 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer2}/retailclient_swtor_0to{vnummer2}.z01"
                    while True:
                        try:
                            wget.download(url2, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer2}/retailclient_swtor_0to{vnummer2}.z01\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_0to{vnummer2}.z02") == True:
                    url3 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer2}/retailclient_swtor_0to{vnummer2}.z02"
                    while True:
                        try:
                            wget.download(url3, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer2}/retailclient_swtor_0to{vnummer2}.z02\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_0to{vnummer2}.z03") == True:
                    url4 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer2}/retailclient_swtor_0to{vnummer2}.z03"
                    while True:
                        try:
                            wget.download(url4, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer2}/retailclient_swtor_0to{vnummer2}.z03\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_0to{vnummer2}.z04") == True:
                    url5 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer2}/retailclient_swtor_0to{vnummer2}.z04"
                    while True:
                        try:
                            wget.download(url5, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer2}/retailclient_swtor_0to{vnummer2}.z04\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_0to{vnummer2}.z05") == True:
                    url6 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer2}/retailclient_swtor_0to{vnummer2}.z05"
                    while True:
                        try:
                            wget.download(url6, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer2}/retailclient_swtor_0to{vnummer2}.z05\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_0to{vnummer2}.z06") == True:
                    url7 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer2}/retailclient_swtor_0to{vnummer2}.z06"
                    while True:
                        try:
                            wget.download(url7, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer2}/retailclient_swtor_0to{vnummer2}.z06\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_0to{vnummer2}.z07") == True:
                    url8 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer2}/retailclient_swtor_0to{vnummer2}.z07"
                    while True:
                        try:
                            wget.download(url8, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer2}/retailclient_swtor_0to{vnummer2}.z07\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_0to{vnummer2}.z08") == True:
                    url9 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer2}/retailclient_swtor_0to{vnummer2}.z08"
                    while True:
                        try:
                            wget.download(url9, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer2}/retailclient_swtor_0to{vnummer2}.z08\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_0to{vnummer2}.z09") == True:
                    url10 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer2}/retailclient_swtor_0to{vnummer2}.z09"
                    while True:
                        try:
                            wget.download(url10, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer2}/retailclient_swtor_0to{vnummer2}.z09\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_0to{vnummer2}.z10") == True:
                    url11 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer2}/retailclient_swtor_0to{vnummer2}.z10"
                    while True:
                        try:
                            wget.download(url11, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer2}/retailclient_swtor_0to{vnummer2}.z10\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_0to{vnummer2}.z11") == True:
                    url12 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer2}/retailclient_swtor_0to{vnummer2}.z11"
                    while True:
                        try:
                            wget.download(url12, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer2}/retailclient_swtor_0to{vnummer2}.z11\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_0to{vnummer2}.z12") == True:
                    url13 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer2}/retailclient_swtor_0to{vnummer2}.z12"
                    while True:
                        try:
                            wget.download(url13, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer2}/retailclient_swtor_0to{vnummer2}.z12\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_0to{vnummer2}.z13") == True:
                    url14 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer2}/retailclient_swtor_0to{vnummer2}.z13"
                    while True:
                        try:
                            wget.download(url14, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer2}/retailclient_swtor_0to{vnummer2}.z13\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_0to{vnummer2}.z14") == True:
                    url15 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer2}/retailclient_swtor_0to{vnummer2}.z14"
                    while True:
                        try:
                            wget.download(url15, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer2}/retailclient_swtor_0to{vnummer2}.z14\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_0to{vnummer2}.z15") == True:
                    url16 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer2}/retailclient_swtor_0to{vnummer2}.z15"
                    while True:
                        try:
                            wget.download(url16, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer2}/retailclient_swtor_0to{vnummer2}.z15\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_0to{vnummer2}.z16") == True:
                    url17 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer2}/retailclient_swtor_0to{vnummer2}.z16"
                    while True:
                        try:
                            wget.download(url17, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer2}/retailclient_swtor_0to{vnummer2}.z16\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_0to{vnummer2}.z17") == True:
                    url18 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer2}/retailclient_swtor_0to{vnummer2}.z17"
                    while True:
                        try:
                            wget.download(url18, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer2}/retailclient_swtor_0to{vnummer2}.z17\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_0to{vnummer2}.z18") == True:
                    url19 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer2}/retailclient_swtor_0to{vnummer2}.z18"
                    while True:
                        try:
                            wget.download(url19, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer2}/retailclient_swtor_0to{vnummer2}.z18\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_0to{vnummer2}.z19") == True:
                    url20 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer2}/retailclient_swtor_0to{vnummer2}.z19"
                    while True:
                        try:
                            wget.download(url20, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer2}/retailclient_swtor_0to{vnummer2}.z19\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_0to{vnummer2}.z20") == True:
                    url21 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer2}/retailclient_swtor_0to{vnummer2}.z20"
                    while True:
                        try:
                            wget.download(url21, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer2}/retailclient_swtor_0to{vnummer2}.z20\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                log1_label.config(text="Download finished!")
                print("Download finished!\n")
    
    vnummer2 = int(vnummer) -1
    vnummerx = str(vnummer2) + "to" + str(vnummer)
    if vwert == "PTS":
        if uwert == "XtoY":
            if not lwert == "client":
                print(f"Download of {vwert} {lwert} version {vnummerx} started!\nPress CTRL+C to stop.")
                if not os.path.exists(f"{saveloc}/assets_swtor_test_{lwert}_{vnummerx}.zip") == True:
                    url = f"http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_{vnummerx}/assets_swtor_test_{lwert}_{vnummerx}.zip"
                    try:
                        wget.download(url, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_{vnummerx}/assets_swtor_test_{lwert}_{vnummerx}.zip\n")
                    except KeyboardInterrupt:
                        print("\nYou stopped the download!")
                        return
                    except Exception as ex:
                        print(ex)
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
                if not os.path.exists(f"{saveloc}/assets_swtor_test_{lwert}_{vnummerx}.z01") == True:
                    url2 = f"http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_{vnummerx}/assets_swtor_test_{lwert}_{vnummerx}.z01"
                    while True:
                        try:
                            wget.download(url2, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_{vnummerx}/assets_swtor_test_{lwert}_{vnummerx}.z01\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_test_{lwert}_{vnummerx}.z02") == True:
                    url3 = f"http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_{vnummerx}/assets_swtor_test_{lwert}_{vnummerx}.z02"
                    while True:
                        try:
                            wget.download(url3, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_{vnummerx}/assets_swtor_test_{lwert}_{vnummerx}.z02\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_test_{lwert}_{vnummerx}.z03") == True:
                    url4 = f"http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_{vnummerx}/assets_swtor_test_{lwert}_{vnummerx}.z03"
                    while True:
                        try:
                            wget.download(url4, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_{vnummerx}/assets_swtor_test_{lwert}_{vnummerx}.z03\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_test_{lwert}_{vnummerx}.z04") == True:
                    url5 = f"http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_{vnummerx}/assets_swtor_test_{lwert}_{vnummerx}.z04"
                    while True:
                        try:
                            wget.download(url5, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_{vnummerx}/assets_swtor_test_{lwert}_{vnummerx}.z04\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_test_{lwert}_{vnummerx}.z05") == True:
                    url6 = f"http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_{vnummerx}/assets_swtor_test_{lwert}_{vnummerx}.z05"
                    while True:
                        try:
                            wget.download(url6, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_{vnummerx}/assets_swtor_test_{lwert}_{vnummerx}.z05\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_test_{lwert}_{vnummerx}.z06") == True:
                    url7 = f"http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_{vnummerx}/assets_swtor_test_{lwert}_{vnummerx}.z06"
                    while True:
                        try:
                            wget.download(url7, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_{vnummerx}/assets_swtor_test_{lwert}_{vnummerx}.z06\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_test_{lwert}_{vnummerx}.z07") == True:
                    url8 = f"http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_{vnummerx}/assets_swtor_test_{lwert}_{vnummerx}.z07"
                    while True:
                        try:
                            wget.download(url8, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_{vnummerx}/assets_swtor_test_{lwert}_{vnummerx}.z07\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_test_{lwert}_{vnummerx}.z08") == True:
                    url9 = f"http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_{vnummerx}/assets_swtor_test_{lwert}_{vnummerx}.z08"
                    while True:
                        try:
                            wget.download(url9, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_{vnummerx}/assets_swtor_test_{lwert}_{vnummerx}.z08\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_test_{lwert}_{vnummerx}.z09") == True:
                    url10 = f"http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_{vnummerx}/assets_swtor_test_{lwert}_{vnummerx}.z09"
                    while True:
                        try:
                            wget.download(url10, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_{vnummerx}/assets_swtor_test_{lwert}_{vnummerx}.z09\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_test_{lwert}_{vnummerx}.z10") == True:
                    url11 = f"http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_{vnummerx}/assets_swtor_test_{lwert}_{vnummerx}.z10"
                    while True:
                        try:
                            wget.download(url11, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_{vnummerx}/assets_swtor_test_{lwert}_{vnummerx}.z10\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_test_{lwert}_{vnummerx}.z11") == True:
                    url12 = f"http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_{vnummerx}/assets_swtor_test_{lwert}_{vnummerx}.z11"
                    while True:
                        try:
                            wget.download(url12, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_{vnummerx}/assets_swtor_test_{lwert}_{vnummerx}.z11\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_test_{lwert}_{vnummerx}.z12") == True:
                    url13 = f"http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_{vnummerx}/assets_swtor_test_{lwert}_{vnummerx}.z12"
                    while True:
                        try:
                            wget.download(url13, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_{vnummerx}/assets_swtor_test_{lwert}_{vnummerx}.z12\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_test_{lwert}_{vnummerx}.z13") == True:
                    url14 = f"http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_{vnummerx}/assets_swtor_test_{lwert}_{vnummerx}.z13"
                    while True:
                        try:
                            wget.download(url14, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_{vnummerx}/assets_swtor_test_{lwert}_{vnummerx}.z13\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_test_{lwert}_{vnummerx}.z14") == True:
                    url15 = f"http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_{vnummerx}/assets_swtor_test_{lwert}_{vnummerx}.z14"
                    while True:
                        try:
                            wget.download(url15, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_{vnummerx}/assets_swtor_test_{lwert}_{vnummerx}.z14\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_test_{lwert}_{vnummerx}.z15") == True:
                    url16 = f"http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_{vnummerx}/assets_swtor_test_{lwert}_{vnummerx}.z15"
                    while True:
                        try:
                            wget.download(url16, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_{vnummerx}/assets_swtor_test_{lwert}_{vnummerx}.z15\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_test_{lwert}_{vnummerx}.z16") == True:
                    url17 = f"http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_{vnummerx}/assets_swtor_test_{lwert}_{vnummerx}.z16"
                    while True:
                        try:
                            wget.download(url17, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_{vnummerx}/assets_swtor_test_{lwert}_{vnummerx}.z16\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_test_{lwert}_{vnummerx}.z17") == True:
                    url18 = f"http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_{vnummerx}/assets_swtor_test_{lwert}_{vnummerx}.z17"
                    while True:
                        try:
                            wget.download(url18, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_{vnummerx}/assets_swtor_test_{lwert}_{vnummerx}.z17\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_test_{lwert}_{vnummerx}.z18") == True:
                    url19 = f"http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_{vnummerx}/assets_swtor_test_{lwert}_{vnummerx}.z18"
                    while True:
                        try:
                            wget.download(url19, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_{vnummerx}/assets_swtor_test_{lwert}_{vnummerx}.z18\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_test_{lwert}_{vnummerx}.z19") == True:
                    url20 = f"http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_{vnummerx}/assets_swtor_test_{lwert}_{vnummerx}.z19"
                    while True:
                        try:
                            wget.download(url20, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_{vnummerx}/assets_swtor_test_{lwert}_{vnummerx}.z19\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_test_{lwert}_{vnummerx}.z20") == True:
                    url21 = f"http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_{vnummerx}/assets_swtor_test_{lwert}_{vnummerx}.z20"
                    while True:
                        try:
                            wget.download(url21, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_{vnummerx}/assets_swtor_test_{lwert}_{vnummerx}.z20\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                log1_label.config(text="Download finished!")
                print("Download finished!\n")
            if lwert == "client":
                print(f"Download of {vwert} {lwert} version {vnummerx} started!\nPress CTRL+C to stop.")
                if not os.path.exists(f"{saveloc}/retailclient_publictest_{vnummerx}.zip") == True:
                    url = f"http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_{vnummerx}/retailclient_publictest_{vnummerx}.zip"
                    try:
                        wget.download(url, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_{vnummerx}/retailclient_publictest_{vnummerx}.zip\n")
                    except KeyboardInterrupt:
                        print("\nYou stopped the download!")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            print("\nNo Connection. Please try again!")
                            log1_label.config(text="No connection.\nPlease try again!")
                            return
                        else:
                            log1_label.config(text="Version not found!")
                            print("\nVersion not found!\n")
                            return
                if not os.path.exists(f"{saveloc}/retailclient_publictest_{vnummerx}.z01") == True:
                    url2 = f"http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_{vnummerx}/retailclient_publictest_{vnummerx}.z01"
                    while True:
                        try:
                            wget.download(url2, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_{vnummerx}/retailclient_publictest_{vnummerx}.z01\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_publictest_{vnummerx}.z02") == True:
                    url3 = f"http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_{vnummerx}/retailclient_publictest_{vnummerx}.z02"
                    while True:
                        try:
                            wget.download(url3, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_{vnummerx}/retailclient_publictest_{vnummerx}.z02\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_publictest_{vnummerx}.z03") == True:
                    url4 = f"http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_{vnummerx}/retailclient_publictest_{vnummerx}.z03"
                    while True:
                        try:
                            wget.download(url4, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_{vnummerx}/retailclient_publictest_{vnummerx}.z03\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_publictest_{vnummerx}.z04") == True:
                    url5 = f"http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_{vnummerx}/retailclient_publictest_{vnummerx}.z04"
                    while True:
                        try:
                            wget.download(url5, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_{vnummerx}/retailclient_publictest_{vnummerx}.z04\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_publictest_{vnummerx}.z05") == True:
                    url6 = f"http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_{vnummerx}/retailclient_publictest_{vnummerx}.z05"
                    while True:
                        try:
                            wget.download(url6, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_{vnummerx}/retailclient_publictest_{vnummerx}.z05\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_publictest_{vnummerx}.z06") == True:
                    url7 = f"http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_{vnummerx}/retailclient_publictest_{vnummerx}.z06"
                    while True:
                        try:
                            wget.download(url7, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_{vnummerx}/retailclient_publictest_{vnummerx}.z06\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_publictest_{vnummerx}.z07") == True:
                    url8 = f"http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_{vnummerx}/retailclient_publictest_{vnummerx}.z07"
                    while True:
                        try:
                            wget.download(url8, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_{vnummerx}/retailclient_publictest_{vnummerx}.z07\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_publictest_{vnummerx}.z08") == True:
                    url9 = f"http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_{vnummerx}/retailclient_publictest_{vnummerx}.z08"
                    while True:
                        try:
                            wget.download(url9, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_{vnummerx}/retailclient_publictest_{vnummerx}.z08\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_publictest_{vnummerx}.z09") == True:
                    url10 = f"http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_{vnummerx}/retailclient_publictest_{vnummerx}.z09"
                    while True:
                        try:
                            wget.download(url10, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_{vnummerx}/retailclient_publictest_{vnummerx}.z09\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_publictest_{vnummerx}.z10") == True:
                    url11 = f"http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_{vnummerx}/retailclient_publictest_{vnummerx}.z10"
                    while True:
                        try:
                            wget.download(url11, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_{vnummerx}/retailclient_publictest_{vnummerx}.z10\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_publictest_{vnummerx}.z11") == True:
                    url12 = f"http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_{vnummerx}/retailclient_publictest_{vnummerx}.z11"
                    while True:
                        try:
                            wget.download(url12, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_{vnummerx}/retailclient_publictest_{vnummerx}.z11\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_publictest_{vnummerx}.z12") == True:
                    url13 = f"http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_{vnummerx}/retailclient_publictest_{vnummerx}.z12"
                    while True:
                        try:
                            wget.download(url13, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_{vnummerx}/retailclient_publictest_{vnummerx}.z12\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_publictest_{vnummerx}.z13") == True:
                    url14 = f"http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_{vnummerx}/retailclient_publictest_{vnummerx}.z13"
                    while True:
                        try:
                            wget.download(url14, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_{vnummerx}/retailclient_publictest_{vnummerx}.z13\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_publictest_{vnummerx}.z14") == True:
                    url15 = f"http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_{vnummerx}/retailclient_publictest_{vnummerx}.z14"
                    while True:
                        try:
                            wget.download(url15, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_{vnummerx}/retailclient_publictest_{vnummerx}.z14\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_publictest_{vnummerx}.z15") == True:
                    url16 = f"http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_{vnummerx}/retailclient_publictest_{vnummerx}.z15"
                    while True:
                        try:
                            wget.download(url16, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_{vnummerx}/retailclient_publictest_{vnummerx}.z15\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_publictest_{vnummerx}.z16") == True:
                    url17 = f"http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_{vnummerx}/retailclient_publictest_{vnummerx}.z16"
                    while True:
                        try:
                            wget.download(url17, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_{vnummerx}/retailclient_publictest_{vnummerx}.z16\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_publictest_{vnummerx}.z17") == True:
                    url18 = f"http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_{vnummerx}/retailclient_publictest_{vnummerx}.z17"
                    while True:
                        try:
                            wget.download(url18, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_{vnummerx}/retailclient_publictest_{vnummerx}.z17\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_publictest_{vnummerx}.z18") == True:
                    url19 = f"http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_{vnummerx}/retailclient_publictest_{vnummerx}.z18"
                    while True:
                        try:
                            wget.download(url19, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_{vnummerx}/retailclient_publictest_{vnummerx}.z18\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_publictest_{vnummerx}.z19") == True:
                    url20 = f"http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_{vnummerx}/retailclient_publictest_{vnummerx}.z19"
                    while True:
                        try:
                            wget.download(url20, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_{vnummerx}/retailclient_publictest_{vnummerx}.z19\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_publictest_{vnummerx}.z20") == True:
                    url21 = f"http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_{vnummerx}/retailclient_publictest_{vnummerx}.z20"
                    while True:
                        try:
                            wget.download(url21, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_{vnummerx}/retailclient_publictest_{vnummerx}.z20\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                log1_label.config(text="Download finished!")
                print("Download finished!\n")
        if uwert == "0toY":
            if not lwert == "client":
                print(f"Download of {vwert} version 0to{vnummer} started!\nPress CTRL+C to stop.")
                if not os.path.exists(f"{saveloc}/assets_swtor_test_{lwert}_0to{vnummer}.zip") == True:
                    url = f"http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_0to{vnummer}/assets_swtor_test_{lwert}_0to{vnummer}.zip"
                    try:
                        wget.download(url, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_0to{vnummer}/assets_swtor_test_{lwert}_0to{vnummer}.zip\n")
                    except KeyboardInterrupt:
                        print("\nYou stopped the download!")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            print("\nNo Connection. Please try again!")
                            log1_label.config(text="No connection.\nPlease try again!")
                            return
                        else:
                            log1_label.config(text="Version not found!")
                            print("\nVersion not found!\n")
                            return
                if not os.path.exists(f"{saveloc}/assets_swtor_test_{lwert}_0to{vnummer}.z01") == True:
                    url2 = f"http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_0to{vnummer}/assets_swtor_test_{lwert}_0to{vnummer}.z01"
                    while True:
                        try:
                            wget.download(url2, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_0to{vnummer}/assets_swtor_test_{lwert}_0to{vnummer}.z01\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_test_{lwert}_0to{vnummer}.z02") == True:
                    url3 = f"http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_0to{vnummer}/assets_swtor_test_{lwert}_0to{vnummer}.z02"
                    while True:
                        try:
                            wget.download(url3, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_0to{vnummer}/assets_swtor_test_{lwert}_0to{vnummer}.z02\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_test_{lwert}_0to{vnummer}.z03") == True:
                    url4 = f"http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_0to{vnummer}/assets_swtor_test_{lwert}_0to{vnummer}.z03"
                    while True:
                        try:
                            wget.download(url4, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_0to{vnummer}/assets_swtor_test_{lwert}_0to{vnummer}.z03\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_test_{lwert}_0to{vnummer}.z04") == True:
                    url5 = f"http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_0to{vnummer}/assets_swtor_test_{lwert}_0to{vnummer}.z04"
                    while True:
                        try:
                            wget.download(url5, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_0to{vnummer}/assets_swtor_test_{lwert}_0to{vnummer}.z04\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_test_{lwert}_0to{vnummer}.z05") == True:
                    url6 = f"http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_0to{vnummer}/assets_swtor_test_{lwert}_0to{vnummer}.z05"
                    while True:
                        try:
                            wget.download(url6, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_0to{vnummer}/assets_swtor_test_{lwert}_0to{vnummer}.z05\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_test_{lwert}_0to{vnummer}.z06") == True:
                    url7 = f"http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_0to{vnummer}/assets_swtor_test_{lwert}_0to{vnummer}.z06"
                    while True:
                        try:
                            wget.download(url7, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_0to{vnummer}/assets_swtor_test_{lwert}_0to{vnummer}.z06\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_test_{lwert}_0to{vnummer}.z07") == True:
                    url8 = f"http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_0to{vnummer}/assets_swtor_test_{lwert}_0to{vnummer}.z07"
                    while True:
                        try:
                            wget.download(url8, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_0to{vnummer}/assets_swtor_test_{lwert}_0to{vnummer}.z07\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_test_{lwert}_0to{vnummer}.z08") == True:
                    url9 = f"http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_0to{vnummer}/assets_swtor_test_{lwert}_0to{vnummer}.z08"
                    while True:
                        try:
                            wget.download(url9, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_0to{vnummer}/assets_swtor_test_{lwert}_0to{vnummer}.z08\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_test_{lwert}_0to{vnummer}.z09") == True:
                    url10 = f"http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_0to{vnummer}/assets_swtor_test_{lwert}_0to{vnummer}.z09"
                    while True:
                        try:
                            wget.download(url10, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_0to{vnummer}/assets_swtor_test_{lwert}_0to{vnummer}.z09\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_test_{lwert}_0to{vnummer}.z10") == True:
                    url11 = f"http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_0to{vnummer}/assets_swtor_test_{lwert}_0to{vnummer}.z10"
                    while True:
                        try:
                            wget.download(url11, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_0to{vnummer}/assets_swtor_test_{lwert}_0to{vnummer}.z10\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_test_{lwert}_0to{vnummer}.z11") == True:
                    url12 = f"http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_0to{vnummer}/assets_swtor_test_{lwert}_0to{vnummer}.z11"
                    while True:
                        try:
                            wget.download(url12, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_0to{vnummer}/assets_swtor_test_{lwert}_0to{vnummer}.z11\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_test_{lwert}_0to{vnummer}.z12") == True:
                    url13 = f"http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_0to{vnummer}/assets_swtor_test_{lwert}_0to{vnummer}.z12"
                    while True:
                        try:
                            wget.download(url13, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_0to{vnummer}/assets_swtor_test_{lwert}_0to{vnummer}.z12\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_test_{lwert}_0to{vnummer}.z13") == True:
                    url14 = f"http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_0to{vnummer}/assets_swtor_test_{lwert}_0to{vnummer}.z13"
                    while True:
                        try:
                            wget.download(url14, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_0to{vnummer}/assets_swtor_test_{lwert}_0to{vnummer}.z13\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_test_{lwert}_0to{vnummer}.z14") == True:
                    url15 = f"http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_0to{vnummer}/assets_swtor_test_{lwert}_0to{vnummer}.z14"
                    while True:
                        try:
                            wget.download(url15, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_0to{vnummer}/assets_swtor_test_{lwert}_0to{vnummer}.z14\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_test_{lwert}_0to{vnummer}.z15") == True:
                    url16 = f"http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_0to{vnummer}/assets_swtor_test_{lwert}_0to{vnummer}.z15"
                    while True:
                        try:
                            wget.download(url16, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_0to{vnummer}/assets_swtor_test_{lwert}_0to{vnummer}.z15\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_test_{lwert}_0to{vnummer}.z16") == True:
                    url17 = f"http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_0to{vnummer}/assets_swtor_test_{lwert}_0to{vnummer}.z16"
                    while True:
                        try:
                            wget.download(url17, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_0to{vnummer}/assets_swtor_test_{lwert}_0to{vnummer}.z16\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_test_{lwert}_0to{vnummer}.z17") == True:
                    url18 = f"http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_0to{vnummer}/assets_swtor_test_{lwert}_0to{vnummer}.z17"
                    while True:
                        try:
                            wget.download(url18, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_0to{vnummer}/assets_swtor_test_{lwert}_0to{vnummer}.z17\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_test_{lwert}_0to{vnummer}.z18") == True:
                    url19 = f"http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_0to{vnummer}/assets_swtor_test_{lwert}_0to{vnummer}.z18"
                    while True:
                        try:
                            wget.download(url19, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_0to{vnummer}/assets_swtor_test_{lwert}_0to{vnummer}.z18\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_test_{lwert}_0to{vnummer}.z19") == True:
                    url20 = f"http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_0to{vnummer}/assets_swtor_test_{lwert}_0to{vnummer}.z19"
                    while True:
                        try:
                            wget.download(url20, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_0to{vnummer}/assets_swtor_test_{lwert}_0to{vnummer}.z19\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_test_{lwert}_0to{vnummer}.z20") == True:
                    url21 = f"http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_0to{vnummer}/assets_swtor_test_{lwert}_0to{vnummer}.z20"
                    while True:
                        try:
                            wget.download(url21, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_test_{lwert}/assets_swtor_test_{lwert}_0to{vnummer}/assets_swtor_test_{lwert}_0to{vnummer}.z20\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                log1_label.config(text="Download finished!")
                print("Download finished!\n")
            if lwert == "client":
                print(f"Download of {vwert} {lwert} version 0to{vnummer} started!\nPress CTRL+C to stop.")
                if not os.path.exists(f"{saveloc}/retailclient_publictest_0to{vnummer}.zip") == True:
                    url = f"http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_0to{vnummer}/retailclient_publictest_0to{vnummer}.zip"
                    try:
                        wget.download(url, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_0to{vnummer}/retailclient_publictest_0to{vnummer}.zip\n")
                    except KeyboardInterrupt:
                        print("\nYou stopped the download!")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            print("\nNo Connection. Please try again!")
                            log1_label.config(text="No connection.\nPlease try again!")
                            return
                        else:
                            log1_label.config(text="Version not found!")
                            print("\nVersion not found!\n")
                            return
                if not os.path.exists(f"{saveloc}/retailclient_publictest_0to{vnummer}.z01") == True:
                    url2 = f"http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_0to{vnummer}/retailclient_publictest_0to{vnummer}.z01"
                    while True:
                        try:
                            wget.download(url2, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_0to{vnummer}/retailclient_publictest_0to{vnummer}.z01\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_publictest_0to{vnummer}.z02") == True:
                    url3 = f"http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_0to{vnummer}/retailclient_publictest_0to{vnummer}.z02"
                    while True:
                        try:
                            wget.download(url3, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_0to{vnummer}/retailclient_publictest_0to{vnummer}.z02\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_publictest_0to{vnummer}.z03") == True:
                    url4 = f"http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_0to{vnummer}/retailclient_publictest_0to{vnummer}.z03"
                    while True:
                        try:
                            wget.download(url4, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_0to{vnummer}/retailclient_publictest_0to{vnummer}.z03\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_publictest_0to{vnummer}.z04") == True:
                    url5 = f"http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_0to{vnummer}/retailclient_publictest_0to{vnummer}.z04"
                    while True:
                        try:
                            wget.download(url5, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_0to{vnummer}/retailclient_publictest_0to{vnummer}.z04\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_publictest_0to{vnummer}.z05") == True:
                    url6 = f"http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_0to{vnummer}/retailclient_publictest_0to{vnummer}.z05"
                    while True:
                        try:
                            wget.download(url6, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_0to{vnummer}/retailclient_publictest_0to{vnummer}.z05\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_publictest_0to{vnummer}.z06") == True:
                    url7 = f"http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_0to{vnummer}/retailclient_publictest_0to{vnummer}.z06"
                    while True:
                        try:
                            wget.download(url7, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_0to{vnummer}/retailclient_publictest_0to{vnummer}.z06\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_publictest_0to{vnummer}.z07") == True:
                    url8 = f"http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_0to{vnummer}/retailclient_publictest_0to{vnummer}.z07"
                    while True:
                        try:
                            wget.download(url8, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_0to{vnummer}/retailclient_publictest_0to{vnummer}.z07\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_publictest_0to{vnummer}.z08") == True:
                    url9 = f"http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_0to{vnummer}/retailclient_publictest_0to{vnummer}.z08"
                    while True:
                        try:
                            wget.download(url9, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_0to{vnummer}/retailclient_publictest_0to{vnummer}.z08\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_publictest_0to{vnummer}.z09") == True:
                    url10 = f"http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_0to{vnummer}/retailclient_publictest_0to{vnummer}.z09"
                    while True:
                        try:
                            wget.download(url10, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_0to{vnummer}/retailclient_publictest_0to{vnummer}.z09\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_publictest_0to{vnummer}.z10") == True:
                    url11 = f"http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_0to{vnummer}/retailclient_publictest_0to{vnummer}.z10"
                    while True:
                        try:
                            wget.download(url11, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_0to{vnummer}/retailclient_publictest_0to{vnummer}.z10\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_publictest_0to{vnummer}.z11") == True:
                    url12 = f"http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_0to{vnummer}/retailclient_publictest_0to{vnummer}.z11"
                    while True:
                        try:
                            wget.download(url12, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_0to{vnummer}/retailclient_publictest_0to{vnummer}.z11\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_publictest_0to{vnummer}.z12") == True:
                    url13 = f"http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_0to{vnummer}/retailclient_publictest_0to{vnummer}.z12"
                    while True:
                        try:
                            wget.download(url13, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_0to{vnummer}/retailclient_publictest_0to{vnummer}.z12\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_publictest_0to{vnummer}.z13") == True:
                    url14 = f"http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_0to{vnummer}/retailclient_publictest_0to{vnummer}.z13"
                    while True:
                        try:
                            wget.download(url14, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_0to{vnummer}/retailclient_publictest_0to{vnummer}.z13\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_publictest_0to{vnummer}.z14") == True:
                    url15 = f"http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_0to{vnummer}/retailclient_publictest_0to{vnummer}.z14"
                    while True:
                        try:
                            wget.download(url15, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_0to{vnummer}/retailclient_publictest_0to{vnummer}.z14\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_publictest_0to{vnummer}.z15") == True:
                    url16 = f"http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_0to{vnummer}/retailclient_publictest_0to{vnummer}.z15"
                    while True:
                        try:
                            wget.download(url16, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_0to{vnummer}/retailclient_publictest_0to{vnummer}.z15\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_publictest_0to{vnummer}.z16") == True:
                    url17 = f"http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_0to{vnummer}/retailclient_publictest_0to{vnummer}.z16"
                    while True:
                        try:
                            wget.download(url17, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_0to{vnummer}/retailclient_publictest_0to{vnummer}.z16\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_publictest_0to{vnummer}.z17") == True:
                    url18 = f"http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_0to{vnummer}/retailclient_publictest_0to{vnummer}.z17"
                    while True:
                        try:
                            wget.download(url18, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_0to{vnummer}/retailclient_publictest_0to{vnummer}.z17\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_publictest_0to{vnummer}.z18") == True:
                    url19 = f"http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_0to{vnummer}/retailclient_publictest_0to{vnummer}.z18"
                    while True:
                        try:
                            wget.download(url19, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_0to{vnummer}/retailclient_publictest_0to{vnummer}.z18\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_publictest_0to{vnummer}.z19") == True:
                    url20 = f"http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_0to{vnummer}/retailclient_publictest_0to{vnummer}.z19"
                    while True:
                        try:
                            wget.download(url20, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_0to{vnummer}/retailclient_publictest_0to{vnummer}.z19\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_publictest_0to{vnummer}.z20") == True:
                    url21 = f"http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_0to{vnummer}/retailclient_publictest_0to{vnummer}.z20"
                    while True:
                        try:
                            wget.download(url21, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_publictest_0to{vnummer}/retailclient_publictest_0to{vnummer}.z20\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                log1_label.config(text="Download finished!")
                print("Download finished!\n")
    if vwert == "movies":
        if uwert == "XtoY":
            if not lwert == "client" and not lwert == "main":
                print(f"Download of {vwert} {lwert} version {vnummerx} started!\nPress CTRL+C to stop.")
                if not os.path.exists(f"{saveloc}/assets_swtor_test_{lwert}_{vnummerx}.zip") == True:
                    url = f"http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_{vnummerx}/movies_{lwert}_{vnummerx}.zip"
                    try:
                        wget.download(url, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_{vnummerx}/movies_{lwert}_{vnummerx}.zip\n")
                    except KeyboardInterrupt:
                        print("\nYou stopped the download!")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            print("\nNo Connection. Please try again!")
                            log1_label.config(text="No connection.\nPlease try again!")
                            return
                        else:
                            log1_label.config(text="Version not found!")
                            print("\nVersion not found!\n")
                            return
                if not os.path.exists(f"{saveloc}/movies_{lwert}_{vnummerx}.z01") == True:
                    url2 = f"http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_{vnummerx}/movies_{lwert}_{vnummerx}.z01"
                    while True:
                        try:
                            wget.download(url2, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_{vnummerx}/movies_{lwert}_{vnummerx}.z01\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/movies_{lwert}_{vnummerx}.z02") == True:
                    url3 = f"http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_{vnummerx}/movies_{lwert}_{vnummerx}.z02"
                    while True:
                        try:
                            wget.download(url3, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_{vnummerx}/movies_{lwert}_{vnummerx}.z02\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/movies_{lwert}_{vnummerx}.z03") == True:
                    url4 = f"http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_{vnummerx}/movies_{lwert}_{vnummerx}.z03"
                    while True:
                        try:
                            wget.download(url4, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_{vnummerx}/movies_{lwert}_{vnummerx}.z03\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/movies_{lwert}_{vnummerx}.z04") == True:
                    url5 = f"http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_{vnummerx}/movies_{lwert}_{vnummerx}.z04"
                    while True:
                        try:
                            wget.download(url5, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_{vnummerx}/movies_{lwert}_{vnummerx}.z04\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/movies_{lwert}_{vnummerx}.z05") == True:
                    url6 = f"http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_{vnummerx}/movies_{lwert}_{vnummerx}.z05"
                    while True:
                        try:
                            wget.download(url6, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_{vnummerx}/movies_{lwert}_{vnummerx}.z05\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/movies_{lwert}_{vnummerx}.z06") == True:
                    url7 = f"http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_{vnummerx}/movies_{lwert}_{vnummerx}.z06"
                    while True:
                        try:
                            wget.download(url7, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_{vnummerx}/movies_{lwert}_{vnummerx}.z06\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/movies_{lwert}_{vnummerx}.z07") == True:
                    url8 = f"http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_{vnummerx}/movies_{lwert}_{vnummerx}.z07"
                    while True:
                        try:
                            wget.download(url8, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_{vnummerx}/movies_{lwert}_{vnummerx}.z07\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/movies_{lwert}_{vnummerx}.z08") == True:
                    url9 = f"http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_{vnummerx}/movies_{lwert}_{vnummerx}.z08"
                    while True:
                        try:
                            wget.download(url9, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_{vnummerx}/movies_{lwert}_{vnummerx}.z08\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/movies_{lwert}_{vnummerx}.z09") == True:
                    url10 = f"http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_{vnummerx}/movies_{lwert}_{vnummerx}.z09"
                    while True:
                        try:
                            wget.download(url10, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_{vnummerx}/movies_{lwert}_{vnummerx}.z09\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/movies_{lwert}_{vnummerx}.z10") == True:
                    url11 = f"http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_{vnummerx}/movies_{lwert}_{vnummerx}.z10"
                    while True:
                        try:
                            wget.download(url11, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_{vnummerx}/movies_{lwert}_{vnummerx}.z10\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/movies_{lwert}_{vnummerx}.z11") == True:
                    url12 = f"http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_{vnummerx}/movies_{lwert}_{vnummerx}.z11"
                    while True:
                        try:
                            wget.download(url12, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_{vnummerx}/movies_{lwert}_{vnummerx}.z11\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/movies_{lwert}_{vnummerx}.z12") == True:
                    url13 = f"http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_{vnummerx}/movies_{lwert}_{vnummerx}.z12"
                    while True:
                        try:
                            wget.download(url13, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_{vnummerx}/movies_{lwert}_{vnummerx}.z12\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/movies_{lwert}_{vnummerx}.z13") == True:
                    url14 = f"http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_{vnummerx}/movies_{lwert}_{vnummerx}.z13"
                    while True:
                        try:
                            wget.download(url14, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_{vnummerx}/movies_{lwert}_{vnummerx}.z13\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/movies_{lwert}_{vnummerx}.z14") == True:
                    url15 = f"http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_{vnummerx}/movies_{lwert}_{vnummerx}.z14"
                    while True:
                        try:
                            wget.download(url15, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_{vnummerx}/movies_{lwert}_{vnummerx}.z14\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/movies_{lwert}_{vnummerx}.z15") == True:
                    url16 = f"http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_{vnummerx}/movies_{lwert}_{vnummerx}.z15"
                    while True:
                        try:
                            wget.download(url16, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_{vnummerx}/movies_{lwert}_{vnummerx}.z15\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/movies_{lwert}_{vnummerx}.z16") == True:
                    url17 = f"http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_{vnummerx}/movies_{lwert}_{vnummerx}.z16"
                    while True:
                        try:
                            wget.download(url17, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_{vnummerx}/movies_{lwert}_{vnummerx}.z16\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/movies_{lwert}_{vnummerx}.z17") == True:
                    url18 = f"http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_{vnummerx}/movies_{lwert}_{vnummerx}.z17"
                    while True:
                        try:
                            wget.download(url18, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_{vnummerx}/movies_{lwert}_{vnummerx}.z17\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/movies_{lwert}_{vnummerx}.z18") == True:
                    url19 = f"http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_{vnummerx}/movies_{lwert}_{vnummerx}.z18"
                    while True:
                        try:
                            wget.download(url19, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_{vnummerx}/movies_{lwert}_{vnummerx}.z18\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/movies_{lwert}_{vnummerx}.z19") == True:
                    url20 = f"http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_{vnummerx}/movies_{lwert}_{vnummerx}.z19"
                    while True:
                        try:
                            wget.download(url20, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_{vnummerx}/movies_{lwert}_{vnummerx}.z19\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/movies_{lwert}_{vnummerx}.z20") == True:
                    url21 = f"http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_{vnummerx}/movies_{lwert}_{vnummerx}.z20"
                    while True:
                        try:
                            wget.download(url21, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_{vnummerx}/movies_{lwert}_{vnummerx}.z20\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                log1_label.config(text="Download finished!")
                print("Download finished!\n")
            else:
                log1_label.config(text="Please select a language!")
        if uwert == "0toY":
            if not lwert == "client" and not lwert == "main":
                print(f"Download of {vwert} version 0to{vnummer} started!\nPress CTRL+C to stop.")
                if not os.path.exists(f"{saveloc}/movies_{lwert}_0to{vnummer}.zip") == True:
                    url = f"http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_0to{vnummer}/movies_{lwert}_0to{vnummer}.zip"
                    try:
                        wget.download(url, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_0to{vnummer}/movies_{lwert}_0to{vnummer}.zip\n")
                    except KeyboardInterrupt:
                        print("\nYou stopped the download!")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            print("\nNo Connection. Please try again!")
                            log1_label.config(text="No connection.\nPlease try again!")
                            return
                        else:
                            log1_label.config(text="Version not found!")
                            print("\nVersion not found!\n")
                            return
                if not os.path.exists(f"{saveloc}/movies_{lwert}_0to{vnummer}.z01") == True:
                    url2 = f"http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_0to{vnummer}/movies_{lwert}_0to{vnummer}.z01"
                    while True:
                        try:
                            wget.download(url2, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_0to{vnummer}/movies_{lwert}_0to{vnummer}.z01\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/movies_{lwert}_0to{vnummer}.z02") == True:
                    url3 = f"http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_0to{vnummer}/movies_{lwert}_0to{vnummer}.z02"
                    while True:
                        try:
                            wget.download(url3, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_0to{vnummer}/movies_{lwert}_0to{vnummer}.z02\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/movies_{lwert}_0to{vnummer}.z03") == True:
                    url4 = f"http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_0to{vnummer}/movies_{lwert}_0to{vnummer}.z03"
                    while True:
                        try:
                            wget.download(url4, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_0to{vnummer}/movies_{lwert}_0to{vnummer}.z03\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/movies_{lwert}_0to{vnummer}.z04") == True:
                    url5 = f"http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_0to{vnummer}/movies_{lwert}_0to{vnummer}.z04"
                    while True:
                        try:
                            wget.download(url5, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_0to{vnummer}/movies_{lwert}_0to{vnummer}.z04\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/movies_{lwert}_0to{vnummer}.z05") == True:
                    url6 = f"http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_0to{vnummer}/movies_{lwert}_0to{vnummer}.z05"
                    while True:
                        try:
                            wget.download(url6, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_0to{vnummer}/movies_{lwert}_0to{vnummer}.z05\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/movies_{lwert}_0to{vnummer}.z06") == True:
                    url7 = f"http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_0to{vnummer}/movies_{lwert}_0to{vnummer}.z06"
                    while True:
                        try:
                            wget.download(url7, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_0to{vnummer}/movies_{lwert}_0to{vnummer}.z06\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/movies_{lwert}_0to{vnummer}.z07") == True:
                    url8 = f"http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_0to{vnummer}/movies_{lwert}_0to{vnummer}.z07"
                    while True:
                        try:
                            wget.download(url8, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_0to{vnummer}/movies_{lwert}_0to{vnummer}.z07\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/movies_{lwert}_0to{vnummer}.z08") == True:
                    url9 = f"http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_0to{vnummer}/movies_{lwert}_0to{vnummer}.z08"
                    while True:
                        try:
                            wget.download(url9, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_0to{vnummer}/movies_{lwert}_0to{vnummer}.z08\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/movies_{lwert}_0to{vnummer}.z09") == True:
                    url10 = f"http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_0to{vnummer}/movies_{lwert}_0to{vnummer}.z09"
                    while True:
                        try:
                            wget.download(url10, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_0to{vnummer}/movies_{lwert}_0to{vnummer}.z09\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/movies_{lwert}_0to{vnummer}.z10") == True:
                    url11 = f"http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_0to{vnummer}/movies_{lwert}_0to{vnummer}.z10"
                    while True:
                        try:
                            wget.download(url11, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_0to{vnummer}/movies_{lwert}_0to{vnummer}.z10\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/movies_{lwert}_0to{vnummer}.z11") == True:
                    url12 = f"http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_0to{vnummer}/movies_{lwert}_0to{vnummer}.z11"
                    while True:
                        try:
                            wget.download(url12, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_0to{vnummer}/movies_{lwert}_0to{vnummer}.z11\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/movies_{lwert}_0to{vnummer}.z12") == True:
                    url13 = f"http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_0to{vnummer}/movies_{lwert}_0to{vnummer}.z12"
                    while True:
                        try:
                            wget.download(url13, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_0to{vnummer}/movies_{lwert}_0to{vnummer}.z12\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/movies_{lwert}_0to{vnummer}.z13") == True:
                    url14 = f"http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_0to{vnummer}/movies_{lwert}_0to{vnummer}.z13"
                    while True:
                        try:
                            wget.download(url14, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_0to{vnummer}/movies_{lwert}_0to{vnummer}.z13\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/movies_{lwert}_0to{vnummer}.z14") == True:
                    url15 = f"http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_0to{vnummer}/movies_{lwert}_0to{vnummer}.z14"
                    while True:
                        try:
                            wget.download(url15, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_0to{vnummer}/movies_{lwert}_0to{vnummer}.z14\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/movies_{lwert}_0to{vnummer}.z15") == True:
                    url16 = f"http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_0to{vnummer}/movies_{lwert}_0to{vnummer}.z15"
                    while True:
                        try:
                            wget.download(url16, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_0to{vnummer}/movies_{lwert}_0to{vnummer}.z15\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/movies_{lwert}_0to{vnummer}.z16") == True:
                    url17 = f"http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_0to{vnummer}/movies_{lwert}_0to{vnummer}.z16"
                    while True:
                        try:
                            wget.download(url17, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_0to{vnummer}/movies_{lwert}_0to{vnummer}.z16\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/movies_{lwert}_0to{vnummer}.z17") == True:
                    url18 = f"http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_0to{vnummer}/movies_{lwert}_0to{vnummer}.z17"
                    while True:
                        try:
                            wget.download(url18, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_0to{vnummer}/movies_{lwert}_0to{vnummer}.z17\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/movies_{lwert}_0to{vnummer}.z18") == True:
                    url19 = f"http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_0to{vnummer}/movies_{lwert}_0to{vnummer}.z18"
                    while True:
                        try:
                            wget.download(url19, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_0to{vnummer}/movies_{lwert}_0to{vnummer}.z18\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/movies_{lwert}_0to{vnummer}.z19") == True:
                    url20 = f"http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_0to{vnummer}/movies_{lwert}_0to{vnummer}.z19"
                    while True:
                        try:
                            wget.download(url20, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_0to{vnummer}/movies_{lwert}_0to{vnummer}.z19\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/movies_{lwert}_0to{vnummer}.z20") == True:
                    url21 = f"http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_0to{vnummer}/movies_{lwert}_0to{vnummer}.z20"
                    while True:
                        try:
                            wget.download(url21, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/movies_{lwert}/movies_{lwert}_0to{vnummer}/movies_{lwert}_0to{vnummer}.z20\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                log1_label.config(text="Download finished!")
                print("Download finished!\n")
            else:
                log1_label.config(text="Please select a language!")
    if vwert == "Live":
        if uwert == "XtoY":
            if not lwert == "client":
                print(f"Download of {vwert} version {vnummerx} started!\nPress CTRL+C to stop.")
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_{vnummerx}.zip") == True:
                    url = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.zip"
                    try:
                        wget.download(url, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.zip\n")
                    except KeyboardInterrupt:
                        print("\nYou stopped the download!")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            print("\nNo Connection. Please try again!")
                            log1_label.config(text="No connection.\nPlease try again!")
                            return
                        else:
                            log1_label.config(text="Version not found!")
                            print("\nVersion not found!\n")
                            return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_{vnummerx}.z01") == True:
                    url2 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z01"
                    while True:
                        try:
                            wget.download(url2, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z01\n")
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
                                log1_label.config(text="Download finished!xy")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_{vnummerx}.z02") == True:
                    url3 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z02"
                    while True:
                        try:
                            wget.download(url3, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z02\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_{vnummerx}.z03") == True:
                    url4 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z03"
                    while True:
                        try:
                            wget.download(url4, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z03\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_{vnummerx}.z04") == True:
                    url5 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z04"
                    while True:
                        try:
                            wget.download(url5, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z04\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_{vnummerx}.z05") == True:
                    url6 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z05"
                    while True:
                        try:
                            wget.download(url6, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z05\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_{vnummerx}.z06") == True:
                    url7 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z06"
                    while True:
                        try:
                            wget.download(url7, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z06\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_{vnummerx}.z07") == True:
                    url8 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z07"
                    while True:
                        try:
                            wget.download(url8, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z07\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_{vnummerx}.z08") == True:
                    url9 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z08"
                    while True:
                        try:
                            wget.download(url9, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z08\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_{vnummerx}.z09") == True:
                    url10 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z09"
                    while True:
                        try:
                            wget.download(url10, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z09\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_{vnummerx}.z10") == True:
                    url11 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z10"
                    while True:
                        try:
                            wget.download(url11, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z10\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_{vnummerx}.z11") == True:
                    url12 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z11"
                    while True:
                        try:
                            wget.download(url12, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z11\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_{vnummerx}.z12") == True:
                    url13 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z12"
                    while True:
                        try:
                            wget.download(url13, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z12\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_{vnummerx}.z13") == True:
                    url14 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z13"
                    while True:
                        try:
                            wget.download(url14, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z13\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_{vnummerx}.z14") == True:
                    url15 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z14"
                    while True:
                        try:
                            wget.download(url15, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z14\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_{vnummerx}.z15") == True:
                    url16 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z15"
                    while True:
                        try:
                            wget.download(url16, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z15\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_{vnummerx}.z16") == True:
                    url17 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z16"
                    while True:
                        try:
                            wget.download(url17, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z16\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_{vnummerx}.z17") == True:
                    url18 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z17"
                    while True:
                        try:
                            wget.download(url18, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z17\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_{vnummerx}.z18") == True:
                    url19 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z18"
                    while True:
                        try:
                            wget.download(url19, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z18\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_{vnummerx}.z19") == True:
                    url20 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z19"
                    while True:
                        try:
                            wget.download(url20, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z19\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_{vnummerx}.z20") == True:
                    url21 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z20"
                    while True:
                        try:
                            wget.download(url21, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_{vnummerx}/assets_swtor_{lwert}_{vnummerx}.z20\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                log1_label.config(text="Download finished!")
                print("Download finished!\n")
            if lwert == "client":
                print(f"Download of {vwert} {lwert} version {vnummerx} started!\nPress CTRL+C to stop.")
                if not os.path.exists(f"{saveloc}/retailclient_swtor_{vnummerx}.zip") == True:
                    url = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.zip"
                    try:
                        wget.download(url, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.zip\n")
                    except KeyboardInterrupt:
                        print("\nYou stopped the download!")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            print("\nNo Connection. Please try again!")
                            log1_label.config(text="No connection.\nPlease try again!")
                            return
                        else:
                            log1_label.config(text="Version not found!")
                            print("\nVersion not found!\n")
                            return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_{vnummerx}.z01") == True:
                    url2 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z01"
                    while True:
                        try:
                            wget.download(url2, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z01\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_{vnummerx}.z02") == True:
                    url3 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z02"
                    while True:
                        try:
                            wget.download(url3, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z02\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_{vnummerx}.z03") == True:
                    url4 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z03"
                    while True:
                        try:
                            wget.download(url4, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z03\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_{vnummerx}.z04") == True:
                    url5 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z04"
                    while True:
                        try:
                            wget.download(url5, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z04\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_{vnummerx}.z05") == True:
                    url6 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z05"
                    while True:
                        try:
                            wget.download(url6, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z05\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_{vnummerx}.z06") == True:
                    url7 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z06"
                    while True:
                        try:
                            wget.download(url7, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z06\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_{vnummerx}.z07") == True:
                    url8 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z07"
                    while True:
                        try:
                            wget.download(url8, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z07\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_{vnummerx}.z08") == True:
                    url9 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z08"
                    while True:
                        try:
                            wget.download(url9, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z08\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_{vnummerx}.z09") == True:
                    url10 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z09"
                    while True:
                        try:
                            wget.download(url10, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z09\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_{vnummerx}.z10") == True:
                    url11 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z10"
                    while True:
                        try:
                            wget.download(url11, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z10\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_{vnummerx}.z11") == True:
                    url12 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z11"
                    while True:
                        try:
                            wget.download(url12, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z11\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_{vnummerx}.z12") == True:
                    url13 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z12"
                    while True:
                        try:
                            wget.download(url13, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z12\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_{vnummerx}.z13") == True:
                    url14 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z13"
                    while True:
                        try:
                            wget.download(url14, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z13\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_{vnummerx}.z14") == True:
                    url15 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z14"
                    while True:
                        try:
                            wget.download(url15, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z14\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_{vnummerx}.z15") == True:
                    url16 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z15"
                    while True:
                        try:
                            wget.download(url16, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z15\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_{vnummerx}.z16") == True:
                    url17 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z16"
                    while True:
                        try:
                            wget.download(url17, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z16\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_{vnummerx}.z17") == True:
                    url18 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z17"
                    while True:
                        try:
                            wget.download(url18, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z17\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_{vnummerx}.z18") == True:
                    url19 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z18"
                    while True:
                        try:
                            wget.download(url19, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z18\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_{vnummerx}.z19") == True:
                    url20 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z19"
                    while True:
                        try:
                            wget.download(url20, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z19\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_{vnummerx}.z20") == True:
                    url21 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z20"
                    while True:
                        try:
                            wget.download(url21, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/publictest/retailclient_publictest/retailclient_swtor_{vnummerx}/retailclient_swtor_{vnummerx}.z20\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                log1_label.config(text="Download finished!")
                print("Download finished!\n")
        if uwert == "0toY":
            if not lwert == "client":
                print(f"Download of {vwert} version 0to{vnummer} started!\nPress CTRL+C to stop.")
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_0to{vnummer}.zip") == True:
                    url = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer}/assets_swtor_{lwert}_0to{vnummer}.zip"
                    try:
                        wget.download(url, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer}/assets_swtor_{lwert}_0to{vnummer}.zip\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_0to{vnummer}.z01") == True:
                    url2 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer}/assets_swtor_{lwert}_0to{vnummer}.z01"
                    while True:
                        try:
                            wget.download(url2, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer}/assets_swtor_{lwert}_0to{vnummer}.z01\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_0to{vnummer}.z02") == True:
                    url3 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer}/assets_swtor_{lwert}_0to{vnummer}.z02"
                    while True:
                        try:
                            wget.download(url3, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer}/assets_swtor_{lwert}_0to{vnummer}.z02\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_0to{vnummer}.z03") == True:
                    url4 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer}/assets_swtor_{lwert}_0to{vnummer}.z03"
                    while True:
                        try:
                            wget.download(url4, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer}/assets_swtor_{lwert}_0to{vnummer}.z03\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_0to{vnummer}.z04") == True:
                    url5 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer}/assets_swtor_{lwert}_0to{vnummer}.z04"
                    while True:
                        try:
                            wget.download(url5, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer}/assets_swtor_{lwert}_0to{vnummer}.z04\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_0to{vnummer}.z05") == True:
                    url6 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer}/assets_swtor_{lwert}_0to{vnummer}.z05"
                    while True:
                        try:
                            wget.download(url6, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer}/assets_swtor_{lwert}_0to{vnummer}.z05\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_0to{vnummer}.z06") == True:
                    url7 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer}/assets_swtor_{lwert}_0to{vnummer}.z06"
                    while True:
                        try:
                            wget.download(url7, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer}/assets_swtor_{lwert}_0to{vnummer}.z06\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_0to{vnummer}.z07") == True:
                    url8 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer}/assets_swtor_{lwert}_0to{vnummer}.z07"
                    while True:
                        try:
                            wget.download(url8, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer}/assets_swtor_{lwert}_0to{vnummer}.z07\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_0to{vnummer}.z08") == True:
                    url9 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer}/assets_swtor_{lwert}_0to{vnummer}.z08"
                    while True:
                        try:
                            wget.download(url9, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer}/assets_swtor_{lwert}_0to{vnummer}.z08\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_0to{vnummer}.z09") == True:
                    url10 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer}/assets_swtor_{lwert}_0to{vnummer}.z09"
                    while True:
                        try:
                            wget.download(url10, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer}/assets_swtor_{lwert}_0to{vnummer}.z09\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_0to{vnummer}.z10") == True:
                    url11 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer}/assets_swtor_{lwert}_0to{vnummer}.z10"
                    while True:
                        try:
                            wget.download(url11, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer}/assets_swtor_{lwert}_0to{vnummer}.z10\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_0to{vnummer}.z11") == True:
                    url12 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer}/assets_swtor_{lwert}_0to{vnummer}.z11"
                    while True:
                        try:
                            wget.download(url12, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer}/assets_swtor_{lwert}_0to{vnummer}.z11\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_0to{vnummer}.z12") == True:
                    url13 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer}/assets_swtor_{lwert}_0to{vnummer}.z12"
                    while True:
                        try:
                            wget.download(url13, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer}/assets_swtor_{lwert}_0to{vnummer}.z12\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_0to{vnummer}.z13") == True:
                    url14 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer}/assets_swtor_{lwert}_0to{vnummer}.z13"
                    while True:
                        try:
                            wget.download(url14, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer}/assets_swtor_{lwert}_0to{vnummer}.z13\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_0to{vnummer}.z14") == True:
                    url15 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer}/assets_swtor_{lwert}_0to{vnummer}.z14"
                    while True:
                        try:
                            wget.download(url15, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer}/assets_swtor_{lwert}_0to{vnummer}.z14\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_0to{vnummer}.z15") == True:
                    url16 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer}/assets_swtor_{lwert}_0to{vnummer}.z15"
                    while True:
                        try:
                            wget.download(url16, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer}/assets_swtor_{lwert}_0to{vnummer}.z15\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_0to{vnummer}.z16") == True:
                    url17 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer}/assets_swtor_{lwert}_0to{vnummer}.z16"
                    while True:
                        try:
                            wget.download(url17, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer}/assets_swtor_{lwert}_0to{vnummer}.z16\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_0to{vnummer}.z17") == True:
                    url18 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer}/assets_swtor_{lwert}_0to{vnummer}.z17"
                    while True:
                        try:
                            wget.download(url18, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer}/assets_swtor_{lwert}_0to{vnummer}.z17\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_0to{vnummer}.z18") == True:
                    url19 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer}/assets_swtor_{lwert}_0to{vnummer}.z18"
                    while True:
                        try:
                            wget.download(url19, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer}/assets_swtor_{lwert}_0to{vnummer}.z18\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_0to{vnummer}.z19") == True:
                    url20 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer}/assets_swtor_{lwert}_0to{vnummer}.z19"
                    while True:
                        try:
                            wget.download(url20, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer}/assets_swtor_{lwert}_0to{vnummer}.z19\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/assets_swtor_{lwert}_0to{vnummer}.z20") == True:
                    url21 = f"http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer}/assets_swtor_{lwert}_0to{vnummer}.z20"
                    while True:
                        try:
                            wget.download(url21, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/assets_swtor_{lwert}/assets_swtor_{lwert}_0to{vnummer}/assets_swtor_{lwert}_0to{vnummer}.z20\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                log1_label.config(text="Download finished!")
                print("Download finished!\n")
            if lwert == "client":
                print(f"Download of {vwert} {lwert} version 0to{vnummer} started!\nPress CTRL+C to stop.")
                if not os.path.exists(f"{saveloc}/retailclient_swtor_0to{vnummer}.zip") == True:
                    url = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer}/retailclient_swtor_0to{vnummer}.zip"
                    try:
                        wget.download(url, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer}/retailclient_swtor_0to{vnummer}.zip\n")
                    except KeyboardInterrupt:
                        print("\nYou stopped the download!")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            print("\nNo Connection. Please try again!")
                            log1_label.config(text="No connection.\nPlease try again!")
                            return
                        else:
                            log1_label.config(text="Version not found!")
                            print("\nVersion not found!\n")
                            return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_0to{vnummer}.z01") == True:
                    url2 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer}/retailclient_swtor_0to{vnummer}.z01"
                    while True:
                        try:
                            wget.download(url2, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer}/retailclient_swtor_0to{vnummer}.z01\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_0to{vnummer}.z02") == True:
                    url3 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer}/retailclient_swtor_0to{vnummer}.z02"
                    while True:
                        try:
                            wget.download(url3, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer}/retailclient_swtor_0to{vnummer}.z02\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_0to{vnummer}.z03") == True:
                    url4 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer}/retailclient_swtor_0to{vnummer}.z03"
                    while True:
                        try:
                            wget.download(url4, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer}/retailclient_swtor_0to{vnummer}.z03\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_0to{vnummer}.z04") == True:
                    url5 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer}/retailclient_swtor_0to{vnummer}.z04"
                    while True:
                        try:
                            wget.download(url5, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer}/retailclient_swtor_0to{vnummer}.z04\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_0to{vnummer}.z05") == True:
                    url6 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer}/retailclient_swtor_0to{vnummer}.z05"
                    while True:
                        try:
                            wget.download(url6, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer}/retailclient_swtor_0to{vnummer}.z05\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_0to{vnummer}.z06") == True:
                    url7 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer}/retailclient_swtor_0to{vnummer}.z06"
                    while True:
                        try:
                            wget.download(url7, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer}/retailclient_swtor_0to{vnummer}.z06\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_0to{vnummer}.z07") == True:
                    url8 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer}/retailclient_swtor_0to{vnummer}.z07"
                    while True:
                        try:
                            wget.download(url8, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer}/retailclient_swtor_0to{vnummer}.z07\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_0to{vnummer}.z08") == True:
                    url9 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer}/retailclient_swtor_0to{vnummer}.z08"
                    while True:
                        try:
                            wget.download(url9, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer}/retailclient_swtor_0to{vnummer}.z08\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_0to{vnummer}.z09") == True:
                    url10 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer}/retailclient_swtor_0to{vnummer}.z09"
                    while True:
                        try:
                            wget.download(url10, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer}/retailclient_swtor_0to{vnummer}.z09\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_0to{vnummer}.z10") == True:
                    url11 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer}/retailclient_swtor_0to{vnummer}.z10"
                    while True:
                        try:
                            wget.download(url11, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer}/retailclient_swtor_0to{vnummer}.z10\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_0to{vnummer}.z11") == True:
                    url12 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer}/retailclient_swtor_0to{vnummer}.z11"
                    while True:
                        try:
                            wget.download(url12, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer}/retailclient_swtor_0to{vnummer}.z11\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_0to{vnummer}.z12") == True:
                    url13 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer}/retailclient_swtor_0to{vnummer}.z12"
                    while True:
                        try:
                            wget.download(url13, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer}/retailclient_swtor_0to{vnummer}.z12\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_0to{vnummer}.z13") == True:
                    url14 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer}/retailclient_swtor_0to{vnummer}.z13"
                    while True:
                        try:
                            wget.download(url14, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer}/retailclient_swtor_0to{vnummer}.z13\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_0to{vnummer}.z14") == True:
                    url15 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer}/retailclient_swtor_0to{vnummer}.z14"
                    while True:
                        try:
                            wget.download(url15, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer}/retailclient_swtor_0to{vnummer}.z14\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_0to{vnummer}.z15") == True:
                    url16 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer}/retailclient_swtor_0to{vnummer}.z15"
                    while True:
                        try:
                            wget.download(url16, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer}/retailclient_swtor_0to{vnummer}.z15\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_0to{vnummer}.z16") == True:
                    url17 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer}/retailclient_swtor_0to{vnummer}.z16"
                    while True:
                        try:
                            wget.download(url17, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer}/retailclient_swtor_0to{vnummer}.z16\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_0to{vnummer}.z17") == True:
                    url18 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer}/retailclient_swtor_0to{vnummer}.z17"
                    while True:
                        try:
                            wget.download(url18, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer}/retailclient_swtor_0to{vnummer}.z17\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_0to{vnummer}.z18") == True:
                    url19 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer}/retailclient_swtor_0to{vnummer}.z18"
                    while True:
                        try:
                            wget.download(url19, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer}/retailclient_swtor_0to{vnummer}.z18\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_0to{vnummer}.z19") == True:
                    url20 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer}/retailclient_swtor_0to{vnummer}.z19"
                    while True:
                        try:
                            wget.download(url20, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer}/retailclient_swtor_0to{vnummer}.z19\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                if not os.path.exists(f"{saveloc}/retailclient_swtor_0to{vnummer}.z20") == True:
                    url21 = f"http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer}/retailclient_swtor_0to{vnummer}.z20"
                    while True:
                        try:
                            wget.download(url21, saveloc)
                            print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/swtor/retailclient_swtor/retailclient_swtor_0to{vnummer}/retailclient_swtor_0to{vnummer}.z20\n")
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
                                log1_label.config(text="Download finished!")
                                print("\nDownload finished!\n")
                                return
                log1_label.config(text="Download finished!")
                print("Download finished!\n")
    if vwert == "liveqatest":
        if uwert == "0toY":
            print(f"Download of {vwert} version 0to{vnummer} started!\nPress CTRL+C to stop.")
            if not os.path.exists(f"{saveloc}/retailclient_liveqatest_0to{vnummer}.zip") == True:
                url = f"http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_0to{vnummer}/retailclient_liveqatest_0to{vnummer}.zip"
                try:
                    wget.download(url, saveloc)
                    print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_0to{vnummer}/retailclient_liveqatest_0to{vnummer}.zip\n")
                except KeyboardInterrupt:
                    print("\nYou stopped the download!")
                    return
                except Exception as ex:
                    exception = type(ex).__name__
                    argumente = str(ex.args)
                    if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                        print("\nNo Connection. Please try again!")
                        log1_label.config(text="No connection.\nPlease try again!")
                        return
                    else:
                        log1_label.config(text="Version not found!")
                        print("\nVersion not found!\n")
                        return
            if not os.path.exists(f"{saveloc}/retailclient_liveqatest_0to{vnummer}.z01") == True:
                url2 = f"http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_0to{vnummer}/retailclient_liveqatest_0to{vnummer}.z01"
                while True:
                    try:
                        wget.download(url2, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_0to{vnummer}/retailclient_liveqatest_0to{vnummer}.z01\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveqatest_0to{vnummer}.z02") == True:
                url3 = f"http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_0to{vnummer}/retailclient_liveqatest_0to{vnummer}.z02"
                while True:
                    try:
                        wget.download(url3, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_0to{vnummer}/retailclient_liveqatest_0to{vnummer}.z02\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveqatest_0to{vnummer}.z03") == True:
                url4 = f"http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_0to{vnummer}/retailclient_liveqatest_0to{vnummer}.z03"
                while True:
                    try:
                        wget.download(url4, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_0to{vnummer}/retailclient_liveqatest_0to{vnummer}.z03\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveqatest_0to{vnummer}.z04") == True:
                url5 = f"http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_0to{vnummer}/retailclient_liveqatest_0to{vnummer}.z04"
                while True:
                    try:
                        wget.download(url5, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_0to{vnummer}/retailclient_liveqatest_0to{vnummer}.z04\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveqatest_0to{vnummer}.z05") == True:
                url6 = f"http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_0to{vnummer}/retailclient_liveqatest_0to{vnummer}.z05"
                while True:
                    try:
                        wget.download(url6, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_0to{vnummer}/retailclient_liveqatest_0to{vnummer}.z05\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveqatest_0to{vnummer}.z06") == True:
                url7 = f"http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_0to{vnummer}/retailclient_liveqatest_0to{vnummer}.z06"
                while True:
                    try:
                        wget.download(url7, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_0to{vnummer}/retailclient_liveqatest_0to{vnummer}.z06\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveqatest_0to{vnummer}.z07") == True:
                url8 = f"http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_0to{vnummer}/retailclient_liveqatest_0to{vnummer}.z07"
                while True:
                    try:
                        wget.download(url8, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_0to{vnummer}/retailclient_liveqatest_0to{vnummer}.z07\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveqatest_0to{vnummer}.z08") == True:
                url9 = f"http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_0to{vnummer}/retailclient_liveqatest_0to{vnummer}.z08"
                while True:
                    try:
                        wget.download(url9, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_0to{vnummer}/retailclient_liveqatest_0to{vnummer}.z08\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveqatest_0to{vnummer}.z09") == True:
                url10 = f"http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_0to{vnummer}/retailclient_liveqatest_0to{vnummer}.z09"
                while True:
                    try:
                        wget.download(url10, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_0to{vnummer}/retailclient_liveqatest_0to{vnummer}.z09\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveqatest_0to{vnummer}.z10") == True:
                url11 = f"http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_0to{vnummer}/retailclient_liveqatest_0to{vnummer}.z10"
                while True:
                    try:
                        wget.download(url11, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_0to{vnummer}/retailclient_liveqatest_0to{vnummer}.z10\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveqatest_0to{vnummer}.z11") == True:
                url12 = f"http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_0to{vnummer}/retailclient_liveqatest_0to{vnummer}.z11"
                while True:
                    try:
                        wget.download(url12, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_0to{vnummer}/retailclient_liveqatest_0to{vnummer}.z11\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveqatest_0to{vnummer}.z12") == True:
                url13 = f"http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_0to{vnummer}/retailclient_liveqatest_0to{vnummer}.z12"
                while True:
                    try:
                        wget.download(url13, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_0to{vnummer}/retailclient_liveqatest_0to{vnummer}.z12\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveqatest_0to{vnummer}.z13") == True:
                url14 = f"http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_0to{vnummer}/retailclient_liveqatest_0to{vnummer}.z13"
                while True:
                    try:
                        wget.download(url14, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_0to{vnummer}/retailclient_liveqatest_0to{vnummer}.z13\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveqatest_0to{vnummer}.z14") == True:
                url15 = f"http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_0to{vnummer}/retailclient_liveqatest_0to{vnummer}.z14"
                while True:
                    try:
                        wget.download(url15, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_0to{vnummer}/retailclient_liveqatest_0to{vnummer}.z14\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveqatest_0to{vnummer}.z15") == True:
                url16 = f"http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_0to{vnummer}/retailclient_liveqatest_0to{vnummer}.z15"
                while True:
                    try:
                        wget.download(url16, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_0to{vnummer}/retailclient_liveqatest_0to{vnummer}.z15\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveqatest_0to{vnummer}.z16") == True:
                url17 = f"http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_0to{vnummer}/retailclient_liveqatest_0to{vnummer}.z16"
                while True:
                    try:
                        wget.download(url17, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_0to{vnummer}/retailclient_liveqatest_0to{vnummer}.z16\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveqatest_0to{vnummer}.z17") == True:
                url18 = f"http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_0to{vnummer}/retailclient_liveqatest_0to{vnummer}.z17"
                while True:
                    try:
                        wget.download(url18, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_0to{vnummer}/retailclient_liveqatest_0to{vnummer}.z17\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveqatest_0to{vnummer}.z18") == True:
                url19 = f"http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_0to{vnummer}/retailclient_liveqatest_0to{vnummer}.z18"
                while True:
                    try:
                        wget.download(url19, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_0to{vnummer}/retailclient_liveqatest_0to{vnummer}.z18\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveqatest_0to{vnummer}.z19") == True:
                url20 = f"http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_0to{vnummer}/retailclient_liveqatest_0to{vnummer}.z19"
                while True:
                    try:
                        wget.download(url20, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_0to{vnummer}/retailclient_liveqatest_0to{vnummer}.z19\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveqatest_0to{vnummer}.z20") == True:
                url21 = f"http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_0to{vnummer}/retailclient_liveqatest_0to{vnummer}.z20"
                while True:
                    try:
                        wget.download(url21, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_0to{vnummer}/retailclient_liveqatest_0to{vnummer}.z20\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
        if uwert == "XtoY":
            print(f"Download of {vwert} version {vnummerx} started!\nPress CTRL+C to stop.")
            if not os.path.exists(f"{saveloc}/retailclient_liveqatest_{vnummerx}.zip") == True:
                url = f"http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_{vnummerx}/retailclient_liveqatest_{vnummerx}.zip"
                try:
                    wget.download(url, saveloc)
                    print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_{vnummerx}/retailclient_liveqatest_{vnummerx}.zip\n")
                except KeyboardInterrupt:
                    print("\nYou stopped the download!")
                    return
                except Exception as ex:
                    exception = type(ex).__name__
                    argumente = str(ex.args)
                    if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                        print("\nNo Connection. Please try again!")
                        log1_label.config(text="No connection.\nPlease try again!")
                        return
                    else:
                        log1_label.config(text="Version not found!")
                        print("\nVersion not found!\n")
                        return
            if not os.path.exists(f"{saveloc}/retailclient_liveqatest_{vnummerx}.z01") == True:
                url2 = f"http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_{vnummerx}/retailclient_liveqatest_{vnummerx}.z01"
                while True:
                    try:
                        wget.download(url2, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_{vnummerx}/retailclient_liveqatest_{vnummerx}.z01\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveqatest_{vnummerx}.z02") == True:
                url3 = f"http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_{vnummerx}/retailclient_liveqatest_{vnummerx}.z02"
                while True:
                    try:
                        wget.download(url3, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_{vnummerx}/retailclient_liveqatest_{vnummerx}.z02\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveqatest_{vnummerx}.z03") == True:
                url4 = f"http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_{vnummerx}/retailclient_liveqatest_{vnummerx}.z03"
                while True:
                    try:
                        wget.download(url4, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_{vnummerx}/retailclient_liveqatest_{vnummerx}.z03\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveqatest_{vnummerx}.z04") == True:
                url5 = f"http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_{vnummerx}/retailclient_liveqatest_{vnummerx}.z04"
                while True:
                    try:
                        wget.download(url5, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_{vnummerx}/retailclient_liveqatest_{vnummerx}.z04\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveqatest_{vnummerx}.z05") == True:
                url6 = f"http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_{vnummerx}/retailclient_liveqatest_{vnummerx}.z05"
                while True:
                    try:
                        wget.download(url6, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_{vnummerx}/retailclient_liveqatest_{vnummerx}.z05\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveqatest_{vnummerx}.z06") == True:
                url7 = f"http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_{vnummerx}/retailclient_liveqatest_{vnummerx}.z06"
                while True:
                    try:
                        wget.download(url7, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_{vnummerx}/retailclient_liveqatest_{vnummerx}.z06\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveqatest_{vnummerx}.z07") == True:
                url8 = f"http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_{vnummerx}/retailclient_liveqatest_{vnummerx}.z07"
                while True:
                    try:
                        wget.download(url8, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_{vnummerx}/retailclient_liveqatest_{vnummerx}.z07\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveqatest_{vnummerx}.z08") == True:
                url9 = f"http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_{vnummerx}/retailclient_liveqatest_{vnummerx}.z08"
                while True:
                    try:
                        wget.download(url9, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_{vnummerx}/retailclient_liveqatest_{vnummerx}.z08\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveqatest_{vnummerx}.z09") == True:
                url10 = f"http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_{vnummerx}/retailclient_liveqatest_{vnummerx}.z09"
                while True:
                    try:
                        wget.download(url10, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_{vnummerx}/retailclient_liveqatest_{vnummerx}.z09\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveqatest_{vnummerx}.z10") == True:
                url11 = f"http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_{vnummerx}/retailclient_liveqatest_{vnummerx}.z10"
                while True:
                    try:
                        wget.download(url11, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_{vnummerx}/retailclient_liveqatest_{vnummerx}.z10\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveqatest_{vnummerx}.z11") == True:
                url12 = f"http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_{vnummerx}/retailclient_liveqatest_{vnummerx}.z11"
                while True:
                    try:
                        wget.download(url12, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_{vnummerx}/retailclient_liveqatest_{vnummerx}.z11\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveqatest_{vnummerx}.z12") == True:
                url13 = f"http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_{vnummerx}/retailclient_liveqatest_{vnummerx}.z12"
                while True:
                    try:
                        wget.download(url13, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_{vnummerx}/retailclient_liveqatest_{vnummerx}.z12\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveqatest_{vnummerx}.z13") == True:
                url14 = f"http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_{vnummerx}/retailclient_liveqatest_{vnummerx}.z13"
                while True:
                    try:
                        wget.download(url14, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_{vnummerx}/retailclient_liveqatest_{vnummerx}.z13\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveqatest_{vnummerx}.z14") == True:
                url15 = f"http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_{vnummerx}/retailclient_liveqatest_{vnummerx}.z14"
                while True:
                    try:
                        wget.download(url15, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_{vnummerx}/retailclient_liveqatest_{vnummerx}.z14\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveqatest_{vnummerx}.z15") == True:
                url16 = f"http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_{vnummerx}/retailclient_liveqatest_{vnummerx}.z15"
                while True:
                    try:
                        wget.download(url16, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_{vnummerx}/retailclient_liveqatest_{vnummerx}.z15\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveqatest_{vnummerx}.z16") == True:
                url17 = f"http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_{vnummerx}/retailclient_liveqatest_{vnummerx}.z16"
                while True:
                    try:
                        wget.download(url17, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_{vnummerx}/retailclient_liveqatest_{vnummerx}.z16\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveqatest_{vnummerx}.z17") == True:
                url18 = f"http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_{vnummerx}/retailclient_liveqatest_{vnummerx}.z17"
                while True:
                    try:
                        wget.download(url18, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_{vnummerx}/retailclient_liveqatest_{vnummerx}.z17\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveqatest_{vnummerx}.z18") == True:
                url19 = f"http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_{vnummerx}/retailclient_liveqatest_{vnummerx}.z18"
                while True:
                    try:
                        wget.download(url19, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_{vnummerx}/retailclient_liveqatest_{vnummerx}.z18\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveqatest_{vnummerx}.z19") == True:
                url20 = f"http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_{vnummerx}/retailclient_liveqatest_{vnummerx}.z19"
                while True:
                    try:
                        wget.download(url20, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_{vnummerx}/retailclient_liveqatest_{vnummerx}.z19\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveqatest_{vnummerx}.z20") == True:
                url21 = f"http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_{vnummerx}/retailclient_liveqatest_{vnummerx}.z20"
                while True:
                    try:
                        wget.download(url21, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveqatest/retailclient_liveqatest/retailclient_liveqatest_{vnummerx}/retailclient_liveqatest_{vnummerx}.z20\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            log1_label.config(text="Download finished!")
            print("Download finished!\n")
    if vwert == "betatest":
        if uwert == "0toY":
            print(f"Download of {vwert} version 0to{vnummer} started!\nPress CTRL+C to stop.")
            if not os.path.exists(f"{saveloc}/retailclient_betatest_0to{vnummer}.zip") == True:
                url = f"http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_0to{vnummer}/retailclient_betatest_0to{vnummer}.zip"
                try:
                    wget.download(url, saveloc)
                    print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_0to{vnummer}/retailclient_betatest_0to{vnummer}.zip\n")
                except KeyboardInterrupt:
                    print("\nYou stopped the download!")
                    return
                except Exception as ex:
                    exception = type(ex).__name__
                    argumente = str(ex.args)
                    if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                        print("\nNo Connection. Please try again!")
                        log1_label.config(text="No connection.\nPlease try again!")
                        return
                    else:
                        log1_label.config(text="Version not found!")
                        print("\nVersion not found!\n")
                        return
            if not os.path.exists(f"{saveloc}/retailclient_betatest_0to{vnummer}.z01") == True:
                url2 = f"http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_0to{vnummer}/retailclient_betatest_0to{vnummer}.z01"
                while True:
                    try:
                        wget.download(url2, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_0to{vnummer}/retailclient_betatest_0to{vnummer}.z01\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_betatest_0to{vnummer}.z02") == True:
                url3 = f"http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_0to{vnummer}/retailclient_betatest_0to{vnummer}.z02"
                while True:
                    try:
                        wget.download(url3, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_0to{vnummer}/retailclient_betatest_0to{vnummer}.z02\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_betatest_0to{vnummer}.z03") == True:
                url4 = f"http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_0to{vnummer}/retailclient_betatest_0to{vnummer}.z03"
                while True:
                    try:
                        wget.download(url4, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_0to{vnummer}/retailclient_betatest_0to{vnummer}.z03\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_betatest_0to{vnummer}.z04") == True:
                url5 = f"http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_0to{vnummer}/retailclient_betatest_0to{vnummer}.z04"
                while True:
                    try:
                        wget.download(url5, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_0to{vnummer}/retailclient_betatest_0to{vnummer}.z04\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_betatest_0to{vnummer}.z05") == True:
                url6 = f"http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_0to{vnummer}/retailclient_betatest_0to{vnummer}.z05"
                while True:
                    try:
                        wget.download(url6, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_0to{vnummer}/retailclient_betatest_0to{vnummer}.z05\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_betatest_0to{vnummer}.z06") == True:
                url7 = f"http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_0to{vnummer}/retailclient_betatest_0to{vnummer}.z06"
                while True:
                    try:
                        wget.download(url7, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_0to{vnummer}/retailclient_betatest_0to{vnummer}.z06\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_betatest_0to{vnummer}.z07") == True:
                url8 = f"http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_0to{vnummer}/retailclient_betatest_0to{vnummer}.z07"
                while True:
                    try:
                        wget.download(url8, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_0to{vnummer}/retailclient_betatest_0to{vnummer}.z07\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_betatest_0to{vnummer}.z08") == True:
                url9 = f"http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_0to{vnummer}/retailclient_betatest_0to{vnummer}.z08"
                while True:
                    try:
                        wget.download(url9, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_0to{vnummer}/retailclient_betatest_0to{vnummer}.z08\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_betatest_0to{vnummer}.z09") == True:
                url10 = f"http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_0to{vnummer}/retailclient_betatest_0to{vnummer}.z09"
                while True:
                    try:
                        wget.download(url10, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_0to{vnummer}/retailclient_betatest_0to{vnummer}.z09\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_betatest_0to{vnummer}.z10") == True:
                url11 = f"http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_0to{vnummer}/retailclient_betatest_0to{vnummer}.z10"
                while True:
                    try:
                        wget.download(url11, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_0to{vnummer}/retailclient_betatest_0to{vnummer}.z10\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_betatest_0to{vnummer}.z11") == True:
                url12 = f"http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_0to{vnummer}/retailclient_betatest_0to{vnummer}.z11"
                while True:
                    try:
                        wget.download(url12, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_0to{vnummer}/retailclient_betatest_0to{vnummer}.z11\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_betatest_0to{vnummer}.z12") == True:
                url13 = f"http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_0to{vnummer}/retailclient_betatest_0to{vnummer}.z12"
                while True:
                    try:
                        wget.download(url13, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_0to{vnummer}/retailclient_betatest_0to{vnummer}.z12\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_betatest_0to{vnummer}.z13") == True:
                url14 = f"http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_0to{vnummer}/retailclient_betatest_0to{vnummer}.z13"
                while True:
                    try:
                        wget.download(url14, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_0to{vnummer}/retailclient_betatest_0to{vnummer}.z13\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_betatest_0to{vnummer}.z14") == True:
                url15 = f"http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_0to{vnummer}/retailclient_betatest_0to{vnummer}.z14"
                while True:
                    try:
                        wget.download(url15, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_0to{vnummer}/retailclient_betatest_0to{vnummer}.z14\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_betatest_0to{vnummer}.z15") == True:
                url16 = f"http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_0to{vnummer}/retailclient_betatest_0to{vnummer}.z15"
                while True:
                    try:
                        wget.download(url16, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_0to{vnummer}/retailclient_betatest_0to{vnummer}.z15\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_betatest_0to{vnummer}.z16") == True:
                url17 = f"http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_0to{vnummer}/retailclient_betatest_0to{vnummer}.z16"
                while True:
                    try:
                        wget.download(url17, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_0to{vnummer}/retailclient_betatest_0to{vnummer}.z16\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_betatest_0to{vnummer}.z17") == True:
                url18 = f"http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_0to{vnummer}/retailclient_betatest_0to{vnummer}.z17"
                while True:
                    try:
                        wget.download(url18, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_0to{vnummer}/retailclient_betatest_0to{vnummer}.z17\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_betatest_0to{vnummer}.z18") == True:
                url19 = f"http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_0to{vnummer}/retailclient_betatest_0to{vnummer}.z18"
                while True:
                    try:
                        wget.download(url19, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_0to{vnummer}/retailclient_betatest_0to{vnummer}.z18\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_betatest_0to{vnummer}.z19") == True:
                url20 = f"http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_0to{vnummer}/retailclient_betatest_0to{vnummer}.z19"
                while True:
                    try:
                        wget.download(url20, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_0to{vnummer}/retailclient_betatest_0to{vnummer}.z19\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_betatest_0to{vnummer}.z20") == True:
                url21 = f"http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_0to{vnummer}/retailclient_betatest_0to{vnummer}.z20"
                while True:
                    try:
                        wget.download(url21, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_0to{vnummer}/retailclient_betatest_0to{vnummer}.z20\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
        if uwert == "XtoY":
            print(f"Download of {vwert} version {vnummerx} started!\nPress CTRL+C to stop.")
            if not os.path.exists(f"{saveloc}/retailclient_betatest_{vnummerx}.zip") == True:
                url = f"http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_{vnummerx}/retailclient_betatest_{vnummerx}.zip"
                try:
                    wget.download(url, saveloc)
                    print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_{vnummerx}/retailclient_betatest_{vnummerx}.zip\n")
                except KeyboardInterrupt:
                    print("\nYou stopped the download!")
                    return
                except Exception as ex:
                    exception = type(ex).__name__
                    argumente = str(ex.args)
                    if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                        print("\nNo Connection. Please try again!")
                        log1_label.config(text="No connection.\nPlease try again!")
                        return
                    else:
                        log1_label.config(text="Version not found!")
                        print("\nVersion not found!\n")
                        return
            if not os.path.exists(f"{saveloc}/retailclient_betatest_{vnummerx}.z01") == True:
                url2 = f"http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_{vnummerx}/retailclient_betatest_{vnummerx}.z01"
                while True:
                    try:
                        wget.download(url2, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_{vnummerx}/retailclient_betatest_{vnummerx}.z01\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_betatest_{vnummerx}.z02") == True:
                url3 = f"http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_{vnummerx}/retailclient_betatest_{vnummerx}.z02"
                while True:
                    try:
                        wget.download(url3, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_{vnummerx}/retailclient_betatest_{vnummerx}.z02\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_betatest_{vnummerx}.z03") == True:
                url4 = f"http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_{vnummerx}/retailclient_betatest_{vnummerx}.z03"
                while True:
                    try:
                        wget.download(url4, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_{vnummerx}/retailclient_betatest_{vnummerx}.z03\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_betatest_{vnummerx}.z04") == True:
                url5 = f"http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_{vnummerx}/retailclient_betatest_{vnummerx}.z04"
                while True:
                    try:
                        wget.download(url5, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_{vnummerx}/retailclient_betatest_{vnummerx}.z04\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_betatest_{vnummerx}.z05") == True:
                url6 = f"http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_{vnummerx}/retailclient_betatest_{vnummerx}.z05"
                while True:
                    try:
                        wget.download(url6, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_{vnummerx}/retailclient_betatest_{vnummerx}.z05\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_betatest_{vnummerx}.z06") == True:
                url7 = f"http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_{vnummerx}/retailclient_betatest_{vnummerx}.z06"
                while True:
                    try:
                        wget.download(url7, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_{vnummerx}/retailclient_betatest_{vnummerx}.z06\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_betatest_{vnummerx}.z07") == True:
                url8 = f"http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_{vnummerx}/retailclient_betatest_{vnummerx}.z07"
                while True:
                    try:
                        wget.download(url8, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_{vnummerx}/retailclient_betatest_{vnummerx}.z07\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_betatest_{vnummerx}.z08") == True:
                url9 = f"http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_{vnummerx}/retailclient_betatest_{vnummerx}.z08"
                while True:
                    try:
                        wget.download(url9, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_{vnummerx}/retailclient_betatest_{vnummerx}.z08\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_betatest_{vnummerx}.z09") == True:
                url10 = f"http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_{vnummerx}/retailclient_betatest_{vnummerx}.z09"
                while True:
                    try:
                        wget.download(url10, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_{vnummerx}/retailclient_betatest_{vnummerx}.z09\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_betatest_{vnummerx}.z10") == True:
                url11 = f"http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_{vnummerx}/retailclient_betatest_{vnummerx}.z10"
                while True:
                    try:
                        wget.download(url11, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_{vnummerx}/retailclient_betatest_{vnummerx}.z10\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_betatest_{vnummerx}.z11") == True:
                url12 = f"http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_{vnummerx}/retailclient_betatest_{vnummerx}.z11"
                while True:
                    try:
                        wget.download(url12, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_{vnummerx}/retailclient_betatest_{vnummerx}.z11\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_betatest_{vnummerx}.z12") == True:
                url13 = f"http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_{vnummerx}/retailclient_betatest_{vnummerx}.z12"
                while True:
                    try:
                        wget.download(url13, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_{vnummerx}/retailclient_betatest_{vnummerx}.z12\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_betatest_{vnummerx}.z13") == True:
                url14 = f"http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_{vnummerx}/retailclient_betatest_{vnummerx}.z13"
                while True:
                    try:
                        wget.download(url14, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_{vnummerx}/retailclient_betatest_{vnummerx}.z13\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_betatest_{vnummerx}.z14") == True:
                url15 = f"http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_{vnummerx}/retailclient_betatest_{vnummerx}.z14"
                while True:
                    try:
                        wget.download(url15, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_{vnummerx}/retailclient_betatest_{vnummerx}.z14\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_betatest_{vnummerx}.z15") == True:
                url16 = f"http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_{vnummerx}/retailclient_betatest_{vnummerx}.z15"
                while True:
                    try:
                        wget.download(url16, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_{vnummerx}/retailclient_betatest_{vnummerx}.z15\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_betatest_{vnummerx}.z16") == True:
                url17 = f"http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_{vnummerx}/retailclient_betatest_{vnummerx}.z16"
                while True:
                    try:
                        wget.download(url17, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_{vnummerx}/retailclient_betatest_{vnummerx}.z16\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_betatest_{vnummerx}.z17") == True:
                url18 = f"http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_{vnummerx}/retailclient_betatest_{vnummerx}.z17"
                while True:
                    try:
                        wget.download(url18, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_{vnummerx}/retailclient_betatest_{vnummerx}.z17\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_betatest_{vnummerx}.z18") == True:
                url19 = f"http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_{vnummerx}/retailclient_betatest_{vnummerx}.z18"
                while True:
                    try:
                        wget.download(url19, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_{vnummerx}/retailclient_betatest_{vnummerx}.z18\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_betatest_{vnummerx}.z19") == True:
                url20 = f"http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_{vnummerx}/retailclient_betatest_{vnummerx}.z19"
                while True:
                    try:
                        wget.download(url20, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_{vnummerx}/retailclient_betatest_{vnummerx}.z19\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_betatest_{vnummerx}.z20") == True:
                url21 = f"http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_{vnummerx}/retailclient_betatest_{vnummerx}.z20"
                while True:
                    try:
                        wget.download(url21, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/betatest/retailclient_betatest/retailclient_betatest_{vnummerx}/retailclient_betatest_{vnummerx}.z20\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            log1_label.config(text="Download finished!")
            print("Download finished!\n")
    if vwert == "cstraining":
        if uwert == "0toY":
            print(f"Download of {vwert} version 0to{vnummer} started!\nPress CTRL+C to stop.")
            if not os.path.exists(f"{saveloc}/retailclient_cstraining_0to{vnummer}.zip") == True:
                url = f"http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_0to{vnummer}/retailclient_cstraining_0to{vnummer}.zip"
                try:
                    wget.download(url, saveloc)
                    print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_0to{vnummer}/retailclient_cstraining_0to{vnummer}.zip\n")
                except KeyboardInterrupt:
                    print("\nYou stopped the download!")
                    return
                except Exception as ex:
                    exception = type(ex).__name__
                    argumente = str(ex.args)
                    if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                        print("\nNo Connection. Please try again!")
                        log1_label.config(text="No connection.\nPlease try again!")
                        return
                    else:
                        log1_label.config(text="Version not found!")
                        print("\nVersion not found!\n")
                        return
            if not os.path.exists(f"{saveloc}/retailclient_cstraining_0to{vnummer}.z01") == True:
                url2 = f"http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_0to{vnummer}/retailclient_cstraining_0to{vnummer}.z01"
                while True:
                    try:
                        wget.download(url2, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_0to{vnummer}/retailclient_cstraining_0to{vnummer}.z01\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_cstraining_0to{vnummer}.z02") == True:
                url3 = f"http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_0to{vnummer}/retailclient_cstraining_0to{vnummer}.z02"
                while True:
                    try:
                        wget.download(url3, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_0to{vnummer}/retailclient_cstraining_0to{vnummer}.z02\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_cstraining_0to{vnummer}.z03") == True:
                url4 = f"http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_0to{vnummer}/retailclient_cstraining_0to{vnummer}.z03"
                while True:
                    try:
                        wget.download(url4, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_0to{vnummer}/retailclient_cstraining_0to{vnummer}.z03\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_cstraining_0to{vnummer}.z04") == True:
                url5 = f"http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_0to{vnummer}/retailclient_cstraining_0to{vnummer}.z04"
                while True:
                    try:
                        wget.download(url5, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_0to{vnummer}/retailclient_cstraining_0to{vnummer}.z04\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_cstraining_0to{vnummer}.z05") == True:
                url6 = f"http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_0to{vnummer}/retailclient_cstraining_0to{vnummer}.z05"
                while True:
                    try:
                        wget.download(url6, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_0to{vnummer}/retailclient_cstraining_0to{vnummer}.z05\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_cstraining_0to{vnummer}.z06") == True:
                url7 = f"http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_0to{vnummer}/retailclient_cstraining_0to{vnummer}.z06"
                while True:
                    try:
                        wget.download(url7, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_0to{vnummer}/retailclient_cstraining_0to{vnummer}.z06\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_cstraining_0to{vnummer}.z07") == True:
                url8 = f"http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_0to{vnummer}/retailclient_cstraining_0to{vnummer}.z07"
                while True:
                    try:
                        wget.download(url8, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_0to{vnummer}/retailclient_cstraining_0to{vnummer}.z07\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_cstraining_0to{vnummer}.z08") == True:
                url9 = f"http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_0to{vnummer}/retailclient_cstraining_0to{vnummer}.z08"
                while True:
                    try:
                        wget.download(url9, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_0to{vnummer}/retailclient_cstraining_0to{vnummer}.z08\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_cstraining_0to{vnummer}.z09") == True:
                url10 = f"http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_0to{vnummer}/retailclient_cstraining_0to{vnummer}.z09"
                while True:
                    try:
                        wget.download(url10, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_0to{vnummer}/retailclient_cstraining_0to{vnummer}.z09\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_cstraining_0to{vnummer}.z10") == True:
                url11 = f"http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_0to{vnummer}/retailclient_cstraining_0to{vnummer}.z10"
                while True:
                    try:
                        wget.download(url11, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_0to{vnummer}/retailclient_cstraining_0to{vnummer}.z10\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_cstraining_0to{vnummer}.z11") == True:
                url12 = f"http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_0to{vnummer}/retailclient_cstraining_0to{vnummer}.z11"
                while True:
                    try:
                        wget.download(url12, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_0to{vnummer}/retailclient_cstraining_0to{vnummer}.z11\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_cstraining_0to{vnummer}.z12") == True:
                url13 = f"http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_0to{vnummer}/retailclient_cstraining_0to{vnummer}.z12"
                while True:
                    try:
                        wget.download(url13, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_0to{vnummer}/retailclient_cstraining_0to{vnummer}.z12\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_cstraining_0to{vnummer}.z13") == True:
                url14 = f"http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_0to{vnummer}/retailclient_cstraining_0to{vnummer}.z13"
                while True:
                    try:
                        wget.download(url14, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_0to{vnummer}/retailclient_cstraining_0to{vnummer}.z13\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_cstraining_0to{vnummer}.z14") == True:
                url15 = f"http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_0to{vnummer}/retailclient_cstraining_0to{vnummer}.z14"
                while True:
                    try:
                        wget.download(url15, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_0to{vnummer}/retailclient_cstraining_0to{vnummer}.z14\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_cstraining_0to{vnummer}.z15") == True:
                url16 = f"http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_0to{vnummer}/retailclient_cstraining_0to{vnummer}.z15"
                while True:
                    try:
                        wget.download(url16, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_0to{vnummer}/retailclient_cstraining_0to{vnummer}.z15\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_cstraining_0to{vnummer}.z16") == True:
                url17 = f"http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_0to{vnummer}/retailclient_cstraining_0to{vnummer}.z16"
                while True:
                    try:
                        wget.download(url17, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_0to{vnummer}/retailclient_cstraining_0to{vnummer}.z16\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_cstraining_0to{vnummer}.z17") == True:
                url18 = f"http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_0to{vnummer}/retailclient_cstraining_0to{vnummer}.z17"
                while True:
                    try:
                        wget.download(url18, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_0to{vnummer}/retailclient_cstraining_0to{vnummer}.z17\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_cstraining_0to{vnummer}.z18") == True:
                url19 = f"http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_0to{vnummer}/retailclient_cstraining_0to{vnummer}.z18"
                while True:
                    try:
                        wget.download(url19, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_0to{vnummer}/retailclient_cstraining_0to{vnummer}.z18\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_cstraining_0to{vnummer}.z19") == True:
                url20 = f"http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_0to{vnummer}/retailclient_cstraining_0to{vnummer}.z19"
                while True:
                    try:
                        wget.download(url20, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_0to{vnummer}/retailclient_cstraining_0to{vnummer}.z19\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_cstraining_0to{vnummer}.z20") == True:
                url21 = f"http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_0to{vnummer}/retailclient_cstraining_0to{vnummer}.z20"
                while True:
                    try:
                        wget.download(url21, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_0to{vnummer}/retailclient_cstraining_0to{vnummer}.z20\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            log1_label.config(text="Download finished!")
            print("Download finished!\n")
        if uwert == "XtoY":
            print(f"Download of {vwert} version {vnummerx} started!\nPress CTRL+C to stop.")
            if not os.path.exists(f"{saveloc}/retailclient_cstraining_{vnummerx}.zip") == True:
                url = f"http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_{vnummerx}/retailclient_cstraining_{vnummerx}.zip"
                try:
                    wget.download(url, saveloc)
                    print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_{vnummerx}/retailclient_cstraining_{vnummerx}.zip\n")
                except KeyboardInterrupt:
                    print("\nYou stopped the download!")
                    return
                except Exception as ex:
                    exception = type(ex).__name__
                    argumente = str(ex.args)
                    if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                        print("\nNo Connection. Please try again!")
                        log1_label.config(text="No connection.\nPlease try again!")
                        return
                    else:
                        log1_label.config(text="Version not found!")
                        print("\nVersion not found!\n")
                        return
            if not os.path.exists(f"{saveloc}/retailclient_cstraining_{vnummerx}.z01") == True:
                url2 = f"http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_{vnummerx}/retailclient_cstraining_{vnummerx}.z01"
                while True:
                    try:
                        wget.download(url2, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_{vnummerx}/retailclient_cstraining_{vnummerx}.z01\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_cstraining_{vnummerx}.z02") == True:
                url3 = f"http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_{vnummerx}/retailclient_cstraining_{vnummerx}.z02"
                while True:
                    try:
                        wget.download(url3, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_{vnummerx}/retailclient_cstraining_{vnummerx}.z02\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_cstraining_{vnummerx}.z03") == True:
                url4 = f"http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_{vnummerx}/retailclient_cstraining_{vnummerx}.z03"
                while True:
                    try:
                        wget.download(url4, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_{vnummerx}/retailclient_cstraining_{vnummerx}.z03\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_cstraining_{vnummerx}.z04") == True:
                url5 = f"http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_{vnummerx}/retailclient_cstraining_{vnummerx}.z04"
                while True:
                    try:
                        wget.download(url5, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_{vnummerx}/retailclient_cstraining_{vnummerx}.z04\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_cstraining_{vnummerx}.z05") == True:
                url6 = f"http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_{vnummerx}/retailclient_cstraining_{vnummerx}.z05"
                while True:
                    try:
                        wget.download(url6, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_{vnummerx}/retailclient_cstraining_{vnummerx}.z05\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_cstraining_{vnummerx}.z06") == True:
                url7 = f"http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_{vnummerx}/retailclient_cstraining_{vnummerx}.z06"
                while True:
                    try:
                        wget.download(url7, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_{vnummerx}/retailclient_cstraining_{vnummerx}.z06\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_cstraining_{vnummerx}.z07") == True:
                url8 = f"http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_{vnummerx}/retailclient_cstraining_{vnummerx}.z07"
                while True:
                    try:
                        wget.download(url8, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_{vnummerx}/retailclient_cstraining_{vnummerx}.z07\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_cstraining_{vnummerx}.z08") == True:
                url9 = f"http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_{vnummerx}/retailclient_cstraining_{vnummerx}.z08"
                while True:
                    try:
                        wget.download(url9, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_{vnummerx}/retailclient_cstraining_{vnummerx}.z08\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_cstraining_{vnummerx}.z09") == True:
                url10 = f"http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_{vnummerx}/retailclient_cstraining_{vnummerx}.z09"
                while True:
                    try:
                        wget.download(url10, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_{vnummerx}/retailclient_cstraining_{vnummerx}.z09\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_cstraining_{vnummerx}.z10") == True:
                url11 = f"http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_{vnummerx}/retailclient_cstraining_{vnummerx}.z10"
                while True:
                    try:
                        wget.download(url11, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_{vnummerx}/retailclient_cstraining_{vnummerx}.z10\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_cstraining_{vnummerx}.z11") == True:
                url12 = f"http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_{vnummerx}/retailclient_cstraining_{vnummerx}.z11"
                while True:
                    try:
                        wget.download(url12, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_{vnummerx}/retailclient_cstraining_{vnummerx}.z11\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_cstraining_{vnummerx}.z12") == True:
                url13 = f"http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_{vnummerx}/retailclient_cstraining_{vnummerx}.z12"
                while True:
                    try:
                        wget.download(url13, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_{vnummerx}/retailclient_cstraining_{vnummerx}.z12\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_cstraining_{vnummerx}.z13") == True:
                url14 = f"http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_{vnummerx}/retailclient_cstraining_{vnummerx}.z13"
                while True:
                    try:
                        wget.download(url14, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_{vnummerx}/retailclient_cstraining_{vnummerx}.z13\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_cstraining_{vnummerx}.z14") == True:
                url15 = f"http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_{vnummerx}/retailclient_cstraining_{vnummerx}.z14"
                while True:
                    try:
                        wget.download(url15, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_{vnummerx}/retailclient_cstraining_{vnummerx}.z14\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_cstraining_{vnummerx}.z15") == True:
                url16 = f"http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_{vnummerx}/retailclient_cstraining_{vnummerx}.z15"
                while True:
                    try:
                        wget.download(url16, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_{vnummerx}/retailclient_cstraining_{vnummerx}.z15\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_cstraining_{vnummerx}.z16") == True:
                url17 = f"http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_{vnummerx}/retailclient_cstraining_{vnummerx}.z16"
                while True:
                    try:
                        wget.download(url17, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_{vnummerx}/retailclient_cstraining_{vnummerx}.z16\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_cstraining_{vnummerx}.z17") == True:
                url18 = f"http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_{vnummerx}/retailclient_cstraining_{vnummerx}.z17"
                while True:
                    try:
                        wget.download(url18, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_{vnummerx}/retailclient_cstraining_{vnummerx}.z17\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_cstraining_{vnummerx}.z18") == True:
                url19 = f"http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_{vnummerx}/retailclient_cstraining_{vnummerx}.z18"
                while True:
                    try:
                        wget.download(url19, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_{vnummerx}/retailclient_cstraining_{vnummerx}.z18\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_cstraining_{vnummerx}.z19") == True:
                url20 = f"http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_{vnummerx}/retailclient_cstraining_{vnummerx}.z19"
                while True:
                    try:
                        wget.download(url20, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_{vnummerx}/retailclient_cstraining_{vnummerx}.z19\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_cstraining_{vnummerx}.z20") == True:
                url21 = f"http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_{vnummerx}/retailclient_cstraining_{vnummerx}.z20"
                while True:
                    try:
                        wget.download(url21, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/cstraining/retailclient_cstraining/retailclient_cstraining_{vnummerx}/retailclient_cstraining_{vnummerx}.z20\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            log1_label.config(text="Download finished!")
            print("Download finished!\n")
    if vwert == "liveeptest":
        if uwert == "0toY":
            print(f"Download of {vwert} version 0to{vnummer} started!\nPress CTRL+C to stop.")
            if not os.path.exists(f"{saveloc}/retailclient_liveeptest_0to{vnummer}.zip") == True:
                url = f"http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_0to{vnummer}/retailclient_liveeptest_0to{vnummer}.zip"
                try:
                    wget.download(url, saveloc)
                    print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_0to{vnummer}/retailclient_liveeptest_0to{vnummer}.zip\n")
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
                        log1_label.config(text="Download finished!")
                        print("\nDownload finished!\n")
                        return
            if not os.path.exists(f"{saveloc}/retailclient_liveeptest_0to{vnummer}.z01") == True:
                url2 = f"http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_0to{vnummer}/retailclient_liveeptest_0to{vnummer}.z01"
                while True:
                    try:
                        wget.download(url2, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_0to{vnummer}/retailclient_liveeptest_0to{vnummer}.z01\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveeptest_0to{vnummer}.z02") == True:
                url3 = f"http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_0to{vnummer}/retailclient_liveeptest_0to{vnummer}.z02"
                while True:
                    try:
                        wget.download(url3, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_0to{vnummer}/retailclient_liveeptest_0to{vnummer}.z02\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveeptest_0to{vnummer}.z03") == True:
                url4 = f"http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_0to{vnummer}/retailclient_liveeptest_0to{vnummer}.z03"
                while True:
                    try:
                        wget.download(url4, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_0to{vnummer}/retailclient_liveeptest_0to{vnummer}.z03\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveeptest_0to{vnummer}.z04") == True:
                url5 = f"http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_0to{vnummer}/retailclient_liveeptest_0to{vnummer}.z04"
                while True:
                    try:
                        wget.download(url5, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_0to{vnummer}/retailclient_liveeptest_0to{vnummer}.z04\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveeptest_0to{vnummer}.z05") == True:
                url6 = f"http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_0to{vnummer}/retailclient_liveeptest_0to{vnummer}.z05"
                while True:
                    try:
                        wget.download(url6, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_0to{vnummer}/retailclient_liveeptest_0to{vnummer}.z05\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveeptest_0to{vnummer}.z06") == True:
                url7 = f"http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_0to{vnummer}/retailclient_liveeptest_0to{vnummer}.z06"
                while True:
                    try:
                        wget.download(url7, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_0to{vnummer}/retailclient_liveeptest_0to{vnummer}.z06\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveeptest_0to{vnummer}.z07") == True:
                url8 = f"http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_0to{vnummer}/retailclient_liveeptest_0to{vnummer}.z07"
                while True:
                    try:
                        wget.download(url8, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_0to{vnummer}/retailclient_liveeptest_0to{vnummer}.z07\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveeptest_0to{vnummer}.z08") == True:
                url9 = f"http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_0to{vnummer}/retailclient_liveeptest_0to{vnummer}.z08"
                while True:
                    try:
                        wget.download(url9, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_0to{vnummer}/retailclient_liveeptest_0to{vnummer}.z08\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveeptest_0to{vnummer}.z09") == True:
                url10 = f"http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_0to{vnummer}/retailclient_liveeptest_0to{vnummer}.z09"
                while True:
                    try:
                        wget.download(url10, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_0to{vnummer}/retailclient_liveeptest_0to{vnummer}.z09\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveeptest_0to{vnummer}.z10") == True:
                url11 = f"http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_0to{vnummer}/retailclient_liveeptest_0to{vnummer}.z10"
                while True:
                    try:
                        wget.download(url11, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_0to{vnummer}/retailclient_liveeptest_0to{vnummer}.z10\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveeptest_0to{vnummer}.z11") == True:
                url12 = f"http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_0to{vnummer}/retailclient_liveeptest_0to{vnummer}.z11"
                while True:
                    try:
                        wget.download(url12, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_0to{vnummer}/retailclient_liveeptest_0to{vnummer}.z11\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveeptest_0to{vnummer}.z12") == True:
                url13 = f"http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_0to{vnummer}/retailclient_liveeptest_0to{vnummer}.z12"
                while True:
                    try:
                        wget.download(url13, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_0to{vnummer}/retailclient_liveeptest_0to{vnummer}.z12\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveeptest_0to{vnummer}.z13") == True:
                url14 = f"http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_0to{vnummer}/retailclient_liveeptest_0to{vnummer}.z13"
                while True:
                    try:
                        wget.download(url14, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_0to{vnummer}/retailclient_liveeptest_0to{vnummer}.z13\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveeptest_0to{vnummer}.z14") == True:
                url15 = f"http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_0to{vnummer}/retailclient_liveeptest_0to{vnummer}.z14"
                while True:
                    try:
                        wget.download(url15, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_0to{vnummer}/retailclient_liveeptest_0to{vnummer}.z14\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveeptest_0to{vnummer}.z15") == True:
                url16 = f"http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_0to{vnummer}/retailclient_liveeptest_0to{vnummer}.z15"
                while True:
                    try:
                        wget.download(url16, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_0to{vnummer}/retailclient_liveeptest_0to{vnummer}.z15\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveeptest_0to{vnummer}.z16") == True:
                url17 = f"http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_0to{vnummer}/retailclient_liveeptest_0to{vnummer}.z16"
                while True:
                    try:
                        wget.download(url17, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_0to{vnummer}/retailclient_liveeptest_0to{vnummer}.z16\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveeptest_0to{vnummer}.z17") == True:
                url18 = f"http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_0to{vnummer}/retailclient_liveeptest_0to{vnummer}.z17"
                while True:
                    try:
                        wget.download(url18, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_0to{vnummer}/retailclient_liveeptest_0to{vnummer}.z17\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveeptest_0to{vnummer}.z18") == True:
                url19 = f"http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_0to{vnummer}/retailclient_liveeptest_0to{vnummer}.z18"
                while True:
                    try:
                        wget.download(url19, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_0to{vnummer}/retailclient_liveeptest_0to{vnummer}.z18\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveeptest_0to{vnummer}.z19") == True:
                url20 = f"http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_0to{vnummer}/retailclient_liveeptest_0to{vnummer}.z19"
                while True:
                    try:
                        wget.download(url20, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_0to{vnummer}/retailclient_liveeptest_0to{vnummer}.z19\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveeptest_0to{vnummer}.z20") == True:
                url21 = f"http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_0to{vnummer}/retailclient_liveeptest_0to{vnummer}.z20"
                while True:
                    try:
                        wget.download(url21, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_0to{vnummer}/retailclient_liveeptest_0to{vnummer}.z20\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            log1_label.config(text="Download finished!")
            print("Download finished!\n")
        if uwert == "XtoY":
            print(f"Download of {vwert} version {vnummerx} started!\nPress CTRL+C to stop.")
            if not os.path.exists(f"{saveloc}/retailclient_liveeptest_{vnummerx}.zip") == True:
                url = f"http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_{vnummerx}/retailclient_liveeptest_{vnummerx}.zip"
                try:
                    wget.download(url, saveloc)
                    print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_{vnummerx}/retailclient_liveeptest_{vnummerx}.zip\n")
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
                        log1_label.config(text="Download finished!")
                        print("\nDownload finished!\n")
                        return
            if not os.path.exists(f"{saveloc}/retailclient_liveeptest_{vnummerx}.z01") == True:
                url2 = f"http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_{vnummerx}/retailclient_liveeptest_{vnummerx}.z01"
                while True:
                    try:
                        wget.download(url2, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_{vnummerx}/retailclient_liveeptest_{vnummerx}.z01\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveeptest_{vnummerx}.z02") == True:
                url3 = f"http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_{vnummerx}/retailclient_liveeptest_{vnummerx}.z02"
                while True:
                    try:
                        wget.download(url3, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_{vnummerx}/retailclient_liveeptest_{vnummerx}.z02\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveeptest_{vnummerx}.z03") == True:
                url4 = f"http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_{vnummerx}/retailclient_liveeptest_{vnummerx}.z03"
                while True:
                    try:
                        wget.download(url4, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_{vnummerx}/retailclient_liveeptest_{vnummerx}.z03\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveeptest_{vnummerx}.z04") == True:
                url5 = f"http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_{vnummerx}/retailclient_liveeptest_{vnummerx}.z04"
                while True:
                    try:
                        wget.download(url5, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_{vnummerx}/retailclient_liveeptest_{vnummerx}.z04\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveeptest_{vnummerx}.z05") == True:
                url6 = f"http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_{vnummerx}/retailclient_liveeptest_{vnummerx}.z05"
                while True:
                    try:
                        wget.download(url6, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_{vnummerx}/retailclient_liveeptest_{vnummerx}.z05\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveeptest_{vnummerx}.z06") == True:
                url7 = f"http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_{vnummerx}/retailclient_liveeptest_{vnummerx}.z06"
                while True:
                    try:
                        wget.download(url7, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_{vnummerx}/retailclient_liveeptest_{vnummerx}.z06\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveeptest_{vnummerx}.z07") == True:
                url8 = f"http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_{vnummerx}/retailclient_liveeptest_{vnummerx}.z07"
                while True:
                    try:
                        wget.download(url8, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_{vnummerx}/retailclient_liveeptest_{vnummerx}.z07\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveeptest_{vnummerx}.z08") == True:
                url9 = f"http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_{vnummerx}/retailclient_liveeptest_{vnummerx}.z08"
                while True:
                    try:
                        wget.download(url9, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_{vnummerx}/retailclient_liveeptest_{vnummerx}.z08\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveeptest_{vnummerx}.z09") == True:
                url10 = f"http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_{vnummerx}/retailclient_liveeptest_{vnummerx}.z09"
                while True:
                    try:
                        wget.download(url10, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_{vnummerx}/retailclient_liveeptest_{vnummerx}.z09\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveeptest_{vnummerx}.z10") == True:
                url11 = f"http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_{vnummerx}/retailclient_liveeptest_{vnummerx}.z10"
                while True:
                    try:
                        wget.download(url11, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_{vnummerx}/retailclient_liveeptest_{vnummerx}.z10\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveeptest_{vnummerx}.z11") == True:
                url12 = f"http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_{vnummerx}/retailclient_liveeptest_{vnummerx}.z11"
                while True:
                    try:
                        wget.download(url12, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_{vnummerx}/retailclient_liveeptest_{vnummerx}.z11\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveeptest_{vnummerx}.z12") == True:
                url13 = f"http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_{vnummerx}/retailclient_liveeptest_{vnummerx}.z12"
                while True:
                    try:
                        wget.download(url13, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_{vnummerx}/retailclient_liveeptest_{vnummerx}.z12\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveeptest_{vnummerx}.z13") == True:
                url14 = f"http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_{vnummerx}/retailclient_liveeptest_{vnummerx}.z13"
                while True:
                    try:
                        wget.download(url14, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_{vnummerx}/retailclient_liveeptest_{vnummerx}.z13\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveeptest_{vnummerx}.z14") == True:
                url15 = f"http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_{vnummerx}/retailclient_liveeptest_{vnummerx}.z14"
                while True:
                    try:
                        wget.download(url15, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_{vnummerx}/retailclient_liveeptest_{vnummerx}.z14\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveeptest_{vnummerx}.z15") == True:
                url16 = f"http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_{vnummerx}/retailclient_liveeptest_{vnummerx}.z15"
                while True:
                    try:
                        wget.download(url16, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_{vnummerx}/retailclient_liveeptest_{vnummerx}.z15\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveeptest_{vnummerx}.z16") == True:
                url17 = f"http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_{vnummerx}/retailclient_liveeptest_{vnummerx}.z16"
                while True:
                    try:
                        wget.download(url17, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_{vnummerx}/retailclient_liveeptest_{vnummerx}.z16\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveeptest_{vnummerx}.z17") == True:
                url18 = f"http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_{vnummerx}/retailclient_liveeptest_{vnummerx}.z17"
                while True:
                    try:
                        wget.download(url18, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_{vnummerx}/retailclient_liveeptest_{vnummerx}.z17\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveeptest_{vnummerx}.z18") == True:
                url19 = f"http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_{vnummerx}/retailclient_liveeptest_{vnummerx}.z18"
                while True:
                    try:
                        wget.download(url19, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_{vnummerx}/retailclient_liveeptest_{vnummerx}.z18\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveeptest_{vnummerx}.z19") == True:
                url20 = f"http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_{vnummerx}/retailclient_liveeptest_{vnummerx}.z19"
                while True:
                    try:
                        wget.download(url20, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_{vnummerx}/retailclient_liveeptest_{vnummerx}.z19\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            if not os.path.exists(f"{saveloc}/retailclient_liveeptest_{vnummerx}.z20") == True:
                url21 = f"http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_{vnummerx}/retailclient_liveeptest_{vnummerx}.z20"
                while True:
                    try:
                        wget.download(url21, saveloc)
                        print(f"\nDownloaded: http://cdn-patch.swtor.com/patch/liveeptest/retailclient_liveeptest/retailclient_liveeptest_{vnummerx}/retailclient_liveeptest_{vnummerx}.z20\n")
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
                            log1_label.config(text="Download finished!")
                            print("\nDownload finished!\n")
                            return
            log1_label.config(text="Download finished!")
            print("Download finished!\n")
        
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
