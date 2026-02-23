# for i in [2, 4, 6, 8, 10]:
#     print(i)
iterable = [2, 4, 6, 8, 10]
iterator = iter(iterable)

while True:
    try:
        item = next(iterator)
        print(item)
    except StopIteration:
        break

for i in range(5):
    print(i)