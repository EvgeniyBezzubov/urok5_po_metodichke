def razvorot (verse, reverse = ""):
    ostov = verse%10
    reverse = reverse + str(ostov)
    if len(str(verse))!= 1:
        verse = verse // 10
        razvorot(verse, reverse)
    else:
        print(reverse)
verse = int(input("введите число на разворот: "))
razvorot(verse)

