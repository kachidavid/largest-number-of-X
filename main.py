def largest_x_row(lst):
    largest =0
    for row in lst:
        x_count = 0
        for number_x_or_o in row:
            if number_x_or_o == 'X':
                x_count += 1
                if x_count > largest:
                    largest = x_count
    return largest
  

