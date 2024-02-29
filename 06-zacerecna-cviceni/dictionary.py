num_res = {
    "Harry": 85,
    "Ron": 71,
    "Hermione": 98,
    "Draco": 69
}

word_res = {}

for key in num_res:
    if num_res[key] >= 91:
        word_res[key] = "Excelentní"
    elif num_res[key] < 91 and num_res[key] > 80:
        word_res[key] = "Vynikající"
    elif num_res[key] < 81 and num_res[key] > 70:
        word_res[key] = "Splněno"
    elif num_res[key] < 71:
        word_res[key] = "Nesplněno"

print(word_res)