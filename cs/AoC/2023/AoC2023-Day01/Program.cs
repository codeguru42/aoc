// See https://aka.ms/new-console-template for more information

using static System.Int32;

var input = File.ReadAllText("input.txt");
var elves = input.Split("\n\n");
var calories = elves.Select(elf =>
{
    var calories = elf.Trim().Split('\n').Select(Parse);
    return calories.Sum();
});
Console.WriteLine(calories.Max());
