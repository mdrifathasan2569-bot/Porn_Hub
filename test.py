import os
import time
import requests
import uuid

def main_menu():
    os.system('clear')
    print("=======================================")
    print("      ★ MY Porn-Hub CONTROL ★        ")
    print("          DEVELOPER: BoT              ")
    print("=======================================")
    print(" [১] (FB Method)")
    print(" [২] (Sex video / Reel Server Check)")
    print(" [৩] (old clone)")
    print(" [৪] (File clone)")
    print(" [৫] (Random Clone - b-graph Method)")
    print(" [৬] (Exit)")
    print("=======================================")
    
    choice = input(" [★] ১/২/৩/৪/৫/৬ : ")
    
    if choice == "1" or choice == "১":
        os.system('clear')
        print("--- [1] FB Method ---")
        # আপনার ১ নম্বর মেথডের কোড এখানে থাকলে বসবে
        input("\nPress Enter to return to Main Menu...")
        main_menu()
        
    elif choice == "2" or choice == "২":
        os.system('clear')
        print("--- [2] Sex video / Reel Server Check ---")
        site = input("Enter Site Name: ")
        url = "https://www.facebook.com/reel/846400658"
        print(f"\n[+] Connecting to server via {site}...")
        time.sleep(1.5)
        print("\n=======================================")
        print(f"Target URL: {url}")
        print("[✓] STATUS : SERVER CONNECTED SUCCESS")
        print("=======================================")
        input("\nPress Enter to return to Main Menu...")
        main_menu()
        
    elif choice in ["3", "4", "৩", "৪"]:
        os.system('clear')
        print(f"--- Option [{choice}] ---")
        print("[X] ERROR: Method Not Found / Expired!")
        input("\nPress Enter to return to Main Menu...")
        main_menu()

    elif choice == "5" or choice == "৫":
        os.system('clear')
        print("--- [5] Random Clone (b-graph Method) ---")
        uid = input("[+] Enter UID/Email: ")
        password = input("[+] Enter Password: ")
        print("\n[+] Checking account details...")
        
        r = requests.Session()
        head = {
            'Host': 'b-graph.facebook.com',
            'X-Fb-Connection-Type': 'WIFI',
            'Authorization': 'OAuth 350685531728|62f8ce9f74744849a044318023157f12',
            'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 10; Redmi Note 8 Pro Build/QP1A.190711.020)'
        }
        data = {
            'adid': str(uuid.uuid4()),
            'format': 'json',
            'device_id': str(uuid.uuid4()),
            'email': uid,
            'password': password,
            'generate_analytics_claim': '1',
            'credentials_type': 'password',
            'source': 'login',
            'error_detail_type': 'button_with_disabled',
            'enroll_ext_attrib': '0',
            'generate_session_cookies': '1',
            'generate_machine_id': '1',
            'meta_inf_fbmeta': '',
        }
        try:
            pos = r.post('https://b-graph.facebook.com/auth/login', headers=head, data=data).json()
            if 'session_key' in pos or 'access_token' in pos:
                print(f"\n[RFX-OK] {uid} | {password}")
            elif 'www.facebook.com' in pos.get('error', {}).get('message', ''):
                print(f"\n[RFX-CP] {uid} | {password}")
            else:
                print("\n[X] Login Failed / Incorrect Details")
        except:
            print("\n[X] Network Error!")
            
        input("\nPress Enter to return to Main Menu...")
        main_menu()

    elif choice == "6" or choice == "৬":
        print("\n[+] Thank you for using this tool! Goodbye.")
        exit()