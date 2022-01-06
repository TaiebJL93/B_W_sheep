import argparse
import sys
from b_w_sheep import SheepProblem

# pylint: disable=missing-function-docstring


def main():
    args = parse_arguments()
    number_b = args.num_B
    number_w = args.num_W
    '''ignore any operation with number_B and number_W equal to zero'''
    if number_b == number_w == 0:
        return 0
    b_sheep = ["B" for i in range(0, number_b)]
    w_sheep = ["W" for i in range(0, number_w)]
    First_list = b_sheep + ["space"] + w_sheep
    final_list = First_list[::-1]
    index = First_list.index("space")
    # Print the first list
    print(First_list)
    my_function = SheepProblem()
    my_function.moving_sheep("W", First_list, index)
    print(First_list)
    save = "W"  # to save the color the sheep of the last step
    while First_list != final_list:
        index = First_list.index("space")
        # we have deal with the space_index position we have 4 possibilities
        # (first_index, second_index,last_index,Before_last)
        if index == 0:
            if First_list[index+1] == "W":
                my_function.moving_sheep("W", First_list, index)
                save = "W"
            elif(First_list[index+1] == "B" and First_list[index+2] == "W"):
                my_function.jumping_step("W", First_list, index)
                save = "W"
            else:
                pass
        elif index == 1:
            if First_list[index-1] == First_list[index+1] == "W":
                my_function.moving_sheep("W", First_list, index)
                save = "W"
            elif First_list[index-1] == First_list[index+1] == "B":
                if First_list[index+2] == "W":
                    my_function.jumping_step("W", First_list, index)
                    save = "W"
                else:
                    my_function.jumping_step("B", First_list, index)
                    save = "B"
            elif First_list[index+1] == "B" and First_list[index-1] == First_list[index+2] == "W":
                my_function.jumping_step("W", First_list, index)
                save = "W"
            elif First_list[index-1] == "B" and save == "B":
                my_function.moving_sheep(save, First_list, index)
            elif First_list[index+1] == "W" and save == "W":
                my_function.moving_sheep(save, First_list, index)
            else:
                pass
        elif index == len(First_list)-1:
            if First_list[index-1] == "B":
                my_function.moving_sheep("B", First_list, index)
                save = "B"
            elif(First_list[index-1] == "W" and First_list[index-2] == "B"):
                my_function.jumping_step("B", First_list, index)
                save = "B"
            else:
                pass
        elif index == len(First_list)-2:
            if First_list[index-1] == First_list[index+1] == "B":
                my_function.moving_sheep("B", First_list, index)
                save = "B"
            elif First_list[index-1] == First_list[index+1] == "W":
                if First_list[-4] == "B":
                    my_function.jumping_step("B", First_list, index)
                    save = "B"
                else:
                    my_function.moving_sheep("W", First_list, index)
                    save = "W"
            elif First_list[-3] == "W" and First_list[-1] == First_list[-4] == "B":
                my_function.jumping_step("B", First_list, index)
                save = "B"
            elif First_list[index-1] == "B" and save == "B":
                my_function.moving_sheep(save, First_list, index)
            elif First_list[index+1] == "W" and save == "W":
                my_function.moving_sheep(save, First_list, index)
            else:
                print("Blocking step")
                sys.exit()
        else:
            if First_list[index-1] == First_list[index+1]:
                if my_function.checking_jump("B", First_list, index) or my_function.checking_jump("W", First_list, index):
                    if First_list[index-1] == "W" and First_list[index-2] == "B":
                        if my_function.checking_jump("B", First_list, index):
                            my_function.jumping_step("B", First_list, index)
                            save = "B"
                        else:
                            try:
                                my_function.moving_sheep(
                                    "W", First_list, index)
                                save = "W"
                            except:
                                print("Block error")
                    elif (First_list[index+1] == "B" and First_list[index+2] == "W"):
                        if my_function.checking_jump("W", First_list, index):
                            my_function.moving_sheep("W", First_list, index)
                            save = "W"
                        else:
                            try:
                                my_function.moving_sheep(
                                    "B", First_list, index)
                                save = "B"
                            except:
                                pass
                else:
                    if First_list[index-1] == "W":
                        my_function.moving_sheep("W", First_list, index)
                        save = "W"
                    else:
                        my_function.moving_sheep("B", First_list, index)
                        save = "B"
            else:
                if((First_list[index-1] == "B" and save == "B") or (First_list[index+1] == "W" and save == "W")):
                    my_function.moving_sheep(save, First_list, index)
                else:
                    if my_function.checking_jump(save, First_list, index):
                        my_function.jumping_step(save, First_list, index)
        print(First_list)


def parse_arguments():
    parser = argparse.ArgumentParser(description="Black/white sheep problem")
    parser.add_argument("-num_of_black_sheep", '--num_B', default=4, type=int,
                        help="The number of the black sheep")
    parser.add_argument("-num_of_white_sheep", '--num_W', default=3, type=int,
                        help="The number of the white sheep")
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    main()
