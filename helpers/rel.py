def unpack_arrays(arr):
    result = []
    
    for sub_arr in arr:
        result.extend(sub_arr)
    
    return result

def convert_to_relative1(data, first, type):
    newdata = []
    for i in range(len(data)):
        
        if i == 0:
            previous_candle = first
        else:
            previous_candle = data[i - 1]
        current_candle = data[i]

        if previous_candle[0] != 0 and previous_candle[0] != current_candle[0]:
            if previous_candle[0] < current_candle[0]:
                relative_open = round((current_candle[0] - previous_candle[0]) / previous_candle[0], 2)
            else:
                relative_open = -round((previous_candle[0] - current_candle[0]) / previous_candle[0], 2)
        else:
            relative_open = 0
        
        if previous_candle[1] != 0 and previous_candle[1] != current_candle[1]:
            if previous_candle[1] < current_candle[1]:
                relative_high = round((current_candle[1] - previous_candle[1]) / previous_candle[1], 2)
            else:
                relative_high = -round((previous_candle[1] - current_candle[1]) / previous_candle[1], 2)
        else:
            relative_high = 0
        
        if previous_candle[2] != 0 and previous_candle[2] != current_candle[2]:
            if previous_candle[2] < current_candle[2]:
                relative_low = round((current_candle[2] - previous_candle[2]) / previous_candle[2], 2)
            else:
                relative_low = -round((previous_candle[2] - current_candle[2]) / previous_candle[2], 2)
        else:
            relative_low = 0
        
        if previous_candle[3] != 0 and previous_candle[3] != current_candle[3]:
            if previous_candle[3] < current_candle[3]:
                relative_close = round((current_candle[3] - previous_candle[3]) / previous_candle[3], 2)
            else:
                relative_close = -round((previous_candle[3] - current_candle[3]) / previous_candle[3], 2)
        else:
            relative_close = 0
        
        if previous_candle[4] != 0 and previous_candle[4] != current_candle[4]:
            if previous_candle[4] < current_candle[4]:
                relative_volume = round((current_candle[4] - previous_candle[4]) / previous_candle[4], 2)
            else:
                relative_volume = -round((previous_candle[4] - current_candle[4]) / previous_candle[4], 2)
        else:
            relative_volume = 0

        # data[i] = [relative_open, relative_high, relative_low, relative_close, relative_volume]
        newdata.append([relative_open, relative_high, relative_low, relative_close, relative_volume])
        one_array = unpack_arrays(newdata)
        if type != 3:
            one_array.append(type)
    return one_array

def convert_to_relative2(data, first, type):
    newdata = []
    for i in range(len(data)):
        
        if i == 0:
            previous_candle = first
        else:
            previous_candle = data[i - 1]
        current_candle = data[i]

        if previous_candle[0] != 0 and previous_candle[0] != current_candle[0]:
            if previous_candle[0] < current_candle[0]:
                relative_open = round(((current_candle[0] - previous_candle[0]) / previous_candle[0]) * 100, 2)
            else:
                relative_open = -round(((previous_candle[0] - current_candle[0]) / previous_candle[0]) * 100, 2)
        else:
            relative_open = 0
        
        if previous_candle[1] != 0 and previous_candle[1] != current_candle[1]:
            if previous_candle[1] < current_candle[1]:
                relative_high = round(((current_candle[1] - previous_candle[1]) / previous_candle[1]) * 100, 2)
            else:
                relative_high = -round(((previous_candle[1] - current_candle[1]) / previous_candle[1]) * 100, 2)
        else:
            relative_high = 0
        
        if previous_candle[2] != 0 and previous_candle[2] != current_candle[2]:
            if previous_candle[2] < current_candle[2]:
                relative_low = round(((current_candle[2] - previous_candle[2]) / previous_candle[2]) * 100, 2)
            else:
                relative_low = -round(((previous_candle[2] - current_candle[2]) / previous_candle[2]) * 100, 2)
        else:
            relative_low = 0
        
        if previous_candle[3] != 0 and previous_candle[3] != current_candle[3]:
            if previous_candle[3] < current_candle[3]:
                relative_close = round(((current_candle[3] - previous_candle[3]) / previous_candle[3]) * 100, 2)
            else:
                relative_close = -round(((previous_candle[3] - current_candle[3]) / previous_candle[3]) * 100, 2)
        else:
            relative_close = 0
        
        if previous_candle[4] != 0 and previous_candle[4] != current_candle[4]:
            if previous_candle[4] < current_candle[4]:
                relative_volume = round(((current_candle[4] - previous_candle[4]) / previous_candle[4]) * 100, 2)
            else:
                relative_volume = -round(((previous_candle[4] - current_candle[4]) / previous_candle[4]) * 100, 2)
        else:
            relative_volume = 0

        # data[i] = [relative_open, relative_high, relative_low, relative_close, relative_volume]
        newdata.append([relative_open, relative_high, relative_low, relative_close, relative_volume])
    one_array = unpack_arrays(newdata)
    if type != 3:
        one_array.append(type)
    return one_array