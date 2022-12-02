defmodule Advent2022.Day02 do
  def play("A", "X"), do: 3
  def play("A", "Y"), do: 6
  def play("A", "Z"), do: 0
  def play("B", "X"), do: 0
  def play("B", "Y"), do: 3
  def play("B", "Z"), do: 6
  def play("C", "X"), do: 6
  def play("C", "Y"), do: 0
  def play("C", "Z"), do: 3

  def choice_score("X"), do: 1
  def choice_score("Y"), do: 2
  def choice_score("Z"), do: 3

  def outcome_score("X"), do: 0
  def outcome_score("Y"), do: 3
  def outcome_score("Z"), do: 6

  def play_by_guide("A", "X"), do: 3
  def play_by_guide("A", "Y"), do: 1
  def play_by_guide("A", "Z"), do: 2
  def play_by_guide("B", "X"), do: 1
  def play_by_guide("B", "Y"), do: 2
  def play_by_guide("B", "Z"), do: 3
  def play_by_guide("C", "X"), do: 2
  def play_by_guide("C", "Y"), do: 3
  def play_by_guide("C", "Z"), do: 1

  def part_1(data) do
    Enum.reduce(data, 0, fn game, acc ->
      [opponent, me] = String.split(game, " ")
      outcome = play(opponent, me)
      choice = choice_score(me)
      acc + outcome + choice
    end)
  end

  def part_2(data) do
    Enum.reduce(data, 0, fn game, acc ->
      [opponent, me] = String.split(game, " ")
      outcome = play_by_guide(opponent, me)
      choice = outcome_score(me)
      acc + outcome + choice
    end)
  end

  def parse(data) do
    data |> String.trim() |> String.split("\n")
  end

  def main(data) do
    data = parse(data)
    {part_1(data), part_2(data)}
  end
end
