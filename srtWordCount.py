import sys

noQuit = 'y'

while noQuit == 'y':
    try:
        print("Make sure your SRT file is in the same directory.")
        print("Must be .srt file.")
        fileName = str(input("Input your SRT file name or the path to it (Do NOT include .srt): "))

        srt = open(fileName + ".srt", "r")

        lines = [line.strip() for line in srt]

        srt.close()

        raw = []

        row = 0

        for line in lines:
            row += 1

            if row <= 2:
                continue

            if line == "":
                row = 0
                continue

            raw.append(line)

        text = " ".join(raw)
        text = text.split(" ")

        print("Word Count: ", len(text))

    except FileNotFoundError:
        print("The input file wasn't found. Is it in this folder and is the path correct?")
        print("Error Code: ", sys.exc_info()[0])
        print("\n")

    noQuit = str(input("Would you like to run again?"))
