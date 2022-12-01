defmodule Advent2022.Day01 do
  def part_1(data) do
    Enum.max(data)
  end

  def part_2(data) do
    data
    |> Enum.take(3)
    |> Enum.sum()
  end

  def parse(data) do
    data
    |> String.split("\n\n")
    |> Enum.map(&parse_elf/1)
    |> Enum.sort_by(& &1, :desc)
  end

  def parse_elf(elf) do
    elf |> String.trim() |> String.split("\n") |> Enum.map(&String.to_integer/1) |> Enum.sum()
  end

  def main(data) do
    data = parse(data)
    {part_1(data), part_2(data)}
  end
end
