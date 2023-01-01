# Unclear

def solution(play_time, adv_time, logs):
    answer = ''
    watch = []
    for log in logs:
        temp = []
        for time in log.split("-"):
            sep = list(map(int, time.split(":")))
            temp.append(sep)
        watch.append(temp)


    return answer


solution("02:03:55", "00:14:15",
         ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"])
