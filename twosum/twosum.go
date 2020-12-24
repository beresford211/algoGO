package main

import (
    "fmt"
    "strconv"
)

func main() {
    arr := []int{2,5,8,7,9,69,15}
    twoSum(arr, 76)
}

func twoSum(numList []int, val int) [][]int {
    m := make(map[string]int)
    var solutions [][]int

    for i := 0; i < len(numList); i++ {
            var diff int = val - numList[i]
            key := strconv.FormatInt(int64(diff), 10)
            fmt.Println(key)
            m[key] = numList[i]
    }

    for i := 0; i < len(numList); i++ {
            var currentVal int
            var exists bool
            currentVal, exists = m[strconv.FormatInt(int64(numList[i]), 10)]

            if exists && currentVal != numList[i] {
                  possibility := []int{ numList[i], currentVal }
                  solutions = append(solutions, possibility)
            }
    }
    return solutions
}
