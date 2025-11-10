

def solution(want, number, discount):
    result = 0

    want_dict = dict(zip(want, number))

    for i in range(len(discount) - 9):

        # 각 일자별 할인 상품의 수를 카운팅해서 want_dict와 동일하면
        # 10일 동안 모든 할인 상품을 구매가능함

        discount_dict = {}
        for j in range(i, i+10):
            food = discount[j]
            discount_dict[food] = discount_dict.get(food, 0) + 1
        
        # 모두 동일하면 조건 만족
        if want_dict == discount_dict:
            result += 1


    return result
    