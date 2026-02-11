// go_runner.go - simple inject runner (reads CSV and prints timeline). Optional webhook POST if --webhook provided.
package main
import (
    "encoding/csv"
    "flag"
    "fmt"
    "log"
    "net/http"
    "bytes"
    "strconv"
    "time"
    "io/ioutil"
)
func main(){
    csvPath := flag.String("csv","injects_master_all.csv","inject CSV path")
    speed := flag.Float64("speed",10.0,"speed multiplier (higher = faster)")
    webhook := flag.String("webhook","", "optional webhook URL (dry-run=false will POST)")
    dryRun := flag.Bool("dry-run", true, "if true, do not actually POST to webhook")
    flag.Parse()

    f, err := ioutil.ReadFile(*csvPath)
    if err!=nil { log.Fatal(err) }
    r := csv.NewReader(bytes.NewReader(f))
    rows, err := r.ReadAll()
    if err!=nil { log.Fatal(err) }
    now := time.Now().UTC()
    for i,row := range rows {
        if i==0 { continue }
        minute, _ := strconv.Atoi(row[1])
        target := now.Add(time.Duration(float64(minute)/ *speed * float64(time.Minute)))
        for time.Now().UTC().Before(target) {
            time.Sleep(200 * time.Millisecond)
        }
        out := fmt.Sprintf("[%s] INJECT %s (%s): %s", time.Now().UTC().Format(time.RFC3339), row[0], row[2], row[4])
        fmt.Println(out)
        if *webhook != "" {
            payload := fmt.Sprintf("{\"id\":\"%s\",\"phase\":\"%s\",\"message\":\"%s\"}", row[0], row[2], row[4])
            if *dryRun {
                fmt.Println("[webhook] DRY-POST to", *webhook, "payload:", payload)
            } else {
                resp, err := http.Post(*webhook, "application/json", bytes.NewBuffer([]byte(payload)))
                if err!=nil { fmt.Println("webhook post error:", err); continue }
                defer resp.Body.Close()
                fmt.Println("[webhook] status", resp.StatusCode)
            }
        }
    }
}
