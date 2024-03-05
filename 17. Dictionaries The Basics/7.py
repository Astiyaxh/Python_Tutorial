def to_dictionary(strings):
    results = {}
    for index, string in enumerate(strings):
        results[string] = index
    return results

detectives = ["Sherlock Holmes", "Hercule Poirot", "Nancy Drew"]
print(to_dictionary(detectives))

#My Solution
# def length_counts(strings):
#     country_lengths = []
#     results = {}

#     for string in strings:
#         country_lengths.append(len(string))

#     for index, length in enumerate(country_lengths):
#         if length in results:
#             results[length] += 1
#         else:
#             results[length] = 1
        
#     return results

def length_counts(elements):
    counts = {}
    
    for element in elements:
        length = len(element)
        current_count = counts.get(length, 0)
        counts[length] = current_count + 1
    return counts

sa_countries = ["Brazil", "Venezuela", "Argentina", "Argentina", "Ecuador", "Bolivia", "Peru"]
print(length_counts(sa_countries))