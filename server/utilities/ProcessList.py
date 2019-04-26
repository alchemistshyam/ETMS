import wmi, os
import win32com
import pythoncom
from flask import jsonify

class ProcessList:
    processList = []

    def get_ProcessList():
        pythoncom.CoInitialize()
        process = wmi.WMI ()
        processList = []
        for pro in process.Win32_Process():
            processes = {
                "processName" : pro.Name,
                "processId" : pro.ProcessId
            }
            processList.insert(0, processes)
        return processList

    @staticmethod
    def validate_ProcessList(processesObject):
        if("processName" in processesObject and "processId" in processesObject):
            return True
        else:
            return False

