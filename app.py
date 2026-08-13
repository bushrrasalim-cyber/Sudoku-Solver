import streamlit as st
from copy import deepcopy
from dsa_core import Solution

st.title("Sudoku Solver")

board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

if "new_board" not in st.session_state:
    st.session_state.new_board = deepcopy(board)

for row in range(9):
    columns = st.columns(9)

    for col in range(9):

        if board[row][col] != ".":
            columns[col].text_input(
                "cell",
                value=board[row][col],
                disabled=True,
                label_visibility="collapsed",
                key=f"cell-{row}-{col}"
            )

            st.session_state.new_board[row][col] = board[row][col]

        else:
            value = columns[col].text_input(
                "cell",
                value=st.session_state.new_board[row][col],
                label_visibility="collapsed",
                key=f"cell-{row}-{col}"
            )

            st.session_state.new_board[row][col] = value


if st.button("Check"):

    correct_board = deepcopy(board)

    solver = Solution()
    solver.solveSudoku(correct_board)

    if st.session_state.new_board == correct_board:
        st.success("Correct! 🎉")
    else:
        st.error("Incorrect. ❌")


if st.button("Show Solution"):

    correct_board = deepcopy(board)

    solver = Solution()
    solver.solveSudoku(correct_board)

    for row in range(9):
        columns = st.columns(9)

        for col in range(9):
            columns[col].text_input(
                "solution",
                value=correct_board[row][col],
                disabled=True,
                label_visibility="collapsed",
                key=f"solution-{row}-{col}"
            )