defmodule Advent.Day01 do
  def part_1(data) do
    part_1_helper(data, 0)
  end

  def part_1_helper(data, total) do
    case data do
      [x | tail] ->
        y = List.first(tail, 0)
        part_1_helper(tail, if(y > x, do: total + 1, else: total))

      [] ->
        total
    end
  end

  def part_2(data) do
    data
    |> Enum.chunk_every(3, 1)
    |> Enum.map(&Enum.sum/1)
    |> part_1()
  end

  def main(data) do
    data = data |> Enum.map(&String.to_integer/1)
    {part_1(data), part_2(data)}
  end
end
