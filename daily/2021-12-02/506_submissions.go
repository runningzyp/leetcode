package main

import (
	"fmt"
	"sort"
	"strconv"
)

type IntSlice []int

func findRelativeRanks(score []int) []string {
	var maps = make(map[int]string)
	var score1 = make([]int, len(score))
	var result []string
	copy(score1, score)
	sort.Ints(score)
	for i, j := 0, len(score)-1; i < j; i, j = i+1, j-1 {
		score[i], score[j] = score[j], score[i]
	}

	for i := range score {
		switch i {
		case 0:
			maps[score[i]] = "Gold Medal"
		case 1:
			maps[score[i]] = "Silver Medal"
		case 2:
			maps[score[i]] = "Bronze Medal"
		default:
			maps[score[i]] = strconv.Itoa(i + 1)
		}
	}
	for i := 0; i < len(score); i++ {
		result = append(result, maps[score1[i]])
	}
	return result
}
func main() {
	var l = []int{10, 3, 8, 9, 4}
	fmt.Print(findRelativeRanks(l))
}
