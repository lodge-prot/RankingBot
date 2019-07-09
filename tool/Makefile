PROGRAM = memget
TARGET  = ./
OBJS    = memget.o
SRCS    = $(OBJS:%.o=%.c)
CC      = gcc
CFLGAS  = -g -Wall -Wextra

$(PROGRAM):$(OBJS)
	$(CC) $(CFLGAS) $(LDFLAGS) -o $(TARGET)/$(PROGRAM) $(OBJS) $(LDLIBS)

clean:
	rm -f *.o $(TARGET)/$(PROGRAM)

