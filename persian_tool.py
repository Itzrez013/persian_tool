def pnum_to_enum(data):
    pnum_list = {'0':'۰','1':'۱','2':'۲','3':'۳','4':'۴','5':'۵','6':'۶','7':'۷','8':'۸','9':'۹'}
    data2 = ""
    for i in data:
        if i in pnum_list.values():
            for num in pnum_list.keys():
                if pnum_list[num]==i:
                    data2+=num
        else:
            data2+=i
    return data2



print(pnum_to_enum("۰ 	۱ 	۲ 	۳ 	۴ 	۵ 	۶ 	۷ 	۸ 	۹"))