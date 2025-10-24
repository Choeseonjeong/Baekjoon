def solution(cipher, code):
    answer = ''
    return ''.join(cipher[code-1::code])