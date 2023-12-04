defmodule Advent2023.Day03 do
  def part_1(lines_with_index) do
    nums = where_to_search(lines_with_index)
    symbols = locate_symbols(lines_with_index)

    nums
    |> Enum.reduce([], fn {n, neighbors}, acc ->
      if Enum.any?(neighbors, fn h ->
           MapSet.member?(symbols, h)
         end) do
        acc ++ [n]
      else
        acc
      end
    end)
    |> Enum.sum()
  end

  def where_to_search(lines_with_index) do
    lines_with_index
    |> Enum.flat_map(fn {line, y} ->
      Regex.scan(~r/\d+/, line, return: :index)
      |> List.flatten()
      |> Enum.map(fn {x, l} ->
        {String.slice(line, x, l) |> String.to_integer(), generate_neighbors(x, y, l)}
      end)
    end)
  end

  def generate_neighbors(x, y, l) do
    for i <- (x - 1)..(x + l), j <- (y - 1)..(y + 1), do: {i, j}
  end

  def locate_symbols(lines_with_index) do
    lines_with_index
    |> Enum.flat_map(fn {line, y} ->
      Regex.scan(~r/[^\w.]/, line, return: :index)
      |> List.flatten()
      |> Enum.map(fn {i, _} -> {i, y} end)
    end)
    |> MapSet.new()
  end

  def locate_gears(lines_with_index) do
    lines_with_index
    |> Enum.flat_map(fn {line, y} ->
      Regex.scan(~r/\*/, line, return: :index)
      |> List.flatten()
      |> Enum.map(fn {i, _} -> {i, y} end)
    end)
    |> MapSet.new()
  end

  def part_2(lines_with_index) do
    gears = locate_gears(lines_with_index)
    nums = where_to_search(lines_with_index)

    gears
    |> Enum.reduce([], fn gear_loc, acc ->
      neighbor_nums = Enum.filter(nums, fn {_, neighbors} -> Enum.member?(neighbors, gear_loc) end)

      if length(neighbor_nums) == 2 do
        acc ++ [(Enum.map(neighbor_nums, fn {n, _} -> n end) |> Enum.product())]
      else
        acc
      end
    end)
    |> Enum.sum()
  end

  def main(input) do
    lines =
      input
      |> String.split("\n", trim: true)
      |> Enum.with_index()

    {part_1(lines), part_2(lines)}
  end
end
