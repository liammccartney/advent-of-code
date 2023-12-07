defmodule Advent2023.Day05 do
  def parse_seeds(line) do
    Regex.scan(~r/\d+/, line)
    |> List.flatten()
    |> Enum.map(&String.to_integer(&1))
  end

  def parse_range(line) do
    Regex.scan(~r/\d+/, line)
    |> List.flatten()
    |> Enum.map(&String.to_integer(&1))
    |> to_map()
  end

  def to_map([dest_start, source_start, range_length]) do
    for x <- 0..(range_length - 1), reduce: %{} do
      acc -> Map.put_new(acc, source_start + x, dest_start + x)
    end
  end

  def lookup(source, mapping) do
    Map.get(mapping, source, source)
  end
end
