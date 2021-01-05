#!/usr/bin/env python3
#
# for practice
# may modify in afterwards
#
######################
import numpy as np
import pyautogui

import sys
import cv2 as cv

import click
import os

from playsound import playsound

def pay(video):
    cap = cv.VideoCapture(video)
    while(cap.isOpened()):
        ret,frame = cap.read()
        # maybe some issue play with before save video file

        try:
            cv.imshow('frame',frame)
        except Exception as e:
            pass

        key = cv.waitKey(50)
        if key & 0xFF == ord('q'):
            break
        if key & 0xFF == ord('p'):
            cv.waitKey(-1)

    cap.release()
    cv.destroyAllWindows()

def record():
    cap = cv.VideoCapture(0)
    while(cap.isOpened()):
        ret,frame = cap.read()
        if ret == True:
            cv.imshow("camera video",frame)
            if cv.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    cv.destroyAllWindows()

def save(save):
    cap = cv.VideoCapture(0)
    fourcc = cv.VideoWriter_fourcc('X','V','I','D')
    out = cv.VideoWriter(save,fourcc,20.0,(640,480))
    while(cap.isOpened()):
        ret,frame = cap.read()
        if ret == True:
            frame = cv.flip(frame,0)
            out.write(frame)
            cv.imshow("camera video",frame)
            if cv.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    out.release()
    cv.destroyAllWindows()

# save screen record
def screen(sfile):
    SCREEN_SIZE = (1920,1080)
    fourcc = cv.VideoWriter_fourcc(*"XVID")
    out = cv.VideoWriter(sfile,fourcc,20.0,(SCREEN_SIZE))

    while True:
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv.cvtColor(frame,cv.COLOR_BGR2RGB)
        out.write(frame)

    cv.destroyAllWindows()
    out.release()

def sound(audio):
    playsound(audio)

@click.command()
@click.option('-p',default='',help='video file path to play,use q to quit,p to pause')
@click.option('-c',is_flag=True,help='only recording the camera video,q to quit')
@click.option('-s',default='',help='save and recording the camera video,need a file name,q to quit')
@click.option('-r',default='',help='recording the screen and save as file,need a file name')
@click.option('-a',default='',help='play a audio sound file,Ctrl-z to stop')

def op(p,c,s,r,a):
    if os.path.isfile(p):
        pay(p)
    elif p == '' and s != '' and not c:
        save(s)
    elif c and p == '' and s == '':
        record()
    elif r != '':
        screen(r)
    elif os.path.isfile(a):
        sound(a)

if __name__=="__main__":
    op()
