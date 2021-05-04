from collections import Counter
def solution(s):

    s = list(s.lstrip('{{').rstrip('}}').split('},{'))

    cnt_list = Counter()
    for i, val in enumerate(s):
        s[i] = list(map(int, val.split(',')))
        s_cnt = Counter(s[i])
        cnt_list += s_cnt

    answer = []
    for key, val in cnt_list.most_common():
        answer.append(key)

    return answer



s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
solution(s)