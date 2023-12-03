defmodule Advent2023.Day02 do
  @limit %{
    "red" => 12,
    "green" => 13,
    "blue" => 14
  }

  def parse_game(line) do
    [game_num, grabs] = String.split(line, ":", trim: true)
    [_, id] = String.split(game_num, " ", trim: true)
    {String.to_integer(id), parse_grabs(grabs)}
  end

  def parse_grabs(grabs) do
    grabs
    |> String.split(~r/,|;/, trim: true)
    |> Enum.map(fn pull ->
      [num, color] = String.split(pull, " ", trim: true)
      [String.to_integer(num), color]
    end)
  end

  def checK_game(game) do
    game
    |> Enum.all?(fn [num, color] ->
      num <= Map.get(@limit, color)
    end)
  end

  def part_1(games) do
    games
    |> String.split("\n", trim: true)
    |> Enum.map(&parse_game(&1))
    |> Enum.filter(fn {_, game} -> checK_game(game) end)
    |> Enum.reduce(0, fn {id, _}, sum -> sum + id end)
  end


  # Part 2
  def group_grabs(game) do
    game
    |> Enum.reduce(%{}, fn [num, color], acc ->
      Map.update(acc, color, [num], fn v -> v ++ [num] end)
    end)
  end

  def find_minimum_distribution(grabs) do
    grabs
    |> Enum.map(fn {color, pulls} -> {color, Enum.max(pulls)} end)
    |> Map.new()
  end

  def find_power(cubes) do
    cubes
    |> Enum.map(fn {_, n} -> n end)
    |> Enum.product()
  end

  def part_2(games) do
    games
    |> String.split("\n", trim: true)
    |> Enum.map(&parse_game(&1))
    |> Enum.map(fn {_, game} -> group_grabs(game) end)
    |> Enum.map(&find_minimum_distribution(&1))
    |> Enum.map(&find_power(&1))
    |> Enum.sum()
  end

  def main(input) do
    {part_1(input), part_2(input)}
  end
end
