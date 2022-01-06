"""
high level support for doing this and that.
"""
# pylint: disable=missing-docstring


class SheepProblem():
    @classmethod
    def moving_sheep(
        cls,
        color_of_sheep,
        my_list,
        index_space
    ):
        ''' Moving one sheep black to white or opposite'''
        if color_of_sheep == "W":
            my_list[index_space], my_list[index_space +
                                          1] = my_list[index_space +1], my_list[index_space]
        else:
            my_list[index_space], my_list[index_space -
                                          1] = my_list[index_space -1], my_list[index_space]

    @classmethod
    def jumping_step(
        cls,
        color_of_sheep,
        my_list,
        index_space
    ):
        ''' Jumping the sheep over one other sheep'''
        if color_of_sheep == "W":
            my_list[index_space], my_list[index_space +
                                          2] = my_list[index_space +2], my_list[index_space]
        else:
            my_list[index_space], my_list[index_space -
                                          2] = my_list[index_space -2], my_list[index_space]

    @classmethod
    def checking_jump(
        cls,
        color_of_sheep,
        my_list,
        index_space
    ):
        ''' Checking if the sheep can make the jump'''
        if color_of_sheep == my_list[index_space +2] == "W" and my_list[index_space +1] == "B":
            return True
        if color_of_sheep == my_list[index_space -2] == "B" and my_list[index_space -1] == "W":
            return True
        return False
