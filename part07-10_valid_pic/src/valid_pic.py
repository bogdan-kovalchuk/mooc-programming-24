import datetime


def is_it_valid(pic: str):
    century = {"+": "18", "-": "19", "A": "20"}
    ctrl_chars = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    try:
        if len(pic) != 11:
            return False

        century_marker = pic[6]
        if century_marker not in century:
            return False

        day = int(pic[:2])
        month = int(pic[2:4])
        year = int(century[century_marker] + pic[4:6])
        datetime.datetime(year, month, day)

        personal_identifier = pic[7:10]
        if not personal_identifier.isdigit():
            return False

        ctrl_char = pic[10]
        if ctrl_char != ctrl_chars[int(pic[:6] + pic[7:10]) % 31]:
            return False

        return True
    except:
        return False


if __name__ == "__main__":
    print(is_it_valid("230827-906F"))
    print(is_it_valid("120488+246L"))
    print(is_it_valid("310823A9877"))
