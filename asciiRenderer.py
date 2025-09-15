from PIL import Image
import cv2
import sys
import os
import time
import numpy as np
from pygame import mixer, init

class ascii_renderer:
    def __init__(self,mode,couleur=False) -> None:
        init()
        self.terminal_size = os.get_terminal_size()
        self.char_list = " .:-=+*#%@"
        self.reset_code = "\033[0m"
        self.color_code = "\033[38;2;{};{};{}m"
        self.couleur = couleur
        self.last_frame = None
        self.isAudio = False
        if mode == "cam":
            self.mode = mode
            self.frame_time = 1/1000
        elif mode == "vid":
            import moviepy
            self.mode = mode
            self.vid = str(input("Entrez le chemain vers la vidéo : "))          
            video = moviepy.VideoFileClip(self.vid)
            audio = video.audio
            self.FPS = video.fps
            self.frame_time = 1.0 / self.FPS
            self.video_duration = video.duration
            if audio is not None:
                audio.write_audiofile(r"audio.mp3")
                self.isAudio = True
        else:
            raise ValueError("Entrez une valeur valide !")

    
    def play_song(self):
        if self.isAudio:
            mixer.music.load(r"audio.mp3")
            mixer.music.play(1)
    
    def set_cursor_pos(self,x,y):
        sys.stdout.write(f"\033[{y};{x}H")
    
    def pxl_to_char(self,rgb,active=False):
        r, g, b = rgb
        grey = sum(rgb) // len(rgb)
        if self.couleur == False or active == False:
            return f"{self.char_list[min(int(grey * len(self.char_list) / 255), len(self.char_list) - 1)]}"
        else:
            return f"{self.color_code.format(r,g,b)}{self.char_list[min(int(grey * len(self.char_list) / 255), len(self.char_list) - 1)]}{self.reset_code}"

    def ascii_render(self,img, cols=200, rows=50):
        if self.last_frame == None:
            image = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
            image = image.resize((cols, rows))
            result = []
            for y in range(rows):
                line = ""
                for x in range(cols):
                    rgb = image.getpixel((x, y))
                    self.set_cursor_pos(x,y)
                    char_mem = self.pxl_to_char(rgb=rgb)
                    line += char_mem
                    char = self.pxl_to_char(rgb=rgb,active=self.couleur)
                    sys.stdout.write(char)
                result.append(line)
            self.last_frame = result
        else:
            image = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
            image = image.resize((cols, rows))
            result = []
            for y in range(rows):
                line = ""
                for x in range(cols):
                    rgb = image.getpixel((x, y))
                    char_mem = self.pxl_to_char(rgb=rgb)
                    line += char_mem
                    if self.last_frame[y][x] != char_mem:
                        self.set_cursor_pos(x,y)
                        char = self.pxl_to_char(rgb=rgb,active=self.couleur)
                        sys.stdout.write(char)
                result.append(line)
            self.last_frame = result
            # image = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
            # image = image.resize((cols, rows))
            # result = []
            # for y in range(rows):
            #     line = ""
            #     for x in range(cols):
            #         rgb = image.getpixel((x, y))
            #         self.set_cursor_pos(x,y)
            #         char_mem = self.pxl_to_char(rgb=rgb)
            #         line += char_mem
            #         char = self.pxl_to_char(rgb=rgb,active=self.couleur)
            #         sys.stdout.write(char)

    
    def limit_fps(self,last_frame_time ):
        elapsed_time = time.time() - last_frame_time

        if elapsed_time < self.frame_time:
            wait_time = int((self.frame_time - elapsed_time) * 1000)
            time.sleep(wait_time / 1000.0)
        
        self.set_cursor_pos(2,2)
        sys.stdout.write(f"FPS : {round(elapsed_time * 1000)}")

    def run(self):
        if self.mode == "cam":
            vid = cv2.VideoCapture(0)
            last_frame_time = time.time()

            while True:
                ret, frame = vid.read()
                cols, rows = os.get_terminal_size()
                self.ascii_render(frame, cols, rows)
                self.limit_fps(last_frame_time)
                last_frame_time = time.time()
        else:
            cap = cv2.VideoCapture(self.vid)
   
            if (cap.isOpened()== False): 
                print("Mauvais chemain")
            self.play_song()
            last_frame_time = time.time()
            while(cap.isOpened()):
                ret, frame = cap.read()
                if ret == True:
                
                    cols, rows = os.get_terminal_size()
                    self.ascii_render(frame, cols, rows)
                
                    self.limit_fps(last_frame_time)

                    last_frame_time = time.time()
                else: 
                    break

            cap.release()