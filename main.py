from functions import *

def menu():
    while True:
        print("\033[34m嘉宾信息管理系统\033[0m")
        print("请选择操作")
        print("1)嘉宾\n2)工作人员\n3)关闭系统")
        choice = input(":")
        if choice == '1':
            print("请验证身份")
            guest_id = input("guest_id:")
            try:
                guest = all_guests[guest_id]
            except:
                print("无效的编号")
            else:
                while True:
                    print("嘉宾操作")
                    print("1)查看基本信息\n2)查询行程信息\n3)返回")
                    choice = input(":")
                    if choice == '1':
                        print(str(guest))
                    elif choice == '2':
                        for event in guest.events:
                            print(f"{event.name}\t{event.startTime}\t{event.endTime}")
                    elif choice == '3':
                        break
        elif choice == '2':
            print("请验证身份")
            staff_id = input("staff_id:")
            staff = None
            for s in all_staffs:
                if s.staff_id == staff_id:
                    staff = s
            if not staff:
                print("无效的id")
            else:
                while True:
                    print("工作人员操作")
                    print("1)写入嘉宾信息\n2)访问嘉宾信息\n3)修改嘉宾权限\n4)活动信息\n5)证件管理\n6)返回上一界面")
                    choice = input(":")
                    if choice == '1':
                        if staff.role not in ["外宾组", "内宾组", "嘉宾组","综合协调组", "接待组"]:
                            print("无权限的操作")
                        else:
                            while True:
                                print("写入嘉宾信息")
                                print("1)从csv文件读取\n2)手动输入\n3)返回")
                                choice = input(":")
                                if choice == '1':
                                    file_name = input("file_name(default = guest_list.csv):")
                                    if not file_name:
                                        file_name = "guest_list.csv"
                                    success = add_guest_from_file(file_name)
                                    if success:
                                        print("写入成功")
                                elif choice == '2':
                                    success = add_guest(input("name:"),
                                                        input("sex:"),
                                                        input("region:"),
                                                        input("id:"),
                                                        input("phone:"),
                                                        input("position:"),
                                                        input("permissionlevel:"),
                                                        input("car_number:"),
                                                        input("arrive_point:"),
                                                        input("arrive_time:"))
                                    if success:
                                        print("写入成功")
                                elif choice == '3':
                                    break
                                else:
                                    print("不支持的操作")
                    elif choice == '2':
                        if staff.role not in ["制证组", "综合协调组", "接待组", "开幕式组", "系列活动组"]:
                            print("无权限的操作")
                        else:
                            while True:
                                print("访问嘉宾信息")
                                print("1)打印嘉宾列表\n2)以编号查找\n3)以姓名查找\n4)以国籍+证件号查找\n5)返回")
                                choice = input(":")
                                if choice == '1':
                                    if len(all_guests) > 0:
                                        print(f"编号  {'姓名': <12}\t{'性别'}\t{'国籍'}\t职位")
                                        for guest in all_guests.values():
                                            print(f"{guest.guest_id}  {guest.name: <12}\t{guest.sex}\t{guest.region}\t{guest.position}")
                                elif choice == '2':
                                    guest_id = input(":")
                                    try:
                                        guest = all_guests[guest_id]
                                    except:
                                        print("未找到目标")
                                    else:
                                        print(f"{guest.guest_id}  {guest.name: <12}\t{guest.sex}\t{guest.region}\t{guest.position}")
                                elif choice == '3':
                                    name = input("name:")
                                    for guest in all_guests.values():
                                        if guest.name == name:
                                            print(f"{guest.guest_id}  {guest.name: <12}\t{guest.sex}\t{guest.region}\t{guest.position}")
                                elif choice == '4':
                                    region = input("region:")
                                    id = input("id:")
                                    for guest in all_guests.values():
                                        if guest.region == region and guest.id == id:
                                            print(f"{guest.guest_id}  {guest.name: <12}\t{guest.sex}\t{guest.region}\t{guest.position}")
                                elif choice == '5':
                                    break
                    elif choice == '3':
                        if staff.role != "综合协调组":
                            print("无权限的操作")
                        else:
                            while True:
                                print("修改嘉宾权限")
                                guest_id = input("guest_id:")
                                for guest in all_guests:
                                    if guest.guest_id == guest_id:
                                        print("查找成功")
                                        new_permissionLevel = input("new_permission:")
                                        guest.permission = Permission(new_permissionLevel, "Guest")
                                        break
                                else:
                                    print("未找到目标")
                    elif choice == '4':
                        while True:
                            print("活动信息操作")
                            print("1)添加活动\n2)查看活动目录\n3)查看活动参与者名单\n4)为活动邀请嘉宾\n5)返回")
                            choice = input(":")
                            if choice == '1':
                                if staff.role in ["开幕式组", "综合协调组", "系列活动组"]:
                                    while True:
                                        print("添加活动")
                                        print("1)手动添加\n2)从文件添加\n3)返回")
                                        choice = input(":")
                                        if choice == '1':
                                            event_name = input("event_name:")
                                            startTime = input("start_time:")
                                            endTime = input("end_time:")
                                            add_event(event_name, startTime, endTime)
                                        elif choice == '2':
                                            file_name = input("file_name(default = events.csv):")
                                            if not file_name:
                                                file_name = "events.csv"
                                                add_event_from_file(file_name)
                                        elif choice == '3':
                                            break
                                else:
                                    print("无权限的操作")
                            elif choice == '2':
                                for event in all_events:
                                    print(f"{event.name}\t{event.startTime}\t{event.endTime}")
                            elif choice == '3':
                                event_name = input("event_name:")
                                for event in all_events:
                                    if event.name == event_name:
                                        for guest in event.attendees:
                                            print(f"{guest.name}\t{guest.region}\t{guest.id}")
                            elif choice == '4':
                                if staff.role in ["开幕式组", "综合协调组", "系列活动组"]:
                                    while True:
                                        print("为活动添加参与嘉宾")
                                        print("1)手动添加\n2)从文件添加\n3)返回")
                                        choice = input(":")
                                        if choice == '1':
                                            print("手动添加嘉宾")
                                            event_name = input("event_name:")
                                            for event in all_events:
                                                if event.name == event_name:
                                                    guest_id = input("guest_id:")
                                                    try:
                                                        guest = all_guests[guest_id]
                                                    except:
                                                        print("未找到目标")
                                                        break
                                                    else:
                                                        event.invit_guest(guest)
                                                        break
                                            else:
                                                print("未找到活动")
                                        elif choice == '2':
                                            print("从文件添加嘉宾")
                                            event_name = input("event_name:")
                                            for event in all_events:
                                                if event.name == event_name:
                                                    file_name = input("file_name:")
                                                    invite_from_file(file_name, event)
                                                    break
                                            else:
                                                print("未找到活动")
                                        elif choice == '3':
                                            break
                                else:
                                    print("无权限的操作")
                            elif choice == '5':
                                break
                    elif choice == '5':
                        while True:
                            print("证件管理")
                            print("1)制作证件并分配至分发站点\n2)查看分配情况\n3)返回")
                            choice = input(":")
                            if choice == '1':
                                for guest in all_guests.values():
                                    make_card(guest)
                                distribute_card()
                            elif choice == '2':
                                for station in checkinstaions:
                                    print(station.location)
                                    for card in station.cards:
                                        print(card.card_id, card.owner.name)
                            elif choice == '3':
                                break
                    elif choice == '6':
                        break
        elif choice == '3':
            break


if __name__ == "__main__":
    system_init()
    menu()
    save_data()