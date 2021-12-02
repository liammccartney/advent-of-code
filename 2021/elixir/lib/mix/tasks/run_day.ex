defmodule Mix.Tasks.RunDay do
  @moduledoc """
  Run A Day's Solutions
  """
  use Mix.Task

  def run(args) do
    day = List.first(args) |> String.capitalize()
    is_example = List.last(args) == "example"
    module = Module.concat(Advent, day)

    day
    |> get_input_data(is_example)
    |> module.part_1
    |> print_solution(day, "Part 1")

    day
    |> get_input_data(is_example)
    |> module.part_2()
    |> print_solution(day, "Part 2")
  end

  defp print_solution(output, day, prefix) do
    IO.puts("#{day} #{prefix}: #{output}")
  end

  defp get_input_data(day, is_example) do
    if is_example do
      File.read!("../input/#{String.downcase(day) <> "_example"}.txt") |> String.split("\n")
    else
      File.read!("../input/#{String.downcase(day)}.txt") |> String.split("\n")
    end
  end
end
