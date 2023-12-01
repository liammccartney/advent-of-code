defmodule Advent2023.Day01 do
  def part_1(calibration_doc) do
    calibration_doc
    |> Enum.map(&parse_calibration(&1))
    |> Enum.sum()
  end

  def part_2(doc) do
    doc |> Enum.map(&parse_calibration_2(&1)) |> Enum.sum()
  end

  def parse(data) do
    data
    |> String.split("\n")
  end

  def parse_calibration(calibration_line) do
    digits =
      calibration_line
      |> String.replace(~r/[^\d]/, "", trim: true)
      |> String.split("", trim: true)

    [List.first(digits), List.last(digits)]
    |> Enum.join()
    |> String.to_integer()
  end

  def parse_calibration_2(calibration_line) do
    digits =
      calibration_line
      |> this_is_dumb()
      |> String.replace(~r/[^\d]/, "", trim: true)
      |> String.split("", trim: true)

    [List.first(digits), List.last(digits)]
    |> Enum.join()
    |> String.to_integer()
  end

  def this_is_dumb(line) do
    Regex.replace(~r/one|two|three|four|five|six|seven|eight|nine|\d/, line, fn d ->
      case d do
        "one" -> "1"
        "two" -> "2"
        "three" -> "3"
        "four" -> "4"
        "five" -> "5"
        "six" -> "6"
        "seven" -> "7"
        "eight" -> "8"
        "nine" -> "9"
        _ -> d
      end
    end)
  end

  def main(data) do
    data = parse(data)
    {part_1(data), part_2(data)}
  end
end
