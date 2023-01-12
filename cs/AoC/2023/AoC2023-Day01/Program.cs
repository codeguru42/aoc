// See https://aka.ms/new-console-template for more information

var input = File.ReadAllText("input.txt");
var elves = Parse(input);
var answer1 = Part1(elves);
Console.WriteLine(answer1);
var answer2 = Part2(elves);
Console.WriteLine(answer2);

IEnumerable<IEnumerable<int>> Parse(string input)
{
    var elves = input.Split("\n\n");
    return elves.Select(elf => elf.Trim().Split('\n').Select(int.Parse));
}

int Part1(IEnumerable<IEnumerable<int>> elves)
{
    var calories = elves.Select(elf => elf.Sum());
    return calories.Max();
}

int Part2(IEnumerable<IEnumerable<int>> elves)
{
    var calories = elves.Select(elf => elf.Sum());
    return calories.OrderByDescending(c => c).Take(3).Sum();
}
