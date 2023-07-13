def badge_maker(name):
    print(f"Hello, my name is {name}.")
    return (f"Hello, my name is {name}.")

def batch_badge_creator(names):
    sentences=[]
    for name in names:
        sentence = (f"Hello, my name is {name}.")
        sentences.append(sentence)
    return sentences

def assign_rooms(names):
    sentences=[]
    for index, name in enumerate(names):
        sentence = (f"Hello, {name}! You'll be assigned to room {index +1}!")
        sentences.append(sentence)
    return sentences

def printer(names):
    sentences1 = batch_badge_creator(names)
    sentences2 = assign_rooms(names)
    
    for sentence in sentences1:
        print(sentence)

    for sentence in sentences2:
        print(sentence)
