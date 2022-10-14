.SUFFIXES: .c .cpp .o .h .x .exe
# Aktualny katalog
DIR = $(notdir $(CURDIR))
# Nazwa jadra systemu operacyjnego
SYSNAME = $(shell uname -s)
# Nazwy plikow
NAME1 = Num1
# Objects file:
OBJS1 = $(NAME1).o
# Pliki wykonawcze
EXEC1 = $(NAME1).exe
#------------------------------------------------------------------------------
# Opcje kompilatora i linkera
CFLAGS = -Wall -std=c++11 -pedantic -O

# Kompilator i linker 
CO = g++
LD = $(CO)
###############################################################################
# Reguly zaleznosci
%.o: %.cpp %.h
	$(CO) $(CFLAGS) -c $<
# Jak wyzej, ale bez zaleznosci od plikow naglowkowych
%.o: %.cpp
	$(CO) $(CFLAGS) -c $<
###############################################################################
$(EXEC1): $(OBJS1)
	$(LD) -o $@ $(CFLAGS)  $^

.PHONY: run1
# Uruchomienie programu
run1: $(EXEC1)
	./$(EXEC1) 

###############################################################################
# Sprzataczka (tez "phony target")
###############################################################################
.PHONY: clean tar
clean:                                                     
	rm -f *.o  *~ *.a *.so *exe *.x core core* a.out;
# Archiwizacja i kompresja
tar: clean
	(cd ../; tar -cvzf $(DIR).tar.gz  $(DIR) )
