package main

import "fmt"

//   Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	var first ListNode
	var point1, point2 *ListNode
	var ret int = 0
	first = ListNode{Val: 0, Next: nil}
	point1 = &first
	for true {
		var Val1, Val2 int
		if l1 != nil {
			Val1 = l1.Val
		} else {
			Val1 = 0
		}
		if l2 != nil {
			Val2 = l2.Val
		} else {
			Val2 = 0
		}
		val := (Val1 + Val2 + ret) % 10
		ret = (Val1 + Val2 + ret) / 10
		point1.Val = val
		point1.Next = &ListNode{Val: 0, Next: nil}
		point2 = point1
		point1 = point1.Next
		if l1 != nil {
			l1 = l1.Next
		}
		if l2 != nil {
			l2 = l2.Next
		}
		if l1 == nil && l2 == nil && ret == 0 {
			break
		}
	}
	if point2 != nil {
		point2.Next = nil
	}
	return &first
}
func main() {
	l1 := &ListNode{Val: 9, Next: &ListNode{Val: 9, Next: &ListNode{Val: 9, Next: nil}}}
	l2 := &ListNode{Val: 5, Next: nil}
	fmt.Println(addTwoNumbers(l1, l2))
}
