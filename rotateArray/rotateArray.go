package main

import "sort"


func main() {
    var arr = []int{1, 2, 3, 4, 5, 6, 7}
    rotateArray(arr, 3)
}

func reverser(arr []int, low int, high int) {

    for low < high {
        lower := arr[low]
        higher := arr[high]
        arr[high] = lower
        arr[low] = higher
        low += 1
        high -= 1
    }
}

func rotateArray(arr []int, rotateNum int) []int {

    var numAfterMod int

    if rotateNum > len(arr) {
      numAfterMod = len(arr) % rotateNum
    }

    if rotateNum == 0 {
        return arr
    }

    reverser(arr, 0, numAfterMod-1)
    reverser(arr, numAfterMod, len(arr)-1)

    sort.Reverse(sort.IntSlice(arr))

    return arr
}

