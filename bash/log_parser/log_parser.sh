#!/bin/bash

echo "=== Log Parser Script ==="

read -p "Enter the path to the log file: " log_file

if [ ! -f "$log_file" ]; then
    echo "Error: File does not exist."
    exit 1
fi

error_count=$(grep -c "ERROR" "$log_file")
warning_count=$(grep -c "WARNING" "$log_file")
info_count=$(grep -c "INFO" "$log_file")

echo ""
echo "Log Summary:"
echo "ERROR entries:   $error_count"
echo "WARNING entries: $warning_count"
echo "INFO entries:    $info_count"