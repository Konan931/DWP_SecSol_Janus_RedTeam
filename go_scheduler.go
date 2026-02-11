// go_scheduler.go - naive scheduler example (sleep-based), not production
package main
import ("time"; "fmt")
func main(){
    fmt.Println("Scheduler demo: sleep for 5s then run task")
    time.Sleep(5 * time.Second)
    fmt.Println("Running scheduled task at", time.Now().UTC().Format(time.RFC3339))
}
