# gain n/3
# lose n/4
start_size = int(input("Start size: "))
end_size = int(input("End size: "))
gain = start_size // 3
loss = start_size // 4
to_sum = gain - loss
year = end_size - start_size

if (start_size > 9) and (end_size > start_size):

    total = start_size + (to_sum * year)
    print(total)