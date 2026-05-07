package main

import (
	"bufio"
	"database/sql"
	"encoding/json"
	"fmt"
	"os"

	"github.com/joho/godotenv"
	_ "github.com/lib/pq"
)

type Log struct {
	User User `json:"user"`
}

type User struct {
	Age  int    `json:"age"`
	Name string `json:"name"`
	Role string `json:"role"`
}

func main() {
	godotenv.Load()
	host := os.Getenv("DB_HOST")
	port := os.Getenv("DB_PORT")
	user := os.Getenv("DB_USER")
	password := os.Getenv("DB_PASSWORD")
	dbname := os.Getenv("DB_NAME")

	connStr := fmt.Sprintf(
		"host=%s port=%s user=%s password=%s dbname=%s sslmode=disable",
		host, port, user, password, dbname,
	)

	db, err := sql.Open("postgres", connStr)
	if err != nil {
		fmt.Println(err)
		return
	}

	defer db.Close()

	err = db.Ping()
	if err != nil {
		fmt.Println("接続失敗:", err)
		return
	}

	fmt.Println("接続成功")

	args := os.Args
	if len(args) != 2 {
		fmt.Println("引数エラー")
		return
	}
	

	file, err := os.Open(args[1])
	if err != nil {
		fmt.Println(err)
		return
	}
	tx, err := db.Begin()
	if err != nil {
		fmt.Println(err)
		return
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		line := scanner.Text()
		var log Log
		err := json.Unmarshal([]byte(line), &log)
		if err != nil {
			tx.Rollback()
			return
		}
		_, err = tx.Exec(
			"INSERT INTO users (age, name, role) VALUES ($1, $2, $3)",
			log.User.Age,
			log.User.Name,
			log.User.Role,
		)
		if err != nil {
			fmt.Println(err)
			tx.Rollback()

			return
		}
		fmt.Println(log.User.Name)
	}
	if err := scanner.Err(); err != nil {
		tx.Rollback()
		fmt.Println(err)
		return
	}
	tx.Commit()
}