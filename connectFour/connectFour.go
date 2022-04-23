package main

import "fmt"
// 6 rows
// 7 columns

type game struct {
    board [6][7]string
}

func checkCol(board [6][7]string, col int) bool {
    for i := len(board)-1; i > 0; i-- {
        currentState := board[i][col] 
        if currentState != "" && i == len(board)-1 {
           return false 
        }
    } 
    return true
}


func main(){
    connectFour()
}


func connectFour() {
    g := game{} 
    fmt.Println(g)
    showColCount := false
    
    for i := 0; i < len(g.board); i++ {
        if showColCount != true {
            fmt.Println("------------------------------")
        }
        fmt.Println("------------------------------")
        for j := 0; j < len(g.board[0]); j++ {
            fmt.Printf("| %s |", g.board[i][j])
        }
        fmt.Println()
    }
}

