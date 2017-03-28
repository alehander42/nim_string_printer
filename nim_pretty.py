import gdb.printing

SIZE = 16
NIM_KINDS = {'NIM_BOOL', 'NimStringDesc', 'Nim'}

class NimStringDescPrinter(object):
    "Print nim"

    def __init__(self, val, chase=0):
        self.val = val
        self.chase = chase

    def to_string(self):
        # just show the string for now
        # * can be a part of a string too, future edge case
        if repr(self.val.address) == '0x0':
            return ''
        else:
            # return repr(type(self.val.address))
            a = star(self.chase)
            return a + str(self.val['data'])[SIZE:-1]

    def display_hint(self):
        return 'nim'

class NimPrinter(object):
    
    def __init__(self, type_desc, val, chase=0):
        self.type_desc, self.val, self.chase = type_desc, val, chase

    def to_string(self):
        return star(self.chase) + getattr(self, self.type_desc.lower())()
    
    def nim_bool(self):
        return 'true' if self.val == 1 else 'false'

    def display_hint(self):
        return 'nim'

def nim_printer():
    pp = gdb.printing.RegexpCollectionPrettyPrinter(
        'nim_pretty')
    pp.add_printer('nim', '^NimStringDesc$', NimStringDescPrinter)
    return pp


def nim(val, chase=0):
    '''
    `val`:   `str` the value
    `chase`: `int` the number of pointers that we chase
    '''
    typ = val.type
    type_desc = str(typ)
    # hot path, it can be just combined with the other types, but
    # I'd fix it later if this script proves usable
    if type_desc == 'NimStringDesc *' and val:
        return NimStringDescPrinter(val.dereference(), chase=chase+1)
    elif typ.code == gdb.TYPE_CODE_PTR or typ.code == gdb.TYPE_CODE_MEMBERPTR:
        if not val:
            return None
        return nim(val.dereference(), chase + 1)
    elif type_desc in NIM_KINDS:
        return NimPrinter(type_desc, val, chase)
    return None
    
def register_printers(objfile):
    objfile.pretty_printers.append(nim)

def star(chase=0):
    result = '*' * chase
    if result:
        result += '  '
    return result
