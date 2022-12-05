defmodule Advent2022.Day04 do
  def part_1(data) do
    data
    |> Enum.reduce(0, &handle_ranges/2)
  end

  def handle_ranges({elf_a_range, elf_b_range}, total) do
    if MapSet.subset?(elf_b_range, elf_a_range) or MapSet.subset?(elf_a_range, elf_b_range) do
      total + 1
    else
      total
    end
  end

  def handle_section_overlaps({elf_a_range, elf_b_range}, total) do
    overlaps = MapSet.intersection(elf_a_range, elf_b_range) |> MapSet.size()

    if overlaps > 0 do
      total + 1
    else
      total
    end
  end

  def part_2(data) do
    data |> Enum.reduce(0, &handle_section_overlaps/2)
  end

  def parse(data) do
    data |> String.trim() |> String.split("\n") |> parse_ranges()
  end

  def parse_ranges(ranges) do
    ranges
    |> Enum.map(fn range_pair ->
      [elf_a, elf_b] = range_pair |> String.split(",")
      [elf_a_start, elf_a_end] = elf_a |> String.split("-") |> Enum.map(&String.to_integer/1)
      [elf_b_start, elf_b_end] = elf_b |> String.split("-") |> Enum.map(&String.to_integer/1)

      {MapSet.new(elf_a_start..elf_a_end), MapSet.new(elf_b_start..elf_b_end)}
    end)
  end

  def main(data) do
    data = parse(data)
    {part_1(data), part_2(data)}
  end
end
