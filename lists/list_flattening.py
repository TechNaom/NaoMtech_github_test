# Splliting parent list in multiple according to data
# List Flattening


# Splliting parent list in multiple lists as per type of data
def getDataLists(input_list):
    # data_lists
    int_list = []
    float_list = []
    string_list = []
    bool_list = []
    lists_list = []
    try:
        # Iterate this list1
        for data in input_list:
            if type(data) == int:
                int_list.append(data)
            elif type(data) == float:
                float_list.append(data)
            elif type(data) == str:
                string_list.append(data)
            elif type(data) == bool:
                bool_list.append(data)
            elif type(data) == list:
                lists_list.append(data)

        return int_list, float_list, string_list, bool_list, lists_list  # tuple_projects()
    except Exception as e:
        print(e.with_traceback())
    return None


# List Flattening
def getFlatList(input_list):
    # Flattening list
    flatten_list = []

    try:
        ## Iterate list1
        for item in input_list:
            if (type(item) == list):
                # Iterating sublist
                for item in item:
                    flatten_list.append(item)
            else:
                flatten_list.append(item)
        return flatten_list
    except Exception as e:
        print(e.with_traceback())
    return None
if __name__ == '__main__':

    list1 = [1, 2, 3, 4, [10, 20, 30, 40], [100, 200, 300, 400], 10.5, "abc", "xyz", True, False]

    # Calling functions
    data_lists = getDataLists(list1)
    flat_list = getFlatList(list1)

    # Prinintg data variables
    print("The data lists is {}".format(data_lists))
    print("The flat_list  is {}".format(flat_list))

    for li in data_lists:
        print(li)
