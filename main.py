# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time, calculate_days_hours_minutes, format_12hr_time
from unittest import main

# Run unit tests automatically
main(module='test_module', exit=False)