package main

import "fmt"

func twoSum(nums []int, target int) []int {
	var maps = make(map[int]int)
	for index, num := range nums {
		if index2, ok := maps[target-num]; ok {
			return []int{index2, index}
		}
		maps[num] = index
	}
	return []int{}
}

func main() {
	nums := []int{1, 3, 2, -3, -4, -5}
	target := 5
	fmt.Print(twoSum(nums, target))
}
