tileLen = [1, 2, 3, 4]

# this gets very slow when target is big
def tiling(target):
	if target < 0:
		return 0
	elif target < 2:
		return 1
	else:
		return sum([tiling(target - i) for i in tileLen])

# PE117
i = 4
rec = (tiling(1), tiling(2), tiling(3), tiling(4))
while i<50:
	rec = (rec[1], rec[2], rec[3], rec[0]+rec[1]+rec[2]+rec[3])
	i+=1

print(rec[3])

# PE116
# note that all-black tile should not be counted.
def one_color_tiling(tileSize, n):
	if n < 0:
		return 0
	elif n < tileSize:
		return 1
	else:
		return one_color_tiling(tileSize, n-1) + one_color_tiling(tileSize, n-tileSize)

r = (one_color_tiling(2, 1), one_color_tiling(2, 2))
g = (one_color_tiling(3, 1), one_color_tiling(3, 2), one_color_tiling(3, 3))
b = (one_color_tiling(4, 1), one_color_tiling(4, 2), one_color_tiling(4, 3), one_color_tiling(4, 4))

i = 1
while i<50:
	r = (r[1], r[0]+r[1])
	g = (g[1], g[2], g[0]+g[2])
	b = (b[1], b[2], b[3], b[0]+b[3])
	i+=1

print(r[0] + g[0] + b[0] - 3)

