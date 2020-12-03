import day1
import day2
import day3
import day4


def main():
    for i in range(1, 5):
        print(f"\n============\nRun day {i}")
        eval(f'day{i}.main()')
        print("============")


if __name__ == "__main__":
    main()
