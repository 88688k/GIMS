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
                    print("1)写入嘉宾信息\n2)访问嘉宾信息\n3)修改嘉宾权限\n4)返回上一界面")
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
                                        for guest in all_guests:
                                            print(guest.name)
                                elif choice == '2':
                                    success = add_guest(input("name:"),
                                                        input("sex:"),
                                                        input("region:"),
                                                        input("id:"),
                                                        input("phone:"),
                                                        input("position:"),
                                                        input("permissionlevel:"))
                                    if success:
                                        print("写入成功")
                                        for guest in all_guests:
                                            print(guest.name)
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
                                        print(f"{'姓名': <12}\t{'性别'}\t{'国籍'}\t职位")
                                        for guest in all_guests:
                                            print(f"{guest.name: <12}\t{guest.sex}\t{guest.region}\t{guest.position}")
                                elif choice == '2':
                                    card_id = input(":")
                                    for guest in all_guests:
                                        if guest.card_id == card_id:
                                            print(f"{guest.name: <12}\t{guest.sex}\t{guest.region}\t{guest.position}")
                                elif choice == '3':
                                    name = input("name:")
                                    for guest in all_guests:
                                        if guest.name == name:
                                            print(f"{guest.name: <12}\t{guest.sex}\t{guest.region}\t{guest.position}")
                                elif choice == '4':
                                    region = input("region:")
                                    id = input("id:")
                                    for guest in all_guests:
                                        if guest.region == region and guest.id == id:
                                            print(f"{guest.name: <12}\t{guest.sex}\t{guest.region}\t{guest.position}")
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
                        break
        elif choice == '3':
            break


if __name__ == "__main__":
    system_init()
    menu()