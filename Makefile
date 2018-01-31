run:
	python trains.py "AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7"

test1:
	python trains.py "AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7" "path" "A-B-C"

test2:
	python trains.py "AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7" "path" "A-D"

test3:
	python trains.py "AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7" "path" "A-D-C"

test4:
	python trains.py "AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7" "path" "A-E-B-C-D"

test5:
	python trains.py "AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7" "path" "A-E-D"

test6:
	python trains.py "AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7" "routesMax" "C-C-3"

test7:
	python trains.py "AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7" "routesExactly" "A-C-4"

test8:
	python trains.py "AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7" "shortest" "A-C"

test9:
	python trains.py "AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7" "shortest" "B-B"

test10:
	python trains.py "AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7" "routesMaxDistance" "C-C-30"

all: test1 test2 test3 test4 test5 test6 test7 test8 test9 test10

clean:
	rm -f *.pyc