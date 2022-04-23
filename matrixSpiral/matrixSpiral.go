package main

import ( "fmt" )

func main() {

    board := [][]string{
        {"x","x","x","x","x"},
        {"x","x","x","x","x"},
        {"x","x","x","x","x"},
        {"x","x","x","x","x"},
        {"x","x","x","x","x"},
    } 

    matrixSpiral(board)
}

func matrixSpiral(board [][]string) {
    top := 0
    bottom := len(board) - 1  
    left := 0
    right := len(board[0]) - 1

//    for top < bottom && left < right {

        for i := left; i <= right; i++ {
            fmt.Printf("%s ", board[top][i])
        }
        top += 1
        fmt.Println("")
        for x := top; x <= bottom; x++ {
            fmt.Println(board[x][right])
        }
        right -= 1


        for p := right; p > left; p-- {
            fmt.Println(board[bottom][p])
        }
        bottom -= 1


        /*

        for x := top; x < bottom; x++ {
            fmt.Println(board[x][right])
        }
        right -= 1

        for p := right; p > left; p-- {
            fmt.Println(board[bottom][p])
        }
        bottom -= 1

        for r := bottom; r > top; r++ {
            fmt.Println(board[r][left])
        }
        left += 1
        */

//    }
}

