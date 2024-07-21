

def sieve(start,interval,end):
    result = []
    last_element = start
    while last_element < end:
        result.append (last_element)
        last_element = last_element + interval
    return result


