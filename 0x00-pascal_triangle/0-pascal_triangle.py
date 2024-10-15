def pascal_triangle(n):
    if n <= 0:
        return []  # To return an empty list is n<=0

    pascal = [[1]]  # For the first row
    for a in range(1, n):
        prev_row = pascal[-1]  # To get the prev. row
        curr_row = [1]  # Begins the current row with 1

        # For the middle values of the row
        for b in range(1, len(prev_row)):
            curr_row.append(prev_row[b-1] + prev_row[b])

        curr_row.append(1)  # To end the row with 1
        pascal.append(curr_row)  # Adds the current row to P's triangle

    return pascal
