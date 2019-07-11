PROGRAM1 := memget
PROGRAM2 := ping-go
TARGET   := ./bin
OBJS     := memget.o
SRCS     := $(OBJS:%.o=%.c)
CC       := gcc
GO	 := go
CFLGAS   := -g -Wall -Wextra

.SUFFIXES: .c .o
.PHONY: all
all: $(PROGRAM1) $(PROGRAM2)

ifeq ($(shell uname),Linux)
GFLAGS	 := CGO_ENABLED=0
endif

$(PROGRAM1):$(OBJS)
	$(CC) $(CFLGAS) $(LDFLAGS) -o $(TARGET)/$(PROGRAM1) $(OBJS) $(LDLIBS)

$(PROGRAM2): ping-go.go
	$(GFLAGS) $(GO) build -o $(TARGET)/$(PROGRAM2) ping-go.go

clean:
	rm -f *.o bin/memget bin/ping-go
