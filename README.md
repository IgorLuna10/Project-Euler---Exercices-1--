# Project Euler Solutions

A collection of programming solutions for the mathematical challenges found on [Project Euler](https://projecteuler.net/).

## 📁 Repository Structure

The project is organized to keep solutions separate from configuration files.

* **Solutions/**: Contains Python scripts for each problem.
* **Dockerfile**: Configuration to run the project in a containerized environment.
* **.gitignore**: Prevents system files (like .DS_Store) from being committed.

## 🚀 Solved Problems

| # | Problem Title | Solution | Key Concept |
|---|---------------|----------|-------------|
| 1 | Multiples of 3 or 5 | [View](./Solutions/1%20-%20Multiples%20of%203%20or%205.py) | Arithmetic Progressions |
| 2 | Even Fibonacci Numbers | [View](./Solutions/2%20-%20Even%20Fibonacci%20Numbers.py) | Iterative Sequences |

## 🐳 Running with Docker

This repository is Dockerized for ease of use. You don't need Python installed on your host machine to run the solutions.

1. **Build the Docker image:**
   ```bash
   docker build -t euler-solutions .

Run a specific solution: (Note: Use double quotes for filenames with spaces)
Bash

    docker run euler-solutions python "Solutions/1 - Multiples of 3 or 5.py"

Author: Igor Luna
