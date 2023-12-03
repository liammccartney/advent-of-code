defmodule Advent2023.Day03 do
  def number_spans(line) do
    Regex.scan(~r/\d+/, line, return: :index) |> List.flatten()
  end

  def symbol_indices(line) do
    Regex.scan(~r/[^\w.]/, line, return: :index) |> List.flatten() |> Enum.map(fn {i, _} -> i end)
  end

  def symbol_coordinates(lines) do
    lines
    |> Enum.with_index()
    |> Enum.map(fn {line, y} ->  
      line
      |> symbol_indices()
      |> Enum.map(fn x -> {y, x}  end)
    end)
    |> List.flatten()
  end

end
