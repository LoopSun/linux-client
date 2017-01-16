#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
Remote Command Handler

Remote Server---[send command(json)]--->Client---[Queue]--->Response to Remote Server

'''

import sh
import uuid

class RemoteCommand():
    def __init__(self, real_command):
        id = uuid.uuid1()  #generate uuid
        self.real_command = real_command


    def command_cleaner(self):
        if self.real_command:
            clean_command = self.real_command.split()
            return clean_command
        else:
            raise TypeError("null command")


    def sudo_command_run(self, command):
        result = sh.sudo(command, _bg=True)
        result_status = "Success" if result.exit_code() == 0 else "Fail"
        return {
            "status": result_status,
            "result": result
        }

    def general_command_run(self, command):
        result = sh.sh(command, _bg=True)
        result_status = "Success" if result.exit_code() == 0 else "Fail"
        return {
            "status": result_status,
            "result": result
        }


    def command_run(self):
        clean_command = self.command_cleaner()
        if self.real_command.startswith("sudo"):
            self.sudo_command_run(clean_command)
        else:
            self.general_command_run(clean_command)