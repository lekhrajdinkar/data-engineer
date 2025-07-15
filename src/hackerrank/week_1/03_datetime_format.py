import os

def timeConversion(s):
    s_arr = s.split(":")
    ampm = s_arr[2][-2::]
    if ampm == 'AM':
        print(s_arr)
        hour = 0 if int(s_arr[0]) == 12 else int(s_arr[0])
        return f"{str(hour):02}"+':'+s_arr[1]+':'+s_arr[2][:2:]
    else:
        print(s_arr)
        print(int(s_arr[0])+12)
        print(int(s_arr[1]))
        print(int(s_arr[2][:2:]))
        hour = int(s_arr[0])  if int(s_arr[0]) == 12 else int(s_arr[0]) + 12
        return f"{str(hour):02}"+':'+s_arr[1]+':'+s_arr[2][:2:]

if __name__ == '__main__':
    t1 = '12:05:45AM'
    result = timeConversion(t1)
    print(result)
