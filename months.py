#!/usr/bin/env python3

# Created by: Zaida Hammel
# Created on: October 2022
# This program connects months to numbers.


def main():
    # this function identifies the month

    # input
    month_number = input("Enter month as a number (ex: 3 for March): ")
    print("")

    # process and output
    match month_number:
        case "1":
            print("Your month is, January.")
        case "2":
            print("Your month is, February.")
        case "3":
            print("Your month is, March.")
        case "4":
            print("Your month is, April.")
        case "5":
            print("Your month is, May.")
        case "6":
            print("Your month is, June.")
        case "7":
            print("Your month is, July.")
        case "8":
            print("Your month is, August.")
        case "9":
            print("Your month is, September.")
        case "10":
            print("Your month is, October.")
        case "11":
            print("Your month is, November.")
        case "12":
            print("Your month is, December.")
        case _:
            print("Invalid month.")


if __name__ == "__main__":
    main()
