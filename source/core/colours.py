PINK = '\033[95m'
BLUE = '\033[94m'
CYAN = '\033[96m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
CLEAR = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

if __name__ == "__main__":
    print(f"Test"
          f"{PINK}Test"
          f"{BLUE}Test"
          f"{CYAN}Test"
          f"{GREEN}Test"
          f"{YELLOW}Test"
          f"{RED}Test"
          f"{CLEAR}Test"
          f"{BOLD}Test{CLEAR}"
          f"{UNDERLINE}Test{CLEAR}"
    )