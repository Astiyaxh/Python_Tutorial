def common_elements(dictofele):
    return [key for key in dictofele.keys() if key in dictofele.values()]
    # result = []
    # for key in dictofele.keys():
    #     if key in dictofele.values():
    #         result.append(key)
    # return result

print(common_elements({"A": "K", "B": "D", "C": "A", "D": "Z"}))