def values_list(enum_cls):
    # create the values_list attribute and then return the class
    enum_cls.values_list = [member.value for member in enum_cls]
    return enum_cls
