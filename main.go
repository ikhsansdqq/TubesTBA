package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	// Create a new scanner to read from standard input
	scanner := bufio.NewScanner(os.Stdin)

	// Prompt the user for input
	fmt.Print("Enter your name: ")

	// Read the input
	scanner.Scan()
	name := scanner.Text()

	// Print the input
	fmt.Printf("Hello, %s!\n", name)
}
