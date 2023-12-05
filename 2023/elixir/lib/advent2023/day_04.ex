defmodule Advent2023.Day04 do
  def part_1(lines) do
    lines
    |> find_winning_numbers_count()
    |> Enum.map(fn n ->
      case n do
        0 -> 0
        1 -> 1
        2 -> 2
        n -> 2 ** (n - 1)
      end
    end)
    |> Enum.sum()
  end

  def find_winning_numbers_count(lines) do
    lines
    |> Enum.map(fn line ->
      [winning, played] =
        line
        |> String.split(":", trim: true)
        |> List.last()
        |> String.split("|", trim: true)
        |> Enum.map(
          &(String.split(&1)
            |> MapSet.new())
        )

      MapSet.intersection(winning, played) |> Enum.count()
    end)
  end

  def part_2(lines) do
    lines
    |> find_winning_numbers_count()
    |> Enum.map(fn n -> {n, 1} end)
    |> win_more_cards(0)
  end

  def win_more_cards([], acc), do: acc

  def win_more_cards([{_, 0} | tail], acc) do
    win_more_cards(tail, acc)
  end

  def win_more_cards([{n, c} | tail], acc) do
    {to_map, rest} = Enum.split(tail, n)

    mapped =
      to_map
      |> Enum.map(fn {p, d} -> {p, d + 1} end)

    win_more_cards([{n, c - 1}] ++ mapped ++ rest, acc + 1)
  end

  def main(input) do
    lines =
      input
      |> String.split("\n", trim: true)

    {part_1(lines), part_2(lines)}
  end
end
