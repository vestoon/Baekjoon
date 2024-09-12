import sys
import collections
input = sys.stdin.readline
sys.setrecursionlimit(1000000)


# Suppose root is right child
def p2p(root, upperBound):  # If input value is bigger than upper bound, it is not your right child, you must return
    left_list = collections.deque()
    left_list.append(upperBound)
    tail = root  # Actually the last element of left list, remain popped
    try:
        nxt = int(input())
        while nxt < tail:
            left_list.appendleft(tail)
            tail = nxt
            nxt = int(input())
        # By the definition of dfs there is no left child
        # nxt is defined and it is right child
        while True:  # Loop for finding the location of right child
            if not nxt:  # EOF
                print(tail)
                while len(left_list) != 1:
                    print(left_list.popleft())
                return 0

            parent = left_list.popleft()
            if nxt > parent:
                print(tail)
                if not left_list:  # When parent is upper bound
                    return nxt

                tail = parent
            else:  # tail < nxt < parent
                left_list.appendleft(parent)
                nxt = p2p(nxt, parent)

    except ValueError:  # EOF
        print(tail)
        while len(left_list) != 1:
            print(left_list.popleft())
        return 0


init = int(input())
p2p(init, 1000000)
