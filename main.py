# -*- coding: utf-8 -*-
# 固定写法，导入相关类库和函数
from util import WoxEx, WoxAPI, load_module, Log

# 统一加载模块
with load_module():
    import pyperclip
    import os
    import win32api


class Main(WoxEx):  # 继承WoxEx
    def query(self, keyword):
        results = list()
        results.append({
            "Title": "e=edge|ed=editplus|r=revit2019",
            "SubTitle": keyword,
            "IcoPath": "Images/app.ico",
            "JsonRPCAction": {
                "method": "ProcessInput",
                "parameters": [keyword],
                "dontHideAfterAction": False
            }
        })
        return results

    def ProcessInput(self, keyword):

        if keyword == "e":
            # os.system('MicrosoftEdge.exe')
            # win32api.ShellExecute(0, 'open', 'C:\\Users\\chenm\\AppData\\Local\\Microsoft\\WindowsApps\\MicrosoftEdge.exe', '', '', 1)
            os.system('%windir%\\explorer.exe shell:Appsfolder\Microsoft.MicrosoftEdge_8wekyb3d8bbwe!MicrosoftEdge')

        elif keyword == "r":
            win32api.ShellExecute(
                0, 'open', 'C:\\Program Files\\Autodesk\\Revit 2019\\Revit.exe', '', '', 1)
        elif keyword == "ed":
            win32api.ShellExecute(
                0, 'open', 'E:\\software\\EditPlus 3\\EditPlus.exe', '', '', 1)
        else:
            pyperclip.copy(keyword)

        Log.info(keyword)


if __name__ == "__main__":
    Main()
