if __name__ == "__main__":
    stack = '[([])((([[[]]])))]{()}'
    if len(stack) % 2 == 0:
        while True:
            if "[]" in stack or "{}" in stack or "()" in stack:
                stack = stack.replace("[]", "")
                stack = stack.replace("{}", "")
                stack = stack.replace("()", "")
                continue
            else:
                break
        if len(stack) == 0:
            print("Последовательность сбалансирована.")
        else:
            print("Последовательность несбалансированна.")
    else:
        print("Последовательность несбалансированна.")
