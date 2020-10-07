'''
Write a program to find longest palindrome in a string.
'''


def expandFromCenter(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1


def longestPalindrome(string):
    if len(string) <= 1:
        print(string)

    else:
        start = 0
        end = 0
        for i in range(len(string)):

            len1 = expandFromCenter(string, i, i)
            len2 = expandFromCenter(string, i, i + 1)

            maxLength = max(len1, len2)

            if maxLength > end - start:
                start = i - (maxLength - 1) // 2
                end = i + maxLength // 2

        return len(string[start:end + 1]), string[start:end + 1]


if __name__ == '__main__':
    string = input()
    print(longestPalindrome(string))
