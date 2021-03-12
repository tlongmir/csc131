

def main():

    time_secs = float(input("Input time in seconds: "))
    year = time_secs // (365 * 24 * 60 * 60) # new
    day = time_secs // (24 * 60 * 60) % 365
    time = time_secs % (24 * 60 * 60)
    hour = time // 3600
    time %= 3600
    minutes = time // 60
    time %= 60
    seconds = time
    print("days:hours:minutes:seconds= %d:%d:%d:%d:%d" % (year, day, hour, minutes, seconds))   

if __name__ == "__main__":
    main()
