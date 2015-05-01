'''
USER: rajat_gupta712
TASK: ADDREV
ALGO: ad-hoc
TAG:  SPOJ
'''
def reverse(num):
  rev = 0
  while(num > 0):
    rev = (10*rev)+num%10
    num //= 10
  return rev

for t in range(int(raw_input())) :
	x, y = map(str, raw_input().split())
	x, y = x[::-1], y[::-1]
	x, y = int(x), int(y)
	z = x + y
	z = reverse(z)
	print z
