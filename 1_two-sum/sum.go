package main

import (
	"fmt"
	"sort"
)

func twoSum(nums []int, target int) []int {
	var nums_b = make([]int, len(nums))
	for i := 0; i < len(nums); i++ {
		nums_b[i] = nums[i]
	}

	var maps = make(map[int]bool)
	var firstIndex, secondIndex int
	var firstValue int
	var lastValue int
	var leftValue int
	firstIndex = -1
	secondIndex = -1
	sort.Ints(nums) // 排序
	for i := 0; i < len(nums); i++ {
		maps[nums[i]] = true
	}
	for i := 0; i < len(nums); i++ {
		leftValue = target - nums[i]
		if _, ok := maps[leftValue]; ok {
			firstValue = nums[i]
			lastValue = leftValue
			break
		}
	}

	for i := 0; i < len(nums_b); i++ {
		if firstIndex == -1 && (nums_b[i] == firstValue || nums_b[i] == lastValue) {
			firstIndex = i
			firstValue = nums_b[i]
			leftValue = target - firstValue
		}
		if nums_b[i] == leftValue && i > firstIndex {
			secondIndex = i
		}
		if firstIndex != -1 && secondIndex != -1 {
			break
		}
	}
	return []int{firstIndex, secondIndex}
}

func main() {
	nums := []int{-1, 1, -3, -4, -5}
	target := -4
	fmt.Print(twoSum(nums, target))
}
