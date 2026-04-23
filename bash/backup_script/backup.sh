#!/bin/bash

echo "=== Backup Script ==="

read -p "Enter the source folder path: " source_dir
read -p "Enter the destination folder path: " dest_dir

if [ ! -d "$source_dir" ]; then
    echo "Error: Source directory does not exist."
    exit 1
fi

if [ ! -d "$dest_dir" ]; then
    echo "Destination directory does not exist. Creating it now..."
    mkdir -p "$dest_dir"
fi

timestamp=$(date +"%Y-%m-%d_%H-%M-%S")
backup_folder="$dest_dir/backup_$timestamp"

mkdir -p "$backup_folder"

cp -r "$source_dir"/* "$backup_folder" 2>/dev/null

if [ $? -eq 0 ]; then
    echo "Backup completed successfully."
    echo "Files copied to: $backup_folder"
else
    echo "Backup completed, but some files may not have copied."
fi