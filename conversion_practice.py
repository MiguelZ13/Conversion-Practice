#!/usr/bin/env python3

import argparse
import sys
import random


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description=""
    )

    # Example arguments
    parser.add_argument(
        "-b", "--bytes",
        type=int,
        default=2,
        help="Number of bytes for generated number"
    )
    
    parser.add_argument(
        "-i", "--input",
        type=str,
        default="hex",
        help="Type that is to be converted"
    )
    
    parser.add_argument(
        "-o", "--output",
        type=str,
        default="dec",
        help="Type that is to be converted into"
    )

    parser.add_argument(
        "-r", "--rounds",
        type=int,
        default="10",
        help="Number of rounds to run"
    )

    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    bytes, inp, out, rounds = args.bytes, args.input, args.output, args.rounds

    inp = inp.lower()
    out = out.lower()
     
    match inp:
        case "dec":
            in_func = (lambda n: n)
        case "binary":
            in_func = (lambda n: bin(n))
        case "hex":
            in_func = (lambda n: hex(n))
        case _:
            print(f"Error: {inp} not a valid output type")
            sys.exit(1)
            
    match out:
        case "dec":
            out_func = (lambda n: n)
        case "binary":
            out_func = (lambda n: bin(n))
        case "hex":
            out_func = (lambda n: hex(n))
        case _:
            print(f"Error: {out} not a valid output type")
            sys.exit(1)
    
    correct = 0
    for i in range(rounds):
        num = random.randint(0, 2 ** (4 * bytes))
        answer = input(f"Give the {out} representation of {in_func(num)}:\n")
        if int(answer) == num:
            correct += 1
            print("Correct!")
        else:
            print(f"Wrong, the correct answer is {out_func(num)}")
    print(f"You got {correct} out of {rounds}")

if __name__ == "__main__":
    main()

