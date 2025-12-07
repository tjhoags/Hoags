#!/usr/bin/env python3
"""
Fetch data from Dropbox for ALC Internal Only - Discord bots folder.

Usage:
    # With access token:
    DROPBOX_ACCESS_TOKEN=your_token python fetch_dropbox_data.py

    # Or with shared link:
    python fetch_dropbox_data.py --shared-link "https://www.dropbox.com/sh/xxx/xxx"
"""

import os
import sys
import argparse
from pathlib import Path

try:
    import dropbox
    from dropbox.exceptions import ApiError, AuthError
except ImportError:
    print("Installing dropbox SDK...")
    os.system("pip install dropbox")
    import dropbox
    from dropbox.exceptions import ApiError, AuthError


def download_folder(dbx, dropbox_path: str, local_path: str):
    """Download all files from a Dropbox folder recursively."""
    local_path = Path(local_path)
    local_path.mkdir(parents=True, exist_ok=True)
    
    try:
        result = dbx.files_list_folder(dropbox_path)
        
        while True:
            for entry in result.entries:
                local_file_path = local_path / entry.name
                
                if isinstance(entry, dropbox.files.FileMetadata):
                    print(f"Downloading: {entry.path_display}")
                    dbx.files_download_to_file(str(local_file_path), entry.path_display)
                elif isinstance(entry, dropbox.files.FolderMetadata):
                    print(f"Entering folder: {entry.path_display}")
                    download_folder(dbx, entry.path_display, str(local_file_path))
            
            if not result.has_more:
                break
            result = dbx.files_list_folder_continue(result.cursor)
            
    except ApiError as e:
        print(f"Error accessing folder '{dropbox_path}': {e}")
        raise


def download_from_shared_link(dbx, shared_link: str, local_path: str):
    """Download files from a shared link."""
    local_path = Path(local_path)
    local_path.mkdir(parents=True, exist_ok=True)
    
    try:
        shared_link_metadata = dropbox.files.SharedLink(url=shared_link)
        
        # List folder contents via shared link
        result = dbx.files_list_folder(path="", shared_link=shared_link_metadata)
        
        while True:
            for entry in result.entries:
                local_file_path = local_path / entry.name
                
                if isinstance(entry, dropbox.files.FileMetadata):
                    print(f"Downloading: {entry.name}")
                    metadata, response = dbx.sharing_get_shared_link_file(
                        url=shared_link,
                        path=f"/{entry.name}"
                    )
                    with open(local_file_path, 'wb') as f:
                        f.write(response.content)
                elif isinstance(entry, dropbox.files.FolderMetadata):
                    print(f"Found subfolder: {entry.name}")
                    # For subfolders, we need to adjust the path
                    subfolder_url = f"{shared_link}?subfolder_nav_tracking=1"
                    download_from_shared_link(dbx, subfolder_url, str(local_file_path))
            
            if not result.has_more:
                break
            result = dbx.files_list_folder_continue(result.cursor)
            
    except ApiError as e:
        print(f"Error accessing shared link: {e}")
        raise


def main():
    parser = argparse.ArgumentParser(description="Download Dropbox folder for ALC Discord bots")
    parser.add_argument("--token", help="Dropbox access token (or set DROPBOX_ACCESS_TOKEN env var)")
    parser.add_argument("--shared-link", help="Dropbox shared folder link")
    parser.add_argument("--folder", default="/ALC Internal Only/Discord bots", 
                       help="Dropbox folder path (default: /ALC Internal Only/Discord bots)")
    parser.add_argument("--output", default="./discord_bots_data",
                       help="Local output directory (default: ./discord_bots_data)")
    args = parser.parse_args()
    
    # Get access token
    access_token = args.token or os.environ.get("DROPBOX_ACCESS_TOKEN")
    
    if not access_token and not args.shared_link:
        print("Error: Please provide either:")
        print("  1. A Dropbox access token via --token or DROPBOX_ACCESS_TOKEN env var")
        print("  2. A shared link via --shared-link")
        print()
        print("To get an access token:")
        print("  1. Go to https://www.dropbox.com/developers/apps")
        print("  2. Create an app or use an existing one")
        print("  3. Generate an access token")
        sys.exit(1)
    
    try:
        # Create Dropbox client
        if access_token:
            dbx = dropbox.Dropbox(access_token)
            # Verify the token works
            dbx.users_get_current_account()
            print("Successfully connected to Dropbox")
            
            print(f"Downloading from: {args.folder}")
            print(f"Saving to: {args.output}")
            download_folder(dbx, args.folder, args.output)
        else:
            # Use shared link (no auth required for public links)
            dbx = dropbox.Dropbox("")  # Empty token for shared links
            print(f"Downloading from shared link: {args.shared_link}")
            print(f"Saving to: {args.output}")
            download_from_shared_link(dbx, args.shared_link, args.output)
        
        print(f"\nDownload complete! Files saved to: {args.output}")
        
    except AuthError:
        print("Error: Invalid access token")
        sys.exit(1)
    except ApiError as e:
        print(f"Dropbox API error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
