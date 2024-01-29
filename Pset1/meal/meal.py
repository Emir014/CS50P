def main():
    time = input("What time is it? ").strip()
    hour = convert(time)

    if 7 <= hour <= 8:
        print("breakfast time")
    elif 12 <= hour <= 13:
        print("lunch time")
    elif 18 <= hour <= 19:
        print("dinner time")

def convert(time):
    time = convert_12_to_24(time)
    hours, minutes = time.split(":")
    hours, minutes = float(hours), float(minutes)
    net_hour = round(hours + minutes / 60, 2)
    return net_hour

def convert_12_to_24(time):
    if time[-4:] == "a.m.":
        time = time.replace("a.m.", "")
        return time
    elif time[-4:] == "p.m.":
        time = time.replace("p.m.", "")
        hour, minutes = time.split(":")
        hour = str(int(hour) + 12)
        time = hour + ":" + minutes
        return time
    else:
        return time

if __name__ == "__main__":
    main()
