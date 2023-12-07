defmodule Advent2023.Day05Test do
  use ExUnit.Case
  alias Advent2023.Day05

  test "parse seeds" do
    line = "seeds: 79 14 55 13"
    expected = [79, 14, 55, 13]

    assert Day05.parse_seeds(line) == expected
  end

  test "parse map" do
    line = "50 98 2"
    expected = %{98 => 50, 99 => 51}

    assert Day05.parse_range(line) == expected
  end

  test "lookup" do
    mapping = %{98 => 50, 99 => 51}

    assert Day05.lookup(98, mapping) == 50
    assert Day05.lookup(100, mapping) == 100
  end
end
