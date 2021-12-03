defmodule Advent.Day02 do
  def main(commands) do
    commands =
      commands
      |> Enum.map(fn raw ->
        [dir, dist] = String.split(raw)
        {String.to_atom(dir), String.to_integer(dist)}
      end)

    {commands |> part_1(), commands |> part_2()}
  end

  def part_1(commands) when is_list(commands) do
    commands
    |> Enum.reduce([x: 0, y: 0], &part_1/2)
    |> calculate_answer()
  end

  def part_1({:forward, dist}, x: x, y: y) do
    [x: x + dist, y: y]
  end

  def part_1({:down, dist}, x: x, y: y) do
    [x: x, y: y + dist]
  end

  def part_1({:up, dist}, x: x, y: y) do
    [x: x, y: y - dist]
  end

  def part_2(commands) when is_list(commands) do
    commands
    |> Enum.reduce([x: 0, y: 0, aim: 0], &part_2/2)
    |> calculate_answer()
  end

  def part_2({:forward, dist}, x: x, y: y, aim: aim) do
    [x: x + dist, y: y + aim * dist, aim: aim]
  end

  def part_2({:down, dist}, x: x, y: y, aim: aim) do
    [x: x, y: y, aim: aim + dist]
  end

  def part_2({:up, dist}, x: x, y: y, aim: aim) do
    [x: x, y: y, aim: aim - dist]
  end

  def calculate_answer(x: x, y: y), do: x * y
  def calculate_answer(x: x, y: y, aim: _), do: x * y
end
