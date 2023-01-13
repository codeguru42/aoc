var MovesMap = new Dictionary<string, char>()
{
    {"A", 'R'},
    {"B", 'P'},
    {"C", 'S'},
    {"X", 'R'},
    {"Y", 'P'},
    {"Z", 'S'},
};

var WinPoints = new Dictionary<char, Dictionary<char, int>>()
{
    {'R', new Dictionary<char, int>() {{'R', 3}, {'P', 6}, {'S', 0}}},
    {'P', new Dictionary<char, int>() {{'R', 0}, {'P', 3}, {'S', 6}}},
    {'S', new Dictionary<char, int>() {{'R', 6}, {'P', 0}, {'S', 3}}},
};

var MovePoints = new Dictionary<char, int>()
{
    {'R', 1},
    {'P', 2},
    {'S', 3},
};

var input = File.ReadAllText("input.txt");
var data = Parse(input);
var answer1 = Part1(data);
Console.WriteLine(answer1);

IEnumerable<IEnumerable<char>> Parse(string input) =>
    input.Trim().Split('\n')
        .Select(line =>
            line.Trim().Split(' ').Select(c => MovesMap[c])
        );

int Part1(IEnumerable<IEnumerable<char>> data)
{
    var scores = data
        .Select(round =>
            {
                var moves = round.ToArray();
                return MovePoints[moves[1]] + WinPoints[moves[0]][moves[1]];
            }
        );
    return scores.Sum();
}

void Part2()
{
}
