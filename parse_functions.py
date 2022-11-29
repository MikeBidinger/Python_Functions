def string_to_list(str: str, seperator: str = "\n", limit: int = 0):
    list = []
    # Parse string to list
    row_list = str.split(seperator)
    # If limit is set
    if limit != 0:
        for idx, x in enumerate(row_list):
            list.append(x)
            # If limit is reached
            if idx == limit:
                break
    # If limit isn't set
    else:
        list = str.split(seperator)
    # Return array (2D)
    return list


def list_to_dict(
    list: list,
    list_widths: list,
    list_headers: list = [],
    key_pos: int = 0,
    key_offset: int = 0,
):
    dict = {}
    headerOffset = 0
    # Get header
    if list_headers == []:
        headerOffset = 1
        cntPos = 0
        for widthHeader in list_widths:
            list_headers.append(list[0][cntPos : widthHeader + cntPos])
            cntPos += widthHeader
    # Parse list to dictionary
    for i in range(headerOffset, len(list)):
        if list[i] != [""]:
            cntPos = 0
            cnt = 0
            if key_pos != -1:
                lenPos = 0
                for j in range(key_pos):
                    lenPos += list_widths[j]
                valKey = list[i][lenPos : list_widths[key_pos]].strip()
            else:
                valKey = i + key_offset
            for widthHeader in list_widths:
                if valKey not in dict:
                    dict[valKey] = {}
                dict[valKey][list_headers[cnt]] = list[i][
                    cntPos : widthHeader + cntPos
                ].strip()
                cntPos += widthHeader
                cnt += 1
    return dict


def dict_to_key_and_item(dict: dict):
    key_list = []
    item_list = []
    for key, item in dict.items():
        key_list.append(key)
        item_list.append(item)
    return key_list, item_list


def dict_to_csv(
    dict: dict, id_header: str, seperator: str = ";", replace_seperator: bool = False
):
    list = []
    header_list = []
    header_list.append(id_header)
    key = next(iter(dict))
    for x in dict[key]:
        header_list.append(x)
    list.append(seperator.join(header_list))
    for i in dict:
        data_list = []
        data_list.append(str(i))
        for x in dict[i].values():
            if replace_seperator == False:
                data_list.append(x)
            else:
                data_list.append(x.replace(seperator, ""))
        list.append(seperator.join(data_list))
    return list
