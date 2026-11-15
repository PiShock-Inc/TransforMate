import os

# Helper function to parse a string into a list of integers
def parse_list(string: str | None) -> list[int]:
    if string is None or string.strip() in ["", "[]"]:
        return []
    output = string.removeprefix("[").removesuffix("]").split(",")
    return [int(output[i].strip()) for i in range(len(output))]


required_variables: list[str] = ["BOT_TOKEN", "USER_REPORTS_CHANNEL_ID"]
for var in required_variables:
    if os.environ.get(var) is None:
        raise Exception(f"{var} hasn't been provided! Aborting...")
    elif str(os.environ.get(var)).strip() == "":
        raise Exception(f"{var} has been provided, but it is blank! Aborting...")

non_vital_variables: list[tuple[str, str]] = [("BLOCKED_USERS", ""), ("CACHE_PATH", "cache"), ("MAX_REGEN_USERS", "100")]
for var, val in non_vital_variables:
    if os.environ.get(var) is None or str(os.environ.get(var)).strip() == "":
        print(f"{var} hasn't been provided, so it will be defaulted to \"{val}\"!")

# General bot configuration
BOT_TOKEN: str = os.environ.get("BOT_TOKEN")  # Token for the bot
BLOCKED_USERS: list[int] = parse_list(os.environ.get("BLOCKED_USERS", ""))  # Users that are blocked from using the bot
USER_REPORTS_CHANNEL_ID: int = int(os.environ.get("USER_REPORTS_CHANNEL_ID"))  # Channel to use for the /report command
CACHE_PATH: str = os.environ.get("CACHE_PATH", "cache")  # What's the path to the cache folder? (In relationship to the utils.py file)
MAX_REGEN_USERS: int = int(os.environ.get("MAX_REGEN_USERS", 100)) # Maximum number of users in a server allowed for /regen_server_tfs
