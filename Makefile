run:
	python trains.py "AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7"

pathABC:
	python trains.py "AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7" "path" "A-B-C"

pathAD:
	python trains.py "AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7" "path" "A-D"

pathADC:
	python trains.py "AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7" "path" "A-D-C"

pathAEBCD:
	python trains.py "AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7" "path" "A-E-B-C-D"

pathAED:
	python trains.py "AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7" "path" "A-E-D"

routes:
	python trains.py "AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7" "routes" "C-C-3"

shortest:
	python trains.py "AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7" "shortest" "A-C"

shortest2:
	python trains.py "AB5, BC5, CD5, DE5, EF5, FG5, EB3, XY7" "shortest" "A-X"

shortest3:
	python trains.py "AB5, DC5, CD5, DE5, EF5, FG5, EB3, GY7" "shortest" "C-Y"

clean:
	rm -f *.pyc