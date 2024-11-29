from ADT import *
import pandas as pd

all_guests = {}
all_staffs = []
all_cards = {}
all_events = []
checkinstaions = []

def add_guest(name,
            sex,
            region,
            id,
            phone,
            position,
            permissionlevel,
            car_number,
            arrive_point,
            arrive_time):
    permissionlevel = int(permissionlevel)
    for guest in all_guests.values():
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
    arrive_time = Time(arrive_time)
    new_guest = Guest(
                 name,
                 sex,
                 region,
                 phone,
                 position,
                 id,
                 permission,
                 car_number,
                 arrive_point,
                 arrive_time)
    guest_id = f"G{new_guest.permission.permissionLevel}0{len(all_guests.values()) + 1}"
    new_guest.guest_id = guest_id
    all_guests[guest_id] = new_guest
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
                  df.loc[i, "permissionLevel"],
                  df.loc[i, "car_number"],
                  df.loc[i, "arrive_point"],
                  df.loc[i, "arrive_time"])
    return True


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
    card_id = guest.guest_id
    new_card = Card(guest.permission, card_id, True, guest)
    guest.card = new_card
    all_cards[card_id] = new_card

def distribute_card():
    for guest in all_guests.values():
        if guest.arrive_point not in checkinstaions:
            new_station = CheckInStaion(guest.arrive_point)
            new_station.cards.append(guest.card)
            checkinstaions.append(new_station)
        else:
            for station in checkinstaions:
                if station.location == guest.arrive_point:
                    station.cards.append(guest.card)

def add_event(name, startTime, endTime):
    startTime = Time(startTime)
    endTime = Time(endTime)
    new_event = Event(name, startTime, endTime)
    all_events.append(new_event)

def add_event_from_file(file_name):
    df = pd.read_csv(file_name)
    if df.empty:
        return False
    else:
        for i in range(len(df)):
            add_event(df.loc[i, "name"],
                      df.loc[i, "startTime"],
                      df.loc[i, "endTime"])
    return True

def invite_from_file(file_name, event):
    df = pd.read_csv(file_name)
    if df.empty:
        return False
    else:
        for i in range(len(df)):
            region = df.loc[i, "region"]
            id = df.loc[i, "id"]
            for guest in all_guests.values():
                if guest.region == region and guest.id == id:
                    event.invite_guest(guest)

def system_init():
    read_staff_data()