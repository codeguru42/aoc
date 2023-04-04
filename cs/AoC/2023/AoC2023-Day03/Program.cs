using static System.Char;

var input = File.ReadAllText("input.txt");
var data = Parse(input);

var answer1 = Part1(data);
Console.WriteLine(answer1);

IEnumerable<string[]> Parse(string input)
{
    return input.Trim().Split('\n')
        .Select(line =>
        {
            var half = line.Length / 2;
            return new string[]
            {
                line[..half],
                line[half..]
            };
        });
}

int Part1(IEnumerable<string[]> rucksacks)
{
    var priorities = rucksacks.Select(rucksack =>
    {
        var common = rucksack[0].Intersect(rucksack[1]).First();
        if (IsLower(common))
        {
            return common - 'a' + 1;
        }
        return common - 'A' + 27;
    });
    return priorities.Sum();
}
