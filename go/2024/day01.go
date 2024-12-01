package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	fi, err := os.Open("day01.txt")

	if err != nil {
		panic(err)
	}

	defer fi.Close()

	scanner := bufio.NewScanner(fi)

	for scanner.Scan() {
		fmt.Println(scanner.Text())
	}
}
