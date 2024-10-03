# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Simple Registry Backup Utility                                              #
# v. 20241002                                                                 #
#                                                                             #
# MIT License                                                                 #
# Copyright (c) 2024 /bandowashere                                            #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #



# import dependencies
import os
import subprocess



# define functions
def backupHive(hive, backupFile):
    try:
        # Use the subprocess to call reg export
        command = f'reg export "{hive}" "{backupFile}" /y'
        result = subprocess.run(command, shell = True, check = True)
        print(f"Registry hive {hive} backed up successfully.")
    except Exception as e:
        print(f"Error backing up registry hive {hive}: {e}")

def backupRegistry(backupFolder):
    try:
        # Create backup folder
        os.makedirs(backupFolder, exist_ok=True)

        # Map hive names to strings
        REGISTRYHIVES = {
            "HKEY_CURRENT_USER": r"HKEY_CURRENT_USER",
            "HKEY_LOCAL_MACHINE": r"HKEY_LOCAL_MACHINE",
            "HKEY_USERS": r"HKEY_USERS",
            "HKEY_CURRENT_CONFIG": r"HKEY_CURRENT_CONFIG",
            "HKEY_CLASSES_ROOT": r"HKEY_CLASSES_ROOT"
        }

        # Backup each hive
        for hiveName, hivePath in REGISTRYHIVES.items():
            backupFile = os.path.join(backupFolder, f"{hiveName}.reg")
            backupHive(hivePath, backupFile)
        print()
    except Exception as e:
        print(f"Error backing up registry: {e}")



# backup registry
desktopPath = os.path.join(os.environ['USERPROFILE'], 'Desktop')
backupFolder = os.path.join(desktopPath, "registry_backups")
backupRegistry(backupFolder)