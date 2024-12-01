package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
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
		p2, _ := strconv.Atoi(pair[1])
		left = append(left, p1)
		right = append(left, p2)
	}

	fmt.Println(left)
	fmt.Println(right)

	if err := scanner.Err(); err != nil {
		panic(err)
	}
}
