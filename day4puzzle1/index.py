import re

debug = False

input = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

input = """Card   1:  5 37 16  3 56 11 23 72  7  8 |  3 79 35 45 72 69 15 14 48 88 96 37 11 75 83 56 23  7 16 50 21 91 32 97 17
Card   2:  1 45 93 96 65 88 78 15 27 26 |  5 84 62 63 45 61  1 80 88 77 40 51 73 21 32 98 74 59 97  9 15 71 25 43 23
Card   3:  9 99 34 44 37 16 67 43 41 83 | 43 41  5 69 90 50 34 94 86 59 98 16 99 28 44 37 47 57  7 14 83 67 76  9 77
Card   4: 45 99 64 82 57  9 56 17 78  7 | 75 56 30 88 64  1 98 27  9 57  7  6 77 44 17 78 82 99 16 91 76 94 63 87 45
Card   5: 76 80 42 88 26 56 79 63  6 37 | 16  4 40 34 46 76 67 69  1 54  5 55 59 24 78 29 26  9 51 44 92 41 63 88 65
Card   6: 59 23 88 38 49 16 24 18 22 89 | 52 25 88 27 23 79 22 84 72 80 39 17 49 96 56 60 44 45 16 63 78 38 19  5 43
Card   7: 81  1 37  6 20 76  3 31 93 83 | 74 32 25 76 43 87 52 93 47 85 83 31 17 72  6 99  1 36 20 81  3 69 78 44 37
Card   8: 74 73 65 29 66 47 43 11 24 38 |  5  3  1 88 29 11 49 67 47 33 31 61 63 75 84 35 18 71 66 92 81 97  8  9 85
Card   9: 67 68  8 74 17 11 28 47 96  2 | 85  7 37 33 15 18 91 96  4 67 16 47 28 26 80 52 17 97 68  8 11 79  2 46 74
Card  10: 91 22 85 35 47 26 99 39 72 38 |  5  7 12 14 62 93 61 56 82  4  1 51 86 36 43 29 50 75 68 25 98 77 74 64 24
Card  11:  4 53 44 83 23 84 40 55 69 82 | 24 48 11 37 60 76 41 29 58 39 45 88 95 67 49 28 36 35 86 33 18 63 51 19 93
Card  12: 40 45 87 58 72 59 89 55 20 91 |  7 62  2 91 59 78  4 44 25 24 57 94 79 75 51 54 55 90 83 30 68 47  3 69 26
Card  13: 92 58 35 96 84 62 31 65 95  5 | 22 52 84 98 62 31 75  7 12 78 51 91 37 58 46 85 21 61 95 49 36  5 79 92  4
Card  14: 75 37 41 53 12 77 97  6 54 29 | 52 65 46 94 20  6 76 75 70 83 29 93 64  1 12 58 89 49 26 16 82 85 74 61 41
Card  15: 20 88 22 99 28 87 16 78 70 71 | 20 89 56 27 61 32 53 22 78  3 54 28 70 64 33 24 23 17  5 47 55 16 21 88  9
Card  16: 42 17 35 68  4 78 73 15 88 61 | 42 88 20 57 40  8 71 92 78 45  3 15 17 67 52 43 84 68  4 18 53 79  6 35 24
Card  17: 19 25 13 51 36 71 56 65 24 50 | 13 82 73 37 83 78 48 88 87 59 97 75 18 53 44 17 84 34 79 95 69 66 76 28 57
Card  18: 80 99 40 59 75 82 25 70 87 92 | 90 32 27 30 95 33 12 31 78 75 26 44 87 83 39 81 55 43 76 22 61 25 99 69 59
Card  19: 88 78 95 67 22  4 50 39 58 72 | 74  6 10 21 77 81 53 86 71 56 37 48 23 83 87 55 80 34 89 16 65  8 28 92 97
Card  20: 54 40 10 45 26 75 88 67 60  3 | 59 69 71 36 95 53 76 80 68 25 96 61 39 65 13  6 49 46 92 28 20 27  7 83 44
Card  21: 70 48 22 94 63 45 25 85 79 24 |  9  4 82 74 14 65 23 20 10 50 48 81 92 16 27 47 60 22 59 55  2 15 62 41 38
Card  22: 21 55 81 79 16 64 96 39 56 72 | 28 67 20 18  3 25 29 46 48 83 14  5 64 62  8 45 32 89 85 80  2 55 65  9 61
Card  23: 17 53 27 13 18 58 81 31 82 35 | 54 78  6 49 75 52  4 19 68 94 80 88 99 89 60  5 83 96 33 23 95 77 27 57 21
Card  24:  1 12 33 55 68 89 91 43 73 16 | 79 93 14 84 42 80 37 86 44 90 39 81 26 72 46 35 59 28  6 76 19 58 95  7 92
Card  25:  2 90 83 88 35 17 95  5  9 72 | 72 37 53 51 95 26 16 88  5 66 76  2 84  4 15 22 93 47  6 82 28  9 90 83 23
Card  26: 63 15 58 95 96 67 27 48 97 40 | 74 96 18 57 14 54 78 40 76 39 10 27  8 87 15 26 66 63 56 49 89 97 95 38 13
Card  27: 34 21 92 88 66 44 63  2 96 81 | 44 26 88 96 34 51 73 74 72  2 54 60 63 79 62 66 58 70 81 16  7 98 21 92 10
Card  28: 73 23  8 50 57 31  9 76 89 87 | 76 50 81 44 57  8 18 89 99 83 78 64 72 47 24 14  2 87 56 10 31 13 96 74 68
Card  29: 52 25 92 30 12 95 38 77 51 36 |  5  7 87 85 70 33 57 10 50 44 61 39 96 65 93 60 79 94 43 52 37 54  6 32 62
Card  30: 96 10 11 51 58 20 70 91 80 85 | 24 96 98 91 51 11 57 85 95 20 84 80 10 62  6  5 70 34 58 29 42 40 59 55 32
Card  31: 55 36 29 98 89 58 82 93 94 22 |  9  3 93 56 97 41 15 94 63 13 42 73 55 20 18 98 89 22 77 45 53 12 44 29 36
Card  32: 92 85  9  6 65 87 59 12 71 55 | 85 96 87 36 93 92 55 88 74 60 71  6  3 65 82  9 94 19 84 59 12 98 28 37 18
Card  33: 90  3 61 94  8 12 62 77 60 14 | 96 62 81 59  3  8 60  7 90 61 23 12 70  5 51 99 71 14 58 63 94 85 50 57 77
Card  34: 20  4 44 50 53 19 88 29 68 56 |  9 44 22 56 53  4 50 40 88 29 80  5  1 30 19 20 49 68 63 47 28 92 93  2 83
Card  35: 26 11 96 48 72 39 19 10 12 70 | 14 56 84 85 30 67 29 90  2 52 20 83 93 73 27 79 82 78 63  3 50 43  6 15 32
Card  36: 40 77 87  9 24 54 71 97 76 32 |  8 93 19 12 66 97 75  9 76  1 71 11 32 15 54 51 83 50 87 72 24  7 77 47  5
Card  37: 79 95 36 38 99 60 29 58 88 81 | 38 60 95 50 22 10 87 59 99 88 67 89 15 39 13 12 44 51 34 86 65 90  2 24 58
Card  38: 33  8 40 69  4 57 79 56 93  9 | 48 11 64 83 95 19 70 36 99 16 30 91 18  4 12 43 38  1 41 44 17 72 98  2 22
Card  39: 75 80 39 25 90 11 20 46 99 17 | 83 74 29 75 61 33 95 51 80 13 76 46 39  8 44 47 49  6 17 22  2 10 85 66 62
Card  40: 76 94 24 53 72 92 28 10 34 39 | 85 69  8 81 48 44 27 42 73 83 25 74 28 66 41 98 95 39 52 82 18 67 55  1 26
Card  41: 92 97 13 88 24 17 54 80 75 79 | 14 41 81 43 39  6 85 56 10 88 27 86 58  7 80 98 97 61 75 93 62 26 59 73 91
Card  42: 15 42 98 99 10 40 58 74 11 97 | 53 52 57 74 25 36 42 86 97 88 43 15 56 99 83 24 19 60 61 10 68  5 18 98  3
Card  43: 14 74 56 87 96 66 94 90 40 93 | 10 87 93 57 98 15 36 17 70 12  1 11 33 32 84 65 41 74 83 25 63 77 56 30 72
Card  44: 24 21 66 99 96 41 84 97 75 78 | 20 78 22 89 71  6 60 35 58 36 18  8 39  4 40 81 34 32 77 26 14 42 53 48 13
Card  45: 36 15 61 12 68 95 60 90 65 84 | 74 20 90  4 37 11 53 25 34 59 15 45 84 91 58 63  7 27 97 93 73  3 31 65 30
Card  46: 72 54 37 45 89  8 67 85 39 62 | 69 57 83 24 93 54 33  3 17 13  8 51 98  7 48 11 28 41 19 38 40 60 62 34 84
Card  47: 29  2 51 82 16 25 46 50 28  6 | 42 24  1 43 87 36 94 74 21 98 15 83 37 50 10 57 62 17 96 33 40 73 93 39 59
Card  48: 80 77 65 41 73  5 88 37 16 47 | 79 48 55 83 93 62 61 95 66 26  7 32 33 21 14  3 43 36 90 44 15 11 37  4 71
Card  49:  4 33 50 26 90 86 63  6 81 42 | 28 14  2 29 22 44 24 36 53 54 17 45 78 68 60 93 31 59 85 57  3 16 64 41 84
Card  50: 65 54 84 16 46 57 47  6 85 81 |  6 69 63  3 91 95 15 34 71 76 81 24 64 94 57 22 19 59 99  1 54 83 65 16 88
Card  51: 83 48 81 82 55 92 25 76 39 56 | 35 81 96 94 82 25 85 11 39 55 56 76 59 62 84 48 58 37 78  2 27 92 83 69 73
Card  52: 47 56 99 64 59 13 25 60 81 93 | 61 19 25 60 41 28 67 49 47 13 36  5 56 81 66 23 52 30 59 99 39  6 93 84 64
Card  53: 59 56 12 96 92 49  1 66 20  2 | 65 66 96 92 56 20 29 59 27  1 97 17 54 53 94 82 75 39  7 34  2 60 49 12 93
Card  54:  4 29 30 48 99 56 60 27  3 95 | 26 17 59 35 73 66 58 57  2 64 76 67 34 65 10 12  6 53 97 63 19 20 70 86 11
Card  55: 84 70 37 64  2 43 91 69  5 93 |  5 53 37 46 25 16 45 70 84 34 91 20  3 62 55 64 10 43 94 93 69 42  2 90 40
Card  56: 57 36 17 21 72  9 39 77 52 53 | 55 47 59 52 85 41 24 74 81 53 42  6 58 51 17 34 54 72 73  2 70 67 10 71 79
Card  57: 75 15 56 65 21 30 43 83 90 59 | 85  9 83 61 70 69 86 51 47 32 96 23 16  7 67 72 99 13 12 93 91 33  3 48  2
Card  58: 77 49 71 63 66 72 97 87 24 95 |  4 12 97 98 24 46 72 14 23 71 87 60 89 73 82 20  9 49 27 85 95 75 77 79  8
Card  59: 81 29 18 22 70 93 59 58 90 31 | 19 90 76 62 15 78 71 52 75 44  4 88 61 73 10 14 25 27 94 50 77 66 89 55 63
Card  60: 97 95  5 56 63 81 94  7 16 17 | 29 68 83  4 10 69 79 89 47 30 97 58 85 44 14 32 50 78 99 81 52  6 46 71 51
Card  61: 99 45 17 68 39 48 25 20 38 55 | 23 95 90 64  9  8 71 89  1 31 42 50 74 77 49 33 30 92 94 81  6 61 36 96 68
Card  62: 64 96 55 52 56 74 28 26 57 27 | 11 33 29 40 70 90  4 64 68 39 35 18 42 85 58 83 23 52 48  6 88 13 74 41 69
Card  63: 36 80 16 61 89 50 11  2 57 96 | 96 13 35 91 62 81 58 90 55 57 99 73 32 76 61 94 60 89 83 27 48 16 70 86 42
Card  64: 99 33 85 46 90 54 11 61 76 27 | 43  6 90 87 59 71 74  4 41 82 10 64 97 17 75 29 95 63 91  7 47 12 77 25 32
Card  65: 30 99 44 66  5 89  8 58 16 78 | 79 36 80  3 24 81 48 22 29 26 33 19 57  6 28 95 86 94 49 51 98 10 55  8 18
Card  66: 98 95 22 68 25 89  6 88 90 35 | 88 18 75 81 65 60 39 77 47 53 85 33 40 44  8 27 66 82 48 63 64 97 24 49 29
Card  67: 63 96 55  9 23 17 42 66 12 56 | 14 76 60 70 78 58 42 52 25 18 94 86 31 79 68 57 73 47 51 89 32 12 63 29 28
Card  68: 75 57 84 29 91 22 36 69 25 32 | 78 28 96 12 42  1 44 54 60 73 48 16 41 23 37 83 31 64 21 92 86 79 33 24 14
Card  69: 51  7 82 59 78 34 39 42 19 24 | 50  9 41 82 94 46 25 31 32 88 92 75 55 63 69 56 98 65 86 93 79 54 10 43 28
Card  70:  4 74 46 53 28  9 14 63 73 21 |  2 36 71 91 42 66  7 77 84 86 49 94 16 83 82 96 25 70 58 53 78 29 23 17 13
Card  71: 21 39 77 83 14 12  5 88 97 47 | 43 38 57 91  3 81 90 30 25 33 84 80 58 10 27 20 28 73  6 54 13 65 31 70 36
Card  72: 68 33  8 24 59 58 65 57 36 38 |  2 95 17 38 58 24 45 31 36 33 59 83 32  6 37 11 67 78 88 48 57 68 80 26  8
Card  73: 56  6 28 51 83 64 35 17 60 87 | 51 93 56 43 30 17 67 61 35 97 88 83 64 24 40  6 68 84 87 75 46 95 60 28 89
Card  74: 82 44 97 85 88 42 61 56  1 40 | 56 12 66 67 44 22 97 40 29 43 24  1 50 42 78 79  7 80 82 88 61 85 89 38 41
Card  75: 83 90 15 43 93 50  8 37 17 89 | 12 89 90 50 91 83 15 37 94  7 10 88 31 14 17 19 43  3 59 71 46 93 63 52  8
Card  76: 14 38 56 48 40  2 43 42 44 75 |  8 55 65 79 87 30 95 89  3 39 22  6 99 74 88 32 98 91  9 70 59 92 78 66 24
Card  77: 36 27 48 94 84 77 75  6 70 22 | 75 48 99  5 45 87 63  6 49 31 94 22 29 37 27 77 50 36 23 80 10 84 70 97 93
Card  78: 95 18 51 10 43 90 23 99 56 68 |  5 94 49 92 22 87 47 36 62 30  7 32 12 64 31 25 41 73 39 34 14 27 80 50 91
Card  79: 17 75 70 51 40 42 84 30 38 15 | 17 86 42 15 75 88 70 84 29 51 39  4 59 65 80  1 40 74 92 46 38 71 64 61 30
Card  80: 36 16 59 77 82 72 87 98 99 32 | 76  9 70 12 97 75 20 30 10 54 74 44 93 22  4 43 32 33 18 17 82 29 28 55 21
Card  81: 97 82 92 35 20 71 15 78 98  6 | 82 71 43 68 70 20 31 55 90 67 19 24 81 60 15  8 88 18 27 76 63 78 47 91 22
Card  82: 42 40 60  2 95 56 10 94 14 99 | 75 89 27 40 35 33 42 79 38 14 94 71 25 85 95 56 82 92 60 99 58 65  2 13 57
Card  83: 60 31 59  4 63 39 23 73 56 24 | 31 23 56 19 59  4 64 42 85  1 34 60 72 35 24 55 16 37 78 52  7 39  2 73 63
Card  84: 13 89 46 61  4 86 94 47 22 63 | 79  7 67 19 72 77 54 15 29 92 65 17 75 70 91 78 26 63 53 21 58 51 43 23 39
Card  85: 38  1 35 22 60 19 24 82 99 43 | 21 82 99 56 60 64 44 24  1 83 23 27 40 35 55 47 43 87 85 12 22 39  4 25 63
Card  86: 32 43 80 27 57 48 65 11 67 90 | 22 67 28 23 36 53 80 39 32 45 43 11 95  2 57 26 40 99 33 27 82 50 48 84 91
Card  87: 44 76 92 13 51 25 35 15 81 61 | 76 44 16  1 41 35  6 84 67 13  5 30 51 34  8  7 55 15 73 90 60 21 50 25 81
Card  88: 40 83 37 66 78 56 26 32 38 11 | 82 58 33  2 24 51 79 56 44 29 90 94 11 40 12 83 37 16 66 96 72 10 34 77 65
Card  89: 75 60 87 69 50 48 91 72 66 64 | 47 30 61 11 17 88 62 71  3  9 67 93 46 13 21 86 23 18 37  4 89 92 51 54 52
Card  90: 44 58 88 53 37 43 33 74 50 15 | 21 76 69  8 87 20 44 74 84 31 52 63 23 91 29 82 42 57 83  5 11 56 34 97 85
Card  91: 61 41 52 39 83 93 33 67 11  6 | 49 13 76 15 98 53 62 19 16 14  1 24 66 27 58 79 23 54 77 63 46 25 57 33 50
Card  92: 10 29 99 80 36 48 74 88 28  5 | 86 22 93 19 24 29 87 92 58 96 10 68 72 75 35 60 26 37 67 79  3 62 63 18 20
Card  93: 28 31 69 88 94 39 36 99  1 90 |  5 38 46 96 53 26 37 66 65 16 31 79  8 92 11 68 93 27 73 33 51 17 86  1 70
Card  94: 81 83 18  7  5 12 59 11 41 26 |  2 16 20 74 65 55 23 88 21 99 35 49 12 33 70 25 91 36 50  6 51 15 45 13 34
Card  95: 14 43 76 25 18 95 15 22 66 83 |  4 45 57 46 33 61 52 17 98 53 37 89 23 27 67 12 86 81 68  9 44 87 24  1 75
Card  96: 82 98 24  1 85 50 20 57 60 93 | 57 92 59 85 81 20 89 50 28 60 64 38 94 71 61 21 93 98 24 82 58 65 42 76  1
Card  97: 20 59 25 39 48 12 85 17 44 65 | 56 49 89 58 83 95 25  2 93 26 42 14 37 77 10 11 40 90 86 59  3 61 87 62 16
Card  98: 56  9 13 23 47 31 54 95 17 58 | 30 59 65 52 23 85 72 75 19 36 95 41 54 49 42 83 64 15 80 31 16  9 27 20 29
Card  99: 38 82 89 49 24 20 65 87 42 31 | 50 64 92 85  1 14 29 61 18 96 53 10 99 17 15 97 88 74 69 12 72 40 66 54 86
Card 100: 16 78 53 13 62 18  9 63 61 94 | 16 10 73  6 36 13 24 63 94 57  5  8 18 52 67 20 62 68 29 78 61 69 53  9 38
Card 101: 20 53 48 71 35 65 26 31 89 44 | 42 10 97 20  1 91 29 96 76 21 78 27 46  3 18 25 68 48 90 41 37 65 28 88 17
Card 102: 63 31 48 76 34 46 44 99 39 35 | 50 56 53 38 46 39 99 73 61 32 18 65 63 31 74 97 48 41 62 35 44 26  4 34 76
Card 103: 31 61 96 44  3 32 51 10 74 95 | 60 15 29 39 19 20 68 28 83 40 42 52 50 41 10 36  7 71 11 18 27 16 75 93 99
Card 104: 38 98 96 64 66 93 53 95 87 73 | 16 45 77 87 92 69 99  3 33 36 31 89 63 93 98  4 83 10 13 51 59 64 37 47 85
Card 105: 24 86 51 27 23 99 25 97 82 72 | 20 27  7 60 71 94 26 33 52 41  6 48 36 22 46 51 44 64 63  3 50 86 47 12 53
Card 106: 71 75 52 24 61 13 45 59 30  1 |  6 96  7 20 65 55 95 57 16 29 22 18 87 56 53 81 51 67 66 23 50 11 91 44 72
Card 107: 47 31  1 45 94 76 35 77 41 96 |  9 47 12 59 89 83 14  5 38 52 39 55 50 90 97 75 87 68 37 26 22 46 27 10 15
Card 108: 90 35 81 74  7 82 11 79 80 33 | 84 74 82 15 34 26 19 83 25 95 90 81 79 97 71 99 22 35  8 41 65 11  7 55 62
Card 109: 80 18 68 10 31 61 64 98 84  7 | 81 54 26 20 52 94 68 88 19 15 87 40 12 91 10 61  1 56 45 85 66 25 82 57 92
Card 110: 79 75 95 63 62 32 78 67 88  3 | 45 80 76 94 10 82 55 26 24 41 65 78  5 47 75 91 38  7 37 88  2 52 97 50 99
Card 111: 69  4 78 87 15 59 22 90 86 40 | 98  4 27 21  9 71 40  5 67 69 94 38 87 92 91 47 54 17 65 43 30  1 51 72 70
Card 112: 30 93 66 43 89 12 32 46  1 76 | 79 63 16 15 95 88 44  7  8 59 32 74 19 97 45 80 61 30 34 68 70  1  3 28 55
Card 113: 36  8  6 21 92 96 67 98 59 34 | 73 44 85 41 11 47 50 53 40 27 90 75 20 79 32 69  3 74 99 78 66 93 56 14 82
Card 114: 74 31 59  5 70 12 95 33 97 46 | 53 92 99 74 94 78 86 25 73 10 17 58 21 37  2 71 79 90 77 76 50 93 87 52  4
Card 115: 38 75 68 26 66 52 13 17 76 33 | 73 60 35 27 91 15 39 41 63 36  4 19 61  5  6  3 70 55 24 11 23 71 67 29 51
Card 116: 73 26 82 27 63 88 34 91 78 59 | 35 56 58 68 71 14  4 94 33 75 72  6 67 55 80 57 28 11 65 84 66 54  3 95 20
Card 117: 66  2 31 29 64 73 92 10 33 83 | 43 42 55 20 61 51 57 58 94 37 14 15 84 69 41 28 11 10 67 34 65 91 78 18  1
Card 118: 63 82 19 38 31 57 93 79 32 56 |  1 43 81 72 32 24 79 84 45 94 38 92 56  5 42 70 63 91 93 71 57 96 51 31 83
Card 119: 34 48 60 44  4 64  3 35 66 30 | 47  3 60 76 67 97 31  1 35 55 84 65 81 52 45 30 50  7 34 71 14 74 89 11 66
Card 120: 86 93 50 94 55 11 83 84 61 15 | 11 42 14 17 63 36 75 49 86 15 55 94 84 61 50 48 80  6 83 39 23 93 67 87 46
Card 121: 92 85 58 71 34 94 60 49 14 17 | 34 74 61 77 89 50 99 49 94 60 68 83 71 27 17 56 46 63 76 26 20 70 41 85 39
Card 122: 99  2 97 77 34 42 35 16 13 33 |  6 42 60 26  9 13 98 30 94 97 33 40 58 91 32 46 47 68 78 34 77 35 93 22 39
Card 123: 34 16 84 71 29 13 53 57 79 43 | 24 37 74 85 35  7 51 44 97 29  9 70 67 45 61 15 65 77 86 20 90 66 73 11 58
Card 124: 39 83 88 46 71  8 66 68 67 52 | 75 66 93  8 20 67  3 73 34 39 71 83 45 15 58 55 31 38 69 29 46 40 48 42 68
Card 125: 73 16 48 77 94 75 79 40 39 22 | 98 37 36 63 10 84 52 53 94 82 46 17 73  2 88 42 16 33 64 62 95 22 77 43 55
Card 126: 10 84 50 23 39 71 86 74 38 53 | 71 16 38 23 28 86 97 53 43 69 10 84  5 72  4 96 15 37 74 50 83 22 39 49 12
Card 127: 92 69 94 70 14 35 44 58  3 96 | 18 89 21 14  2 17 76 50 29 72 87 56 39 25 33 37 68 60 55 66 53 80 62 26 38
Card 128: 58 45 46 29 74 94 61  1 18 72 | 20 76 24 41 14 86 53 85 90 80 83 68 48 10 49 25 75 89 92 93 23 37 38 96 33
Card 129:  9 19 94 34 58 89 13  1 47 37 | 53 21 17 73 50 79 24 25  2 92 47 75  8 30 98 12 85 80 62 65 86 84 40 49 67
Card 130: 66 46 68 96 19  2 21 32 63 13 | 82 68 63 21 25 43 44 91 40 97 20 75  2 46 80 83  5 59 66 56 45 93 98 95 47
Card 131: 13 20 75 52  6 26 90 36  3 82 | 58 98 40  5 12 82 56 64 16  9 17 74 77 76 85 31 53 28 67  4 18 97 47 57 43
Card 132: 90 86 97 51 21 60 45  8 94 91 | 97 70 38 89 73 14 30 10 39 18 91  8 55 12 86 45 37 54  9  5 23 33 29 51 71
Card 133: 18 22 20  1 76 64 59 26 73 15 | 75 54 45 77 30 51 32  6 78 11 70 40 22 26 59 79  2 50 94 24 85 29 31 25 73
Card 134: 61 72 44 50 47 22 78 62 21 32 | 51 61 59 81 67 54 58 55 87 52 85 62 48 34 35 68 74 82 91 11 84 80 98  1 94
Card 135: 81 98 77 10 91 59 49 66 55 79 |  8 30 40 46 53 50 41 18 66 76 83 72 34  1 49 11 87  9 94 51 79  7 63 90 37
Card 136: 96 28 21 15 42 65 91 43 82 60 | 95 23 34 51 29 58 31 89  4 16 36 20  5 61 33 47 59 75 80 55  9 67 28 74 45
Card 137: 53 27 50 59 83 75 48 25 90 89 | 93 87 31 17 35  1 13 24 91 16 90 52 94 99 60 42  4 10 19 32  7 69 80 38 71
Card 138: 40  8 61 37 83 55 88 50 77  5 | 99 73 66 63 90 78 24  3 29 62 35 75 92  6 39 42 19 95 13 80 25 64 54 49 68
Card 139: 24 87 36  5 58 46 84  4 80 19 | 31 10 49 87 53 17 67 37 44 80 19 43 46 86 32  4 15 24 58 64 85 66  5 81 82
Card 140: 92 93 56 21 97 86  5 11 45  3 | 45 21 66 59 56 44 79 16 86 13  8  3 88 71 52 55 54 60  2 37 93 92 97 11  5
Card 141: 98 73  9  7 74 71 43 63  5 89 | 83 73 44 12 86 97 74 71 43 78 14 98  8 53 16 51  7 20 88 89 93 37 46 58 63
Card 142: 57 96 47 59 56 58 76 52  1 84 | 80 68  6 61 82 24 42 17 86 79 22 65 31 81 27 41 70 33 77 54 49 99 37 66 64
Card 143: 34 98 19 48 99 54 66 28 26 33 | 99 89 39 44 81 98 71 67 91 47 48 45 54  7 24 55 51 94 33 34 26 66 19 95 28
Card 144: 82 37  3 29 57 39 34 44  5 70 |  3  6 39  1  2 10  5 82 37 56 29 50 30 48 47 70 58 12 44  9 69 57 88 51 34
Card 145: 73 65 86 88 99 81 26 70 11 62 | 86  3 14 88 66 11 90 30 67 80  8 79 23 44  2  1 45 13 32 72 31 26 55 64 70
Card 146:  8 54 27 20 89 28 51  3 19 40 | 13 81 90 98  9  6 93 88  1 82 79 48 14 31 20 58 65 91 78 38 62  7 73 64 52
Card 147: 70 63 99 58 80 73 38 95 69 90 | 67 82 72 73 70 92 91 63 80 20  4 69 95 64 38 58 50 10 90 99 78 68 49  1 26
Card 148: 61 41 24 78 96 40 91 23 70 19 | 28  1 16 76 19 95 60 92 82 41 25 87 63 30 91 96 12 70 77 27 23 90 24 72 61
Card 149: 43 89 27 28 50 39  6 83 69 45 | 12 43 34 39 73 40 66 95 36 96 74  6 72 81 24 25 78 92 42 22 87 86 59 89 97
Card 150:  9 14 44 72 64 11 95 68 73 75 | 44 14 60 54 97 64 11  4 57 79 40 53 39  2 51 46 75 42  9 37  6 83 80 25 72
Card 151: 91 12 67 98 83 16 14 62 69 36 | 35 66 73 90 28 36 43 37 69 24 95 85 27 48 39 44 16 62 53 72 15  1 63 19  5
Card 152: 42 27 33  9 32 99 76 30  3 53 | 42 43 17 41  5  6 47  8 91 66 85 12 31  9 99 76 58 13 90 11 46 53 54 29 30
Card 153: 51 60 22 62 57 11 16 85  9  3 | 17 52 62 87 97 73 25 34 65 88 72 16 94  3 32 27 96 86 42 91 80 41 95 79 11
Card 154: 36 13 59 96 52 90 79  6 14 74 | 28 92 63  4 48 85 12  6 13 91 86 76 44 16 93 97 43 54 52 49 60 84  8 75 21
Card 155: 91 27 43 97  4 68  6 79  5 72 | 22 77 90 15 50  4 52 70 88 85 24 27 12 80 82 81 74 36 45 92 39 78 54 71  5
Card 156: 80 45 22 79  4 23 21 63 34 37 |  6 99 74 11 62 54 36 63 59 14 37 70 44 25 31 15 97 12 39  2 75 90  4 46 18
Card 157: 43 37 94 45 96 99 15 33 54 38 | 18 70 62 12  5  7 17 33 24  8 79 15 51 44 87 57 99  4 25 34 74 65 63 13 76
Card 158: 21 65  8 67 37 97 99 24 16 68 | 51 85 26 80 72 81 57 37 82 93 46 94 68 54 24 32 18 48  1 69 49 29 27 40 39
Card 159:  3  2 61 25 92 69 30 10 57 78 | 88 46 33  3 52 89 55  4 24 82  9 98 62 66 54 23 28 13 50 68 39  1 15 63 74
Card 160:  1 28 51 92 96 79 22 97 17 62 | 64 46 44 75 50 43 39 30 37 91 82 11  4 34 27 71 65 40 81 53 38 52 60  2 23
Card 161: 26 12 82 16 52 15 97 42  2 20 | 68 22 49 59 32 53 10 72  4 92 25 56 84 65 69 75 88  9 37 86  1 78 89 41 99
Card 162:  3 32 24 52 49 80 10 39 43 72 | 60 39 23 25 56 21 10 12 24 70 32 83 80 43 19 28 34 22 52 72 49 74  3 15 29
Card 163: 77 57 96 84 68 59 24 92 60  5 | 66 33 57 73 44 92 60 34 39 62 96 80  2 77 91  5 24 51 31 64 68 59 36 84 88
Card 164: 76 60 92 78 34 44 23 14 22  1 | 92 17 44 32 53 34 54 28 73 93 89 67 84 18 60 72 85 10 26 21 23 78 33 51 79
Card 165: 66 99 39 27 18 79 96  7 50 44 |  7 96 41 98 78 57 44  8 61 50 79 68 99 38 40 10 66 31 14 18 27 89 70 39 69
Card 166: 73 42 83 91 88 21 43 16 10 55 | 73  8 28 10 76 16 99 55 97 62 42 65 35 72 83 52 57 50 91 21 37 74 36 88 96
Card 167: 64 38 97 19 73 72 67 79 94 21 | 21 38 54 73 66 49 29 25 75 19 85  6 64 34 97 13 30 28 79 67 36 72 94 68 82
Card 168: 16 37 31 29 99 88 54 66  3 57 | 88 31 38 21 11 79 13  9 36 27 78 47 97 74 64  7 42 32  2 50 46 80 87 96 60
Card 169:  6 18 54 82 21 27 34 62 91 12 | 52 26 12 56 39 21  5 91 89  6 18 34 43 62 40 67 76 83 27 31 92 82 54 45 55
Card 170: 31 82 50 80 27 16 34 22 38 54 | 80 22 63 31 23 38 34 66 16 82  9 75 64 54 85 50 99 81 92 53 77 30 13 27 35
Card 171: 44 50 51 70 77 73 55 41 80 60 | 63 60 69 80 25 48 36 56 96  1 88 14 75 30  7 50 40 95 87 51 41 59 11 65 70
Card 172: 33 60 55 35 38 86 78 56 31 14 | 60 67 83 33 21 40 14 69 38 94 32 54  3 17 49 19 22 86 31 79 73 71 56 75 78
Card 173: 75 30 84  6 15 21 76 28 66 83 | 98 94 57 58 26 74 90 69 64 66 51 30 28 38 82 21 86 15 75 78 97  9 19 72 56
Card 174: 49 63 32 42 78 24 55 70 76 95 | 78 90 82 98 50 60 76  3 49 44 74 18 68 32 55 29 72 24 63 99 96 12 70 59 31
Card 175: 15 69 87 40 61 58 81 77 21 12 | 27 31 77 43 47 85 80 44 21  1 33  3 84  7 54 51 69 40 70 71 12 49 61 22 15
Card 176: 40  7 45 71 92 88 27 97 58  8 |  2 82 67 15 81 63 16 49 65 89 35 60 79 29 74 43 56 45 95 84 10 32 92 96 64
Card 177:  8 70 28 81 60 12 64 98 84 72 | 32 58 80 65 90 79 95 31 56 43 82 45 94 21 92 55 89 96 53 54 19 51  6 52 33
Card 178: 16 59 30 28 62 24  8  6 92 91 | 96 24 30 28 37 42 50 69 67 62 49 84 92 65 95 34 68 17 47 59  2 60 79 53 16
Card 179: 68 58 26 30 90 16  9  6 44 92 | 97  4 95 64 12 18 52 96 29 67 84 69 91 23 56 24 10 20 98 87 80 79 65 22 48
Card 180: 30 32 52  1 10 23 62 43 51 79 | 70 72 87 82  3 83 24 73 34 64 75 71 84 89 26 65 27 47 41 39 81 37 36 18 17
Card 181: 80  2 77  4 29 98 52 21 86 90 | 46 61 34 66  6 57  8 59 32 16 80 89 86 83 26 27 53 29 55 31 92 84 18 56 14
Card 182: 77 54 92 15 91 12 89 56 45 87 | 82 13 40 26 15 16 44 97  9 52 33 20 36 63 99 57 49 46 19 22 79  3 32 37 73
Card 183: 41 43 38 48 97 95 69 98 81 80 | 22 93 36 50 23 37 34  9 27  8 35 49 82 71 65 98 39 56 10  5 69 86 16 88 21
Card 184: 50 96 62 20 87 19 90 13 41 82 | 52 85 38 89 59 30 64 91 74  6 39 60 61 77 97 18 42 49 12 36 55 56  3 75 96
Card 185: 43 62 42 28 85 36 21 39 59 16 | 63  1 35 52 15 98 65 68 27 61 40 95 74 80 11 83 94 89 47 90 25 72 32 31 23
Card 186: 48  6 85 22 91  9 76  2 15 21 | 83 44 33 78 24 96 38 43 20 16 59 67 99 86 36 58 80 31 11 14 28 98  5 57 42
Card 187: 18 71 35 72 10 45 11  4 44 56 | 16 72 23 30 56 73 45 63 99 10 57 88 65  4 12  8 94 71 11 18 44 35 80 74 78
Card 188: 89 11 73 22 99 41 28 61 66 52 | 98 85 99 64 97 28 71 66 26 58 53  3 92 95 22 67 83 13 51 11 57 79 25 19 89
Card 189: 61 49 23 38 82 95 62  2 15 67 | 14  2 68 82 61 11 86 65 70 40 38 95 67 80 23 62 27 36 90 55 25 57 35 49 15
Card 190: 74 47 34 96 42 10 58 71 82 80 | 32 42 68 58 74  6 93 82 50 91 80 33 71 55 47 30 70 43 62 98 75 11  4 96 10
Card 191: 48 39 13 22 77 86  8 34 71  6 | 44 20 73 16 31 67 66  1 21  2 80 54 49 42 45 35 30 87 83 57 60  4 50 76 26
Card 192: 70 77 39 63 81 88  7 78 85 44 | 97 81 85 12 96 71 63 84 88 45  9 77 27 78 51 52 82 44  7 10 80 60 70 39 49
Card 193: 11 62 85  7  5 47 58 68 88 65 | 98 55 47  5  7 85 22 62 82 46 38 59 68 30 26 84 45 40 58 31 81 11 65 93 88
Card 194: 60 49 75 21 54 34 40  6 39 67 | 84 60 14 34 65 49  7 39 32 54 74 25 40 75 21 72  6 35  5 41 78 20 26 77 67
Card 195: 55 11 12 81  4  7 97 61 15 58 | 69 29 95 11 12 77  4 30 55 15 44 39  2 89 38 71 51 25 40  6 21 81 58  7 98
Card 196: 90 78  2  3 77 24 33 45 32 30 | 16 11 39 27 85 34 79 59  6 33 46 21 48 36 58 99 40 74 63 82 96 42  7 95 90
Card 197: 21 13  3 45  1 33 54 70 23 22 | 23 73 21 34 76 78  4  1 46 11 60 64 42 26 81 13 90 51  2 79 74 45  3 72 84
Card 198: 44 17 16 71 52 50 11 69 14 86 | 90 70 65  7 91 17 63 81 24 39 69 42 87 57 36 35 74 31 22 80 50 88 13 41 78
Card 199: 60 13 93 42 74 66  3 89 40  8 | 43 37 38 54 99 36 44 62  1 91 60 52 76 21 20 86 17 97 98  7 79 57 28 48 35
Card 200: 40 39 37 63 65  8 25 47 85 12 | 62 35 28 68 63 27 98 40 43 17 78 87 41 86 13 61  5 23  4 20 93 31 66 18 49
Card 201: 41 57  5 59 95 15 18 44 75 28 |  1 33 29 38 76 73 36 17 19  4 52 84 68 32 35 27 92 58 81 78  2 61 97 85 22
Card 202: 60 80 88 13 96 57  1 58 39 52 | 52 34 58  2 59 50 79 92 63 98 96 36 62 77 37 56 78  4 54 51  9 76 85 21 57
Card 203: 39 28 57 98  3 73 22  8 23 68 | 44  9 43 17 50 14 97  1 41 76 61 90 20 62 78  5 89 85 64 55 16 72 19  4 37
Card 204: 99 82 81 86 88 31 92  8 93 94 | 28 74 53 55 76 77 57 94 97 45 41 17 38 36 98 86 39 24 10 42 27 65 73 34 96
Card 205: 55  7  8 82 24 95 85 99 22 59 | 58 64 84 42 26 59 20 37 49 57 62 15 18  1 32  2 86 69 96 63 47 77 60 19 93
Card 206: 73 34 51 18 57 42 91 27 84 95 |  6 88 80 82 98 89 36 10 33 78 37 21 45 96  5 93 15 63 62 92 49 94  1 64 85
Card 207: 83 32 10 94 28  8 61 98 53 48 | 31 78 60 79 87 37 97 34 11 71 66  1 29 74 24 41 22 42 46 85 80 47 17 54 14
Card 208: 11 17 75 84 85 40 89 23 54 80 | 31 54 85 61 39 79 27 56 62 64 11 80  3 72 14 73 19 48 99 89 15 42 23  9 97
Card 209: 30 75 20 84 70 26 72 23  9 97 |  5 76 67 41 18 84 36 54 70 65 75 25 82 23 50  9  7 46 33 85 38 11 97 95 40
Card 210: 76 25 97 64 92 68 60 43 63 53 | 31  1 91 45 39 62 89 50 77 37 38 25  8 28 71 97 49 99 55  9 27 52 64 76 73
Card 211: 62 52 55 90 57 38 95 65 39 92 | 67 46 95  3 38 18 26  5 75 55 92 41 85 28 84 42 37 73 64 69 33 14 34 94 35
Card 212: 91 93 76 59 88 48 97 44 96 78 | 22 20 48 74 61 91 69 25 59 44  6 93 42 36 96 76 60 88 37 32 78 97 16 47 89
Card 213: 79 33 53 91 63 62 42  3 72 25 | 59 69 60  7 82 68 73 97 23 48 39 38 76 71  9 29 37 53 67 92 85 55 15 13 61
Card 214: 51 20 73 22 11 83 14 71 26 74 | 85 48 41 50 93 70 21 76  2 16 22 95  6 25 20 19 72 58 11 45 83 54 26 73 51
Card 215: 47 72 51 32  7 13 99 36 17 48 | 22 47  6 36  8 91 35 11  3 42 30 21 38 43 28 64 99 72 75 18 84 13 52 82 55
Card 216: 34 39 74 27  3 44 62 85 42 87 | 51 59 19 80 33 89  1 79 84 82 85 60 61 56  6 50 77 92 55 21 34 83 38 98 26
Card 217: 11 33 54 13 67 99 61 86 57  7 | 95 32 57 34 98 33  7 54 71 26 42 73 52 56 13 79 67 78 75 58  9 81 24 41 96
Card 218: 50  9 20 47 18 95 63 31 75 30 | 73  5 26 92 74 57 77 20 96 32  8  9 88 71 75 28 17 29 81 27 90 49 25 67 87
Card 219:  5 55 89 78 12 19 47 64 87 81 | 16 66 55  2 13 10 93 88 39 47 22 54 65 59  8 75 99 19 61 43 68 86 67 49 70
Card 220: 84 11 98 89 83 95 48 71 45 88 | 14  7 33 52 19 30 66 81 37 57 21  8 47 17 72 95 63 59 29 18 27 26 76 91 73
Card 221: 78 17 79  4 63 65 56 57 22 92 | 48 94 32 37 26 58 64 87 24 95 19 41 12 25 74 93 30  1 66 27  3 43 50 35 11
Card 222: 74 14 52 95 73 11 55 26 90 78 | 17 21 93 28 90 61 63 50 19 57 91 66 86 79 62 41  3 23 75 15 56 18 92 83 49
Card 223: 98 82 47 14  2 48  1 50 18 62 | 67 78 16 58 35 87 93 44 77 13 74 34 32 92 88 54 36 61 91 72  9 59 89 73  5"""

def debugprint(*args):
    if debug == True:
        print(*args)

def parse_list_of_numbers(list_of_numbers):
   return [int(number.strip()) for number in list_of_numbers.split(" ") if number]

def parse_line(line):
    scratchcard_regex = r"^Card\s+(\d+):\s+(.*)\|\s(.*)$"
    matches = re.match(scratchcard_regex, line)
    if not matches:
        raise Exception("Invalid line: " + line)

    card_number = matches.group(1)
    winning_numbers = parse_list_of_numbers(matches.group(2))
    card = parse_list_of_numbers(matches.group(3))
    debugprint(f"Card {card_number} has winning numbers {winning_numbers} and numbers {card}")
    number_matches = len([number for number in card if number in winning_numbers])
    debugprint(f"Card {card_number} has {number_matches} matches")
    if number_matches == 0:
        return 0
    return pow(2, number_matches - 1)

def parse_input(input):
    total = 0
    for line in input.splitlines():
        total += parse_line(line)
    return total

print(parse_input(input))