def solution(number, k):
    ans = []
    
    for num in number:
        while ans and k > 0 and ans[-1] < num:
            ans.pop()
            k -= 1
        ans.append(num)
    if k > 0:
        ans = ans[:-k]
        
    return ''.join(ans)