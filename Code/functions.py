def get_answer() -> str:
    answer = input(">>> ").strip()

    if answer in ["q", "exit"]:
        input("Press enter to exit...")
        exit()
    elif answer in ["r", "restart"]:
        input("Press enter to restart...")
        return None
    else:
        return answer.replace("a:", "ä").replace("o:", "ö")
