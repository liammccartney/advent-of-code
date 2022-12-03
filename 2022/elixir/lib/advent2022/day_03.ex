defmodule Advent2022.Day03 do
  def part_1(data) do
    data
    |> Enum.reduce([], &handle_rucksack/2)
    |> Enum.map(&to_priority/1)
    |> Enum.sum()
  end

  def to_priority(snak) do
    if snak >= 97 do
      snak - 96
    else
      snak - 38
    end
  end

  def handle_rucksack(rucksack, dupes) do
    letters = String.graphemes(rucksack)
    [comparment_a, comparment_b] = Enum.chunk_every(letters, div(length(letters), 2))

    MapSet.intersection(MapSet.new(comparment_a), MapSet.new(comparment_b))
    |> MapSet.to_list()
    |> List.to_charlist()
    |> Kernel.++(dupes)
  end

  def part_2(data) do
    data
    |> Enum.chunk_every(3)
    |> Enum.reduce([], &handle_badges/2)
    |> Enum.map(&to_priority/1)
    |> Enum.sum()
  end

  def handle_badges(rucksacks, badges) do
    [a, b, c] =
      rucksacks |> Enum.map(fn rucksack -> rucksack |> String.graphemes() |> MapSet.new() end)

    MapSet.intersection(a, b)
    |> MapSet.intersection(c)
    |> MapSet.to_list()
    |> List.to_charlist()
    |> Kernel.++(badges)
  end

  def parse(data) do
    data |> String.trim() |> String.split("\n")
  end

  def main(data) do
    data = parse(data)
    {part_1(data), part_2(data)}
  end
end
