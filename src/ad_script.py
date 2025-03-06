import msal
import pandas as pd
import re
import os

# Function to extract name and surname from the username
def extract_name_surname(username:str) -> tuple:
    match = re.match(r"(\w+)\.(\w+)@", username)
    if match:
        return match.groups()
    else:
        return None, None

# Function that returns the username cropped to 20 characters for AD
def full_username(name:str, surname:str) -> str:
    full_username = f"{name}.{surname}"
    return full_username[:20]

# Function to authenticate the user
def authenticate_user(username:str, password:str, tenant_username:str, client_id:str) -> bool:
    authority = 'https://login.microsoftonline.com/' + tenant_username
    app = msal.PublicClientApplication(client_id, authority=authority)

    result = app.acquire_token_by_username_password(username, password, scopes=["https://graph.microsoft.com/.default"])

    if "access_token" in result:
        print("Authentication successful.")
        return True
    else:
        print("Authentication failed:", result.get("error"))
        return False

# Function to retrieve the VM name
def get_vm_name(name:str, surname:str, excel_folder:str) -> str:
    try:
        for file in os.listdir(excel_folder):
            if file.endswith(".xlsx"):
                file_path = os.path.join(excel_folder, file)
                print(f"Checking: {file_path}")
                
                df = pd.read_excel(file_path)
                match = df[(df['Nome'].str.lower() == name.lower()) & (df['Cognome'].str.lower() == surname.lower())]
                
                if not match.empty:
                    return match.iloc[0]['VDI']
        
        return None

    except Exception as e:
        print(f"Error reading Excel files: {e}")
        return None