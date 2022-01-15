def grid_print(list1):
        for i in (list1):
                for j in i:
                        print(j, end=' ')
                 this is a cool feature called multi cursorprint()
        # for i in list1:
        #         print(" ".join(i))



grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

grid_print(grid)

# lst = [ [1,2,3], [4,5,6], [7,8,9]]
