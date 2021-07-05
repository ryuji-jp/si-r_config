

def comand(list):
    
    if "vlan" in list:
        list2 = list.split("vlan")[0]
        print(list)
        print(list2)
        return list2

    if "flowctl" in list:
        list2 = list.split("flowctl")[0]
        print(list)
        print(list2)
        return list2

    if "use" in list:
        list2 = list.split("use")[0]
        print(list)
        print(list2)
        return list2

    if "address" in list:
        list2 = list.split("address")[0]
        print(list)
        print(list2)
        return list2

    if "nat" in list:
        list2 = list.split("nat")[0]
        print(list)
        print(list2)
        return list2