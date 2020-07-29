def reverse_dic(d, ret=None):
    try:
        if ret is None:
            ret = []
        for k, v in sorted(d.items()):
            ret.append(k)
            if isinstance(v, dict):
                reverse_dic(v, ret)
            else:
                ret.append(v)
        output = { ret[1]: ret[0] }
        for i in ret[2:]:
            output = { i: output }   
        return output
    except AttributeError:
        print("Input must be dictionary")
        raise
    except IndexError:
        return {}