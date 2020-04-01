""" Jay 가 제안주신 두 리스트를 비교해서 item을 찾아내는 optimized 방법
    두번째 리스트가 클수록, 찾는 Variant가 두번째 리스트에 많이 포함될 수록 효율적 """


def return_two_list(a_path="test.txt", b_path="pp5.txt"):
    query_list = []
    subject_list = []
    with open(a_path) as ken:
        for line in ken:
            split_line = line.strip().split("\t")
            query_list.append(split_line[0])
    query_list = list(set(query_list))
    query_list.sort()

    with open(b_path) as pp5:
        for line in pp5:
            split_line = line.strip().split('\t')
            subject_list.append(split_line[0])
    subject_list = list(set(subject_list))
    subject_list.sort()
    return query_list, subject_list


def logan_binary(query: str, data: list):
    lo = 0
    hi = None
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(data) - 1
    while lo < hi:
        mid = (lo + hi) // 2

        if data[mid] < query:
            lo = mid + 1
        else:
            hi = mid

    if data[lo] != query:
        return "notfound"
    else:
        return lo


def brutal_search(q_list, s_list):
    result = []
    for variant in q_list:
        for i, s_variant in enumerate(s_list):
            if s_variant == variant:
                result.append(i)
                break
    return result


def binary_search(q_list, s_list):
    result = []
    for variant in q_list:
        index = logan_binary(variant, s_list)
        if index != "notfound":
            result.append(index)
    return result


def optimized_search(q_list, s_list):
    result = []
    start_idx = 0
    end_idx = 0
    last_searched_idx = 0
    s_len = len(s_list)
    last_lower = 1
    for variant in q_list:
        leap_size = 1
        while(s_list[end_idx] < variant):
            last_lower = end_idx
            end_idx = start_idx + 1 + leap_size
            if end_idx >= s_len:
                end_idx = s_len - 1
                break
            leap_size = leap_size * 2
            
        last_searched_idx = logan_binary(variant, s_list[start_idx:end_idx])
        if last_searched_idx != "notfound":
            start_idx = start_idx + last_searched_idx
            end_idx = start_idx
            if start_idx >= s_len: start_idx = s_len - 1
            if end_idx >= s_len: end_idx = s_len -1
            result.append(start_idx)
        else:
            start_idx = last_lower
            end_idx = start_idx
            if start_idx >= s_len: start_idx = s_len - 1
            if end_idx >= s_len: end_idx = s_len -1
    return result


if __name__ == "__main__":
    import timeit

    query_list, subject_list = return_two_list()
    print(len(query_list), len(subject_list))
    
    start = timeit.default_timer()
    bin_res = binary_search(query_list, subject_list)
    end = timeit.default_timer()
    print(f"binary searching time: {end-start} sec.")

    start = timeit.default_timer()
    opt_res = optimized_search(query_list, subject_list)
    end = timeit.default_timer()
    print(f"binary searching time: {end-start} sec.")
