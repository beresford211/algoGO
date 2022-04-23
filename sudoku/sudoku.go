package main

import (
    "fmt"
)

board [][]byte

func main () {

}

func sudokuSolver() {
    for x := range board {
        for y := range board {
           if board[x][y] == 0 {
               for i := 0; i < 10; i++ {

                    // check if we can use this value "i + 1"
               } 
           } 
        }
    } 
}

func isPossible(board [][]byte, num int, x int, y int) {
    leng := len(board)

    for i := range board {
        if board[i][y] == num {
            return false
        }
    }

    for n := range board {
        if board[x][n] == num {
            return false
        }
    }


    xBoard := (x / 3) * 3
    yBoard := (y / 3) * 3
    for p := 0; p < 3; p++ {
        for w := 0; w < 3; w++ {
           piece := board[p + xBoard][w + yBoard]              
           if piece == num {
            return false
           }
        }
    }

    return true
}


func checkCol(board [][]byte, col int) bool {
    numsCount := map[int]bool{ 1: false,
        2: false,
        3: false,
        4: false,
        5: false,
        6: false,
        7: false,
        8: false,
        9: false }
    i := 0

    for k := range numsCount {
        currentVal := board[i][col]
        if numsCount[currentVal] {
            return false
        } else {
            numsCount[currentVal] = true
        }
    }
}

func checkRow(board [][]byte, row int) bool {
    numsCount := map[int]bool{
        1: false,
        2: false,
        3: false,
        4: false,
        5: false,
        6: false,
        7: false,
        8: false,
        9: false }
    i := 0
    for k := range numsCount {
        currentVal := board[row][i]
        if numsCount[currentVal] {
            return false
        } else {
            numsCount[currentVal] = true
        }
    }
}
