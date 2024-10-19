def q4(paragraph):
    words = paragraph.lower().split()
    # print(words)
    word_counts = {}
    res = []
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    
    max_count = max(word_counts.values())
    
    for word, c in word_counts.items():
        if c == max_count:
            res.append(word)
            
    return res
    

print(q4("“I want to know how to achieve the things I want” "))