defmodule Advent2023.Day03Test do
  use ExUnit.Case
  doctest Advent2023.Day03

  @schematic """
  467..114..
  ...*......
  ..35..633.
  ......#...
  617*......
  .....+.58.
  ..592.....
  ......755.
  ...$.*....
  .664.598..
  """
  test "find number spans in a line" do
    line = "467..114.."
    expected = [{0, 3}, {5, 3}]
    assert Advent2023.Day03.number_spans(line) == expected
  end

  test "find symbol coords in a line" do
    line = "...$.*...."
    expected = [3, 5]
    assert Advent2023.Day03.symbol_indices(line) == expected
  end

  test "find symbol coords in a schematic" do
    expected = [
      {1, 3},
      {3, 6},
      {4, 3},
      {5, 5},
      {8, 3},
      {8, 5}
    ]

    lines = @schematic |> String.split("\n", trim: true)
    
    assert Advent2023.Day03.symbol_coordinates(lines) == expected

  end
end
