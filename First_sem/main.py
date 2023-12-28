def main():
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())

    if (x1 > x3 and x2 < x4) or (x2 > x3 and x1 < x4):
        print(0)
    elif (y1 > y3 and y2 < y4) or (y2 > y3 and y1 < y4):
        print(0)
    else:
        print((abs(x2 - x1) * abs(y2 - y1)))


if __name__ == "__main__":
    main()