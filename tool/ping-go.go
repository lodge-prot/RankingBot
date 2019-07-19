package main

import (
    "fmt"
    "os"
    "io"
    "bufio"
    "os/exec"
    //"time"
    "flag"
    "strings"
    //"reflect"
)

type HostList struct {
    ipaddr int
    hostname string
}

func get_container_list_to_text(filepath string) (container_list []string){
    f, err := os.Open(filepath)
    if err != nil {
	panic(err)
    }
    defer f.Close()

    reader := bufio.NewReaderSize(f, 4096)
    for line := ""; err == nil; line, err = reader.ReadString('\n') {
        if err == io.EOF {
            break
        }
        if err != nil {
            panic(err)
        }
	container_list = append(container_list, line)
    }
    return
}

func exec_ping(cl []string) {
    for _, s := range cl {
	if s == "" {
	    continue
	}
	out, err := exec.Command("ping", strings.TrimRight(s, "\r\n"), "-c", "3").Output()
	if err != nil {
	    fmt.Println("[FAILED] : ", s, err, out)
	    continue
	}
	fmt.Printf("[OK] : %s", s)
    }
}

func main() {
    fmt.Println("===== START =====")

    flag.Parse()
    var container_list []string = get_container_list_to_text(flag.Args()[0])
    exec_ping(container_list)

    fmt.Println("=====  END  =====")
}
