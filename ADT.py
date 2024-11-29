class Guest:
    def __init__(self,
                 name,
                 sex,
                 region,
                 phone,
                 position,
                 id,
                 permission,
                 car_number,
                 arrive_point,
                 arrive_time) -> None:
        self.name = name
        self.sex = sex
        self.region = region
        self.phone = phone
        self.position = position
        self.id = id
        self.permission = permission
        self.car_number = car_number
        self.arrive_point = arrive_point
        self.arrive_time = arrive_time
        self.card = None
        self.events = []
        self.guest_id = None
    
    def __str__(self) -> str:
        return f"{self.name} {self.sex} {self.region} {self.id} {self.phone}"

class Staff:
    def __init__(self, name, role) -> None:
        self.name = name
        self.role = role
        self.staff_id = None
        # self.permission = permission

class CheckInStaion:
    def __init__(self, location) -> None:
        self.location = location
        self.cards = []

class Permission:
    # levelsForStaff = ["read", "write", "read and write"]
    levelsForGuest = ["normal guest", "VIP", "SVIP"]
    def __init__(self, permissionLevel, role) -> None:
        # if role == "Guest":
        self.permissionLevel, self.description = permissionLevel, Permission.levelsForGuest[permissionLevel]
        # else:
        #     self.permissionLevel, self.description = permissionLevel, Permission.levelsForStaff[permissionLevel]

class Event:
    def __init__(self, name, startTime, endTime) -> None:
        self.startTime = startTime
        self.endTime = endTime
        self.name = name
        self.attendees = []

    def invite_guest(self, guest):
        self.attendees.append(guest)
        guest.events.append(self)

    def invite_by_permission(self, guests, permissionlevel):
        for guest in guests:
            if guest.permission.permissionLevel == permissionlevel:
                self.invite_guest(guest)

class Card:
    def __init__(self, permission, card_id, status, guest) -> None:
        self.permission = permission
        self.card_id = card_id
        self.status = status
        self.owner = guest
        self.station = None

class Time:
    def __init__(self, month, day, hour, minute) -> None:
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
    
    def __init__(self, string):
        string = string.split(" ")
        self.month = string[0].split("-")[1]
        self.day = string[0].split("-")[2]
        self.hour = string[1].split(":")[0]
        self.minute = string[1].split(":")[1]
    
    def __eq__(self, other: object) -> bool:
        if self.month == other.month and self.day == other.day:
            return True
        else:
            return False
    
    def __lt__(self, other):
        if self.month < other.month:
            return True
        elif self.month == other.month:
            if self.day < other.day:
                return True
            else:
                return False
        else:
            return False
    
    def __str__(self) -> str:
        return f"{self.month}月{self.day}日{self.hour}时{self.minute}分"