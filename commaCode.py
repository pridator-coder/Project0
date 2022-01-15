def comma_and(list_Value):
    # list_Value.insert(len(list_Value)-1,' and ')
    for i in (list_Value):
        if list_Value.index(i)==len(list_Value)-2:
            print(i,end=', and ')
        elif list_Value.index(i)==len(list_Value)-1:
            print(i, end='')
        else:
            print(i,end=', ')


spam = ['apples', 'bananas', 'tofu', 'cats']
comma_and(spam)
