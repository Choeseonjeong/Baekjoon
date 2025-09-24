def solution(record):
    arr = dict()
    answer = []

    for i in record:
        parts = i.split()
        if parts[0] == "Enter":
            _, user_id, name = parts
            arr[user_id] = name
            answer.append([user_id, "님이 들어왔습니다."])
        elif parts[0] == "Leave":
            _, user_id = parts
            answer.append([user_id, "님이 나갔습니다."])
        elif parts[0] == "Change":
            _, user_id, name = parts
            arr[user_id] = name
    result = [arr[user_id] + msg for user_id, msg in answer]
    return result
   
