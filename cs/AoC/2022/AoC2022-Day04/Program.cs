var input = File.ReadAllText("input.txt");
var data = Parse(input);

var answer1 = Part1(data);
Console.WriteLine(answer1);

var answer2 = Part2(data);
Console.WriteLine(answer2);

IEnumerable<IEnumerable<IEnumerable<int>>> Parse(string input)
{
    return input.Trim().Split('\n')
        .Select(line => { return line.Split(',').Select(range => range.Split('-').Select(Int32.Parse)); });
}

bool Part1(object o)
{
    throw new NotImplementedException();
}

bool Part2(object o)
{
    throw new NotImplementedException();
}
