using static System.Char;

var input = File.ReadAllText("input.txt");
var data = Parse(input);

var answer1 = Part1(data);
Console.WriteLine(answer1);

var answer2 = Part2(data);
Console.WriteLine(answer2);

string[] Parse(string input)
{
    return input.Trim().Split('\n');
}

int Score(char item)
{
    if (IsLower(item))
    {
        return item - 'a' + 1;
    }

    return item - 'A' + 27;
}

int Part1(IEnumerable<string> rucksacks)
{
    var priorities = rucksacks.Select(rucksack =>
    {
        var half = rucksack.Length / 2;
        var common = rucksack[..half].Intersect(rucksack[half..]).First();
        return Score(common);
    });
    return priorities.Sum();
}

int Part2(IEnumerable<string> rucksacks)
{
    var priorities = rucksacks.Chunk(3).Select(rucksack =>
    {
        var common = rucksack[0].Intersect(rucksack[1]).Intersect(rucksack[2]).First();
        return Score(common);
    });
    return priorities.Sum();
}
