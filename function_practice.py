def hello():
    print("A greeting to the user.")

hello()

def pack(first, second, third):
    list_list = [first, second, third]
    print(list_list)

pack("One", "Two", "Three")

def lunch(any_list):
    if any_list:
        list_count = len(any_list)
        print("First I eat " + any_list[0])
        for i in range(1, list_count):
            print("Next I eat " + any_list[i])
    else:
        print("My Lunchbox is Empty!")


food_items = ["Chicken", "Beef", "Broccoli"]
lunch(food_items)