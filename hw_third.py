from collections import Counter
import sys

def parse_log_line(line: str) -> dict:
    """
    Parses a single log line into its components: date, time, level, and message.

    Args:
        line (str)

    Returns:
        dict: A dictionary with the parsed log components
    """
    date, time, level, message = line.split(" ", maxsplit=3)
    return {
        "date": date,
        "time": time,
        "level": level,
        "message": message,
    }
    
def load_logs(file_path: str) -> list:
    """
    Loads and parses log lines from a specified file.

    Args:
        file_path (str): The path to the log file to be loaded.

    Returns:
        list: A list of parsed log entries. Each entry is processed by the
              `parse_log_line` function. Returns an empty list if the file
              is not found.
    """
    try:
        with open(file_path, "r") as file:
            return [parse_log_line(line[:-1]) for line in file.readlines()]
    except FileNotFoundError:
        print("File not found")
        return []


def filter_logs_by_level(logs: list, level: str) -> list:
    """
    Filters a list of log entries by the specified log level.

    Args:
        logs (list): A list of log entries, where each log entry is a dictionary with a "level" key.
        level (str): The log level to filter.

    Returns:
        list: A list of log entries that match the specified log level.
    """
    try:
        return list(filter(lambda log: log["level"] == level.upper(), logs))
    except TypeError:
        print("TypeError: The provided logs input is not a list.")
    except KeyError:
        print("KeyError: One or more log entries are missing the 'level' key.")
    return []

def count_logs_by_level(logs: list) -> dict:
    """
    Counts the occurrences of each log level in a list of log entries.

    Args:
        logs (list): A list of dictionaries, where each dictionary represents a log entry
                     and is expected to contain a "level" key.

    Returns:
        dict: A dictionary with log levels as keys and their counts as values.
    """
    try:
        return Counter(log["level"] for log in logs)
    except KeyError as e:
        print(f"Error: Missing key in log entry - {e}")
        return {}
    except TypeError as e:
        print(f"Error: Invalid input - {e}")
        return {}

def display_log_counts(counts: dict):
    """
    Displays a table of log levels and their respective counts.

    Args:
        counts (dict): A dictionary with log levels as keys and their counts as values.   
    """
    try:
        title_level = "Рівень логування"
        title_quantity = "Кількість"
        title = title_level + " | " + title_quantity
        print(title)
        print("-" * len(title))

        for level, count in counts.items():
            print(f"{level:<{len(title_level)}} | {count:<{len(title_quantity)}}")
    except AttributeError as e:
        print(f"Error: Invalid input data structure - {e}")


def main():
    args = sys.argv
    if len(args) > 1:
        path_file = args[1]
        
        logs = load_logs(path_file)
        try:
            level = args[2]
            logs_filtered = filter_logs_by_level(logs, level)
            print(logs_filtered)
        except IndexError:
            print("2 argumnt is not found")
        count = count_logs_by_level(logs)
        display_log_counts(count)

main()