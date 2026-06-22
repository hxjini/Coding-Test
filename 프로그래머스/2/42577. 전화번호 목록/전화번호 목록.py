def solution(phone_book):
    phone_book.sort()
    phone_set = set()
    
    for phone in phone_book:
        for i in range(1, len(phone)):
            if phone[:i] in phone_set:
                return False
        phone_set.add(phone)
        
    return True