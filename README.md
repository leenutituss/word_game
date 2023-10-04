## Boggle Word Finder
This Python script provides a function called find_word for finding words on a Boggle board. A Boggle board is represented as a 2D array of characters, and the function checks whether a given word can be formed on the board according to Boggle rules.
## Working of function
The find_word function takes two arguments: board (the Boggle board) and word (the word to be found)
## is_valid(x, y)
A helper function is_valid(x, y) is used to check whether a given cell (x, y) is within the boundaries of the Boggle board
## search(x, y, index)
The main work is done in the search(x, y, index) function, which recursively explores the board to find the given word.
If index equals the length of the word, it means the entire word has been found, and the function returns True.
If the current cell (x, y) is invalid or contains a character different from the current character in the word, the function returns False.
The character in the current cell (x, y) is temporarily replaced with "#" to mark it as visited.
The function then checks the neighboring cells (up, down, left, right, and diagonal) using the dx and dy arrays.
For each neighboring cell, it calls itself recursively with the updated position (x + dx[i], y + dy[i]) and index + 1.
If any of the recursive calls returns True, it means a valid path to the word has been found, and the function returns True.
After the recursive calls, the original character in the current cell is restored.
## Main Loop
The main loop of the find_word function iterates through all cells of the Boggle board and calls the search function for each cell to find the word starting from that cell.
## Example
testBoard = [
      ["E","A","R","A"],
      ["N","L","E","C"],
      ["I","A","I","S"],
      ["B","Y","O","R"]]

result = find_word(testBoard, "C")
print(result)  

        
