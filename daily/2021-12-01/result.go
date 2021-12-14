package main

func maxPower(s string) int {
	var ret string
	maxp := 1
	retp := 1
	for i := 0; i < len(s); i++ {
		if string(s[i]) == ret {
			retp += 1
		} else {
			retp = 1
		}
		if maxp < retp {
			maxp = retp
		}
		ret = string(s[i])
	}
	return maxp
}

func main() {
	print(maxPower("hooraaaaaaaaaaay"))
}
