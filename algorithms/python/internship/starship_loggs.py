script = ['ABS', 'ABC', 'AC']


def ooo(n: int, log_dict) -> str:
    number_id = {(log_dict[i].split()[0]): (log_dict[i].split()[3]) for i in range(n)}
    id = []
    for i in range(n):
        id.append(log_dict[i].split()[3])
    unique_id = list(set(id))
    print(number_id)
    # for o in range(len(unique_id)):
    #     for p in range(n):
    #         if log_dict[p].split()[3] == unique_id[o] and log_dict[p].split()[0] == unique_id[o]:
    #             log_dict[p].split()[4]


def read_input():
    n = int(input())
    log_dict = {i: input() for i in range(n)}
    return n, log_dict


n, log_dict = read_input()
ooo(n, log_dict)
