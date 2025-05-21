import sys

input = sys.stdin.readline

N, M = map(int, input().split())

chess = []
for _ in range(N):
    chess.append(input().strip())

# Initialize counters for both possible chess patterns
min_count = float('inf')  # To track minimum repainting needed

# Check every possible 8x8 section
for start_row in range(N - 7):
    for start_col in range(M - 7):
        # Count for starting with black at (0,0)
        count_black_start = 0
        # Count for starting with white at (0,0)
        count_white_start = 0
        
        for row in range(8):
            for col in range(8):
                # Actual position on the board
                actual_row = start_row + row
                actual_col = start_col + col
                
                # Determine correct colors
                # If sum of coordinates is even, it should match start color
                if (row + col) % 2 == 0:
                    # Should be black for black start
                    if chess[actual_row][actual_col] != 'B':
                        count_black_start += 1
                    # Should be white for white start
                    if chess[actual_row][actual_col] != 'W':
                        count_white_start += 1
                else:
                    # Should be white for black start
                    if chess[actual_row][actual_col] != 'W':
                        count_black_start += 1
                    # Should be black for white start
                    if chess[actual_row][actual_col] != 'B':
                        count_white_start += 1
        
        # Update minimum count
        min_count = min(min_count, count_black_start, count_white_start)

print(min_count)