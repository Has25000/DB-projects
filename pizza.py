import numpy as np
def main():
    print("1 - size")
    print("2 - toppings")
    print("3 - slices")
    print("10 - exit")
    toppings = []
    num_of_slices =0
    size_of_pizza = "2"
    while True:
        choice = input("enter a number: ")
        if choice == "1":
            size_of_pizza = size()

        elif choice == "2":
            toppings = topping()
            
        elif choice =="3":
            num_of_slices = slices()
              
        elif choice == "10":
            slices_in_pizza = 0
            match size_of_pizza:
                case "1":
                    slices_in_pizza = 4
                case "2":
                    slices_in_pizza = 6
                case "3":
                    slices_in_pizza = 8
            area_left, perimeter_left = area(size_of_pizza, slices_in_pizza, num_of_slices)
            match size_of_pizza:
                case "1":
                    size_of_pizza = "small" 
                case "2":
                    size_of_pizza = "medium" 
                case "3":
                    size_of_pizza = "large" 
            print("enjoy your pizza!")
            print("Pizza toppings: {}".format(toppings))
            print("pizza size:  {}".format(size_of_pizza))
            print("slices:  {}".format(num_of_slices))
            print("slices left: {}".format(slices_in_pizza - num_of_slices))
            print("area of pizza left: {}".format(area_left))
            print("perimeter of pizza left:  {}".format(perimeter_left))
            break
        else:
            print("input a valid response")
    print(toppings, num_of_slices, size_of_pizza)

def topping():
    food = []
    while True:
        topping = input("what topping do you want? ")
        food.append(topping)
        print("1 - yes")
        print("2 - no")
        End = input("do you want to add more TOPPINGS? ")
        if End == "2":
            break   
    return food

def slices():
    slice = input("how many slices do you want? ")
    slice = int(slice)
    return slice

def size():
    list_of_sizes = ["1", "2", "3"]
    print("1 - small")
    print("2 - medium") 
    print("3 - large")  
    sizes = input("what size do u want? ")
    if sizes not in list_of_sizes:
        print("please enter a valid size")
        sizes = size()
    return sizes


def area(size, slices, slices_ate):
    diameter = {
        "3": 15,
        "2": 12,
        "1": 9
    }
    pizza_diameter = diameter[size]
    pizza_radius = pizza_diameter/2
    pi = np.pi
    area = pi*(pizza_radius**2)
    perimeter = pizza_diameter*pi 
    ratio = (slices-slices_ate)/slices
    area_of_pizza_left= area*ratio 
    perimeter_of_pizza_left= perimeter*ratio 
    return area_of_pizza_left, perimeter_of_pizza_left

if __name__ == "__main__":
    main()
    