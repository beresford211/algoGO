package main

import "fmt"

func main () {
    nums := []int{1, -7, 2, 15, -11, 2}
    maximum_sub_sum(nums) 
}

func maximum_sub_sum(nums []int) {
    var count int
    var prev int


    for i, v := range nums {

        if prev = 0 || (prev + v) > prev {
            prev += v 
        }

        if prev = 0 || (prev + v) > prev {
            prev += v 
        }

        fmt.Println(i) 
        fmt.Println(v) 
        count += v
        fmt.Println(count) 
    }



}


