
def is_palindrome(s):

    """ (str) -> bool
    Return True if and only if s is a palindrome

    >>>is_palindrome('noon')
    True
    >>>is_palindrome('racecar')
    True
    >>>is_palindrome('dented')
    False

    """
    #n is the number of characters in s.
    n = len(s)
    first_half = s[0:n//2]
  

    return s[:n//2] == reverse(s[n - n//2:])

def reverse(s):
    """ (str) -> str

    Return a reversed version of s.

    >>> reverse('hello')
    'olleh'
    >>> reverse ('a')
    'a'
    """

    rev = ''
    for ch in s:
        rev = ch + rev

    return rev
