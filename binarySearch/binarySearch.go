package main

import (
    "fmt"
)

func main() {

  list1 := []int{1, 3, 6, 7, 9, 13}
  r := binarySearch(list1, 14, 0, len(list1))
  fmt.Println("Hello, World!", r)
}

func binarySearch(list []int, target int, low int, high int) int {

    var midPoint = (low + high) / 2
    if high <= low {
      return -1
    }

    if list[midPoint] == target {
      return midPoint
    } else if list[midPoint] > target {
      return binarySearch(list, target, low, midPoint - 1)
    } else {
      return binarySearch(list, target, low + 1, high)
    }
}
