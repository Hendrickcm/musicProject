import speech_recognition as sr
from playsound import playsound # WINDOWS
from requests import get
from bs4 import BeautifulSoup
import webbrowser as browser
import os
from gtts import gTTS
import pyautogui
import pygame

import sys

from datetime import date
from datetime import datetime




##### CONFIGURACIONES #####
hotword = 'cecilia'

# bandera para activar tecnopolis.ai 1 sola vez ...
flag_curso = 0
flag_sesion = 0
flag_teoria = 0

flag_fb = 0 # bandera para activar facebook messenger 1 sola vez ...

def play_audio(archivo):
    pygame.mixer.init()
    pygame.mixer.music.load(archivo)
    pygame.mixer.music.play()

def responder(archivo):
    #call(['afplay', 'audios/' + arquivo + '.mp3']) # OSC
    playsound('./static/audios/' + archivo + '.mp3')        # WINDOWS
    
def crear_audio(mensaje):
        #os.remove('audios/mensaje.mp3')
        nombre_archivo = 'mensaje.mp3'
        if nombre_archivo in os.listdir('./static/audios/'):
            print('archivo: ',nombre_archivo,len(nombre_archivo))
            os.remove("./static/audios/"+nombre_archivo)       # ... borrra archivo
        tts = gTTS(text=mensaje, lang='es', slow =False)
        tts.save('./static/audios/mensaje.mp3')
        print('CECILIA: ', mensaje)
        play_audio('./static/audios/ErrorWapp.mp3')        # WINDOWS
        #call(['afplay', 'audios/mensaje.mp3']) # OSX
              
def ejecutar_comandos(trigger):
    
    if  'curso' in trigger and flag_curso == 0:
        abrir_curso()
        
    elif 'sesión' in trigger and flag_sesion == 0:
        iniciar_sesion()
        
        
    elif 'teoría' in trigger and flag_teoria == 0:
        teoria_musical()   
        
            
    else:
        mensaje = trigger.strip(hotword)
        crear_audio(mensaje)
        print('COMANDO INVALIDO', mensaje)
        play_audio('./static/audios/comando_invalido.mp3')
        
    
## .... funciones de los comandos ...

def abrir_curso():
    global flag_curso 
    flag_curso = 1  # activa bandera de youtube en 1
    play_audio('./static/audios/cursos.mp3')
    pyautogui.click(x=593, y=146)
    pyautogui.PAUSE=1
    
def iniciar_sesion():
    global flag_sesion
    flag_sesion = 1
    play_audio('./static/audios/sesioninicio.mp3')
    pyautogui.PAUSE=1
    pyautogui.click(x=791, y=171)
    pyautogui.click(x=728, y=527)
    pyautogui.typewrite('prueba')
    play_audio('./static/audios/contra.mp3')    
    pyautogui.PAUSE=1
    pyautogui.click(x=731, y=631)
    pyautogui.typewrite('prueba')
    pyautogui.PAUSE=1
    pyautogui.click(x=1065, y=706)
    
def teoria_musical():
    global flag_teoria
    flag_teoria = 1
    play_audio('./static/audios/teoria.mp3')
    pyautogui.click(x=1915, y=674)
    pyautogui.PAUSE=1
    pyautogui.click(x=684, y=643)
        
## fin funciones de los comandos ...


def monitorear_audio():
    microfono = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            print("Esperando el Comando: ")
            audio = microfono.listen(source)
            try:
                trigger= microfono.recognize_google(audio, language='es')
                trigger = trigger.lower()       # convierte a minusculas ...
                
                if hotword in trigger:
                    trigger = trigger.replace('cecilia','')        # borra camila de la cadena trigger
                    print('Comando: ', trigger)
                    play_audio('./static/audios/comando.mp3') 
                    pyautogui.PAUSE=1        
                    ejecutar_comandos(trigger)
                    break

            except sr.UnknownValueError:
                play_audio('./static/audios/comando_invalido.mp3')
                print("Google no entiende este audio")
            except sr.RequestError as e:
                print("No se pudieron solicitar los resultados del servicio Google Cloud Speech; {0}".format(e))

    return trigger   # retorna el comando a ejecutar ...


def main():
    play_audio('./static/audios/Inicio.mp3')
    while True:
        play_audio('./static/audios/Opciones.mp3')
        monitorear_audio()

main()