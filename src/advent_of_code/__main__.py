import pathlib

import click

import advent_of_code.twentytwentythree.dayone
import advent_of_code.twentytwentythree.daytwo


@click.group()
@click.pass_context
def cli(ctx):
    pass


@cli.group()
@click.pass_context
def twentytwentythree(ctx):
    pass


@twentytwentythree.command()
@click.pass_context
def dayone(ctx):
    p = advent_of_code.twentytwentythree.dayone.PuzzleOne(
        pathlib.Path("data/2023/1/input.txt")
    )

    print(f"puzzle one: {p.run()}")

    p = advent_of_code.twentytwentythree.dayone.PuzzleTwo(
        pathlib.Path("data/2023/1/input.txt")
    )

    print(f"puzzle two: {p.run()}")


@twentytwentythree.command()
@click.pass_context
def daytwo(ctx):
    p = advent_of_code.twentytwentythree.daytwo.PuzzleOne(
        pathlib.Path("data/2023/2/input.txt")
    )

    result = p.run()

    print(f"puzzle one: {result}")

    p = advent_of_code.twentytwentythree.daytwo.PuzzleTwo(
        pathlib.Path("data/2023/2/input.txt")
    )

    result = p.run()

    print(f"puzzle two: {result}")


if __name__ == "__main__":
    cli(obj={})
