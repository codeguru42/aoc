package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	left, right := parse()
	fmt.Println(part1(left, right))
	fmt.Println(part2(left, right))
}

func parse() ([]int, []int) {
	fi, err := os.Open("day01.txt")

	if err != nil {
		panic(err)
	}

	defer fi.Close()

	scanner := bufio.NewScanner(fi)
	var left []int
	var right []int

	for scanner.Scan() {
		line := scanner.Text()
		pair := strings.Split(line, " ")
		p1, _ := strconv.Atoi(pair[0])
		p2, _ := strconv.Atoi(pair[3])
		left = append(left, p1)
		right = append(right, p2)
	}

	if err := scanner.Err(); err != nil {
		panic(err)
	}

	return left, right
}

func part1(left []int, right []int) int {
	sort.Slice(left, func(i, j int) bool { return left[i] < left[j] })
	sort.Slice(right, func(i, j int) bool { return right[i] < right[j] })

	var diffs []float64
	for i, val := range left {
		diffs = append(diffs, math.Abs(float64(val-right[i])))
	}

	var sum float64 = 0
	for _, val := range diffs {
		sum += val
	}

	return int(sum)
}

func part2(left []int, right []int) int {
	var counts = make(map[int]int)
	for _, val := range right {
		counts[val] = counts[val] + 1
	}

	var sum = 0
	for _, val := range left {
		sum += val * counts[val]
	}

	return sum
}
