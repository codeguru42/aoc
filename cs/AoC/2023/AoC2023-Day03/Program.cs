// See https://aka.ms/new-console-template for more information

var input = File.ReadAllText("input.txt");
var data = Parse(input);

foreach (var rucksack in data)
{
    Console.WriteLine($"{rucksack[0]} {rucksack[1]}");
}

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
