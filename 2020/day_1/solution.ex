defmodule Expenses do
  def part1() do
    target = 2020

    get_data()
    |> MapSet.new()
    |> find_pair(target)
    |> calc(target)
  end

  def find_pair(set, target) do
    set
    |> Enum.find(fn n -> MapSet.member?(set, target - n) end)
  end

  def calc(n, target) do
    n * (target - n)
  end

  def get_data() do
    File.read!("input.txt")
    |> String.split("\n", trim: true)
    |> Enum.map(&String.to_integer/1)
  end
end

IO.puts("Part 1:")

Expenses.part1()
|> IO.puts()
