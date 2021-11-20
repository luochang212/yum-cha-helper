# -*- coding: utf-8 -*-

"""Yum Cha Helper
    Author: github@luochang212
    Date: 2021-11-20
    Usage: 
        (open cron)
        00 15 * * * source ~/.bash_profile; cd [PATH_TO_YOUR_SCRIPT]; python helper.py -s >> ../log/helper.log 2>> ../log/helper.err
"""


import os
import subprocess
import configparser
import argparse

import pyttsx3


BASE_PATH = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = '../conf/set.conf'


class Helper:
    """Yum Cha Helper"""

    def __init__(self, config_path: str = CONFIG_PATH):
        config_path = os.path.join(BASE_PATH, config_path)
        self.config = self.get_config(config_path)
        self.args = self.set_argparse()

    @staticmethod
    def set_argparse():
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "-s", "--speech", action='store_true', help='speech synthesis')
        args = parser.parse_args()

        return args

    @staticmethod
    def get_config(filename: str):
        config = configparser.ConfigParser()
        config.read(filename)
        return config

    @staticmethod
    def send_notification(title: str, content: str):
        cmd = f'display notification "{content}" with title "{title}"'
        subprocess.call(["osascript", "-e", cmd])

    @staticmethod
    def send_speech_synthesis(text):
        engine = pyttsx3.init()
        # Property options: ting-ting.premium, mei-jia
        engine.setProperty('voice', "com.apple.speech.synthesis.voice.sin-ji")
        engine.say(text)
        engine.runAndWait()
        engine.stop()

    def controller(self):
        title = self.config.get('notification', 'title')
        content = self.config.get('notification', 'content')
        self.send_notification(title, content)

        if self.args.speech:
            speech_text = self.config.get('speech', 'text')
            self.send_speech_synthesis(speech_text)


if __name__ == '__main__':
    h = Helper()
    h.controller()
