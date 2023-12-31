var MovesMap = new Dictionary<string, char>()
{
    {"A", 'R'},
    {"B", 'P'},
    {"C", 'S'},
    {"X", 'R'},
    {"Y", 'P'},
    {"Z", 'S'},
};

var StrategyMap = new Dictionary<string, Dictionary<char, char>>()
{
    {"X", new Dictionary<char, char>() {{'R', 'S'}, {'P', 'R'}, {'S', 'P'}}},
    {"Y", new Dictionary<char, char>() {{'R', 'R'}, {'P', 'P'}, {'S', 'S'}}},
    {"Z", new Dictionary<char, char>() {{'R', 'P'}, {'P', 'S'}, {'S', 'R'}}},
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
var answer2 = Part2(data);
Console.WriteLine(answer2);

IEnumerable<string[]> Parse(string input) =>
    input.Trim().Split('\n')
        .Select(line =>
            line.Trim().Split(' ')
        );

int Part1(IEnumerable<string[]> data)
{
    var scores = data
        .Select(round =>
            {
                var moves = round.Select(r => MovesMap[r]).ToArray();
                return MovePoints[moves[1]] + WinPoints[moves[0]][moves[1]];
            }
        );
    return scores.Sum();
}

int Part2(IEnumerable<string[]> data)
{
    var scores = data
        .Select(round =>
            {
                var you = MovesMap[round[0]];
                var me = StrategyMap[round[1]][you];
                return MovePoints[me] + WinPoints[you][me];
            }
        );
    return scores.Sum();
}
