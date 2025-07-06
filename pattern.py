def print_hv_pattern():
    # Print H
    for i in range(7):
        if i == 3:
            print("* * * * *")
        else:
            print("*       *")

    print()  # New line between H and V

    # Print V
    for i in range(7):
        if i < 4:
            print(" " * i + "*")
        else:
            print(" " * (6 - i) + "*")

if __name__ == "__main__":
    print_hv_pattern()