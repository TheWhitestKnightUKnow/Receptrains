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

test11:
	python trains.py "AB4, BF6, AD5, DE7, FD8, CF3, DE4, EB7" "path" "A-C"

test12:
	python trains.py "AB4, BF6, AD5, DE7, FD8, CF3, DE4, EB7" "routesMax" "A-C-4"

test13:
	python trains.py "AB4, BF6, AD5, DE7, FD8, CF3, DE4, EB7" "routesExactly" "A-C-4"

test14:
	python trains.py "AB4, BF6, AD5, DE7, FD8, CF3, DE4, EB7" "routesMaxDistance" "A-C-12"

test15:
	python trains.py "AB4, BF6, AD5, DE7, FD8, CF3, DE4, EB7" "shortest" "A-C"

# Given example inputs
# Expected outputs:
# 1. 9
# 2. 5
# 3. 13
# 4. 22
# 5. 'NO SUCH ROUTE'
# 6. 2
# 7. 3
# 8. 9
# 9. 9
# 10. 7
all: test1 test2 test3 test4 test5 test6 test7 test8 test9 test10

# Should all return 0 or 'NO SUCH ROUTE'
disconnected: test11 test12 test13 test14 test15

clean:
	rm -f *.pyc