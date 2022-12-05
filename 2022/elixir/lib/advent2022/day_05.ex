defmodule Advent2022.Day05 do
  def part_1({diagram, procedure}) do
    Enum.reduce(procedure, diagram, fn [from: from, move: move, to: to], diagram ->
      {diagram, stack} = part_1_helper({diagram, []}, move, from)
      diagram |> Map.update!(to, fn tower -> tower ++ stack end)
    end)
  end

  def part_1_helper({diagram, stack}, 0, _from) do
    {diagram, stack}
  end

  def part_1_helper({diagram, stack}, move, from) do
    IO.inspect(diagram, pretty: true)

    case diagram |> Map.fetch!(from) |> List.pop_at(-1) do
      {nil, tower} ->
        {diagram |> Map.put(from, tower), stack} |> part_1_helper(move - 1, from)

      {crate, tower} ->
        {diagram |> Map.put(from, tower), stack ++ [crate]} |> part_1_helper(move - 1, from)
    end
  end

  def part_2(_data) do
    :todo
  end

  def parse(data) do
    [diagram, procedure] = String.split(data, "\n\n")
    {parse_diagram(diagram), parse_procedure(procedure)}
  end

  def parse_diagram(diagram) do
    diagram
    |> String.split("\n")
    |> Enum.map(&String.trim/1)
    |> Enum.drop(-1)
    |> Enum.map(fn tower ->
      tower |> String.split(" ") |> Enum.map(fn crate -> crate |> String.slice(1..1) end)
    end)
    |> Enum.with_index()
    |> Enum.into(%{}, fn {tower, index} -> {index + 1, tower} end)
  end

  def parse_procedure(procedure) do
    procedure
    |> String.split("\n")
    |> Enum.map(fn step ->
      regex = ~r/move (?<move>\d+) from (?<from>\d+) to (?<to>\d+)/
      %{"from" => from, "move" => move, "to" => to} = Regex.named_captures(regex, step)
      [from: String.to_integer(from), move: String.to_integer(move), to: String.to_integer(to)]
    end)
  end

  def main(data) do
    data = parse(data)
    {part_1(data), part_2(data)}
  end
end
