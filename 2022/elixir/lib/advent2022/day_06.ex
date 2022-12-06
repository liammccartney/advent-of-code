defmodule Advent2022.Day06 do
  def part_1(data) do
    data
    |> Enum.chunk_every(4, 1, :discard)
    |> Enum.find_index(fn window ->
      MapSet.size(MapSet.new(window)) == length(window)
    end)
    |> Kernel.+(4)
  end

  def part_2(data) do
    data
    |> Enum.chunk_every(14, 1, :discard)
    |> Enum.find_index(fn window ->
      MapSet.size(MapSet.new(window)) == length(window)
    end)
    |> Kernel.+(14)
  end

  def parse(data) do
    data
    |> String.trim()
    |> String.to_charlist()
  end

  def main(data) do
    data = parse(data)
    {part_1(data), part_2(data)}
  end
end
