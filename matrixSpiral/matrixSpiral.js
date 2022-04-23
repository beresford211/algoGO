function matrixSpiral(board) {
  let col = 0;
  let row = 0;
  let cole = board.length - 1;
  let rowe = board[0].length - 1;
  let num = 1;

  while(col <= cole || row <= rowe){
    for (let i = col; i <= cole; i++) {
      board[row][i] = num;
      num++;
    }
    row++;

    for (let x = row; x <= rowe; x++) {
      board[x][cole] = num;
      num++;
    }
    cole--;

    for (let y = cole; y >= col; y--) {
      board[rowe][y] = num;
      num++;
    }
    rowe--;

    for (let p = rowe; p >= row; p--) {
      board[p][col] = num;
      num++;
    }
    col++;
  }

  console.log("board[0].length", board)
}

let n = [
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0]
]

matrixSpiral(n)
