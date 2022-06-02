def triangle(num,mode='left'):
    if num > 0 and mode == 'left':
        for i in range(0, num):
            for j in range(0, i + 1):
                print("#",end="")
            print("\r")
    elif num < 0 and mode == 'left':
        num = abs(num)
        for k in range(num):
            for l in range(num - k):
                print("#",end="")
            print("\r")

    elif num > 0 and mode == 'right':
     for i in range(num):
        for j in range(1, num - i):
           print(" ", end="")
        for k in range(0, i + 1):
           print("#", end="")
        print()

    elif num > 0 and mode == 'isosceles':
      for i in range(num):
        for j in range(num - i - 1):
          print(' ', end='')
        for k in range(2 * i + 1):
            print('#', end='')
        print()
    
    elif num < 0 and mode == 'isosceles':
        num = abs(num)
        for i in range(num):
            for j in range(i):
              print(' ', end='')
            for j in range(2*(num-i)-1):
                print("#",end="")
            print()
triangle(-3,'isosceles')