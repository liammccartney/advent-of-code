defmodule Advent2022.Day01 do
  def part_1(data) do
    data
    |> Enum.reduce([], fn elf, acc ->
      elf = Enum.map(elf, &String.to_integer/1)
      acc ++ [Enum.sum(elf)]
    end)
    |> Enum.max()
  end

  def main(data) do
    data = data |> Enum.chunk_by(fn d -> d == "" end) |> Enum.filter(fn elf -> elf != [""] end)
    {part_1(data), :todo}
  end
end
