class Guest:
    def __init__(self,
                 name,
                 sex,
                 region,
                 phone,
                 position,
                 id,
                 permission) -> None:
        self.name = name
        self.sex = sex
        self.region = region
        self.phone = phone
        self.position = position
        self.id = id
        self.permission = permission
        self.card = None
        self.events = []
        self.shedule = []
        self.checkInStation = None
        self.guest_id = None
    
    def __str__(self) -> str:
        return self.name + self.sex + self.region + self.id + self.phone

class Staff:
    def __init__(self, name, role) -> None:
        self.name = name
        self.role = role
        self.staff_id = None
        # self.permission = permission

class CheckInStaion:
    def __init__(self, location, startTime, endTime) -> None:
        self.location = location
        self.startTime = startTime
        self.endTime = endTime
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
        self.guest = card_id
        self.status = status
        self.owner = guest

class Time:
    def __init__(self, month, day) -> None:
        self.month = month
        self.day = day
    
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
        return f"{self.month}月{self.day}日"