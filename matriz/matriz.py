import numpy as np

def array_5x5() -> np.ndarray:
    """
    Return a array 5x5
    """
    return np.random.randint(10,size=(5,5))

def check_seq(arr:np.ndarray) -> bool:
    """
    Returns the sequence if the sequence is found in the array
    """

    SEQ_LIST = [f"{n}, {n}, {n}, {n}" for n in range(10)]

    for seq in SEQ_LIST:
        check_arr = repr(arr).count(seq)
        check_transpose = repr(arr.transpose()).count(seq)
        if check_arr >= 1 or check_transpose >= 1:
            return seq

def check_array():
    """
    Prints the array and the sequence if the array has 4 consecutive digits
    """
    arr = array_5x5()
    seq = check_seq(arr)
    if seq:
        print("Found in:\n", arr)
        print("The sequence is: ", seq)


if __name__ == "__main__":
    for i in range(200):
        check_array()
