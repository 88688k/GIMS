from ADT import *
import pandas as pd

all_guests = []
all_staffs = []
all_cards = []
all_events = []

def add_guest(name,
            sex,
            region,
            id,
            phone,
            position,
            permissionlevel):
    permissionlevel = int(permissionlevel)
    for guest in all_guests:
        guest:Guest
        if guest.region == region and guest.id == id:
            if permissionlevel > guest.permission.permissionlevel:
                new_permission = Permission(permissionlevel, "Guest")
                guest.permission = new_permission
                print("权限已更新")
                return
    if sex not in ["男", "女"]:
        print("不支持的性别")
        return False
    permission = Permission(permissionlevel, "Guest")
    new_guest = Guest(
                 name,
                 sex,
                 region,
                 phone,
                 position,
                 id,
                 permission)
    all_guests.append(new_guest)
    return True

def add_guest_from_file(file_name):
    df = pd.read_csv(file_name)
    if df.empty:
        return False
    for i in range(len(df)):
        add_guest(df.loc[i, "name"],
                  df.loc[i, "sex"],
                  df.loc[i, "region"],
                  df.loc[i, "id"],
                  df.loc[i, "phone"],
                  df.loc[i, "position"],
                  df.loc[i, "permissionLevel"])
    return True


    # for line in file.readlines():
    #     line:str
    #     line = line.strip()
    #     items = line.split(" ")
    #     for item in items[:]:
    #         if item == "" or item == '\n':
    #             items.remove(item)
    #     add_guest(items[0], items[1], items[2], items[3], items[4], items[5], items[6])


def add_staff(name, role, staff_id = None):
    # permission = Permission(permissionlevel, "Staff")
    new_staff = Staff(name, role)
    if not staff_id:
        new_staff.staff_id = f"S00{len(all_staffs) + 1}"
    else:
        new_staff.staff_id = staff_id
    all_staffs.append(new_staff)

def add_staff_from_file(file_name):
    df = pd.read_csv(file_name)
    if df.empty:
        return False
    for i in range(len(df)):
        add_staff(df.loc[i, "name"],
                  df.loc[i, "role"])
    return True

def read_staff_data():
    df = pd.read_csv("data/staff_data.csv")
    if not df.empty:
        for i in range(len(df)):
            add_staff(df.loc[i, "name"],
                      df.loc[i, "role"],
                      df.loc[i, "staff_id"])

def make_card(guest):
    card_id = f"G{guest.permission.permissionLevel}0{len(all_cards) + 1}"
    new_card = Card(guest.permission, card_id, True, guest)
    all_cards.append(new_card)

def add_event(name, startTime, endTime):
    new_event = Event(name, startTime, endTime)
    all_events.append(new_event)

def system_init():
    read_staff_data()