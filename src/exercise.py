def main():
    #write your code below this line
    intList = []
    while(True):
      number = int(input())
      if(number==-1):
        break
      intList.append(number)
    from1 = int(input("From where?"))
    to1 = int(input("To where?"))
    for i in range(from1,to1+1):
      print(intList[i])
    



if __name__ == '__main__':
    main()
