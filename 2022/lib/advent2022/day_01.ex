defmodule Advent2022.Day01 do
  def total_calories_per_elf(elves) do
    elves
    |> Enum.reduce([], fn elf, acc ->
      acc ++ [Enum.sum(elf)]
    end)
  end

  def part_1(data) do
    data
    |> total_calories_per_elf()
    |> Enum.max()
  end

  def part_2(data) do
    data
    |> total_calories_per_elf()
    |> Enum.sort_by(& &1, :desc)
    |> Enum.take(3)
    |> IO.inspect()
    |> Enum.sum()
  end

  def main(data) do
    data =
      data
      |> Enum.chunk_by(fn d -> d == "" end)
      |> Enum.filter(fn elf -> elf != [""] end)
      |> Enum.map(fn elf -> Enum.map(elf, &String.to_integer/1) end)

    {part_1(data), part_2(data)}
  end
end
