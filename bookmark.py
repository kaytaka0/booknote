import os
import json

from config import TARGET_FOLDER_NAME

def get_chrome_bookmark():
    bm_path = os.path.join(os.environ['HOME'], '.config/google-chrome/Default/Bookmarks')
    with open(bm_path, 'r') as f:
        bm_json = f.read()
    
    bm = json.loads(bm_json)
    bm_folders = bm['roots']['bookmark_bar']['children']
    
    target_folder = [folder for folder in bm_folders if folder['name'] == TARGET_FOLDER_NAME]
    if len(target_folder) > 1:
        raise Exception(f'Duplicate target folders {TARGET_FOLDER_NAME}')
    elif len(target_folder) < 1:
        raise Exception(f'Cannot find target folder {TARGET_FOLDER_NAME}')
    elif target_folder[0]['type'] != 'folder':
        raise Exception(f'{TARGET_FOLDER_NAME} is not a bookmark folder')
    
    target_folder = target_folder[0]
    # print(target_folder)
    for bm in target_folder['children']:
        print(bm['name'])

        

get_chrome_bookmark()