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
	python trains.py "AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AX7" "routes" "C-X-3"

test7:
	python trains.py "AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7" "routes" "A-C-4"

test8:
	python trains.py "AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7" "shortest" "A-C"

test9:
	python trains.py "AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7" "shortest" "B-B"

test10:
	python trains.py "AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7" "routes" "C-C-30"

clean:
	rm -f *.pyc