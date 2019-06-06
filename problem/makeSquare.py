"""
convert triangle to a square

    *             * * *
  * * *     -->   * * *
* * * * *         * * *

Input:- 3

Output:- 2

"""
def main():
    row = int(raw_input("Enter the no. of rows : "))
    if row % 2 == 0:
        num = row - 1
        print num * (num + 1) / 2
    else:
        num = row / 2
        print 2 * ( num * (num + 1) / 2)

main()
