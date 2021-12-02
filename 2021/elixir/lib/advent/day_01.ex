defmodule Advent.Day01 do
  def part_1(data) do
    data
    |> Enum.with_index()
    |> Enum.reduce(0, fn {x, i}, acc ->
      y = Enum.at(data, i + 1)
      if !is_nil(y) && y > x, do: acc + 1, else: acc
    end)
  end

  def part_2(data) do
    windowed =
      data
      |> Enum.with_index()
      |> Enum.map(fn {x, i} ->
        y = Enum.at(data, i + 1)
        z = Enum.at(data, i + 2)
        x + (y || 0) + (z || 0)
      end)

    windowed
    |> Enum.with_index()
    |> Enum.reduce(0, fn {x, i}, acc ->
      y = Enum.at(windowed, i + 1)
      if !is_nil(y) && y > x, do: acc + 1, else: acc
    end)
  end

  def main(data) do
    data = data |> Enum.map(&String.to_integer/1)
    {part_1(data), part_2(data)}
  end
end
