package main

func lengthOfLongestSubstring(s string) int {
	var l []string
	var lengh int
	for i := 0; i < len(s); i++ {
		var exist bool = false
		var order int = 0
		for order = 0; order < len(l); order++ {
			if l[order] == string(s[i]) {
				exist = true
				break
			}

		}
		if exist {
			if order+1 >= len(l) {
				l = []string{}
			} else {
				l = l[order+1:]
			}

			l = append(l, string(s[i]))
		} else {
			l = append(l, string(s[i]))
			if lengh < len(l) {
				lengh = len(l)
			}
		}
	}
	return lengh
}
func main() {
	print(lengthOfLongestSubstring("pwwkew"))
}
