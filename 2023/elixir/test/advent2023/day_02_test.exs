defmodule Advent2023.Day02Test do
  use ExUnit.Case
  doctest Advent2023.Day02

  test "parses a line" do
    line = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"

    final =
      {1,
       [
         [3, "blue"],
         [4, "red"],
         [1, "red"],
         [2, "green"],
         [6, "blue"],
         [2, "green"]
       ]}

    assert Advent2023.Day02.parse_game(line) == final

    line = "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"

    final =
      {3,
       [
         [8, "green"],
         [6, "blue"],
         [20, "red"],
         [5, "blue"],
         [4, "red"],
         [13, "green"],
         [5, "green"],
         [1, "red"]
       ]}

    assert Advent2023.Day02.parse_game(line) == final
  end

  test "checks a game" do
    # Possible Game
    game =
      [
        [3, "blue"],
        [4, "red"],
        [1, "red"],
        [2, "green"],
        [6, "blue"],
        [2, "green"]
      ]

    assert Advent2023.Day02.checK_game(game)

    game =
      [
        [8, "green"],
        [6, "blue"],
        [20, "red"],
        [5, "blue"],
        [4, "red"],
        [13, "green"],
        [5, "green"],
        [1, "red"]
      ]

    assert !Advent2023.Day02.checK_game(game)
  end

  test "checks a series of games" do
    test_input =
      """
      Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
      Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
      Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
      Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
      Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
      """

    assert Advent2023.Day02.part_1(test_input) == 8
  end

  test "group grabs" do
    game =
      [
        [8, "green"],
        [6, "blue"],
        [20, "red"],
        [5, "blue"],
        [4, "red"],
        [13, "green"],
        [5, "green"],
        [1, "red"]
      ]

    final = %{
      "red" => [20, 4, 1],
      "green" => [8, 13, 5],
      "blue" => [6, 5]
    }

    assert Advent2023.Day02.group_grabs(game) == final
  end

  test "minimum possible distribution" do
    grabs = %{
      "red" => [20, 4, 1],
      "green" => [8, 13, 5],
      "blue" => [6, 5]
    }

    final = %{
      "red" => 20,
      "green" => 13,
      "blue" => 6
    }

    assert Advent2023.Day02.find_minimum_distribution(grabs) == final
  end

  test "power of cubes" do
    distribution = %{
      "red" => 20,
      "green" => 13,
      "blue" => 6
    }

    assert Advent2023.Day02.find_power(distribution) == 1560
  end

  test "part 2" do
    test_input =
      """
      Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
      Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
      Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
      Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
      Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
      """

    assert Advent2023.Day02.part_2(test_input) == 2286
  end
end
