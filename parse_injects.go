
// parse_injects.go - simple CSV parser for injects (reads and prints inject timeline)
package main
import (
    "encoding/csv"
    "fmt"
    "log"
    "os"
    "sort"
    "strconv"
)
type Inject struct {
    ID string
    Minute int
    Phase string
    Message string
}
func main() {
    f, err := os.Open("injects_master.csv")
    if err != nil { log.Fatal(err) }
    defer f.Close()
    r := csv.NewReader(f)
    rows, err := r.ReadAll()
    if err != nil { log.Fatal(err) }
    var injects []Inject
    for i,row := range rows {
        if i==0 { continue }
        minute, _ := strconv.Atoi(row[1])
        injects = append(injects, Inject{ID:row[0], Minute:minute, Phase:row[2], Message:row[4]})
    }
    sort.Slice(injects, func(i,j int) bool { return injects[i].Minute < injects[j].Minute })
    for _,inj := range injects {
        fmt.Printf("%3d' - %s - %s: %s\n", inj.Minute, inj.ID, inj.Phase, inj.Message)
    }
}
