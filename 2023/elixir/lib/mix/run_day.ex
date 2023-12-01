defmodule Mix.Tasks.RunDay do
  @moduledoc """
  Run A Day's Solutions
  """
  use Mix.Task

  def run(args) do
    day = List.first(args)
    is_example = List.last(args) == "example"
    module = Module.concat(Advent2023, "Day" <> day)

    day
    |> get_input_data(is_example)
    |> module.main
    |> print_solution(day)
  end

  defp print_solution({part_1, part_2}, day) do
    IO.puts("#{day} Part 1: #{part_1}")
    IO.puts("#{day} Part 2: #{part_2}")
  end

  defp get_input_data(day, is_example) do
    if is_example do
      File.read!("../input/day#{String.downcase(day) <> "_example"}.txt")
    else
      File.read!("../input/day#{String.downcase(day)}.txt")
    end
  end
end
