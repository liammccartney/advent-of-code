defmodule Mix.Tasks.Benchmark do
  @moduledoc """
  Run A Day's Solutions
  """
  use Mix.Task

  defp get_input_data(day, is_example) do
    if is_example do
      File.read!("../input/day#{String.downcase(day) <> "_example"}.txt")
    else
      File.read!("../input/day#{String.downcase(day)}.txt")
    end
  end

  def run(args) do
    day = List.first(args)
    is_example = List.last(args) == "example"
    module = Module.concat(Advent2023, "Day" <> day)

    input = get_input_data(day, is_example)

    Benchee.run(%{
      "main" => fn -> module.main(input) end
    })
  end
end
